# Projet DreamPark — Gestion de Parking

Projet Python réalisé dans le cadre du cours **MIOC501T — Programmation Orientée Objet**  
L3 Informatique — Université Toulouse 2 Jean Jaurès

**Auteur : ABOULKHASSIM Abdallah**

---

## Présentation

DreamPark est un système de gestion de parking intelligent. Le projet est structuré en trois parties progressives, chacune ajoutant une couche de fonctionnalités au-dessus de la précédente.

| Partie | Contenu |
|--------|---------|
| `partie0/` | Modèle objet complet (squelette de classes + tests unitaires) |
| `partie2/` | Implémentation du use case *"Reprendre la voiture"* |
| `partie3/` | Module de statistiques avec architecture MVC |

---

## Structure du projet

```
projet_parking/
├── partie0/          # Modèle objet — squelette
│   └── src/
│       ├── modele/   # 15 classes du domaine
│       └── tests/    # Tests unitaires par classe
│
├── partie2/          # Use case "Reprendre la voiture"
│   └── src/
│       ├── model/    # Classes implémentées
│       ├── tests/    # 22 tests (100% passent)
│       └── demo_reprendre_voiture.py
│
└── partie3/          # Statistiques MVC
    ├── src/
    │   ├── model/       # Modèle + Statistiques
    │   ├── controller/  # StatistiquesController
    │   ├── view/        # StatistiquesView (texte + HTML)
    │   └── demo_statistiques.py
    └── tests/           # 4 tests (100% passent)
```

---

## Classes du domaine

`Parking` · `Place` · `Voiture` · `Client` · `Acces` · `Placement` · `Borne_Ticket` · `Teleporteur` · `Panneau_Affichage` · `Camera` · `Abonnement` · `Contrat` · `Service` · `Livraison` · `Maintenance` · `Entretien` · `Voiturier` · `Statistiques`

---

## Lancer les tests

```bash
# Partie 2
cd partie2
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest src/tests/ -v

# Partie 3
cd partie3
PYTHONPATH=src pytest tests/ -v
```
