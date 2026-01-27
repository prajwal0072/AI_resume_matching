# AI Resume–Job Matching System

🔗 Live Demo: https://airesumematching-prajwal.streamlit.app/

---

## 🚀 Project Overview

The **AI Resume–Job Matching System** is a web application that helps you compare a candidate’s resume against a job description using **natural language processing (NLP)** and **semantic similarity**. The system uses Python, Word2Vec embeddings, and skill extraction to compute how well a resume matches a given job description — providing both a **match percentage** and **skill gap analysis**.

This tool is useful for:
- Job seekers evaluating fit for a role
- Recruiters screening resumes
- HR teams automating applicant comparisons

---

## 💡 How It Works

1. **Upload Resume (PDF)**  
   The app extracts text from your uploaded PDF resume using PyMuPDF (`fitz`).

2. **Paste Job Description**  
   Enter the text of a job posting or JD.

3. **Analyze Match**  
   A neural embedding (Word2Vec) model compares semantic meaning between resume and JD tokens.

4. **Results Displayed**
   - ⚡ **Match Percentage**
   - 🎯 **Recommendation** (Good / Average / Poor)
   - ✅ **Matched Skills**
   - ❌ **Missing Skills**

---

## 🧪 Example Use

1. Upload your resume PDF.
2. Paste a job description like:

