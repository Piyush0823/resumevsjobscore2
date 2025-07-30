import streamlit as st
from matcher_preprocessing import preprocess
from matcher_similarity import get_similarity_score
from matcher_keywords import extract_matching_keywords

st.title("Resume vs Job Description Matcher & Score Generator")

resume_text = st.text_area("Paste your Resume(skills)", height=200)
jd_text = st.text_area("Paste Job Description", height=200)

if st.button("Match & Score"):
    if resume_text.strip() and jd_text.strip():
        resume = preprocess(resume_text)
        jd = preprocess(jd_text)
        score, vectorizer = get_similarity_score(resume, jd)
        st.metric(label="Similarity Score", value=f"{score:.2f}")
        keywords = extract_matching_keywords(resume, jd, vectorizer)
        st.markdown("**Matching Keywords:**")
        if len(keywords) > 0:
            st.write(", ".join(keywords))
        else:
            st.write("No significant keyword overlap found.")
    else:
        st.warning("Please paste both your resume and the job description.")
