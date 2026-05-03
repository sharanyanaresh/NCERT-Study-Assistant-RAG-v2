from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = f"chunk_{i}"

    return chunks