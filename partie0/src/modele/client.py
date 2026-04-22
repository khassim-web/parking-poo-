"""
Module de gestion des clients.

Ce module définit la classe Client qui représente un utilisateur
du parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

class Client:
    """
    Représente un client du parking DreamPark.
    
    Un client peut être standard ou abonné. Les abonnés bénéficient
    de services supplémentaires.
    
    Attributes:
        id_client (int): Identifiant unique du client
        nom (str): Nom de famille
        prenom (str): Prénom
        telephone (str): Numéro de téléphone
        email (str): Adresse email
        voitures (list[Voiture]): Liste des voitures du client
        est_abonne (bool): True si le client a un abonnement actif
        historique (list[dict]): Historique des passages du client
    """
    
    def __init__(self, id_client, nom, prenom, telephone, email):
        """
        Initialise un nouveau client.
        
        Args:
            id_client (int): Identifiant unique
            nom (str): Nom de famille
            prenom (str): Prénom
            telephone (str): Numéro de téléphone
            email (str): Adresse email
            
        Raises:
            ValueError: Si l'id_client est négatif
            ValueError: Si nom ou prenom sont vides
            ValueError: Si telephone ou email sont invalides
            
        Example:
            >>> client = Client(1, "Dupont", "Jean", "0612345678", "jean@email.com")
            >>> print(client.nom)
            Dupont
        """
        pass
    
    def ajouter_voiture(self, voiture):
        """
        Ajoute une voiture au client.
        
        Args:
            voiture (Voiture): La voiture à ajouter
            
        Returns:
            bool: True si l'ajout a réussi
            
        Raises:
            TypeError: Si l'argument n'est pas une instance de Voiture
            ValueError: Si la voiture existe déjà pour ce client
            
        Example:
            >>> client = Client(1, "Dupont", "Jean", "0612345678", "jean@email.com")
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> client.ajouter_voiture(voiture)
            True
        """
        pass
    
    def est_client_regulier(self, seuil=10):
        """
        Détermine si le client est régulier.
        
        Args:
            seuil (int): Nombre minimum de passages pour être régulier
            
        Returns:
            bool: True si le nombre de passages >= seuil
            
        Example:
            >>> client = Client(1, "Dupont", "Jean", "0612345678", "jean@email.com")
            >>> client.est_client_regulier(10)
            False
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle du client.
        
        Returns:
            str: Description du client
            
        Example:
            >>> client = Client(1, "Dupont", "Jean", "0612345678", "jean@email.com")
            >>> print(client)
            Client: Jean Dupont (Abonné)
        """
        pass