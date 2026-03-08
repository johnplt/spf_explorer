import os
from langchain_docling import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank

def setup_ultimate_rag(pdf_path):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    
    loader = DoclingLoader(file_path=pdf_path)
    docs = loader.load()
    
    # On utilise un découpeur récursif qui respecte le Markdown
    # On veut des morceaux qui permettent d'avoir assez de contexte
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=400,
        separators=["\n## ", "\n### ", "\n\n", "\n", " "]
    )
    
    final_splits = text_splitter.split_documents(docs)
    
    print(f"📦 Document découpé en {len(final_splits)} morceaux.")
    vectorstore = FAISS.from_documents(final_splits, embeddings)
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 15})
    
    compressor = FlashrankRerank()
    return ContextualCompressionRetriever(base_compressor=compressor, base_retriever=retriever)