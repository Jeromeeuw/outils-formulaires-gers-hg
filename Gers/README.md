# Documentation des scripts Gers

Ce dossier contient plusieurs scripts pour la gestion, la génération et la modification de formulaires (HTML/JSON) à partir de fichiers Excel ou pour le tri de formulaires existants.

## Structure générale

- **ajout de ligne/**
  - `excel_to_json/excel_to_json.py` : Convertit un fichier Excel en JSON.
  - `ajout_lignes_formulaire.py` : Ajoute des lignes à un formulaire existant (JSON ou HTML).
- **création/**
  - `creation_html-gers.py` : Génère des formulaires HTML à partir de données JSON.
  - `json générateur GERS/html-to-json/html_to_json_Gers.py` : Convertit des fichiers HTML en JSON (pour la génération de formulaires ou d'extractions).
  - `json générateur GERS/excel_to_json/excel_to_json.py.py` : Variante de conversion Excel → JSON pour des besoins spécifiques.
- **trie par ordre alphabétique/**
  - `sort_html_table.py` : Trie les tableaux HTML par ordre alphabétique et sauvegarde le résultat dans un dossier dédié.

## Fonctionnement des scripts

### 1. Conversion Excel → JSON
- Utiliser `ajout de ligne/excel_to_json/excel_to_json.py` ou `création/json générateur GERS/excel_to_json/excel_to_json.py.py`.
- Ces scripts lisent un fichier Excel (ex : `Template.xlsx`), vérifient la structure, puis exportent les données en JSON.
- **Exemple d'utilisation :**
  ```bash
  python excel_to_json.py chemin/vers/fichier.xlsx chemin/vers/sortie.json
  ```

### 2. Ajout de lignes à un formulaire
- Utiliser `ajout de ligne/ajout_lignes_formulaire.py`.
- Ce script permet d’ajouter des lignes à un formulaire existant (JSON ou HTML).
- Il propose de choisir le fichier à modifier et gère le formatage des noms et quantités.
- **Exemple d'utilisation :**
  ```bash
  python ajout_lignes_formulaire.py
  ```

### 3. Génération ou modification de formulaires HTML
- Utiliser `création/creation_html-gers.py` pour générer un nouveau formulaire HTML à partir d'un JSON.
- Ces scripts nettoient les noms de champs pour les rendre compatibles avec AngularJS (ng-model).
- **Exemple d'utilisation :**
  ```bash
  python creation_html-gers.py
  ```

### 4. Conversion HTML → JSON
- Utiliser `création/json générateur GERS/html-to-json/html_to_json_Gers.py`.
- Ce script extrait les données d’un formulaire HTML pour les convertir en JSON.
- **Exemple d'utilisation :**
  ```bash
  python html_to_json_Gers.py
  ```

### 5. Tri de tableaux HTML
- Utiliser `trie par ordre alphabétique/sort_html_table.py`.
- Ce script trie les tableaux HTML par ordre alphabétique et sauvegarde le résultat dans `sorted_files/`.
- **Exemple d'utilisation :**
  ```bash
  python sort_html_table.py
  ```

## Fichiers importants
- Fichiers HTML d’exemple :
  - `trie par ordre alphabétique/Admission - Kit n°1 - H_sorted.html`
  - `création/json générateur GERS/html-to-json/Kit n°5 antibio + Perfusion.html`
  - `création/Fer Iniect - Kit n°19 - H.html`
- Fichiers Excel modèles :
  - `ajout de ligne/excel_to_json/Template/Template.xlsx`
  - `ajout de ligne/excel_to_json/Template/Template - REF.xlsx`
  - `ajout de ligne/excel_to_json/Kit n°22 - Post Opératoire CCVT normé.xlsx`
  - `création/json générateur GERS/excel_to_json/Kit urinaire Normé.xlsx`
  - `création/json générateur GERS/excel_to_json/excel fini/Kit chimio SC.xlsx`
  - `création/json générateur GERS/excel_to_json/excel fini/Admission Normé - Kit n°1 - H.xlsx`

## Dépendances
- Python 3
- pandas (pour la conversion Excel → JSON)
- unidecode (pour le nettoyage des noms)
- beautifulsoup4 (pour le tri de tableaux HTML)

Installer les dépendances :
```bash
pip install pandas unidecode beautifulsoup4
```

## Conseils
- Toujours vérifier la structure du fichier Excel avant conversion.
- Les scripts affichent des messages d’erreur explicites en cas de problème de format.
- Les fichiers générés sont placés dans les dossiers `excel fini/`, `json fini/`, ou `sorted_files/` selon le script.

---
Pour toute question ou amélioration, contacter le responsable du projet.
