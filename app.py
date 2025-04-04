# app.py

import streamlit as st
from PyPDF2 import PdfReader
import os
from sentence_transformers import SentenceTransformer
import numpy as np
import tempfile

from qa_engine import get_relevant_chunks, build_prompt, answer_question

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

st.title("📄 PaperBot - Research Paper Chat Assistant")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Extract text from PDF
    reader = PdfReader(tmp_path)
    raw_text = ""
    for page in reader.pages:
        raw_text += page.extract_text()

    # Break into chunks
    text_chunks = raw_text.split("\n\n")
    embeddings = embedder.encode(text_chunks)

    st.success("✅ Paper uploaded and processed!")

    question = st.text_input("Ask a question about the paper:")

    if question:
        # ✅ FIX: Pass question instead of top_k here
        relevant_chunks = get_relevant_chunks(question, text_chunks)
        prompt = build_prompt(question, relevant_chunks)
        answer = answer_question(prompt)

        st.subheader("🧠 Answer")
        st.write(answer)
