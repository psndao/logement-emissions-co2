import requests
import pandas as pd
import os

def extract_dpe_api(size=1000, save_path="data/raw/dpe_data.csv"):
    """
    Extrait des données de l'API ADEME DPE et sauvegarde en CSV
    """
    import requests, pandas as pd, os
    
    url = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe03existant/lines"
    params = {"size": size}

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()["results"]
        df = pd.DataFrame(data)

        # Création du dossier s’il n’existe pas
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Sauvegarde dans le bon dossier du projet
        df.to_csv(save_path, index=False)
        print(f"✅ Données sauvegardées dans {save_path} ({len(df)} lignes)")
        return df
    else:
        print("❌ Erreur API :", response.status_code)
        return None

if __name__ == "__main__":
    extract_dpe_api(size=5000)
