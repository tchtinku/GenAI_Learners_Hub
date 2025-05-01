from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Data paths
RESUMES_DIR = BASE_DIR / "data" / "resumes"
JOB_DESCRIPTIONS_DIR = BASE_DIR / "data" / "job_descriptions"
INDEX_PATH = BASE_DIR / "data" / "faiss_index.index"