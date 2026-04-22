"""
Module de gestion des livraisons.

Ce module définit la classe Livraison qui hérite de Service.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime
from .service import Service

class Livraison(Service):
    """
    Service de livraison de véhicule.
    
    Hérite de Service et ajoute des fonctionnalités spécifiques
    à la livraison de véhicules.
    
    Attributes:
        Attributs hérités de Service:
            id_service, voiture, client, date_demande, date_debut,
            date_fin, statut, cout
            
        Attributs spécifiques:
            type_livraison (str): Type ('RECUPERATION', 'LIVRAISON_VEHICULE')
            adresse (str): Adresse de livraison/récupération
            heure_demandee (datetime): Heure souhaitée
            heure_effective (datetime): Heure effective
            voiturier (Voiturier): Voiturier assigné
    """
    
    def __init__(self, id_service, voiture, client, type_livraison, adresse, heure_demandee):
        """
        Initialise une nouvelle livraison.
        
        Args:
            id_service (int): Identifiant unique
            voiture (Voiture): Voiture concernée
            client (Client): Client demandeur
            type_livraison (str): Type de livraison
            adresse (str): Adresse de destination
            heure_demandee (datetime): Heure souhaitée
            
        Raises:
            ValueError: Si le type_livraison n'est pas reconnu
            ValueError: Si l'adresse est vide
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> client = Client(1, "Dupont", "Jean", "0612", "jean@mail.com")
            >>> heure = datetime(2025, 12, 1, 14, 0)
            >>> livraison = Livraison(
            ...     1, voiture, client, "LIVRAISON_VEHICULE",
            ...     "10 rue de la Paix", heure
            ... )
        """
        super().__init__(id_service, voiture, client)
        pass
    
    def calculer_cout(self):
        """
        Calcule le coût de la livraison.
        
        Implémentation de la méthode abstraite de Service.
        
        Returns:
            float: Coût en euros
            
        Note:
            Pour certains abonnements, le coût peut être 0.
            
        Example:
            >>> livraison = Livraison(1, voiture, client, "LIVRAISON_VEHICULE", 
            ...                       "10 rue X", heure)
            >>> cout = livraison.calculer_cout()
        """
        pass
    
    def executer(self):
        """
        Exécute le service de livraison.
        
        Implémentation de la méthode abstraite de Service.
        
        Returns:
            bool: True si l'exécution a réussi
            
        Example:
            >>> livraison = Livraison(1, voiture, client, "LIVRAISON_VEHICULE",
            ...                       "10 rue X", heure)
            >>> livraison.executer()
            True
        """
        pass
    
    def assigner_voiturier(self, voiturier):
        """
        Assigne un voiturier à la livraison.
        
        Args:
            voiturier (Voiturier): Voiturier à assigner
            
        Returns:
            bool: True si l'assignation a réussi
            
        Raises:
            TypeError: Si l'argument n'est pas une instance de Voiturier
            ValueError: Si le voiturier n'est pas disponible
            
        Example:
            >>> livraison = Livraison(1, voiture, client, "LIVRAISON_VEHICULE",
            ...                       "10 rue X", heure)
            >>> voiturier = Voiturier(1, "Martin", "Paul", "0612")
            >>> livraison.assigner_voiturier(voiturier)
            True
        """
        pass
    
    def modifier_horaire(self, nouvelle_heure):
        """
        Modifie l'heure de livraison.
        
        Args:
            nouvelle_heure (datetime): Nouvelle heure souhaitée
            
        Returns:
            bool: True si la modification a réussi
            
        Raises:
            ValueError: Si la nouvelle heure est dans le passé
            
        Example:
            >>> livraison = Livraison(1, voiture, client, "LIVRAISON_VEHICULE",
            ...                       "10 rue X", heure)
            >>> nouvelle_heure = datetime(2025, 12, 1, 16, 0)
            >>> livraison.modifier_horaire(nouvelle_heure)
            True
        """
        pass
    
    def modifier_adresse(self, nouvelle_adresse):
        """
        Modifie l'adresse de livraison.
        
        Args:
            nouvelle_adresse (str): Nouvelle adresse
            
        Returns:
            bool: True si la modification a réussi
            
        Raises:
            ValueError: Si l'adresse est vide
            
        Example:
            >>> livraison = Livraison(1, voiture, client, "LIVRAISON_VEHICULE",
            ...                       "10 rue X", heure)
            >>> livraison.modifier_adresse("20 avenue Y")
            True
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la livraison.
        
        Returns:
            str: Description
            
        Example:
            >>> livraison = Livraison(1, voiture, client, "LIVRAISON_VEHICULE",
            ...                       "10 rue X", heure)
            >>> print(livraison)
            Livraison #1 - LIVRAISON_VEHICULE (AB-123-CD) → 10 rue X
        """
        pass