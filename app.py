import streamlit as st
from ats_scorer import calculate_ats_score, missing_keywords
from resume_generator import professional_template, minimal_template, fresher_template
from generators.docx_generator import create_docx
from generators.pdf_generator import create_pdf

# -------------------------------------------------
# PAGE CONFIG (MUST BE AT TOP)
# -------------------------------------------------
st.set_page_config(page_title="ATS Resume Builder", layout="wide")
st.title("📄 ATS Resume Builder")

# -------------------------------------------------
# TEMPLATE SELECTION (CANVA-LIKE)
# -------------------------------------------------
st.header("Choose Resume Template")

if "template" not in st.session_state:
    st.session_state.template = "professional"

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/professional.png", caption="Professional")
    if st.button("Use Professional"):
        st.session_state.template = "professional"

with col2:
    st.image("assets/minimal.png", caption="Minimal")
    if st.button("Use Minimal"):
        st.session_state.template = "minimal"

with col3:
    st.image("assets/fresher.png", caption="Fresher")
    if st.button("Use Fresher"):
        st.session_state.template = "fresher"

template = st.session_state.template

# -------------------------------------------------
# USER PROFILE INPUT
# -------------------------------------------------
st.header("Step 1: Enter Your Profile")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")

summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma separated)")

# -------------------------------------------------
# EDUCATION (STRUCTURED – ATS SAFE)
# -------------------------------------------------
st.subheader("Education")

degree = st.text_input("Degree (Current / Completed)")
college = st.text_input("College / University")
degree_year = st.text_input("Year / Expected Year")
cgpa = st.text_input("CGPA / Percentage")

st.markdown("### Class 12")
board_12 = st.text_input("Board (12th)")
percent_12 = st.text_input("Percentage (12th)")

st.markdown("### Class 10")
board_10 = st.text_input("Board (10th)")
percent_10 = st.text_input("Percentage (10th)")

# -------------------------------------------------
# PROFILE DICTIONARY
# -------------------------------------------------
profile = {
    "name": name,
    "email": email,
    "phone": phone,
    "summary": summary,
    "skills": skills,
    "degree": degree,
    "college": college,
    "degree_year": degree_year,
    "cgpa": cgpa,
    "board_12": board_12,
    "percent_12": percent_12,
    "board_10": board_10,
    "percent_10": percent_10,
}

# -------------------------------------------------
# JOB DESCRIPTION INPUT
# -------------------------------------------------
st.header("Step 2: Job Description")
jd_text = st.text_area("Paste Job Description")

# -------------------------------------------------
# RESUME GENERATION
# -------------------------------------------------
if st.button("Generate Resume"):

    # Generate resume based on selected template
    if template == "professional":
        resume_text = professional_template(profile)
    elif template == "minimal":
        resume_text = minimal_template(profile)
    else:
        resume_text = fresher_template(profile)

    st.subheader("Generated Resume")
    st.text(resume_text)

    # ATS Score
    if jd_text.strip():
        score = calculate_ats_score(resume_text, jd_text)
        st.metric("ATS Score", f"{score}%")
        st.write("Missing Keywords:", missing_keywords(resume_text, jd_text))

    # -------------------------------------------------
    # DOWNLOAD OPTIONS
    # -------------------------------------------------
    docx_path = create_docx(resume_text)
    with open(docx_path, "rb") as f:
        st.download_button(
            "Download DOCX",
            f,
            file_name="ATS_Resume.docx"
        )

    pdf_path = create_pdf(resume_text)
    with open(pdf_path, "rb") as f:
        st.download_button(
            "Download PDF",
            f,
            file_name="ATS_Resume.pdf"
        )
