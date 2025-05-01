import streamlit as st
from src.embedder import ResumeMatcher
from src.utils import extract_text_from_pdf, load_sample_jds
import os

# Initialize matcher
matcher = ResumeMatcher()

# UI Setup
st.set_page_config(page_title="AI Resume Matcher", layout="wide")
st.title("🔍 AI Resume Matcher")
st.markdown("""*"Why apply to 100 jobs when AI can find the best 5?"*""")

# File Upload
resume_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

if resume_file:
    try:
        resume_text = extract_text_from_pdf(resume_file)
        jds = load_sample_jds()
        
        if st.button("Find Matching Jobs"):
            if not jds:
                st.warning("No job descriptions found. Add some TXT files to data/job_descriptions/")
            else:
                matcher.build_index(list(jds.values()))
                matches = matcher.match_resume(resume_text)
                
                st.subheader("Your Top Matches:")
                for idx, score in matches:
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.metric(label="Match Score", value=f"{score*100:.1f}%")
                    with col2:
                        job_title = list(jds.keys())[idx]
                        with st.expander(f"{job_title}"):
                            st.write(jds[job_title])
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

# Sidebar
with st.sidebar:
    st.header("How It Works")
    st.markdown("""
    1. Upload your resume (PDF)
    2. We analyze its content
    3. Match against job descriptions
    4. Get your top 3 matches
    """)
    st.markdown("---")
    st.markdown("💡 **Tip:** Add more job descriptions as `.txt` files in `data/job_descriptions/`")