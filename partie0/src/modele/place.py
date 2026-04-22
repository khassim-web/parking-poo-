"""
Module de gestion des places de parking.

Ce module définit la classe Place qui représente une place de stationnement
dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""


class Place:
    """
    Représente une place de parking dans le système DreamPark.
    
    Une place possède un identifiant unique, des dimensions (longueur, hauteur),
    un niveau et un état (libre ou occupée).
    
    Attributes:
        id_place (int): Identifiant unique de la place dans le système
        numero (int): Numéro affiché de la place
        niveau (int): Niveau/étage où se trouve la place (0 pour rez-de-chaussée)
        longueur (float): Longueur de la place en mètres
        hauteur (float): Hauteur maximale autorisée en mètres
        est_libre (bool): État de disponibilité de la place
        voiture_occupante (Optional[Voiture]): Référence vers la voiture garée
    """
    
    def __init__(self, id_place: int, numero: int, niveau: int, 
             longueur: float, hauteur: float):
        """
        Initialise une nouvelle place de parking.
    
        Args:
            id_place : Identifiant unique de la place
            numero : Numéro de la place
            niveau : Niveau/étage de la place
            longueur : Longueur de la place en mètres
            hauteur : Hauteur maximale en mètres
        
        Raises:
            ValueError: Si id_place <= 0
            ValueError: Si numero <= 0
            ValueError: Si longueur <= 0 ou hauteur <= 0
        
        Example:
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> place.est_libre
            True
        """
        pass
    
    def est_compatible(self, voiture):
        """
        Vérifie si une voiture peut être garée dans cette place.
        
        Compare les dimensions de la voiture avec celles de la place.
        
        Args:
            voiture (Voiture): La voiture à vérifier
            
        Returns:
            bool: True si la voiture peut être garée, False sinon
            
        Raises:
            TypeError: Si l'argument n'est pas une instance de Voiture
            
        Note:
            Une voiture est compatible si :
            - Sa longueur <= longueur de la place
            - Sa hauteur <= hauteur de la place
            
        Example:
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> place.est_compatible(voiture)
            True
        """
        pass
    
    def occuper(self, voiture):
        """
        Occupe la place avec une voiture.
        
        Marque la place comme occupée et associe la voiture.
        
        Args:
            voiture (Voiture): La voiture qui va occuper la place
            
        Returns:
            bool: True si l'occupation a réussi, False sinon
            
        Raises:
            ValueError: Si la place est déjà occupée
            TypeError: Si l'argument n'est pas une instance de Voiture
            ValueError: Si la voiture n'est pas compatible avec la place
            
        Example:
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> place.occuper(voiture)
            True
            >>> place.est_libre
            False
        """
        pass
    
    def liberer(self):
        """
        Libère la place de parking.
        
        Marque la place comme libre et supprime la référence à la voiture.
        
        Returns:
            Voiture: La voiture qui occupait la place (None si déjà libre)
            
        Raises:
            ValueError: Si la place est déjà libre
            
        Example:
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> place.occuper(voiture)
            >>> ancienne_voiture = place.liberer()
            >>> place.est_libre
            True
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la place.
        
        Returns:
            str: Description de la place
            
        Example:
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> print(place)
            Place 101 (Niveau 0) - 5.0m x 2.5m - Libre
        """
        pass