import pandas as pd
import json
import os
import sys

def excel_to_json(excel_file_path, output_json_path):
    # Charger le fichier Excel
    try:
        df = pd.read_excel(excel_file_path)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Excel : {e}")
        sys.exit(1)
    
    # Vérifier que le fichier contient des données
    if df.empty:
        print("Le fichier Excel est vide.")
        sys.exit(1)
    
    # Vérifier que le fichier contient au moins une colonne
    if len(df.columns) < 1:
        print("Le fichier Excel doit contenir au moins une colonne : 'Type de materiel'.")
        sys.exit(1)
    
    # Renommer les colonnes en fonction de leur disponibilité
    df = df.rename(columns={df.columns[0]: "Type de materiel"})
    
    if len(df.columns) > 1:
        second_col_name = df.columns[1]
        if df[second_col_name].dtype == 'object':
            df = df.rename(columns={df.columns[1]: "Référence"})
        else:
            df = df.rename(columns={df.columns[1]: "Quantité Demandée"})
    
    if len(df.columns) > 2:
        df = df.rename(columns={df.columns[2]: "Quantité Demandée"})
    
    # Convertir en liste de dictionnaires, en supprimant "Référence" et "Quantité Demandée" si elles sont absentes
    items = []
    for _, row in df.iterrows():
        item = {"Type de materiel": row["Type de materiel"]}
        
        if "Référence" in df.columns and pd.notna(row["Référence"]):
            item["Référence"] = row["Référence"]
        
        if "Quantité Demandée" in df.columns and pd.notna(row["Quantité Demandée"]):
            item["Quantité Demandée"] = int(row["Quantité Demandée"])
        
        items.append(item)
    
    # Construire la structure JSON complète
    json_data = {
        "Titre du formulaire": os.path.splitext(os.path.basename(excel_file_path))[0],
        "Items": items
    }
    
    # Sauvegarder en fichier JSON
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Fichier JSON généré : {output_json_path}")

def list_excel_files():
    excel_files = [f for f in os.listdir('.') if f.endswith('.xls') or f.endswith('.xlsx')]
    if not excel_files:
        print("Aucun fichier Excel trouvé dans le répertoire actuel.")
        sys.exit(1)
    
    print("Fichiers Excel disponibles :")
    for idx, file in enumerate(excel_files, 1):
        print(f"{idx}. {file}")
    
    choice = int(input("Choisissez un fichier en entrant son numéro : "))
    if choice < 1 or choice > len(excel_files):
        print("Choix invalide.")
        sys.exit(1)
    
    return excel_files[choice - 1]

if __name__ == "__main__":
    excel_file = list_excel_files()
    json_file = os.path.splitext(excel_file)[0] + ".json"
    excel_to_json(excel_file, json_file)