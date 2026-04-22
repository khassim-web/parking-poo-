"""
Module de gestion des voitures.

Ce module définit la classe Voiture qui représente un véhicule
dans le système de parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

class Voiture:
    """
    Représente un véhicule dans le système DreamPark.
    
    Attributes:
        immatriculation (str): Numéro d'immatriculation du véhicule
        longueur (float): Longueur du véhicule en mètres
        hauteur (float): Hauteur du véhicule en mètres
        proprietaire (Client): Référence vers le propriétaire
        place_actuelle (Place): Place occupée actuellement (None si hors parking)
    """
    
    def __init__(self, immatriculation, longueur, hauteur, proprietaire=None):
            """Initialise une voiture."""
            if not immatriculation or immatriculation.strip() == "":
                raise ValueError("L'immatriculation ne peut pas être vide")
        
            if longueur <= 0 or hauteur <= 0:
                raise ValueError("Les dimensions doivent être positives")
        
            self.immatriculation = immatriculation
            self.longueur = longueur
            self.hauteur = hauteur
            self.proprietaire = proprietaire
            self.place_actuelle = None
    
    def est_dans_parking(self):
        """Vérifie si la voiture est dans le parking."""
        return self.place_actuelle is not None
    
    def garer(self, place):
        """Gare la voiture dans une place."""
        if self.est_dans_parking():
            raise ValueError("La voiture est déjà garée")
        
        self.place_actuelle = place
    
    def retirer(self):
        """Retire la voiture du parking."""
        if not self.est_dans_parking():
            raise ValueError("La voiture n'est pas dans le parking")
        
        place = self.place_actuelle
        self.place_actuelle = None
        return place

    
    def __str__(self):
        return f"Voiture {self.immatriculation} ({self.longueur}m x {self.hauteur}m)"
    
    