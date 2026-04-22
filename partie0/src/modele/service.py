"""
Module de gestion des services du parking.

Ce module définit la classe Service qui est la classe parent abstraite
de tous les services du parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Service(ABC):
    """
    Classe abstraite représentant un service du parking DreamPark.
    
    Cette classe est la classe parent de tous les services proposés
    (Livraison, Maintenance, Entretien). Elle définit le comportement
    commun à tous les services.
    
    Attributes:
        id_service (int): Identifiant unique du service
        voiture (Voiture): Voiture concernée par le service
        client (Client): Client demandeur du service
        date_demande (datetime): Date de la demande
        date_debut (datetime): Date de début du service
        date_fin (datetime): Date de fin du service
        statut (str): Statut ('EN_ATTENTE', 'EN_COURS', 'TERMINEE', 'ANNULEE')
        cout (float): Coût du service en euros
    """
    
    def __init__(self, id_service, voiture, client):
        """
        Initialise un nouveau service.
        
        Args:
            id_service (int): Identifiant unique
            voiture (Voiture): Voiture concernée
            client (Client): Client demandeur
            
        Raises:
            ValueError: Si l'id_service est négatif
            TypeError: Si les arguments ne sont pas du bon type
            ValueError: Si le client n'est pas abonné
            
        Note:
            Service est une classe abstraite. Utiliser les classes concrètes :
            Livraison, Maintenance ou Entretien.
            
        Example:
            >>> # Service ne peut pas être instanciée directement
            >>> # Utiliser : Livraison, Maintenance ou Entretien
        """
        pass
    
    @abstractmethod
    def calculer_cout(self):
        """
        Calcule le coût du service.
        
        Méthode abstraite à implémenter dans les classes filles.
        
        Returns:
            float: Coût du service en euros
        """
        pass
    
    @abstractmethod
    def executer(self):
        """
        Exécute le service.
        
        Méthode abstraite à implémenter dans les classes filles.
        
        Returns:
            bool: True si l'exécution a réussi
        """
        pass
    
    def verifier_eligibilite_client(self):
        """
        Vérifie si le client est éligible aux services.
        
        Seuls les clients abonnés peuvent bénéficier des services.
        
        Returns:
            bool: True si le client est abonné
            
        Raises:
            ValueError: Si le client n'est pas abonné
            
        Example:
            >>> # Dans une classe fille
            >>> service.verifier_eligibilite_client()
            True
        """
        pass
    
    def demarrer(self):
        """
        Démarre l'exécution du service.
        
        Change le statut de 'EN_ATTENTE' à 'EN_COURS' et enregistre
        la date de début.
        
        Returns:
            bool: True si le démarrage a réussi
            
        Raises:
            ValueError: Si le service n'est pas au statut 'EN_ATTENTE'
            
        Example:
            >>> # Dans une classe fille
            >>> service.demarrer()
            True
        """
        pass
    
    def terminer(self):
        """
        Termine le service.
        
        Change le statut à 'TERMINEE' et enregistre la date de fin.
        
        Returns:
            bool: True si la terminaison a réussi
            
        Raises:
            ValueError: Si le service n'est pas en cours
            
        Example:
            >>> # Dans une classe fille
            >>> service.terminer()
            True
        """
        pass
    
    def annuler(self, raison):
        """
        Annule le service.
        
        Args:
            raison (str): Raison de l'annulation
            
        Returns:
            bool: True si l'annulation a réussi
            
        Raises:
            ValueError: Si le service est déjà terminé
            
        Example:
            >>> # Dans une classe fille
            >>> service.annuler("Client indisponible")
            True
        """
        pass
    
    def get_duree(self):
        """
        Calcule la durée du service.
        
        Returns:
            int: Durée en minutes (0 si pas encore commencé)
            
        Example:
            >>> # Dans une classe fille
            >>> duree = service.get_duree()
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle du service.
        
        Returns:
            str: Description du service
        """
        pass