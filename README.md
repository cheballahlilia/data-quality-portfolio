# Data Quality Portfolio

Mini-framework de contrôle qualité de données développé en Python (pandas).

## Objectif

Démontrer la mise en place de règles de contrôle qualité sur un jeu de données de transactions financières, avec génération de rapports horodatés.

## Contrôles implémentés

- Détection des valeurs nulles par colonne
- Détection des montants négatifs
- Détection des doublons sur le montant
- Validation des statuts (valeurs autorisées : `validé`, `en attente`)

## Fonctionnement

Le script `semaine2.py` :
1. Charge un fichier CSV de transactions
2. Applique les règles de contrôle qualité
3. Génère un rapport horodaté (`rapport_qualite_YYYYMMDD_HHMMSS.txt`)

## Lancer le script

```bash
python semaine2.py
```

## À venir

- Connexion à BigQuery
- Tests dbt
- Suites Great Expectations
- Alerting automatisé