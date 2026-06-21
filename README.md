# TalentMatch AI - Resume Screening and Candidate Ranking System

## Introduction

Recruitment is a time-consuming process, especially when recruiters have to manually go through hundreds of resumes for a single job opening. The objective of this project is to automate the initial screening process by using Artificial Intelligence and Natural Language Processing techniques.

TalentMatch AI is a resume screening system that compares candidate resumes with a given job description and ranks applicants based on their suitability for the role. The system also highlights matching skills, missing skills, and provides a recommendation that can help recruiters make faster decisions.

---

## Objectives

* Automate resume screening.
* Reduce manual effort during recruitment.
* Match resumes with job requirements.
* Rank candidates according to their relevance.
* Provide explainable results instead of only a score.

---

## Features

* Upload multiple PDF resumes.
* Enter any job description.
* Automatic text extraction from resumes.
* Skill matching and gap analysis.
* Candidate ranking based on semantic similarity.
* Hiring recommendation generation.
* Downloadable ranking report.
* Interactive dashboard built using Streamlit.

---

## Technology Stack

**Frontend**

* Streamlit

**Backend**

* Python

**Libraries Used**

* Sentence Transformers
* spaCy
* Scikit-learn
* Pandas
* NumPy
* PyMuPDF
* PyTorch

---

## Project Workflow

### Step 1: Job Description Input

The recruiter enters a job description containing the required skills, education, and experience.

### Step 2: Resume Upload

One or more candidate resumes are uploaded in PDF format.

### Step 3: Resume Parsing

The system extracts text from the uploaded resumes using PyMuPDF.

### Step 4: Requirement Extraction

The job description is analyzed to identify important skills, educational qualifications, and experience requirements.

### Step 5: Candidate Evaluation

Sentence Transformer embeddings are generated for both the resume and job description. Semantic similarity is then calculated to determine how closely the resume matches the job requirements.

### Step 6: Skill Analysis

The system identifies:

* Matched Skills
* Missing Skills
* Skill Match Percentage

### Step 7: Ranking

All uploaded candidates are ranked according to their overall score.

### Step 8: Recommendation

Based on the final score, the system provides a recommendation such as:

* Strongly Recommended
* Recommended
* Consider
* Not Recommended

---

## Folder Structure

TalentMatch_AI/

├── backend/

├── frontend/

├── data/

├── models/

├── notebooks/

├── requirements.txt

└── README.md

---

## How to Run the Project

1. Clone the repository.

```bash
git clone [repository-link](https://github.com/palpriyadarshini-pixel/TalentMatch_AI.git)
```

2. Create a virtual environment.

```bash
python -m venv venv
```

3. Activate the environment.

```bash
venv\Scripts\activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Download the spaCy model.

```bash
python -m spacy download en_core_web_sm
```

6. Run the application.

```bash
streamlit run frontend/streamlit_app.py
```

---

## Results

The system successfully:

* Processes multiple resumes simultaneously.
* Extracts information from PDF files.
* Matches resumes with job descriptions.
* Ranks candidates automatically.
* Generates explanations for the ranking.

---

## Future Scope

Some possible improvements for future versions include:

* OCR support for scanned resumes.
* Resume recommendation and feedback system.
* Integration with LinkedIn profiles.
* AI-generated interview questions.
* Support for additional file formats such as DOCX.
* Fine-tuned transformer models for specific industries.

---

## Conclusion

TalentMatch AI demonstrates how Artificial Intelligence can be applied to recruitment and talent acquisition. By combining NLP techniques, semantic similarity, and skill analysis, the system helps recruiters identify suitable candidates more efficiently. The project reduces manual screening effort and provides a structured approach to candidate evaluation.
