# Partie 2 : Use Case "Reprendre la Voiture"

## Objectif

Implémenter le use case complet permettant à un client de récupérer sa voiture.

## Fonctionnalités implémentées

### Classes complétées
- [x] Place : méthode `liberer()`
- [x] Voiture : méthode `retirer()`
- [x] Borne_Ticket : méthodes `lire_ticket()`, `calculer_montant_du()`, `traiter_paiement()`
- [x] Teleporteur : méthode `teleporter_vers_acces()`
- [x] Panneau_Affichage : méthode `incrementer()`
- [x] Placement : méthodes `get_duree_placement()`, `terminer_placement()`
- [x] Acces : méthode `teleporter_vers_acces()`
- [x] Parking : méthode `liberer_place()`

## Installation
```bash
cd partie2
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Exécution

### Lancer les tests
```bash
# Tous les tests
pytest src/tests/ -v

# Test du use case complet
pytest src/tests/test_use_case_reprendre_voiture.py -v

# Avec couverture
pytest --cov=src/modele src/tests/
```

### Démonstration
```bash
python src/demo_reprendre_voiture.py
```

## Auteur

**BARRY Fatimatou**  
L3 MIASHS - Université Toulouse 2 Jean Jaurès
