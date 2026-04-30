# 🔐 SecureAI: Cybersecurity RAG Assistant

An AI-powered web application that answers cybersecurity questions using Retrieval-Augmented Generation (RAG) with real-world documents from CISA, NIST, and OWASP.

---

## 🚀 Project Overview

SecureAI is a chatbot-style assistant that helps users understand cybersecurity concepts using trusted sources.

Instead of guessing answers, the system:
- Retrieves relevant content from PDF documents
- Uses that context to generate accurate responses
- Avoids answering outside its knowledge scope

---

## 🧠 Key Features

- 💬 Chat-style web interface (Flask)
- 📄 Real document-based answers (PDF RAG)
- 🔍 Context retrieval using embeddings
- 🧠 LLM integration (Groq - LLaMA 3)
- ⚠️ Safe fallback for out-of-scope questions
- ⚡ Fast and lightweight architecture

---

## ⚙️ How It Works

1. User enters a question  
2. System searches relevant text from PDFs  
3. Context is passed to the LLM  
4. LLM generates a grounded answer  

---

## 🏗️ Tech Stack

**Backend**
- Python
- Flask

**AI / RAG**
- LangChain
- ChromaDB (Vector Database)
- HuggingFace Embeddings
- Groq API (LLaMA 3)

**Frontend**
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

---

## ⚙️ Setup Instructions

### 1. Clone repository

---

### 2. Install dependencies

---

### 3. Add API Key

Create a `.env` file:

---

### 4. Run the app

Open in browser:

---

## 💡 Example Questions

- What is phishing?
- What is the NIST Cybersecurity Framework?
- What should I do if I receive a suspicious email?
- What is malware?

---

## ⚠️ Limitations

- Answers only from provided documents
- No real-time cybersecurity updates
- Limited to knowledge base scope

---

## 📸 Screenshots

![App Screenshot](https://github.com/Vinod16-crypto/Cybersecurity-Rag-Assistant/blob/main/RAG%20Screenshot.pdf)
https://github.com/Vinod16-crypto/Cybersecurity-Rag-Assistant/blob/main/RAG%20Screenshot%20II.pdf

---

## 📌 Future Improvements

- Cloud deployment (Render / AWS)
- Chat history support
- More cybersecurity datasets
- User authentication

---

## 👨‍💻 Author

Vinod  
Aspiring Data Scientist / AI Engineer

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐