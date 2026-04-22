# Partie 0 — Modèle Objet DreamPark

**Auteur : ABOULKHASSIM Abdallah**  
L3 Informatique — Université Toulouse 2 Jean Jaurès

---

## Objectif

Définir le modèle objet complet du système de parking DreamPark.  
Cette partie contient l'architecture complète des classes avec leurs attributs, signatures de méthodes et tests unitaires associés.

---

## Classes implémentées

| Classe | Rôle |
|--------|------|
| `Parking` | Gestionnaire central (places, accès, historique) |
| `Place` | Place de stationnement (dimensions, état) |
| `Voiture` | Véhicule (immatriculation, longueur, hauteur) |
| `Client` | Propriétaire d'une voiture |
| `Acces` | Point d'entrée/sortie (caméra, borne, téléporteurs, panneau) |
| `Placement` | Association Voiture ↔ Place avec horodatage |
| `Borne_Ticket` | Émission de tickets et traitement des paiements |
| `Teleporteur` | Transport instantané des véhicules |
| `Panneau_Affichage` | Affichage du nombre de places disponibles |
| `Camera` | Capture d'immatriculation et de dimensions |
| `Abonnement` | Abonnement client (mensuel, annuel, pack garanti) |
| `Contrat` | Association Client ↔ Abonnement |
| `Service` | Classe abstraite des services (Livraison, Maintenance, Entretien) |
| `Livraison` | Service de livraison de véhicule à domicile |
| `Maintenance` | Service de maintenance technique |
| `Entretien` | Service d'entretien courant (lavage, nettoyage) |
| `Voiturier` | Personnel effectuant les livraisons |

---

## Structure

```
partie0/
├── src/
│   ├── modele/       # Classes du domaine
│   └── tests/        # Tests unitaires par classe
└── docs/             # Documentation HTML (pdoc)
```

---

## Documentation

La documentation HTML générée avec `pdoc` est disponible dans `docs/`.
