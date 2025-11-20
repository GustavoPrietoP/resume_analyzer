import streamlit as st
import ollama
import PyPDF2
import docx2txt
import re
import os

# Config
MODEL = "llama3.1:8b"  # change to any model you pulled

st.title("🚀 AI Resume Analyzer")
st.markdown("Upload a resume and paste a job description → get instant match score & feedback")

# File uploader
resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste the Job Description", height=300)

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

if resume_file and job_desc:
    # Extract resume text
    if resume_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(resume_file)
    else:
        resume_file.seek(0)
        resume_text = extract_text_from_docx(resume_file)

    resume_text = clean_text(resume_text)

    with st.spinner("Analyzing resume with AI..."):
        prompt = f"""
You are an expert technical recruiter.
Here is the candidate's resume:
\"\"\"{resume_text}\"\"\"

Here is the job description:
\"\"\"{job_desc}\"\"\"

Analyze and return your answer **strictly in this JSON format only** (no extra text):

{{
  "match_score": <0-100 integer>,
  "summary": "<2-sentence overall fit summary>",
  "strengths": ["bullet 1", "bullet 2", ...],
  "gaps": ["missing skill or experience 1", "missing skill or experience 2", ...],
  "recommendations": ["suggestion 1", "suggestion 2", ...],
  "ats_friendly": true/false,
  "ats_issues": ["issue 1", "issue 2", ...] or []
}}

Be honest and critical.
"""

        response = ollama.chat(model=MODEL, messages=[{'role': 'user', 'content': prompt}])
        raw = response['message']['content']

        # Try to extract JSON (LLMs sometimes add extra text)
        try:
            import json
            json_start = raw.find("{")
            json_end = raw.rfind("}") + 1
            result = json.loads(raw[json_start:json_end])
        except:
            st.error("AI returned malformed response. Try again.")
            st.code(raw)
            result = None

        if result:
            st.success(f"Match Score: **{result['match_score']}/100**")
            st.metric("Fit Score", f"{result['match_score']}%")

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("✅ Strengths")
                for s in result['strengths']:
                    st.write("• " + s)
            with col2:
                st.subheader("⚠️ Gaps / Missing")
                for g in result['gaps']:
                    st.write("• " + g)

            st.subheader("💡 Recommendations")
            for r in result['recommendations']:
                st.write("• " + r)

            st.subheader("📋 ATS Check")
            if result['ats_friendly']:
                st.success("Resume is ATS-friendly")
            else:
                st.warning("Potential ATS issues:")
                for issue in result['ats_issues']:
                    st.write("• " + issue)

            with st.expander("Show full parsed resume text"):
                st.text(resume_text[:4000] + "...")

# Run with: streamlit run resume_analyzer.py
