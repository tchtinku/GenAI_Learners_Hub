import PyPDF2
import re
from pathlib import Path
from src.config import RESUMES_DIR, JOB_DESCRIPTIONS_DIR
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    """Extract text from Streamlit UploadedFile object"""
    pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.getvalue()))
    return " ".join([page.extract_text() for page in pdf_reader.pages])

def clean_text(text):
    """Clean and normalize text"""
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'[^\w\s-]', '', text)  # Remove special chars
    return text.lower()

def load_sample_jds():
    """Load all job descriptions from directory"""
    jds = {}
    for jd_file in JOB_DESCRIPTIONS_DIR.glob("*.txt"):
        with open(jd_file, 'r') as f:
            jds[jd_file.stem] = clean_text(f.read())
    return jds