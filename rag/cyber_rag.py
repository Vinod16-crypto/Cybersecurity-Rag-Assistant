from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
import os

# 1. Load PDFs from data/docs folder
pdf_folder = "data/docs"
documents = []

for file_name in os.listdir(pdf_folder):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(pdf_folder, file_name)
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())

# 2. Split PDF text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=80
)

chunks = text_splitter.split_documents(documents)

# 3. Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Store chunks in Chroma vector database
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 6. RAG answer function
def rag_answer(question):
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    if not context.strip():
        return {
            "answer": "This question is outside my cybersecurity knowledge scope.",
            "context": ""
        }

    context = context[:600]

    prompt = f"""
You are a professional cybersecurity assistant.

Instructions:
- Use ONLY the provided context
- Answer clearly and concisely
- Use bullet points where helpful
- Do NOT repeat the context
- Do NOT hallucinate
- If unsure → say it's outside scope
- Keep answers under 120 words

Context:
{context}

Question:
{question}

Give a clean, professional answer:
"""

    try:
        response = llm.invoke(prompt)

        return {
            "answer": response.content,
            "context": context
        }

    except Exception as e:
        print("ERROR:", e)

        return {
            "answer": "⚠️ AI service unavailable. Showing retrieved cybersecurity knowledge only.",
            "context": context
        }