# 📘 NCERT Study Assistant — RAG v2.0

A production-style **Retrieval-Augmented Generation (RAG)** system that answers questions from the NCERT Class 9 Science textbook using **semantic search (embeddings) + vector database + LLM grounding**.

---

## 🚀 Overview

This project upgrades a basic QA system to **Version 2.0** by introducing:

- Structure-aware chunking
- Dense embeddings (semantic search)
- Vector database retrieval (Chroma)
- Grounded LLM responses (Groq + Llama)
- Honest evaluation (including out-of-scope handling)

The system retrieves relevant textbook content and generates **context-grounded answers**, reducing hallucination and improving reliability.

---

## 🧠 Key Features

- 📄 **PDF → Structured Text** using OpenDataLoader
- ✂️ **Chunking with overlap** for better context retention
- 🔍 **Semantic Retrieval** using HuggingFace embeddings
- 🗄️ **Chroma Vector DB** for fast similarity search
- 🤖 **LLM QA (Groq / Llama3)** with retrieval grounding
- 📊 **Evaluation pipeline** with in-scope + out-of-scope questions

---

## ⚙️ Tech Stack

| Component        | Tool Used                          |
|-----------------|------------------------------------|
| Framework        | LangChain                          |
| Loader           | OpenDataLoader-PDF                 |
| Chunking         | RecursiveCharacterTextSplitter     |
| Embeddings       | HuggingFace (Sentence Transformers)|
| Vector DB        | ChromaDB                           |
| LLM              | Groq (Llama3-8B)                   |
| Evaluation       | Pandas                             |

---

## 📂 Project Structure
NCERT-Study-Assistant-RAG-v2/
│
├── notebooks/
│ └── rag_pipeline.ipynb
│
├── src/
│ ├── loader.py
│ ├── chunking.py
│ ├── retriever.py
│ ├── qa_system.py
│ └── evaluation.py
│
├── outputs/
│ ├── wk10_chunks.json
│ ├── retrieval_log.json
│ ├── eval_scored.csv
│ └── eval_v2_scored.csv
│
├── data/ # (PDF NOT included)
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── reflection.md


---

## ▶️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/NCERT-Study-Assistant-RAG-v2.git
cd NCERT-Study-Assistant-RAG-v2
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add API Key

Create .env file:

GROQ_API_KEY=your_key_here
5. Add NCERT PDF

Download from:
https://ncert.nic.in/textbook.php

Place locally and update path in notebook.

6. Run Notebook

Open:

notebooks/rag_pipeline.ipynb

Run all cells.

🧪 Evaluation

Evaluation includes:

✔ In-scope questions (textbook-based)
❌ Out-of-scope questions (to test refusal)
📊 Metrics:
Correctness
Groundedness
Refusal accuracy

Results saved in:

outputs/eval_scored.csv
outputs/eval_v2_scored.csv
⚠️ Challenges Faced
Retrieval mismatch due to chunk boundaries
Keyword vs semantic gap
PDF noise (headers/footers)
Out-of-scope hallucination
Top-k tuning trade-off
📈 Improvements from v1
Aspect	v1 (Week 9)	v2 (This Project)
Retrieval	BM25 (keyword)	Embeddings (semantic)
Storage	None	Vector DB (Chroma)
Pipeline	Manual	LangChain modular
Accuracy	Medium	Higher + grounded
Evaluation	Basic	Structured scoring
🎯 Conclusion

This project demonstrates a production-ready RAG pipeline that improves:

Answer accuracy
Context relevance
System reliability

It aligns with modern LLM application architecture used in industry.

📌 Notes
No secrets committed
No large files pushed
Clean modular structure
Reproducible setup

Sharanya Naresh