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
    
    def __init__(self, immatriculation, longueur, hauteur):
        """
        Initialise une nouvelle voiture.
        
        Args:
            immatriculation (str): Numéro d'immatriculation
            longueur (float): Longueur en mètres
            hauteur (float): Hauteur en mètres
            
        Raises:
            ValueError: Si l'immatriculation est vide
            ValueError: Si longueur ou hauteur sont négatives ou nulles
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> print(voiture.immatriculation)
            AB-123-CD
        """
        pass
    
    def est_dans_parking(self):
        """
        Vérifie si la voiture est actuellement dans le parking.
        
        Returns:
            bool: True si la voiture occupe une place
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> voiture.est_dans_parking()
            False
        """
        pass
    
    def garer(self, place):
        """
        Gare la voiture à une place donnée.
        
        Args:
            place (Place): La place où garer la voiture
            
        Returns:
            bool: True si le stationnement a réussi
            
        Raises:
            TypeError: Si l'argument n'est pas une instance de Place
            ValueError: Si la voiture est déjà garée
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> voiture.garer(place)
            True
        """
        pass
    
    def retirer(self):
        """
        Retire la voiture de sa place actuelle.
        
        Returns:
            Place: La place libérée
            
        Raises:
            ValueError: Si la voiture n'est pas garée
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> place = voiture.retirer()
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la voiture.
        
        Returns:
            str: Description de la voiture
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> print(voiture)
            Voiture AB-123-CD (4.5m x 1.8m)
        """
        pass
    
    