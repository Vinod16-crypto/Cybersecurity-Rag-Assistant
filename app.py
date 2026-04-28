from unittest import result

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, jsonify
from rag.cyber_rag import rag_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({
            "answer": "No question provided",
            "context": ""
        })

    result = rag_answer(question)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)