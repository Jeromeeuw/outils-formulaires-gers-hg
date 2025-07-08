# Documentation des scripts Haute-Garonne

Ce dossier contient plusieurs scripts pour la gestion et la génération de formulaires (HTML/JSON) à partir de fichiers Excel ou pour la modification de formulaires existants.

## Structure générale

- **ajout de ligne/**
  - `excel_to_json/excel_to_json.py` : Convertit un fichier Excel en JSON.
  - `ajout_lignes_formulaire.py` : Ajoute des lignes à un formulaire existant (JSON ou HTML).
- **Création/**
  - `creation_html.py` : Génère des formulaires HTML à partir de données JSON.
  - `creation_html-HG-Gers(pedia).py` : Variante pour la génération de formulaires HTML (version pédiatrique ou multi-départements).

## Fonctionnement des scripts

### 1. Conversion Excel → JSON
- Utiliser `ajout de ligne/excel_to_json/excel_to_json.py`.
- Ce script lit un fichier Excel (ex : `Template - REF.xlsx`), vérifie la structure, puis exporte les données en JSON.
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

### 3. Génération de formulaires HTML
- Utiliser `Création/creation_html.py` ou `creation_html-HG-Gers(pedia).py`.
- Ces scripts génèrent des formulaires HTML à partir de fichiers JSON.
- Ils nettoient les noms de champs pour les rendre compatibles avec AngularJS (ng-model).
- **Exemple d'utilisation :**
  ```bash
  python creation_html.py
  ```

## Dépendances
- Python 3
- pandas (pour la conversion Excel → JSON)
- unidecode (pour le nettoyage des noms)

Installer les dépendances :
```bash
pip install pandas unidecode
```

## Conseils
- Toujours vérifier la structure du fichier Excel avant conversion.
- Les scripts affichent des messages d’erreur explicites en cas de problème de format.
- Les fichiers générés sont placés dans les dossiers `excel fini/`, `json fini/`, ou `HTML/` selon le script.

---
Pour toute question ou amélioration, contacter le responsable du projet.
