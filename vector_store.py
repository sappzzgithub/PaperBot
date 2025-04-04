# vector_store.py
import faiss
import numpy as np

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def search_faiss_index(index, query_embedding, k=3):
    distances, indices = index.search(np.array([query_embedding]), k)
    return indices[0]
