"""
Module de gestion des contrats.

Ce module définit la classe Contrat qui est une classe d'association
entre Client et Abonnement.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime

class Contrat:
    """
    Classe d'association entre Client et Abonnement.
    
    Cette classe représente la relation contractuelle entre un client
    et un abonnement, avec les attributs de cette relation.
    
    Attributes:
        client (Client): Client signataire (extrémité de l'association)
        abonnement (Abonnement): Abonnement souscrit (extrémité de l'association)
        date_signature (datetime): Date de signature du contrat
        date_debut (datetime): Date de début du contrat
        date_fin (datetime): Date de fin du contrat
        conditions (dict): Conditions particulières du contrat
        est_actif (bool): True si le contrat est en vigueur
    """
    
    def __init__(self, client, abonnement):
        """
        Initialise un nouveau contrat (association).
        
        Args:
            client (Client): Client signataire
            abonnement (Abonnement): Abonnement souscrit
            
        Raises:
            TypeError: Si les arguments ne sont pas du bon type
            
        Example:
            >>> client = Client(1, "Dupont", "Jean", "0612", "jean@mail.com")
            >>> abonnement = Abonnement(1, "MENSUEL", 50.0, 1)
            >>> contrat = Contrat(client, abonnement)
        """
        pass
    
    def ajouter_condition(self, cle, valeur):
        """
        Ajoute une condition particulière au contrat.
        
        Args:
            cle (str): Nom de la condition
            valeur: Valeur de la condition
            
        Returns:
            bool: True si l'ajout a réussi
            
        Example:
            >>> contrat = Contrat(client, abonnement)
            >>> contrat.ajouter_condition("places_reservees", 2)
            True
        """
        pass
    
    def get_condition(self, cle, defaut=None):
        """
        Récupère la valeur d'une condition.
        
        Args:
            cle (str): Nom de la condition
            defaut: Valeur par défaut si la condition n'existe pas
            
        Returns:
            Valeur de la condition ou valeur par défaut
            
        Example:
            >>> contrat = Contrat(client, abonnement)
            >>> contrat.get_condition("places_reservees", 0)
            0
        """
        pass
    
    def est_valide(self):
        """
        Vérifie si le contrat est encore valide.
        
        Returns:
            bool: True si le contrat est actif et dans les dates
            
        Example:
            >>> contrat = Contrat(client, abonnement)
            >>> contrat.est_valide()
            True
        """
        pass
    
    def resilier(self):
        """
        Résilie le contrat.
        
        Returns:
            bool: True si la résiliation a réussi
            
        Example:
            >>> contrat = Contrat(client, abonnement)
            >>> contrat.resilier()
            True
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle du contrat.
        
        Returns:
            str: Description du contrat
            
        Example:
            >>> contrat = Contrat(client, abonnement)
            >>> print(contrat)
            Contrat: Jean Dupont - Abonnement MENSUEL (Actif)
        """
        pass