"""
Module de gestion de la maintenance des véhicules.

Ce module définit la classe Maintenance qui hérite de Service.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime
from .service import Service

class Maintenance(Service):
    """
    Service de maintenance pour les véhicules.

    Attributes (hérités + spécifiques):
        type_intervention (str): Type ('REVISION', 'VIDANGE', 'CONTROLE_TECHNIQUE', 'REPARATION')
        description (str): Description détaillée
        duree_estimee (int): Durée estimée en heures
        duree_reelle (int): Durée réelle en heures
        cout_estime (float): Coût estimé
        cout_final (float): Coût final
        garage (str): Nom du garage/prestataire
        rapport (dict): Rapport d'intervention
    """

    TYPES_VALIDES = ['REVISION', 'VIDANGE', 'CONTROLE_TECHNIQUE', 'REPARATION']
    TARIFS = {'REVISION': 150.0, 'VIDANGE': 80.0, 'CONTROLE_TECHNIQUE': 60.0, 'REPARATION': 200.0}

    def __init__(self, id_service, voiture, client, type_intervention, description):
        if type_intervention not in self.TYPES_VALIDES:
            raise ValueError(f"Type invalide. Types acceptés : {self.TYPES_VALIDES}")
        if not description or description.strip() == "":
            raise ValueError("La description ne peut pas être vide")

        super().__init__(id_service, voiture, client)
        self.type_intervention = type_intervention
        self.description = description
        self.duree_estimee = 2
        self.duree_reelle = None
        self.cout_estime = self.TARIFS[type_intervention]
        self.cout_final = None
        self.garage = None
        self.rapport = None

    def calculer_cout(self):
        """Calcule le coût de la maintenance."""
        return self.cout_final if self.cout_final is not None else self.cout_estime

    def executer(self):
        """Exécute le service de maintenance."""
        self.demarrer()
        self.terminer()
        return True

    def assigner_garage(self, nom_garage):
        """Assigne un garage/prestataire à la maintenance."""
        if not nom_garage or nom_garage.strip() == "":
            raise ValueError("Le nom du garage ne peut pas être vide")
        self.garage = nom_garage
        return True

    def prendre_en_charge_vehicule(self):
        """Prend en charge le véhicule pour la maintenance."""
        if self.garage is None:
            raise ValueError("Aucun garage n'est assigné")
        return True

    def terminer_intervention(self, rapport):
        """Termine l'intervention et enregistre le rapport."""
        champs_requis = ['operations_effectuees', 'duree_reelle', 'cout_final']
        for champ in champs_requis:
            if champ not in rapport:
                raise ValueError(f"Le rapport est incomplet, champ manquant : {champ}")

        self.rapport = rapport
        self.duree_reelle = rapport['duree_reelle']
        self.cout_final = rapport['cout_final']
        if self.statut == "EN_COURS":
            self.terminer()
        return True

    def __str__(self):
        return f"Maintenance #{self.id_service} - {self.type_intervention} ({self.voiture.immatriculation}) - {self.statut}"
