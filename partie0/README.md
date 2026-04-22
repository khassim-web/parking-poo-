# Partie 0 — Modèle Objet DreamPark

**Auteur : ABOULKHASSIM Abdallah**  
L3 Informatique — Université Toulouse 2 Jean Jaurès

---

## Objectif

Concevoir et définir le modèle objet complet du système de parking DreamPark.  
Cette partie contient l'architecture de toutes les classes avec leurs attributs, leurs signatures de méthodes et leurs tests unitaires.  
Les méthodes sont volontairement laissées vides (`pass`) — elles sont implémentées dans les parties suivantes.

---

## Classes du domaine

| Classe | Rôle |
|--------|------|
| `Parking` | Gestionnaire central (places, accès, historique) |
| `Place` | Place de stationnement (dimensions, état libre/occupée) |
| `Voiture` | Véhicule (immatriculation, longueur, hauteur) |
| `Client` | Propriétaire d'une ou plusieurs voitures |
| `Acces` | Point d'entrée/sortie équipé (caméra, borne, téléporteurs, panneau) |
| `Placement` | Association Voiture ↔ Place avec horodatage |
| `Borne_Ticket` | Émission de tickets et traitement des paiements |
| `Teleporteur` | Transport instantané des véhicules vers une place ou un accès |
| `Panneau_Affichage` | Affichage en temps réel du nombre de places disponibles |
| `Camera` | Capture d'immatriculation et mesure des dimensions |
| `Abonnement` | Abonnement client (mensuel, annuel, pack garanti) |
| `Contrat` | Association Client ↔ Abonnement |
| `Service` | Classe abstraite parente des services (Livraison, Maintenance, Entretien) |
| `Livraison` | Service de livraison/récupération de véhicule à domicile |
| `Maintenance` | Service de maintenance technique (révision, vidange, réparation) |
| `Entretien` | Service d'entretien courant (lavage, nettoyage intérieur) |
| `Voiturier` | Personnel effectuant les livraisons de véhicules |

---

## Structure

```
partie0/
├── src/
│   ├── modele/           # 17 classes du domaine
│   │   ├── parking.py
│   │   ├── place.py
│   │   ├── voiture.py
│   │   ├── client.py
│   │   ├── acces.py
│   │   ├── placement.py
│   │   ├── borne_ticket.py
│   │   ├── teleporteur.py
│   │   ├── panneau_affichage.py
│   │   ├── camera.py
│   │   ├── abonnement.py
│   │   ├── contrat.py
│   │   ├── service.py
│   │   ├── livraison.py
│   │   ├── maintenance.py
│   │   ├── entretien.py
│   │   └── voiturier.py
│   └── tests/            # Un fichier de test par classe
└── docs/                 # Documentation HTML générée avec pdoc
```

---

## Documentation

La documentation HTML est disponible dans le dossier `docs/`.  
Ouvrir `docs/modele/index.html` dans un navigateur pour la consulter.
