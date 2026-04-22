# Projet DreamPark — Gestion de Parking

Projet Python réalisé dans le cadre du cours **MIOC501T — Programmation Orientée Objet**  
L3 Informatique — Université Toulouse 2 Jean Jaurès

**Auteur : ABOULKHASSIM Abdallah**

---

## Présentation

DreamPark est un système de gestion de parking intelligent modélisé en Python.  
Le projet est structuré en trois parties progressives :

| Partie | Contenu |
|--------|---------|
| `partie0/` | Modèle objet complet — 17 classes du domaine + tests unitaires |
| `partie2/` | Implémentation du use case *"Reprendre la voiture"* — 22 tests |
| `partie3/` | Module de statistiques avec architecture MVC — rapport HTML |

---

## Prérequis

- Python **3.12** ou supérieur
- `pip` pour l'installation des dépendances

---

## Structure du projet

```
projet_parking/
├── README.md
│
├── partie0/                  # Modèle objet — squelette
│   └── src/
│       ├── modele/           # 17 classes du domaine
│       └── tests/            # Tests unitaires par classe
│
├── partie2/                  # Use case "Reprendre la voiture"
│   └── src/
│       ├── model/            # Classes entièrement implémentées
│       ├── tests/            # 22 tests (100% passent)
│       └── demo_reprendre_voiture.py
│
└── partie3/                  # Statistiques MVC
    ├── src/
    │   ├── model/            # Modèle métier + Statistiques
    │   ├── controller/       # StatistiquesController
    │   ├── view/             # StatistiquesView (texte + HTML)
    │   └── demo_statistiques.py
    └── tests/                # 4 tests (100% passent)
```

---

## Classes du domaine

`Parking` · `Place` · `Voiture` · `Client` · `Acces` · `Placement` · `Borne_Ticket` · `Teleporteur` · `Panneau_Affichage` · `Camera` · `Abonnement` · `Contrat` · `Service` · `Livraison` · `Maintenance` · `Entretien` · `Voiturier` · `Statistiques`

---

## Installation et lancement

### Partie 2

```bash
cd partie2
python3 -m venv .venv
source .venv/bin/activate       # Windows : .venv\Scripts\activate
pip install -r requirements.txt

pytest src/tests/ -v            # Lancer les tests
python src/demo_reprendre_voiture.py  # Lancer la démo
```

### Partie 3

```bash
cd partie3
PYTHONPATH=src pytest tests/ -v                          # Lancer les tests
PYTHONPATH=src python src/demo_statistiques.py           # Lancer la démo
```

---

## Résultats des tests

```
Partie 2 : 22 passed
Partie 3 :  4 passed
```
