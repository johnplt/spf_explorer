# 🏥 Health Explorer: Hybrid RAG & MCP Architecture

Prototype d'assistant intelligent pour la veille sanitaire, combinant l'analyse de rapports textuels (Santé Publique France) et l'interrogation de données structurées (Data.gouv MCP).

## 🚀 Architecture Technique
Ce projet utilise une approche **Advanced RAG** pour pallier les limites des systèmes classiques sur des documents denses :

* **Extraction :** Analyse de bulletins épidémiologiques PDF complexes.
* **Indexing :** Vectorisation via `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (optimisé pour le français).
* **Re-ranking :** Implémentation d'un **Cross-Encoder Flashrank** (`ms-marco-MiniLM-L-12-v2`) pour filtrer le bruit documentaire et isoler les tendances réelles.
* **Hybridation :** Connecteur prêt pour le protocole **MCP (Model Context Protocol)** de Data.gouv pour enrichir les analyses textuelles avec des indicateurs épidémiologiques temps-réel.

## 🛠️ Stack Technique
- **Framework :** LangChain 1.0 (Classic)
- **Vector Store :** FAISS (Local)
- **Reranker :** Flashrank (Compression de contexte)
- **Data Source :** Bulletins OSCOUR® & Data.gouv

## 📈 Résultats & Précision
Le système est capable d'isoler des tendances fines au sein de rapports hebdomadaires, comme illustré ci-dessous :
> **Question :** "Quelles sont les pathologies en augmentation en semaine 09 ?"
> **Réponse :** Identification précise des hausses (Traumatismes +13%, Varicelle +18%, etc.) en ignorant les sections méthodologiques redondantes.

## 🛠️ Installation
```bash
pip install -r requirements
```