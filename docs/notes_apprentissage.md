# Fiche de révision — Session de formation Data Quality

## 1. Python — ce que tu as appris

### Concepts clés
- **pandas** : librairie Python pour manipuler des données tabulaires (équivalent d'un DataFrame Talend)
- **pd.read_csv()** : lire un fichier CSV → équivalent d'un tFileInputDelimited en Talend
- **df.isnull()** : détecter les valeurs nulles → équivalent d'un tMap avec condition `== null`
- **df[condition]** : filtrer des lignes → équivalent d'un tFilterRow en Talend
- **.isin(liste)** : vérifier si une valeur est dans une liste → équivalent de `IN` en SQL
- **~** devant une condition : signifie NOT → inverse le filtre
- **pd.to_datetime(..., errors="coerce")** : convertir en date, les valeurs invalides deviennent `NaT`
- **datetime.now().strftime(format)** : récupérer la date/heure actuelle formatée
- **len(df)** : compter le nombre de lignes

### Structure professionnelle
```python
def ma_fonction(df):
    # traitement
    return resultat

def main():
    # appels des fonctions dans l'ordre
    df = charger_donnees("fichier.csv")
    ...

if __name__ == "__main__":
    main()
```
> `if __name__ == "__main__"` : n'exécute le bloc que si le fichier est lancé directement (pas importé)

### Écrire dans un fichier
```python
with open("fichier.txt", "w") as f:
    f.write("contenu\n")
```
> Le `with` gère l'ouverture et la fermeture automatiquement

---

## 2. pytest — tests unitaires

### Principe
- On crée un petit DataFrame **dont on connaît le résultat à l'avance**
- On appelle la fonction à tester
- `assert` vérifie que le résultat est bien celui attendu
- Si `assert` est faux → le test échoue

### Exemple type
```python
def test_verifier_montants_negatifs():
    df = pd.DataFrame({"montant": [100, -50, 200]})
    resultat = verifier_montants_negatifs(df)
    assert len(resultat) == 1  # on attend exactement 1 ligne négative
```

### Lancer les tests
```bash
pytest
```

### Importer depuis un sous-dossier
```python
import sys
sys.path.insert(0, "checks")
from data_quality_checks import ma_fonction
```

---

## 3. Git — commandes essentielles

| Commande | Ce que ça fait |
|----------|---------------|
| `git init` | Initialiser un repo Git dans le dossier |
| `git add .` | Préparer tous les fichiers pour le commit |
| `git status` | Voir l'état des fichiers (modifiés, ajoutés...) |
| `git commit -m "message"` | Enregistrer un snapshot du code |
| `git push` | Envoyer les commits sur GitHub |
| `git mv ancien nouveau` | Renommer un fichier en gardant l'historique |

### .gitignore
Fichier qui liste ce que Git doit ignorer :
```
reports/
__pycache__/
rapport_qualite_*.txt
```

---

## 4. dbt — concepts clés

### Ce qu'est dbt
- Outil de **transformation de données en SQL**
- Tu écris du SQL, dbt gère l'exécution, la documentation et les tests
- Équivalent d'un tMap/tAggregate Talend mais en SQL pur, versionnable et testable

### Commandes essentielles
| Commande | Ce que ça fait |
|----------|---------------|
| `dbt debug` | Vérifie que la connexion fonctionne |
| `dbt seed` | Charge un fichier CSV dans la base de données |
| `dbt run` | Exécute les modèles SQL |
| `dbt test` | Lance les tests de validation |

### ref() — la notion clé de dbt
```sql
from {{ ref('transactions') }}
```
> Au lieu d'écrire le nom de la table en dur, tu références le modèle par son nom. dbt calcule le bon chemin automatiquement.

### Tests natifs dbt (schema.yml)
```yaml
- name: ma_colonne
  tests:
    - not_null      # aucune valeur nulle
    - unique        # pas de doublons
    - accepted_values:
        values: ['validé', 'en attente']
```

---

## 5. Structure de ton projet

```
data-quality-portfolio/       ← projet Python + pytest
├── checks/
│   └── data_quality_checks.py   # 6 contrôles Data Quality
├── tests/
│   └── test_data_quality_checks.py  # 3 tests unitaires
├── data/
│   └── transactions.csv
├── reports/
├── .gitignore
└── README.md

dbt_finance/                  ← projet dbt
├── models/
│   ├── transactions_summary.sql
│   └── schema.yml
├── seeds/
│   └── transactions.csv
└── dbt_project.yml
```

---

## 6. Points à approfondir

| Sujet | Pourquoi c'est important | Ressource |
|-------|--------------------------|-----------|
| pandas — fonctions avancées | groupby, merge, pivot | pandas.pydata.org |
| pytest — fixtures | Partager des données de test entre plusieurs tests | docs.pytest.org |
| dbt — tests accepted_values | Valider les valeurs autorisées d'une colonne | docs.getdbt.com |
| dbt — documentation | `dbt docs generate` crée un site de doc automatique | docs.getdbt.com |
| Git — branches | Travailler sur une feature sans toucher au code principal | git-scm.com |

---

## 7. Ce que tu peux dire en entretien

> *"J'ai développé un mini-framework de Data Quality en Python avec pandas, structuré en fonctions, avec génération de rapports horodatés et tests unitaires pytest. J'ai également initié un projet dbt avec modèles SQL, seeds et tests natifs not_null/unique. L'ensemble est versionné sur GitHub."*