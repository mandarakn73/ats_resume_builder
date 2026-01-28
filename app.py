import streamlit as st
from ats_scorer import calculate_ats_score, missing_keywords
from resume_generator import generate_resume

st.set_page_config(page_title="ATS Resume Builder", layout="wide")

st.title("📄 ATS Resume Builder")

profile = {
    "name": st.text_input("Full Name"),
    "email": st.text_input("Email"),
    "phone": st.text_input("Phone"),
    "summary": st.text_area("Summary"),
    "skills": st.text_area("Skills"),
    "experience": st.text_area("Experience"),
    "projects": st.text_area("Projects"),
    "education": st.text_area("Education")
}

jd_text = st.text_area("Job Description")

if st.button("Generate Resume"):
    resume_text = generate_resume(profile)
    st.text(resume_text)

    if jd_text:
        score = calculate_ats_score(resume_text, jd_text)
        st.metric("ATS Score", f"{score}%")
        st.write("Missing Keywords:", missing_keywords(resume_text, jd_text))

    st.download_button("Download Resume", resume_text, "ATS_Resume.txt")
