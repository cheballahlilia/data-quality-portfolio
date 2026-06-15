import pandas as pd
from data_quality_checks import verifier_montants_negatifs, verifier_doublons, verifier_statuts

def test_verifier_montants_negatifs():
    df = pd.DataFrame({"montant": [100, -50, 200]})
    resultat = verifier_montants_negatifs(df)
    assert len(resultat) == 1

def test_verifier_doublons():
    df = pd.DataFrame({"montant": [100, 100, 200]})
    resultat = verifier_doublons(df)
    assert len(resultat) == 2

def test_verifier_status():
    df = pd.DataFrame({"statut": ["validé", "validé", "en attente", "en attente", None, "validé"]})
    resultat = verifier_statuts(df)
    assert len(resultat)== 1