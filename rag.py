from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
import os

VECTOR_DB_PATH = "vector_store"

def build_vector_store():
    docs = []

    for file in os.listdir("knowledge"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(f"knowledge/{file}")
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    embeddings = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTOR_DB_PATH)

    print("✅ Vector store built successfully")

def load_vector_store():
    embeddings = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return FAISS.load_local(VECTOR_DB_PATH, embeddings)


if __name__ == "__main__":
    build_vector_store()