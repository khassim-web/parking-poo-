# Partie 3 — Statistiques (Architecture MVC)

**Auteur : ABOULKHASSIM Abdallah**  
L3 Informatique — Université Toulouse 2 Jean Jaurès

---

## Objectif

Implémenter un module de statistiques pour le parking DreamPark en suivant le patron de conception **MVC (Modèle-Vue-Contrôleur)**.  
Ce module permet de générer des rapports d'activité (console et HTML) à partir de l'historique des passages.

---

## Architecture MVC

```
src/
├── model/
│   └── statistiques.py             # Modèle — historique et calculs
├── controller/
│   └── statistiques_controller.py  # Contrôleur — orchestration
└── view/
    └── statistiques_view.py        # Vue — affichage texte et export HTML
```

### Modèle — `Statistiques`

Gère la persistance en mémoire des placements terminés et calcule les indicateurs.

| Méthode | Description |
|---------|-------------|
| `ajouter_passage(placement)` | Archive un placement finalisé |
| `get_chiffre_affaires_total()` | Calcule le chiffre d'affaires total |
| `get_frequentation_par_service()` | Répartition des passages par type de service |
| `identifier_clients_reguliers(seuil)` | Détecte les clients dont le nombre de passages dépasse le seuil |

### Contrôleur — `StatistiquesController`

Orchestre la récupération des données du modèle et pilote la génération des rapports via la vue.

| Méthode | Description |
|---------|-------------|
| `collecter_donnees()` | Agrège CA, fréquentation et clients réguliers |
| `generer_rapport_texte()` | Affiche le rapport dans la console |
| `generer_rapport_html(fichier)` | Exporte le rapport dans un fichier HTML |

### Vue — `StatistiquesView`

Gère la présentation des données sous deux formats :

- **Console** : résumé rapide lisible par l'administrateur
- **HTML** : document stylisé avec tableau détaillé des passages

---

## Lancer les tests

```bash
cd partie3
PYTHONPATH=src pytest tests/ -v
```

## Lancer la démonstration

```bash
cd partie3
PYTHONPATH=src python src/demo_statistiques.py
```

Le fichier `rapport_final_dreampark.html` est généré dans le dossier `partie3/`.

---

## Résultats

```
4 passed in 0.01s
```

## Exemple de rapport console

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
