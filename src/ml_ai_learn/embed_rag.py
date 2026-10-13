import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
from numpy import dot
import numpy as np

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

def cosine_similarity(a,b):
   return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
model=SentenceTransformer('all-MiniLM-L6-v2')
text="Saniya is a software engineer at SAP"
res=model.encode(text)
print(res.shape)

t1="all-MiniLM-L6-v2 is a sentence transformer model"
t2="Saniya is a software developer at SAP Labs"

v1=model.encode(t1)
v2=model.encode(t2)
similarity=cosine_similarity(v1,v2)
print(f"Cosine similarity between '{t1}' and '{t2}': {similarity}")