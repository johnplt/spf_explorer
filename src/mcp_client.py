# src/mcp_client.py

def get_latest_stats_from_mcp(indicator_name="incidence_grippe"):
    """
    Simule la réponse du serveur MCP de data.gouv.fr.
    Le serveur MCP permet normalement de transformer des requêtes naturelles 
    en requêtes SQL sur les fichiers CSV de Santé publique France.
    """
    
    # Simulation d'un résultat structuré extrait de data.gouv
    # En production, ce dictionnaire serait généré dynamiquement par le serveur MCP
    mcp_response = {
        "metadata": {
            "source": "Santé publique France via data.gouv.fr",
            "dataset": "Surveillance épidémiologique (Sursaud)",
            "last_update": "2024-03-06"
        },
        "data": {
            "date": "2024-W09",
            "valeur": 154,
            "unite": "cas pour 100 000 habitants",
            "statut": "en augmentation",
            "region": "France entière"
        }
    }
    
    # On retourne juste la partie utile pour la synthèse
    return mcp_response["data"]