# Resume vs Job Description Matcher & Score Generator

A simple Streamlit app to match resume content against a job description using TF-IDF and cosine similarity, highlighting common keywords.

## Features

- Paste your resume and job description.
- Get a similarity score.
- See overlapping keywords.

## Install & Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Start the app:
    ```
    streamlit run app.py
    ```

## Files

- `app.py`: Streamlit UI.
- `matcher/`: Logic modules.
    - `preprocessing.py`: Basic text cleaning.
    - `similarity.py`: Vectorizing & scoring.
    - `keywords.py`: Keyword extraction.

## Customization

Expand preprocessing, support more advanced NLP, or add resume/job description upload features as needed!