# Data Quality Portfolio

Mini-framework de contrôle qualité de données développé en Python.

## Objectif

Démontrer la mise en place de règles de contrôle qualité sur un jeu de données
de transactions financières, avec génération de rapports horodatés et tests automatisés.

## Structure du projet

    data-quality-portfolio/
    ├── checks/
    │   └── data_quality_checks.py   
    ├── tests/
    │   └── test_data_quality_checks.py  
    ├── data/
    │   └── transactions.csv         
    ├── reports/                     
    ├── .gitignore
    └── README.md
    
## Contrôles implémentés

- Détection des valeurs nulles par colonne
- Détection des montants négatifs
- Détection des doublons sur le montant
- Validation des statuts (valeurs autorisées : `validé`, `en attente`)
- Détection des dates invalides ou manquantes
- Détection des dates dans le futur

## Lancer le script

```bash
python checks/data_quality_checks.py
```

## Lancer les tests

```bash
pytest
```

## Environnement technique

- Python 3.13
- pandas
- pytest

## À venir

- Connexion à BigQuery
- Modèles dbt avec tests natifs
- Suites Great Expectations
- Alerting automatisé
- Intégration CI/CD