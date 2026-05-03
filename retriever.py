from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vectorstore(chunks):
    embedding = HuggingFaceEmbeddings()

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory="outputs/chroma_db"
    )

    return db