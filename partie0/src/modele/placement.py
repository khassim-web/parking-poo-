"""
Module de gestion du placement des véhicules.

Ce module définit la classe Placement qui est une classe d'association
entre Voiture et Place.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime

class Placement:
    """
    Classe d'association entre Voiture et Place.
    
    Cette classe représente la relation entre une voiture et une place
    dans le parking, avec les attributs de cette relation.
    
    Attributes:
        voiture (Voiture): Voiture placée (extrémité de l'association)
        place (Place): Place assignée (extrémité de l'association)
        date_placement (datetime): Date et heure du placement
        acces_utilise (Acces): Accès par lequel le véhicule est entré
        statut (str): Statut du placement ('EN_COURS', 'TERMINE')
        ticket (dict): Ticket associé au placement
    """
    
    def __init__(self, voiture, place, acces):
        """
        Initialise un nouveau placement (association).
        
        Args:
            voiture (Voiture): Voiture à placer
            place (Place): Place assignée
            acces (Acces): Accès utilisé
            
        Raises:
            TypeError: Si les arguments ne sont pas du bon type
            ValueError: Si la place n'est pas compatible avec la voiture
            ValueError: Si la place est déjà occupée
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> acces = Acces(1, "Nord")
            >>> placement = Placement(voiture, place, acces)
        """
        pass
    
    def verifier_compatibilite(self):
        """
        Vérifie la compatibilité entre la voiture et la place.
        
        Returns:
            bool: True si la voiture peut être garée dans la place
            
        Example:
            >>> placement = Placement(voiture, place, acces)
            >>> placement.verifier_compatibilite()
            True
        """
        pass
    
    def get_duree_placement(self):
        """
        Calcule la durée du placement.
        
        Returns:
            int: Durée en minutes depuis le début du placement
            
        Example:
            >>> placement = Placement(voiture, place, acces)
            >>> duree = placement.get_duree_placement()
            >>> print(duree)
            45
        """
        pass
    
    def terminer_placement(self):
        """
        Termine le placement et met à jour le statut.
        
        Returns:
            bool: True si la terminaison a réussi
            
        Raises:
            ValueError: Si le placement est déjà terminé
            
        Example:
            >>> placement = Placement(voiture, place, acces)
            >>> placement.terminer_placement()
            True
        """
        pass
    
    def get_infos_placement(self):
        """
        Récupère toutes les informations du placement.
        
        Returns:
            dict: Informations complètes
                - immatriculation: str
                - numero_place: int
                - date_placement: datetime
                - acces: str
                - statut: str
                - duree: int
                
        Example:
            >>> placement = Placement(voiture, place, acces)
            >>> infos = placement.get_infos_placement()
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle du placement.
        
        Returns:
            str: Description du placement
            
        Example:
            >>> placement = Placement(voiture, place, acces)
            >>> print(placement)
            Placement: AB-123-CD → Place 101 (EN_COURS)
        """
        pass