import os
from bs4 import BeautifulSoup

# Lister les fichiers HTML dans le répertoire actuel
html_files = [f for f in os.listdir() if f.endswith(".html")]

# Afficher la liste des fichiers disponibles
if not html_files:
    print("Aucun fichier HTML trouvé dans le répertoire actuel.")
    exit()

print("Fichiers HTML disponibles :")
for i, file in enumerate(html_files, 1):
    print(f"{i}. {file}")

# Demander à l'utilisateur de choisir un fichier
while True:
    try:
        choice = int(input("Entrez le numéro du fichier à trier : "))
        if 1 <= choice <= len(html_files):
            input_file = html_files[choice - 1]
            break
        else:
            print("Veuillez entrer un numéro valide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Définir le dossier de sortie
output_dir = "sorted_files"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, input_file.replace(".html", "_sorted.html"))

with open(input_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Trouver le tableau des matériels
table = soup.find("table", class_="table")
if table:
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")
    
    # Trier les lignes par ordre alphabétique sur la première colonne (Type de matériel)
    sorted_rows = sorted(rows, key=lambda row: row.find("th").text.strip().lower())
    
    # Remettre les lignes triées dans le tableau
    tbody.clear()
    for row in sorted_rows:
        tbody.append(row)

    # Sauvegarder le fichier modifié
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(soup))
    
    print(f"Le fichier trié a été enregistré sous '{output_file}'")
else:
    print("Tableau non trouvé dans le fichier HTML.")
