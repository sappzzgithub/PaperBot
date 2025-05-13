# qa_engine.py

import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyDUEbgFtW_ZCPQFOtE2TqyeTFs48f4ix6M"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")  # New lightweight model

# Select top-k relevant chunks (basic filtering)
def get_relevant_chunks(question, chunks, top_k=3):
    relevant_chunks = sorted(chunks, key=lambda x: question.lower() in x.lower(), reverse=True)
    return relevant_chunks[:top_k]

# Construct the prompt
def build_prompt(question, relevant_chunks):
    context = "\n\n".join(relevant_chunks)
    return f"""You are a helpful assistant. Use the following research paper context to answer the question clearly and simply.

Context:
{context}

Question: {question}
"""

# Generate answer using Gemini Pro
def answer_question(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API Error: {e}"
