# app.py
import streamlit as st
import pandas as pd
import io, os, re, tempfile
import pdfplumber
from docx import Document
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy
@st.cache_resource
def load_spacy():
    return spacy.load("en_core_web_sm")

nlp = load_spacy()

# Load skills list
def load_skills(path="skills.txt"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f if line.strip()]
    # fallback list
    return ["python","java","c++","sql","javascript","machine learning","nlp","excel","aws","docker"]

SKILLS = load_skills()

def parse_pdf_bytes(b):
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(b)) as pdf:
            pages = [p.extract_text() or "" for p in pdf.pages]
            text = "\n".join(pages)
    except Exception as e:
        st.warning(f"PDF parse issue: {e}")
    return text

def parse_docx_bytes(b, filename="temp.docx"):
    # write to temporary file for python-docx compatibility
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    tmp.write(b)
    tmp.close()
    text = ""
    try:
        doc = Document(tmp.name)
        text = "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        st.warning(f"DOCX parse issue: {e}")
    finally:
        os.unlink(tmp.name)
    return text

def parse_txt_bytes(b):
    try:
        return b.decode("utf-8")
    except:
        try:
            return b.decode("latin-1")
        except:
            return ""

def parse_resume_bytes(b, filename):
    ext = filename.lower().split(".")[-1]
    if ext == "pdf":
        return parse_pdf_bytes(b)
    elif ext in ("docx","doc"):
        return parse_docx_bytes(b, filename)
    else:
        return parse_txt_bytes(b)

def extract_skills(text, skills_list):
    t = text.lower()
    found = [s for s in skills_list if s in t]
    return list(dict.fromkeys(found))  # unique, preserve order

def extract_years_experience(text):
    # find patterns like: "5 years", "3.5 yrs", "7+ years"
    matches = re.findall(r'(\d{1,2}(?:\.\d+)?)\s*(?:\+)?\s*(?:years|yrs|year)', text.lower())
    if matches:
        return max([float(m) for m in matches])
    # fallback: look for "x - y years"
    match = re.search(r'(\d{1,2})\s*-\s*(\d{1,2})\s*years', text.lower())
    if match:
        return (float(match.group(1)) + float(match.group(2))) / 2.0
    return None

def rank_resumes(job_desc, resumes_texts, filenames, skills_list):
    # TF-IDF vectorize
    corpus = [job_desc] + resumes_texts
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    X = vectorizer.fit_transform(corpus)
    job_vec = X[0]
    resumes_vecs = X[1:]
    sims = cosine_similarity(job_vec, resumes_vecs).flatten()

    rows = []
    for fn, sim, text in zip(filenames, sims, resumes_texts):
        skills_found = extract_skills(text, skills_list)
        years = extract_years_experience(text)
        rows.append({
            "filename": fn,
            "score": float(sim),
            "matched_skills": ", ".join(skills_found) if skills_found else "",
            "years_experience": years if years is not None else ""
        })
    df = pd.DataFrame(rows).sort_values("score", ascending=False).reset_index(drop=True)
    df['years_experience'] = pd.to_numeric(df['years_experience'], errors='coerce')
    return df

# Streamlit UI
st.set_page_config(page_title="AI Resume Screening", layout="wide")
st.title("AI-Powered Resume Screening (TF-IDF + Cosine)")

st.markdown("Upload resumes (PDF, DOCX, TXT). Paste a job description (or upload a text file). Click **Run Screening**.")

# Job description input
job_text = st.text_area("Paste job description here", height=250)
job_file = st.file_uploader("Or upload job description (.txt)", type=["txt"], key="jobfile")

if job_file is not None:
    try:
        job_text = job_file.getvalue().decode("utf-8")
    except:
        job_text = job_file.getvalue().decode("latin-1")

# Resume upload
uploaded = st.file_uploader("Upload resumes (multiple)", type=["pdf","docx","txt"], accept_multiple_files=True)

if st.button("Run Screening"):
    if not job_text or len(job_text.strip()) < 20:
        st.error("Please provide a job description (paste or upload).")
    elif not uploaded:
        st.error("Please upload one or more resumes.")
    else:
        resumes_texts = []
        filenames = []
        for up in uploaded:
            b = up.getvalue()
            txt = parse_resume_bytes(b, up.name)
            resumes_texts.append(txt)
            filenames.append(up.name)
        with st.spinner("Processing and ranking..."):
            df = rank_resumes(job_text, resumes_texts, filenames, SKILLS)
        st.success("Done.")
        st.dataframe(df)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download ranked CSV", csv, file_name="ranked_resumes.csv", mime="text/csv")
        st.markdown("**Notes:** Scores are cosine similarity between the job description and the resume text (TF-IDF). Use the skills file to improve skill matching.")
