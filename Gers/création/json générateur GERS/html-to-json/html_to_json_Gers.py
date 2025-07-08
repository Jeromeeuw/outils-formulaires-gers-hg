from bs4 import BeautifulSoup
import json
import os
import sys
import re

def extract_form_data_from_html(html_file_path, output_json_path):
    with open(html_file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Extraire le titre du formulaire
    titre_label = soup.find("label", class_="ng-binding")
    titre_formulaire = titre_label.text.strip() if titre_label else "Formulaire Inconnu"

    # Extraire les matériels et leurs informations
    table = soup.find("table", class_="table table-striped table-bordered caption-top")
    items = []

    if table:
        tbody = table.find("tbody")
        rows = tbody.find_all("tr")

        for row in rows:
            cols = row.find_all("th") + row.find_all("td")
            if len(cols) >= 2:  # Vérifier la présence des colonnes Type et Référence
                type_materiel = cols[0].text.strip()
                reference = cols[1].text.strip() if len(cols) > 1 else ""
                quantite_demandee = None

                # Recherche de la quantité demandée dans les inputs
                input_qd = cols[1].find("input") if len(cols) > 1 else None
                if input_qd and "ng-init" in input_qd.attrs:
                    ng_init = input_qd["ng-init"]
                    # Extraction correcte de la quantité demandée dans tous les formats possibles
                    match = re.search(r'=(\d+)', ng_init) or re.search(r':\s*(\d+)', ng_init)
                    if match:
                        quantite_demandee = match.group(1)

                item_data = {
                    "Type de materiel": type_materiel,
                    "Référence": reference
                }
                if quantite_demandee and quantite_demandee.isdigit():
                    item_data["Quantité Demandée"] = int(quantite_demandee)
                
                items.append(item_data)

    # Structurer les données en JSON
    json_data = {
        "Titre du formulaire": titre_formulaire,
        "Items": items
    }

    # Sauvegarder en fichier JSON
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Fichier JSON généré : {output_json_path}")

def list_html_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    if not html_files:
        print("Aucun fichier HTML trouvé dans le répertoire actuel.")
        sys.exit(1)
    
    print("Fichiers HTML disponibles :")
    for idx, file in enumerate(html_files, 1):
        print(f"{idx}. {file}")
    
    choice = int(input("Choisissez un fichier en entrant son numéro : "))
    if choice < 1 or choice > len(html_files):
        print("Choix invalide.")
        sys.exit(1)
    
    return html_files[choice - 1]

if __name__ == "__main__":
    html_file = list_html_files()
    json_file = html_file.replace(".html", ".json")
    extract_form_data_from_html(html_file, json_file)
