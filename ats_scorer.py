from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)

def missing_keywords(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    return list(jd_words - resume_words)[:15]
