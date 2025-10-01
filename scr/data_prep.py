import pandas as pd
import os

def prepare_dpe(input_path="data/raw/dpe_data.csv", output_path="data/processed/dpe_clean.csv"):
    # Colonnes qu’on garde
    cols_keep = [
        "surface_habitable_logement",
        "annee_construction",
        "periode_construction",
        "type_batiment",
        "type_energie_principale_chauffage",
        "type_generateur_chauffage_principal",
        "emission_ges_chauffage",
        "emission_ges_ecs",
        "emission_ges_eclairage",
        "emission_ges_5_usages",
        "emission_ges_5_usages_par_m2",
        "etiquette_ges",
        "code_postal_ban",
        "nom_commune_ban"
    ]
    
    df = pd.read_csv(input_path, low_memory=False)
    
    # les colonnes dans cols_keep 
    df = df[[c for c in cols_keep if c in df.columns]]
    
    # on nettoie les valeurs manquantes et aberrantes
    df = df.dropna(subset=["emission_ges_5_usages", "surface_habitable_logement"])
    df = df[df["emission_ges_5_usages"] > 0]
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"✅ Données prêtes sauvegardées : {output_path} ({len(df)} lignes)")
    return df

if __name__ == "__main__":
    prepare_dpe()
