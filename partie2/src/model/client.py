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
        Initialise un client.
        
        Args:
            id_client (int): Identifiant unique
            nom (str): Nom du client
            prenom (str): Prénom du client
            telephone (str): Numéro de téléphone
            email (str): Adresse email
        """
        if not nom or nom.strip() == "":
            raise ValueError("Le nom ne peut pas être vide")
        
        if not email or "@" not in email:
            raise ValueError("Email invalide")
        
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.voitures = []
        self.est_abonne = False
        self.historique = []
    
    def ajouter_voiture(self, voiture):
        """
        Ajoute une voiture au client.
        
        Args:
            voiture (Voiture): La voiture à ajouter
        """
        if voiture in self.voitures:
            raise ValueError("Cette voiture existe déjà pour ce client")
        
        self.voitures.append(voiture)
        voiture.proprietaire = self
    
    def est_client_regulier(self, seuil=10):
        """
        Vérifie si le client est régulier.
        
        Args:
            seuil (int): Nombre de passages minimum
        
        Returns:
            bool: True si régulier
        """
        return len(self.historique) >= seuil
    
    
    def __str__(self):
        etat = "Abonné" if self.est_abonne else "Standard"
        return f"Client: {self.prenom} {self.nom} ({etat})"