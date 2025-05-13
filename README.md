# PaperBot 🧠📚 - AI Research Paper Assistant

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Sentence-Transformers](https://img.shields.io/badge/Sentence_Transformers-000000?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

PaperBot is an AI-powered chatbot that helps you interact with research papers through natural language questions. It can process various document formats and provide intelligent answers based on the paper's content.

## ✨ Features

- **Multi-format Support**: Upload PDFs, Word documents, and other research paper formats
- **Natural Language Interface**: Ask questions in plain English about the paper
- **Gemini Flash 2.0 API**: Powered by Google's advanced AI for high-quality responses
- **Semantic Search**: Sentence Transformers for accurate document understanding
- **User-friendly Interface**: Simple Streamlit web interface
- **Research-focused**: Designed specifically for academic papers

## 🛠️ Technologies Used

- **Backend**: 
  - Google Gemini API
  - Sentence Transformers (all-MiniLM-L6-v2)
  
- **Frontend**: 
  - Streamlit
  
- **Document Processing**:
  - PyPDF2 (for PDF parsing)
  - python-docx (for Word documents)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google API key (for Gemini)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sangsthita/Research-BOT-.git
   cd PaperBot-


### Steps to run the Project on your machine 

1. Assuming that you have cloned the repository from github got the folder Research-BOT folder 

2. Inside the folder run this command 
   ```bash
    pip install -r .\requirements.txt

3. Now you are ready with the necessary required libs next run the streamlit application 
   ```bash
   streamlit run app.py

