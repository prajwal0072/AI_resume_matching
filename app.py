import streamlit as st
from preprocess import preprocess_text
from skill_extractor import extract_skills
from resume_parser import extract_text_from_pdf
from matcher import calculate_match_score

# Page configuration
st.set_page_config(
    page_title="AI Resume–Job Matcher",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume–Job Matching System")

st.write(
    "Upload your resume and paste the job description to "
    "see how well they match using NLP and Word2Vec."
)

# Upload resume
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Job description input
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# ✅ Submit button (NEW)
submit = st.button("🔍 Analyze Resume")

# Run analysis ONLY when button is clicked
if submit:
    if resume_file and job_description:
        with st.spinner("Analyzing resume and job description..."):

            # Step 1: Extract resume text
            resume_text = extract_text_from_pdf(resume_file)

            # Step 2: Preprocess text
            resume_tokens = preprocess_text(resume_text)
            jd_tokens = preprocess_text(job_description)

            # Step 3: Skill extraction
            resume_skills = extract_skills(resume_tokens)
            jd_skills = extract_skills(jd_tokens)
            missing_skills = list(set(jd_skills) - set(resume_skills))

            # Step 4: Match score
            match_score = calculate_match_score(
                resume_tokens,
                jd_tokens
            )

        # Display results
        st.success(f"Match Percentage: {match_score}%")

        if match_score >= 80:
            st.info("✅ Recommendation: Good Match")
        elif match_score >= 50:
            st.warning("⚠️ Recommendation: Average Match")
        else:
            st.error("❌ Recommendation: Poor Match")

        st.subheader("✅ Matched Skills")
        if resume_skills:
            st.write(resume_skills)
        else:
            st.write("No matching skills found.")

        st.subheader("❌ Missing Skills")
        if missing_skills:
            st.write(missing_skills)
        else:
            st.write("No missing skills. Great fit!")
    else:
        st.warning("⚠️ Please upload a resume and paste a job description.")
