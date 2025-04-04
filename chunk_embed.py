# chunk_embed.py
from sentence_transformers import SentenceTransformer
import numpy as np

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def embed_chunks(chunks, model):
    return model.encode(chunks, show_progress_bar=True)
