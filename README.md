# AI-Powered Resume Screening Tool

A production-ready AI-based resume screening web application that automatically analyzes and ranks resumes against a given job description using Natural Language Processing (NLP) techniques. This tool leverages TF-IDF vectorization and cosine similarity to provide accurate, efficient candidate shortlisting.

Built with Python and Streamlit, containerized using Docker, automated via Jenkins CI/CD, and deployed on Render Cloud for seamless scalability.

## Table of Contents

- [Live Deployment](#live-deployment)
- [Key Features](#key-features)
- [How the System Works](#how-the-system-works)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Run with Docker](#run-with-docker)
- [Screenshots](#screenshots)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Live Deployment

- **Live App (Render):** [https://resume-screening-app-t5k6.onrender.com](https://resume-screening-app-t5k6.onrender.com))
- **Docker Hub Image:** [https://hub.docker.com/r/sumanbiswas22/resume-screening-app](https://hub.docker.com/r/sumanbiswas22/resume-screening-app)

## Key Features

- **Multi-Format Resume Upload:** Supports PDF, DOCX, and TXT formats for flexible resume submission.
- **Job Description Input:** Accepts pasted text or uploaded text files for job descriptions.
- **Intelligent Ranking:** Utilizes TF-IDF vectorization and cosine similarity for precise resume-job matching.
- **Skill Extraction and Matching:** Automatically identifies and matches skills from a comprehensive predefined list.
- **Detailed Output:** Displays ranked candidates with similarity scores, matched skills, and experience details.
- **Export Functionality:** Download screening results as CSV for further analysis or reporting.
- **Containerization:** Fully Dockerized for easy deployment and portability.
- **CI/CD Automation:** Integrated Jenkins pipeline for continuous integration and deployment.
- **Cloud Deployment:** Hosted on Render for reliable, scalable cloud access.

## How the System Works

1. **Resume Parsing:** Extracts raw text from uploaded resume files using specialized libraries for each format.
2. **Text Vectorization:** Converts job descriptions and resumes into numerical vectors using TF-IDF, capturing term importance.
3. **Similarity Calculation:** Computes cosine similarity scores between the job description vector and each resume vector.
4. **Skill Matching:** Performs substring-based matching against a curated skills dataset to identify relevant competencies.
5. **Ranking and Output:** Sorts resumes by similarity score in descending order, presenting a ranked list with additional insights.

## Tech Stack

| Category          | Technology     |
|-------------------|----------------|
| Frontend          | Streamlit      |
| Backend           | Python         |
| Machine Learning  | Scikit-learn   |
| NLP               | spaCy          |
| Containerization  | Docker         |
| CI/CD             | Jenkins        |
| Cloud Deployment  | Render         |
| Image Registry    | Docker Hub     |

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd resume_screening_tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the spaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Access the app at `http://localhost:8501` in your web browser.

## Usage

1. Input a job description by pasting text or uploading a `.txt` file.
2. Upload one or more resumes in PDF, DOCX, or TXT format.
3. Click "Run Screening" to initiate the analysis.
4. Review the ranked results table, including scores, matched skills, and experience.
5. Optionally, download the results as a CSV file.

## Run with Docker (Recommended)

Pull and run the pre-built Docker image:

```bash
docker pull sumanbiswas22/resume-screening-app:latest
docker run -p 8501:8501 sumanbiswas22/resume-screening-app:latest
```

Access the application at `http://localhost:8501`.

## Screenshots

### Main Interface
![Main Interface](Screenshot%202025-10-09%20132123.png)

### Results View
![Results View](Screenshot%202025-10-09%20132209.png)

## Notes

- Similarity scores range from 0 to 1, representing cosine similarity between the job description and resume texts using TF-IDF.
- Skill matching accuracy is enhanced through substring-based extraction from the `skills.txt` file.
- For optimal results, ensure all input texts are in English and well-formatted.

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. Ensure all changes include appropriate tests and documentation updates.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
