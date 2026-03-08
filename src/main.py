import os
from rag_engine import setup_ultimate_rag
from langchain_ollama import OllamaLLM # Pour le local
from langchain_core.prompts import ChatPromptTemplate
from mcp_client import get_latest_stats_from_mcp

# Configuration du modèle local (Ollama doit tourner en fond)
llm = OllamaLLM(model="qwen2.5:0.5b") 

def ask_assistant(query, retriever):
    print(f"\n🔍 Analyse en cours pour : {query}")
    
    # 1. Retrieval + Reranking
    context_docs = retriever.invoke(query)
    top_docs = context_docs[:3]
    context_text = "\n\n".join([doc.page_content for doc in top_docs])

    # 2. Prompt de synthèse (Le "cerveau")
    template = """
Tu es un assistant expert en analyse de bulletins sanitaires.
Ton rôle est d'extraire des faits précis depuis le CONTEXTE fourni.

DIRECTIVES :
1. Réponds uniquement en utilisant les informations du CONTEXTE.
2. Si la question porte sur une évolution (hausse/baisse), cite le pourcentage (%) et le volume (nombre de passages).
3. Si l'information est absente, réponds simplement : "Information non trouvée dans le bulletin".
4. Ne fais aucune interprétation ou calcul global.

CONTEXTE : 
{context}

QUESTION : 
{question}

RÉPONSE PRÉCISE :
"""
    print("\n--- DEBUG : TEXTE ENVOYÉ AU MODÈLE ---")
    print(context_text[:500]) # On affiche les 500 premiers caractères
    print("--------------------------------------\n")
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    # 3. Génération de la réponse
    response = chain.invoke({"context": context_text, "question": query})
    
    print("\n✅ RÉPONSE SYNTHÉTISE :")
    print(response.strip())
    print(f"\nSources : {len(context_docs)} segments analysés via Docling.")

if __name__ == "__main__":
    PDF_PATH = "data/raw/bullnat_oscour_20260303.pdf"
    retriever = setup_ultimate_rag(PDF_PATH)
    ask_assistant("De combien augmente les passages pour varicelle en semaine 09 ?", retriever)