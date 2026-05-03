
---

# 📄 `reflection.md` (Full-Marks Version)

```markdown
# 📘 Reflection — RAG Study Assistant v2.0

---

## 1. What was your approach in this project?

The project was implemented as a **Retrieval-Augmented Generation (RAG)** system.

The pipeline consisted of:

1. Extracting structured content from the NCERT PDF
2. Splitting text into meaningful overlapping chunks
3. Converting chunks into embeddings using a sentence transformer model
4. Storing embeddings in a vector database (Chroma)
5. Retrieving top-k relevant chunks for a given query
6. Passing retrieved context to an LLM (Groq) for grounded answer generation

This approach ensures that answers are **based on actual textbook content rather than model memory**.

---

## 2. What challenges did you face?

### a) Retrieval accuracy issues
Sometimes irrelevant chunks were retrieved due to overlapping topics in the textbook.

### b) Chunking problems
Too small chunks lost context, while large chunks introduced noise.

### c) Semantic mismatch
Keyword-based queries did not match textbook phrasing.

### d) PDF extraction noise
Headers, page numbers, and repeated text affected retrieval quality.

### e) Hallucination in out-of-scope queries
Model attempted to answer questions not present in textbook.

---

## 3. How did you solve these challenges?

- Used **RecursiveCharacterTextSplitter** with overlap for better context retention  
- Switched from keyword retrieval to **embedding-based semantic search**  
- Cleaned extracted text to remove noise  
- Tuned **top-k retrieval parameter**  
- Designed prompts to ensure answers are **strictly grounded in retrieved context**  

---

## 4. What improvements did you make over Version 1?

| Component        | Version 1            | Version 2 (Current)        |
|-----------------|---------------------|----------------------------|
| Retrieval        | BM25 (keyword)      | Embeddings (semantic)      |
| Storage          | None                | Vector DB (Chroma)         |
| Pipeline         | Manual              | LangChain-based            |
| Accuracy         | Lower               | Improved                   |
| Evaluation       | Basic               | Structured + measurable    |

Version 2 significantly improves both **accuracy and robustness**.

---

## 5. What did you learn?

- Importance of **semantic retrieval over keyword matching**
- Role of **chunking strategy in RAG performance**
- How embeddings enable meaning-based search
- Importance of evaluation in LLM systems
- How modular pipelines improve scalability and maintainability

---

## 6. What would you improve further?

- Add hybrid retrieval (BM25 + embeddings)
- Improve chunking using document structure (headings, tables)
- Add citation support in answers
- Deploy as a web application (Streamlit)
- Implement re-ranking models for better retrieval precision

---

## 7. Final Reflection

This project helped bridge the gap between:

- Conceptual understanding of RAG systems  
- Practical implementation using modern tools  

It demonstrated how to build a **real-world, production-style QA system** that is:

- Reliable  
- Scalable  
- Grounded in source data  

---
