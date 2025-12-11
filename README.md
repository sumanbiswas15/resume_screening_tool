# AI-Powered Resume Screening Tool

An AI-powered resume screening web application built with Streamlit. It uses TF-IDF vectorization and cosine similarity to automatically rank resumes based on a given job description. The tool supports PDF, DOCX, and TXT resumes, extracts skills using a predefined skills list, and provides a ranked output with similarity scores, matched skills, and experience details. Includes CSV export for easy reporting.

## Features

- **Resume Upload**: Supports PDF, DOCX, and TXT formats.
- **Job Description Input**: Paste or upload a job description text file.
- **Ranking Algorithm**: Uses TF-IDF and cosine similarity for scoring resumes based on text similarity.
- **Skill Extraction**: Matches skills from resumes against a comprehensive skills list (`skills.txt`).
- **Output**: Displays a ranked table with scores, matched skills, and years of experience.
- **Downloadable Results**: Export ranked resumes as CSV.

## How It Works

1. **Text Extraction**: Parses uploaded resumes to extract plain text.
2. **Vectorization**: Applies TF-IDF to the job description and all resume texts.
3. **Similarity Calculation**: Computes cosine similarity between job vector and each resume vector to get scores.
4. **Skill Matching**: Searches for skills in resume text using substring matching.
5. **Ranking**: Sorts resumes by similarity score in descending order.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd resume_screening_tool
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download spaCy model:
   ```
   python -m spacy download en_core_web_sm
   ```

4. Run the application:
   ```
   streamlit run app.py
   ```

5. Open the provided URL (usually `http://localhost:8501`) in your browser.

## Usage

1. Paste or upload a job description.
2. Upload one or more resumes (PDF, DOCX, TXT).
3. Click "Run Screening" to process and rank resumes.
4. View the results table and download the CSV if needed.

## Skills List

The `skills.txt` file contains a list of skills used for matching. It has been expanded to include a wide range of technical and soft skills for better accuracy.

## Screenshots

### Screenshot 1: Main Interface
![Main Interface](Screenshot%202025-10-09%20132123.png)

### Screenshot 2: Results View
![Results View](Screenshot%202025-10-09%20132209.png)

## Dependencies

- streamlit
- pandas
- scikit-learn
- pdfplumber
- python-docx
- spacy

## Notes

- Scores represent cosine similarity (0-1) between job description and resume texts using TF-IDF.
- Skills matching improves by using the skills file for substring-based extraction.
- For best results, ensure job descriptions and resumes are in English.

## License

[Add license if applicable]
