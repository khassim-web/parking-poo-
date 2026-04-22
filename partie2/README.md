# Partie 2 — Use Case "Reprendre la Voiture"

**Auteur : ABOULKHASSIM Abdallah**  
L3 Informatique — Université Toulouse 2 Jean Jaurès

---

## Objectif

Implémenter le use case complet permettant à un client de récupérer sa voiture du parking DreamPark.  
Cette partie s'appuie sur le modèle objet défini en Partie 0 et complète les méthodes nécessaires au scénario.

---

## Scénario "Reprendre la voiture"

```
Client arrive à l'accès
        ↓
Insère son ticket dans la borne
        ↓
La borne calcule le montant dû
  (tarif : 2 €/h, 30 premières minutes offertes)
        ↓
Client paie (CB / Espèces / Badge)
        ↓
Le téléporteur ramène la voiture à l'accès
        ↓
La place est libérée
        ↓
Le panneau d'affichage est mis à jour
```

---

## Méthodes implémentées

| Classe | Méthodes |
|--------|----------|
| `Place` | `liberer()` |
| `Voiture` | `retirer()` |
| `Borne_Ticket` | `lire_ticket()`, `calculer_montant_du()`, `traiter_paiement()` |
| `Teleporteur` | `teleporter_vers_acces()` |
| `Panneau_Affichage` | `incrementer()`, `mettre_a_jour()`, `allumer()`, `eteindre()` |
| `Placement` | `get_duree_placement()`, `terminer_placement()` |
| `Acces` | `teleporter_vers_acces()`, `retirer_camera()`, `capturer_vehicule()` |
| `Parking` | `liberer_place()`, `enregistrer_passage()`, `get_statistiques()` |
| `Camera` | `capturer_image()`, `mesurer_dimensions()` |
| `Abonnement` | `est_valide()`, `renouveler()`, `resilier()` |
| `Service` | `demarrer()`, `terminer()`, `annuler()` |
| `Livraison` | `executer()`, `assigner_voiturier()` |
| `Maintenance` | `executer()`, `terminer_intervention()` |
| `Entretien` | `demarrer_entretien()`, `terminer_entretien()` |

---

## Installation

```bash
cd partie2
python3 -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer les tests

```bash
# Tous les tests
pytest src/tests/ -v

# Use case complet uniquement
pytest src/tests/test_use_case_reprendre_voiture.py -v

# Avec couverture de code
pytest --cov=src/model src/tests/
```

## Lancer la démonstration

```bash
python src/demo_reprendre_voiture.py
```

---

## Résultats

```
22 passed in 0.12s
```
