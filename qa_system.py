from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

def build_qa_system(retriever):
    llm = ChatGroq(model="llama3-8b-8192")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa_chain