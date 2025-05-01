from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from pathlib import Path
from src.config import INDEX_PATH

class ResumeMatcher:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self._initialize_index()
    
    def _initialize_index(self):
        """Initialize or load existing FAISS index"""
        if INDEX_PATH.exists():
            self.load_index()
        else:
            self.index = faiss.IndexFlatL2(384)  # Dimension for all-MiniLM-L6-v2
    
    def embed_text(self, text):
        return self.model.encode(text, convert_to_tensor=False)
    
    def build_index(self, job_descriptions):
        """Create and save FAISS index"""
        embeddings = np.array([self.embed_text(jd) for jd in job_descriptions]).astype('float32')
        self.index = faiss.IndexFlatL2(384)
        self.index.add(embeddings)
        self.save_index()
    
    def match_resume(self, resume_text, top_k=3):
        """Find top matching jobs"""
        if self.index is None:
            raise ValueError("Index not initialized. Call build_index() first.")
            
        resume_embedding = self.embed_text(resume_text).reshape(1, -1)
        distances, indices = self.index.search(resume_embedding.astype('float32'), top_k)
        return [(indices[0][i], 1 - distances[0][i]) for i in range(top_k)]
    
    def save_index(self):
        faiss.write_index(self.index, str(INDEX_PATH))
    
    def load_index(self):
        self.index = faiss.read_index(str(INDEX_PATH))