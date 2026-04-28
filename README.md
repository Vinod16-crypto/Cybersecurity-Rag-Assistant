# Cybersecurity RAG Assistant

A Flask web application that converts the notebook-based Cybersecurity Multi-Agent RAG idea into a portfolio-ready app.

## What it shows

- Flask web app with HTML, CSS, and JavaScript
- RAG pipeline using ChromaDB + HuggingFace embeddings
- Optional OpenAI LLM response generation
- Optional ML intrusion detection model trained from CSV
- Ready for Render deployment

## Recommended dataset

Use **UNSW-NB15** first because it is smaller and easier for training than full CICIDS2017. Use CICIDS2017 if you want a stronger but heavier project.

## Run locally

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# add your OPENAI_API_KEY in .env
python app.py
```

Open: http://127.0.0.1:5000

## Train ML model

```bash
python ml/train_model.py --csv data/your_intrusion_dataset.csv
```

This saves:

```text
models/intrusion_model.joblib
```

## Deploy on Render

1. Push this folder to GitHub.
2. Create a new Render Web Service.
3. Build command:

```bash
pip install -r requirements.txt
```

4. Start command:

```bash
gunicorn app:app
```

5. Add environment variable:

```text
OPENAI_API_KEY=your_key
```

## Project story for resume

Built an AI-powered cybersecurity assistant using Retrieval-Augmented Generation to answer threat, compliance, and incident-response questions from a cybersecurity knowledge base. Added an optional machine learning module for intrusion detection using network traffic datasets.
