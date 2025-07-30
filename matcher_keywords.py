import numpy as np

def extract_matching_keywords(resume, jd, vectorizer):
    features = np.array(vectorizer.get_feature_names_out())
    resume_vec = vectorizer.transform([resume]).toarray()[0]
    jd_vec = vectorizer.transform([jd]).toarray()[0]
    common = (resume_vec > 0) & (jd_vec > 0)
    return features[common]