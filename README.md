# Documentation des scripts Gers & Haute-Garonne

Ce projet regroupe des scripts pour la gestion, la génération et la modification de formulaires (HTML/JSON) à partir de fichiers Excel, pour les départements du Gers et de la Haute-Garonne. Il permet d’automatiser la création, la conversion, l’ajout de lignes et le tri de formulaires médicaux ou logistiques.

## Structure générale

- **Gers/**
  - Scripts de conversion Excel → JSON, ajout de lignes, génération/modification HTML, tri de tableaux HTML.
  - Dossiers : `ajout de ligne/`, `création/`, `trie par ordre alphabétique/`.
  - Scripts principaux : `creation_html-gers.py` (génération HTML), `modifier_html-gers.py` (modification HTML).
- **Haute-Garonne/**
  - Scripts similaires pour la gestion des formulaires du département.
  - Dossiers : `ajout de ligne/`, `Création/`, `Fini/`, etc.

## Principaux scripts et leur usage

### Conversion Excel → JSON
- Permet de transformer un fichier Excel (modèle de matériel ou de kit) en fichier JSON exploitable par les autres scripts.
- **Exemple d’utilisation :**
  ```bash
  python excel_to_json.py chemin/vers/fichier.xlsx chemin/vers/sortie.json
  ```

### Ajout de lignes à un formulaire
- Ajoute dynamiquement des lignes à un formulaire existant (JSON ou HTML).
- **Exemple d’utilisation :**
  ```bash
  python ajout_lignes_formulaire.py
  ```

### Génération de formulaires HTML
- Gers : utiliser `creation_html-gers.py` pour générer un formulaire HTML.
- Haute-Garonne : utiliser `creation_html.py` ou `creation_html-HG-Gers(pedia).py`.
- **Exemple d’utilisation :**
  ```bash
  python creation_html-gers.py
  python creation_html.py
  ```

### Tri de tableaux HTML (Gers)
- Trie les tableaux HTML par ordre alphabétique et sauvegarde le résultat dans un dossier dédié.
- **Exemple d’utilisation :**
  ```bash
  python sort_html_table.py
  ```

## Fichiers importants
- Fichiers HTML d’exemple :
  - Gers : `trie par ordre alphabétique/Admission - Kit n°1 - H_sorted.html`, `création/json générateur GERS/html-to-json/Kit n°5 antibio + Perfusion.html`, etc.
  - Haute-Garonne : `ajout de ligne/test.html`, `Fini/Kit adulte/Kit n°1 Inclusion.html`, etc.
- Fichiers Excel modèles :
  - Gers : `ajout de ligne/excel_to_json/Template/Template.xlsx`, etc.
  - Haute-Garonne : `ajout de ligne/excel_to_json/Template - REF.xlsx`, etc.

## Dépendances
- Python 3
- pandas (pour la conversion Excel → JSON)
- unidecode (pour le nettoyage des noms)
- beautifulsoup4 (pour le tri de tableaux HTML)

Installer les dépendances :
```bash
pip install pandas unidecode beautifulsoup4
```

## Conseils et bonnes pratiques
- Toujours vérifier la structure du fichier Excel avant conversion.
- Les scripts affichent des messages d’erreur explicites en cas de problème de format.
- Les fichiers générés sont placés dans les dossiers `excel fini/`, `json fini/`, `HTML/`, ou `sorted_files/` selon le script.
- Ne pas inclure de données personnelles ou médicales dans les fichiers partagés ou versionnés.

---
Pour toute question ou amélioration, contacter le responsable du projet.
