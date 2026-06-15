import pandas as pd
from datetime import datetime

def charger_donnees(fichier):
    df = pd.read_csv(fichier)
    print(f"Fichier chargé : {len(df)} lignes")
    return df

def verifier_nulls(df):
    nulls = df.isnull().sum()
    print("\n=== Valeurs nulles ===")
    print(nulls)
    return nulls

def verifier_montants_negatifs(df):
    negatifs = df[df["montant"] < 0]
    print("\n=== Montants négatifs ===")
    print(negatifs)
    return negatifs

def verifier_doublons(df):
    doublons = df[df.duplicated(subset=["montant"], keep=False)]
    print("\n=== Doublons sur montant ===")
    print(doublons)
    return doublons

def verifier_statuts(df):
    valeurs_autorisees = ["validé", "en attente"]
    anomalies = df[~df["statut"].isin(valeurs_autorisees)]
    print("\n=== Statuts invalides ou nulls ===")
    print(anomalies)
    return anomalies

def verifier_dates(df):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    aujourdhui = pd.Timestamp.now()
    
    dates_invalides = df[df["date"].isnull()]
    dates_futures = df[df["date"] > aujourdhui]
    
    print("\n=== Dates invalides ou manquantes ===")
    print(dates_invalides)
    print("\n=== Dates dans le futur ===")
    print(dates_futures)
    
    return dates_invalides, dates_futures

def exporter_rapport(df, nulls, negatifs, doublons, statuts, dates_invalides, dates_futures):
    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nom_fichier = f"rapport_qualite_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nom_fichier, "w") as f:
        f.write("=== RAPPORT DATA QUALITY ===\n\n")
        f.write(f"Date d'exécution : {maintenant}\n\n")
        f.write(f"Nombre total de lignes : {len(df)}\n\n")
        f.write("Valeurs nulles par colonne :\n")
        f.write(nulls.to_string())
        f.write(f"\n\nNombre de montants négatifs : {len(negatifs)}\n")
        f.write(f"Nombre de doublons : {len(doublons)}\n")
        f.write(f"Nombre de statuts invalides : {len(statuts)}\n")
        f.write(f"Nombre de dates invalides ou manquantes : {len(dates_invalides)}\n")
        f.write(f"Nombre de dates dans le futur : {len(dates_futures)}\n")
    print("\nRapport exporté dans", nom_fichier)

def main():
    df = charger_donnees("transactions.csv")
    nulls = verifier_nulls(df)
    negatifs = verifier_montants_negatifs(df)
    doublons = verifier_doublons(df)
    statuts = verifier_statuts(df)
    dates_invalides, dates_futures = verifier_dates(df)
    exporter_rapport(df, nulls, negatifs, doublons, statuts, dates_invalides, dates_futures)

if __name__ == "__main__":
    main()