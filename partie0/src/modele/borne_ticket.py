"""
Module de gestion des bornes à tickets-paiement.

Ce module définit la classe Borne_Ticket qui gère l'émission des tickets
et les paiements dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime

class Borne_Ticket:
    """
    Représente une borne à tickets-paiement du parking DreamPark.
    
    La borne gère l'émission de tickets, les paiements, et l'interaction
    avec les clients. Elle est utilisée par un Acces (relation d'agrégation).
    
    Attributes:
        id_borne (int): Identifiant unique
        tickets_emis (list[dict]): Liste des tickets émis
        est_operationnelle (bool): True si la borne fonctionne
    """
    
    def __init__(self, id_borne):
        """
        Initialise une nouvelle borne.
        
        Args:
            id_borne (int): Identifiant unique
            
        Raises:
            ValueError: Si l'id_borne est négatif
            
        Note:
            La borne est créée indépendamment et peut être
            installée sur un Acces (agrégation).
            
        Example:
            >>> borne = Borne_Ticket(1)
            >>> borne.est_operationnelle
            True
        """
        pass
    
    def interroger_client(self):
        """
        Interroge le client pour connaître son statut.
        
        Returns:
            dict: Informations du client
                - est_abonne: bool
                - mode_paiement: str
                - services_demandes: list
                
        Example:
            >>> borne = Borne_Ticket(1)
            >>> info_client = borne.interroger_client()
        """
        pass
    
    def generer_ticket(self, voiture, place, client_info):
        """
        Génère un ticket de parking.
        
        Args:
            voiture (Voiture): Voiture garée
            place (Place): Place assignée
            client_info (dict): Informations du client
            
        Returns:
            dict: Ticket généré
                - numero_ticket: str
                - immatriculation: str
                - numero_place: int
                - heure_entree: datetime
                - type_client: str
                
        Raises:
            ValueError: Si la borne n'est pas opérationnelle
            
        Example:
            >>> borne = Borne_Ticket(1)
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> place = Place(1, 101, 0, 5.0, 2.5)
            >>> client_info = {"est_abonne": False}
            >>> ticket = borne.generer_ticket(voiture, place, client_info)
        """
        pass
    
    def lire_ticket(self, numero_ticket):
        """
        Lit les informations d'un ticket.
        
        Args:
            numero_ticket (str): Numéro du ticket
            
        Returns:
            dict: Informations du ticket
            
        Raises:
            ValueError: Si le ticket n'existe pas
            
        Example:
            >>> borne = Borne_Ticket(1)
            >>> ticket = borne.lire_ticket("TKT-001")
        """
        pass
    
    def calculer_montant_du(self, ticket):
        """
        Calcule le montant dû pour un ticket.
        
        Args:
            ticket (dict): Ticket de parking
            
        Returns:
            float: Montant en euros
            
        Example:
            >>> borne = Borne_Ticket(1)
            >>> ticket = {"heure_entree": datetime.now(), "type_client": "STANDARD"}
            >>> montant = borne.calculer_montant_du(ticket)
        """
        pass
    
    def traiter_paiement(self, montant, mode_paiement):
        """
        Traite un paiement.
        
        Args:
            montant (float): Montant à payer
            mode_paiement (str): Mode de paiement ('CB', 'ESPECES', 'BADGE')
            
        Returns:
            bool: True si le paiement a réussi
            
        Raises:
            ValueError: Si le montant est négatif
            ValueError: Si le mode de paiement n'est pas reconnu
            
        Example:
            >>> borne = Borne_Ticket(1)
            >>> borne.traiter_paiement(5.50, "CB")
            True
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la borne.
        
        Returns:
            str: Description de la borne
            
        Example:
            >>> borne = Borne_Ticket(1)
            >>> print(borne)
            Borne #1 (Opérationnelle)
        """
        pass