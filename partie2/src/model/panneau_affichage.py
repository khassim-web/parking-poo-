"""
Module de gestion des panneaux d'affichage.

Ce module définit la classe Panneau_Affichage qui affiche le nombre
de places disponibles dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""
from datetime import datetime
class Panneau_Affichage:
    """
    Représente un panneau d'affichage du parking DreamPark.
    
    Le panneau affiche en temps réel le nombre de places disponibles.
    Il est utilisé par un Acces (relation d'agrégation).
    
    Attributes:
        id_panneau (int): Identifiant unique
        nb_places_affiche (int): Nombre de places actuellement affiché
        est_allume (bool): True si le panneau est allumé
        historique_affichages (list[dict]): Historique des mises à jour
    """

    def __init__(self, id_panneau):
        self.id_panneau = id_panneau
        self.nb_places_affiche = 0
        self.est_allume = True
        self.historique_affichages = []
    
    def afficher(self, nb_places):
        """Affiche un nombre de places."""
        if not self.est_allume:
            raise ValueError("Le panneau est éteint")
        
        self.nb_places_affiche = nb_places
        self.historique_affichages.append({
            'action': 'AFFICHAGE',
            'valeur': nb_places,
            'date': datetime.now()
        })
    
    def decrementer(self):
        """Décrémente le compteur de places disponibles."""
        if not self.est_allume:
            raise ValueError("Le panneau est éteint")
        
        if self.nb_places_affiche <= 0:
            raise ValueError("Impossible de décrémenter, déjà à 0")
        
        self.nb_places_affiche -= 1
        self.historique_affichages.append({
            'action': 'DECREMENT',
            'valeur': self.nb_places_affiche,
            'date': datetime.now()
        })
        
        return self.nb_places_affiche
    
    def incrementer(self):
        """Incrémente le compteur de places disponibles."""
        if not self.est_allume:
            raise ValueError("Le panneau est éteint")
        
        self.nb_places_affiche += 1
        self.historique_affichages.append({
            'action': 'INCREMENT',
            'valeur': self.nb_places_affiche,
            'date': datetime.now()
        })
        
        return self.nb_places_affiche
    
    def mettre_a_jour(self, nouveau_nb_places):
        """Met à jour l'affichage avec un nouveau nombre de places."""
        if nouveau_nb_places < 0:
            raise ValueError("Le nombre de places ne peut pas être négatif")
        self.nb_places_affiche = nouveau_nb_places
        self.historique_affichages.append({
            'action': 'MISE_A_JOUR',
            'valeur': nouveau_nb_places,
            'date': datetime.now()
        })
        return True

    def allumer(self):
        """Allume le panneau."""
        self.est_allume = True
        return True

    def eteindre(self):
        """Éteint le panneau."""
        self.est_allume = False
        return True

    def __str__(self):
        etat = "Allumé" if self.est_allume else "Éteint"
        return f"Panneau #{self.id_panneau} - {self.nb_places_affiche} places disponibles ({etat})"