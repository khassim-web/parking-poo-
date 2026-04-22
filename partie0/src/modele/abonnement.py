"""
Module de gestion des abonnements.

Ce module définit la classe Abonnement qui représente un abonnement
au parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime, timedelta

class Abonnement:
    """
    Représente un abonnement au parking DreamPark.
    
    Un abonnement donne accès à des services privilégiés :
    livraison, entretien, maintenance, et stationnement garanti.
    
    Attributes:
        id_abonnement (int): Identifiant unique
        type_abonnement (str): Type ('MENSUEL', 'ANNUEL', 'PACK_GARANTI')
        tarif (float): Coût de l'abonnement
        date_debut (datetime): Date de début de l'abonnement
        date_fin (datetime): Date de fin de l'abonnement
        services_inclus (list[str]): Types de services inclus
                                    ['LIVRAISON', 'MAINTENANCE', 'ENTRETIEN']
        est_actif (bool): True si l'abonnement est valide
    """
    
    def __init__(self, id_abonnement, type_abonnement, tarif, duree_mois=1):
        """
        Initialise un nouvel abonnement.
        
        Args:
            id_abonnement (int): Identifiant unique
            type_abonnement (str): Type ('MENSUEL', 'ANNUEL', 'PACK_GARANTI')
            tarif (float): Coût de l'abonnement en euros
            duree_mois (int): Durée en mois (1 pour mensuel, 12 pour annuel)
            
        Raises:
            ValueError: Si l'id_abonnement est négatif
            ValueError: Si le tarif est négatif
            ValueError: Si le type_abonnement n'est pas reconnu
            ValueError: Si la durée est négative ou nulle
            
        Example:
            >>> abonnement = Abonnement(1, "MENSUEL", 50.0, 1)
            >>> print(abonnement.type_abonnement)
            MENSUEL
        """
        pass
    
    def est_valide(self):
        """
        Vérifie si l'abonnement est encore valide.
        
        Returns:
            bool: True si la date actuelle est entre date_debut et date_fin
            
        Example:
            >>> abonnement = Abonnement(1, "MENSUEL", 50.0)
            >>> abonnement.est_valide()
            True
        """
        pass
    
    def renouveler(self, duree_mois=None):
        """
        Renouvelle l'abonnement pour une nouvelle période.
        
        Args:
            duree_mois (int, optional): Durée du renouvellement
                                        (None = même durée que l'original)
            
        Returns:
            bool: True si le renouvellement a réussi
            
        Raises:
            ValueError: Si la durée est négative ou nulle
            
        Example:
            >>> abonnement = Abonnement(1, "MENSUEL", 50.0)
            >>> abonnement.renouveler()
            True
        """
        pass
    
    def resilier(self):
        """
        Résilie l'abonnement immédiatement.
        
        Returns:
            bool: True si la résiliation a réussi
            
        Raises:
            ValueError: Si l'abonnement est déjà inactif
            
        Example:
            >>> abonnement = Abonnement(1, "MENSUEL", 50.0)
            >>> abonnement.resilier()
            True
        """
        pass
    
    def calculer_jours_restants(self):
        """
        Calcule le nombre de jours restants avant expiration.
        
        Returns:
            int: Nombre de jours restants (0 si expiré)
            
        Example:
            >>> abonnement = Abonnement(1, "MENSUEL", 50.0)
            >>> jours = abonnement.calculer_jours_restants()
            >>> print(jours)
            30
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle de l'abonnement.
        
        Returns:
            str: Description de l'abonnement
            
        Example:
            >>> abonnement = Abonnement(1, "MENSUEL", 50.0)
            >>> print(abonnement)
            Abonnement MENSUEL - 50.0€ (Actif jusqu'au 2025-12-27)
        """
        pass