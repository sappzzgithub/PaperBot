import streamlit as st
from PyPDF2 import PdfReader
import os
from sentence_transformers import SentenceTransformer
import numpy as np
import tempfile
from qa_engine import get_relevant_chunks, build_prompt, answer_question
from docx import Document
import base64

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Set page config
st.set_page_config(
    page_title="PaperBot",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# === Background Setup ===
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        color: #f1f1f1;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the path to your background image (use raw string)
set_background(r"/Users/sakshizanjad/Desktop/DeepLearning /Research-BOT-/bg/backgrndimage.avif")

# === Custom CSS for better readability ===
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        color: #f1f1f1;
    }
    .stTextInput > div > div > input {
        background-color: #1f2937;
        color: #f1f1f1;
    }
    .stFileUploader {
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #374151;
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📘 About PaperBot")
    st.markdown("""
        PaperBot is your AI-powered assistant to interact with research papers.  
        Upload a PDF, Word, or Text file, ask any question, and get context-aware answers.
    """)
    st.markdown("#### 📌 Steps to Proceed")
    st.markdown("""
    1. Upload a research paper (PDF, DOCX, or TXT)  
    2. Wait for it to process  
    3. Ask a question related to the paper  
    4. View the Generated answer based on the paper
    """)

# Main Title
st.markdown("<h1 style='text-align: center;'>📄 PaperBot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #d1d5db;'>Your AI-Powered Research Paper Chat Assistant</h4><br>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("📤 Upload a research paper (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

def extract_text_from_file(file_path, file_type):
    raw_text = ""
    if file_type == "pdf":
        reader = PdfReader(file_path)
        for page in reader.pages:
            raw_text += page.extract_text()
    elif file_type == "docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            raw_text += para.text + "\n"
    elif file_type == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
    return raw_text

if uploaded_file is not None:
    with st.spinner("Processing your paper..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        file_type = uploaded_file.name.split(".")[-1].lower()
        raw_text = extract_text_from_file(tmp_path, file_type)

        text_chunks = raw_text.split("\n\n")
        embeddings = embedder.encode(text_chunks)

        st.success("✅ Document uploaded and processed!")

        # Metadata
        st.markdown("#### 📑 File Metadata")
        st.markdown(f"- **File Type:** `{file_type.upper()}`")
        st.markdown(f"- **File Size:** {os.path.getsize(tmp_path) / 1024:.2f} KB")

        # Ask a question
        question = st.text_input("💬 Ask a question about the document:")

        if question:
            relevant_chunks = get_relevant_chunks(question, text_chunks)
            prompt = build_prompt(question, relevant_chunks)
            answer = answer_question(prompt)

            st.markdown("### 🧠 Answer")
            st.markdown(f"> {answer}", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr style="border: 1px solid #374151; margin-top: 60px;"/>
    <div style='text-align: center; color: #9CA3AF; font-size: 14px; margin-top: 20px;'>
        Made with ❤️ by 
        <a href="https://in.linkedin.com/in/sakshi-zanjad-a036a7279" style="color: #60A5FA; text-decoration: none;" target="_blank"><b>Sakshi Zanjad</b></a>, 
        <a href="https://in.linkedin.com/in/sangsthita-panda-55a869190" style="color: #60A5FA; text-decoration: none;" target="_blank"><b>Sangstitha Panda</b></a>, and 
        <a href="https://in.linkedin.com/in/archit-gupta-23ab7b1a3" style="color: #60A5FA; text-decoration: none;" target="_blank"><b>Archit Gupta</b></a>
    </div>
""", unsafe_allow_html=True)
