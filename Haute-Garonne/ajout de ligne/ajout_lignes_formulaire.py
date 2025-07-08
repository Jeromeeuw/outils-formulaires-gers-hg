import json
import re
import os
from unidecode import unidecode

def nettoyer_nom(nom):
    nom_nettoye = unidecode(nom)
    caracteres_a_remplacer = ["'", " ", "/", "+", ",", "-", "?", "!", ":", ".", "%", "(", ")", "&"]
    for caractere in caracteres_a_remplacer:
        nom_nettoye = nom_nettoye.replace(caractere, "")
    return nom_nettoye

def verifier_quantite(quantite):
    if re.match(r'^\d+$', str(quantite)):
        return int(quantite)
    else:
        return str(quantite)

def ajouter_extension(fichier, extension):
    if not fichier.endswith(extension):
        fichier += extension
    return fichier

def lister_fichiers(dossier=".", extension=".json"):
    return [f for f in os.listdir(dossier) if f.endswith(extension)]

def choisir_fichier(extension):
    fichiers = lister_fichiers(extension=extension)
    if not fichiers:
        print(f"Aucun fichier {extension} trouvé.")
        exit(1)
    print(f"\nFichiers {extension} disponibles :")
    for i, f in enumerate(fichiers):
        print(f"{i + 1}. {f}")
    choix = input(f"Sélectionnez un fichier {extension} (numéro) : ").strip()
    if not choix.isdigit() or int(choix) < 1 or int(choix) > len(fichiers):
        print("Choix invalide.")
        exit(1)
    return fichiers[int(choix) - 1]

def inserer_lignes_html(html_path, data, titre_formulaire_clean):
    with open(html_path, 'r', encoding='utf-8') as file:
        html = file.read()

    lignes = ""
    for item in data["Items"]:
        type_materiel_clean = nettoyer_nom(item["Type de materiel"])
        quantite = verifier_quantite(item.get("Quantité Demandée", ""))
        if isinstance(quantite, int):
            lignes += f"""
<tr class="empty">
    <th scope="row">{item['Type de materiel']}</th>
    <td>{item.get('Référence', '/')}</td>
    <td><input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM"
    ng-init="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM = (container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM !== undefined) ? container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM : {quantite}"
    mgapp-keyboard class="form-control" min="0"/></td>
    <td><input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEL" mgapp-keyboard class="form-control" min="0"/></td>
</tr>"""
        else:
            lignes += f"""
<tr class="empty">
    <th scope="row">{item['Type de materiel']}</th>
    <td>{item.get('Référence', '/')}</td>
    <td><input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM" mgapp-keyboard class="form-control" min="0"/></td>
    <td><input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEL" mgapp-keyboard class="form-control" min="0"/></td>
</tr>"""

    nouveau_html = re.sub(r"(</tbody>)", lignes + r"\1", html, flags=re.IGNORECASE)

    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(nouveau_html)

def generer_formulaire():
    json_path = choisir_fichier(".json")
    html_path = choisir_fichier(".html")

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    titre_formulaire = input("Entrez le titre du formulaire : ").strip()
    titre_formulaire_clean = nettoyer_nom(titre_formulaire)

    inserer_lignes_html(html_path, data, titre_formulaire_clean)
    print(f"\n✅ Lignes ajoutées avec succès dans {html_path} !")

# Exécution
generer_formulaire()