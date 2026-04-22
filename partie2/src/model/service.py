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
        self.id_service = id_service
        self.voiture = voiture
        self.client = client
        self.date_demande = datetime.now()
        self.date_debut = None
        self.date_fin = None
        self.statut = "EN_ATTENTE"
        self.cout = 0.0

    @abstractmethod
    def calculer_cout(self):
        pass

    @abstractmethod
    def executer(self):
        pass

    def verifier_eligibilite_client(self):
        """Vérifie si le client est éligible aux services (doit être abonné)."""
        if not self.client.est_abonne:
            raise ValueError("Le client doit être abonné pour bénéficier de ce service")
        return True

    def demarrer(self):
        """Démarre l'exécution du service."""
        if self.statut != "EN_ATTENTE":
            raise ValueError("Le service doit être en attente pour démarrer")
        self.statut = "EN_COURS"
        self.date_debut = datetime.now()
        return True

    def terminer(self):
        """Termine le service."""
        if self.statut != "EN_COURS":
            raise ValueError("Le service doit être en cours pour être terminé")
        self.statut = "TERMINEE"
        self.date_fin = datetime.now()
        self.cout = self.calculer_cout()
        return True

    def annuler(self, raison):
        """Annule le service."""
        if self.statut == "TERMINEE":
            raise ValueError("Impossible d'annuler un service déjà terminé")
        self.statut = "ANNULEE"
        self.date_fin = datetime.now()
        return True

    def get_duree(self):
        """Calcule la durée du service en minutes."""
        if self.date_debut is None:
            return 0
        fin = self.date_fin if self.date_fin else datetime.now()
        return int((fin - self.date_debut).total_seconds() / 60)

    def __str__(self):
        return f"Service #{self.id_service} ({self.statut})"
