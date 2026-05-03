from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader

def load_documents(path):
    loader = OpenDataLoaderPDFLoader(
        file_path=path,
        format="markdown"
    )
    return loader.load()