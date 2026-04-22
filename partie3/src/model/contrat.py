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

    Attributes:
        client (Client): Client signataire
        abonnement (Abonnement): Abonnement souscrit
        date_signature (datetime): Date de signature du contrat
        date_debut (datetime): Date de début du contrat
        date_fin (datetime): Date de fin du contrat
        conditions (dict): Conditions particulières du contrat
        est_actif (bool): True si le contrat est en vigueur
    """

    def __init__(self, client, abonnement):
        self.client = client
        self.abonnement = abonnement
        self.date_signature = datetime.now()
        self.date_debut = abonnement.date_debut
        self.date_fin = abonnement.date_fin
        self.conditions = {}
        self.est_actif = True
        client.est_abonne = True

    def ajouter_condition(self, cle, valeur):
        """Ajoute une condition particulière au contrat."""
        self.conditions[cle] = valeur
        return True

    def get_condition(self, cle, defaut=None):
        """Récupère la valeur d'une condition."""
        return self.conditions.get(cle, defaut)

    def est_valide(self):
        """Vérifie si le contrat est encore valide."""
        return self.est_actif and self.abonnement.est_valide()

    def resilier(self):
        """Résilie le contrat."""
        self.est_actif = False
        self.abonnement.resilier()
        self.client.est_abonne = False
        return True

    def __str__(self):
        etat = "Actif" if self.est_actif else "Résilié"
        return f"Contrat: {self.client.prenom} {self.client.nom} - Abonnement {self.abonnement.type_abonnement} ({etat})"
