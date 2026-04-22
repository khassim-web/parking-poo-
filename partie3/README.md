# Partie 3 — Statistiques (Architecture MVC)

**Auteur : ABOULKHASSIM Abdallah**  
L3 Informatique — Université Toulouse 2 Jean Jaurès

---

## Objectif

Implémenter un module de statistiques pour le parking DreamPark selon le patron de conception **MVC (Modèle-Vue-Contrôleur)**.

---

## Architecture MVC

```
src/
├── model/
│   └── statistiques.py        # Modèle — historique des passages
├── controller/
│   └── statistiques_controller.py  # Contrôleur — orchestration
└── view/
    └── statistiques_view.py   # Vue — affichage texte + export HTML
```

### Modèle — `Statistiques`

Gère la persistance en mémoire des placements terminés.

| Méthode | Description |
|---------|-------------|
| `ajouter_passage(placement)` | Archive un placement finalisé |
| `get_chiffre_affaires_total()` | Calcule le CA total |
| `get_frequentation_par_service()` | Répartition par type de service |
| `identifier_clients_reguliers(seuil)` | Détecte les clients fréquents |

### Contrôleur — `StatistiquesController`

Orchestre la récupération des données et pilote la génération des rapports.

| Méthode | Description |
|---------|-------------|
| `collecter_donnees()` | Agrège CA, fréquentation, clients réguliers |
| `generer_rapport_texte()` | Affichage console |
| `generer_rapport_html(fichier)` | Export HTML stylisé |

### Vue — `StatistiquesView`

Gère la présentation des données.

- Rapport **console** : résumé rapide pour l'administrateur
- Rapport **HTML** : document structuré avec tableau des passages

---

## Installation et exécution

```bash
cd partie3
PYTHONPATH=src pytest tests/ -v      # 4 tests
PYTHONPATH=src python src/demo_statistiques.py  # Génère le rapport HTML
```

## Résultats

```
4 passed in 0.01s
```

Le rapport HTML est généré dans `rapport_final_dreampark.html`.

---

## Exemple de rapport

```
========================================
   RAPPORT D'ACTIVITÉ - DREAMPARK
========================================
Chiffre d'affaires total : 50.00€

Répartition par service :
 - Standard: 2 passage(s)
 - Maintenance: 1 passage(s)
 - Livraison: 1 passage(s)

Clients réguliers à fidéliser :
 - Voiture AA-111-AA: 2 visites
========================================
```
