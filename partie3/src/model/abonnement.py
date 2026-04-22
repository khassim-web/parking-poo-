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
        est_actif (bool): True si l'abonnement est valide
    """

    TYPES_VALIDES = ['MENSUEL', 'ANNUEL', 'PACK_GARANTI']

    def __init__(self, id_abonnement, type_abonnement, tarif, duree_mois=1):
        if tarif < 0:
            raise ValueError("Le tarif ne peut pas être négatif")
        if type_abonnement not in self.TYPES_VALIDES:
            raise ValueError(f"Type invalide. Types acceptés : {self.TYPES_VALIDES}")
        if duree_mois <= 0:
            raise ValueError("La durée doit être positive")

        self.id_abonnement = id_abonnement
        self.type_abonnement = type_abonnement
        self.tarif = tarif
        self.duree_mois = duree_mois
        self.date_debut = datetime.now()
        self.date_fin = self.date_debut + timedelta(days=duree_mois * 30)
        self.services_inclus = ['LIVRAISON', 'MAINTENANCE', 'ENTRETIEN']
        self.est_actif = True

    def est_valide(self):
        """Vérifie si l'abonnement est encore valide."""
        return self.est_actif and self.date_debut <= datetime.now() <= self.date_fin

    def renouveler(self, duree_mois=None):
        """Renouvelle l'abonnement pour une nouvelle période."""
        if duree_mois is None:
            duree_mois = self.duree_mois
        if duree_mois <= 0:
            raise ValueError("La durée doit être positive")

        self.date_fin = self.date_fin + timedelta(days=duree_mois * 30)
        self.est_actif = True
        return True

    def resilier(self):
        """Résilie l'abonnement immédiatement."""
        if not self.est_actif:
            raise ValueError("L'abonnement est déjà inactif")
        self.est_actif = False
        self.date_fin = datetime.now()
        return True

    def calculer_jours_restants(self):
        """Calcule le nombre de jours restants avant expiration."""
        if not self.est_actif:
            return 0
        delta = self.date_fin - datetime.now()
        return max(0, delta.days)

    def __str__(self):
        jours = self.calculer_jours_restants()
        etat = f"Actif jusqu'au {self.date_fin.strftime('%Y-%m-%d')}" if self.est_actif else "Résilié"
        return f"Abonnement {self.type_abonnement} - {self.tarif}€ ({etat})"
