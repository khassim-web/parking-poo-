"""
Module de gestion de l'entretien des véhicules.

Ce module définit la classe Entretien qui représente un service
d'entretien courant pour les véhicules dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime

class Entretien:
    """
    Représente un service d'entretien de véhicule.

    Attributes:
        id_entretien (int): Identifiant unique
        voiture (Voiture): Voiture concernée
        client (Client): Client demandeur
        type_entretien (str): Type ('LAVAGE', 'NETTOYAGE_INTERIEUR', 'LAVAGE_COMPLET', 'CONTROLE_BASIQUE')
        description (str): Description détaillée
        date_demande (datetime): Date de la demande
        date_debut (datetime): Date de début effective
        date_fin (datetime): Date de fin effective
        duree_estimee (int): Durée estimée en minutes
        duree_reelle (int): Durée réelle en minutes
        cout (float): Coût du service en euros
        statut (str): Statut ('EN_ATTENTE', 'EN_COURS', 'TERMINEE', 'ANNULEE')
        prestataire (str): Nom du prestataire
        observations (str): Observations après entretien
    """

    TYPES_VALIDES = ['LAVAGE', 'NETTOYAGE_INTERIEUR', 'LAVAGE_COMPLET', 'CONTROLE_BASIQUE']
    TARIFS = {
        'LAVAGE': 15.0,
        'NETTOYAGE_INTERIEUR': 20.0,
        'LAVAGE_COMPLET': 30.0,
        'CONTROLE_BASIQUE': 10.0
    }
    DUREES = {
        'LAVAGE': 30,
        'NETTOYAGE_INTERIEUR': 45,
        'LAVAGE_COMPLET': 60,
        'CONTROLE_BASIQUE': 20
    }

    def __init__(self, id_entretien, voiture, client, type_entretien, description=""):
        if type_entretien not in self.TYPES_VALIDES:
            raise ValueError(f"Type invalide. Types acceptés : {self.TYPES_VALIDES}")

        self.id_entretien = id_entretien
        self.voiture = voiture
        self.client = client
        self.type_entretien = type_entretien
        self.description = description
        self.date_demande = datetime.now()
        self.date_debut = None
        self.date_fin = None
        self.duree_estimee = self.DUREES[type_entretien]
        self.duree_reelle = None
        self.cout = self.TARIFS[type_entretien]
        self.statut = "EN_ATTENTE"
        self.prestataire = None
        self.observations = ""

    def verifier_eligibilite_client(self):
        """Vérifie si le client est éligible au service d'entretien."""
        if not self.client.est_abonne:
            raise ValueError("Le client doit être abonné pour bénéficier de ce service")
        return True

    def calculer_cout_et_duree(self):
        """Calcule le coût et la durée de l'entretien."""
        return {
            'cout': self.TARIFS[self.type_entretien],
            'duree_estimee': self.DUREES[self.type_entretien]
        }

    def assigner_prestataire(self, nom_prestataire):
        """Assigne un prestataire à l'entretien."""
        if not nom_prestataire or nom_prestataire.strip() == "":
            raise ValueError("Le nom du prestataire ne peut pas être vide")
        if self.prestataire is not None:
            raise ValueError("Un prestataire est déjà assigné")
        self.prestataire = nom_prestataire
        return True

    def prendre_en_charge_vehicule(self):
        """Prend en charge le véhicule pour l'entretien."""
        if self.prestataire is None:
            raise ValueError("Aucun prestataire n'est assigné")
        if not self.voiture.est_dans_parking():
            raise ValueError("La voiture n'est pas dans le parking")
        return True

    def demarrer_entretien(self):
        """Démarre l'entretien du véhicule."""
        if self.statut != "EN_ATTENTE":
            raise ValueError("L'entretien doit être en attente pour démarrer")
        self.statut = "EN_COURS"
        self.date_debut = datetime.now()
        return True

    def terminer_entretien(self, observations=""):
        """Termine l'entretien et enregistre les observations."""
        if self.statut != "EN_COURS":
            raise ValueError("L'entretien n'est pas en cours")
        self.statut = "TERMINEE"
        self.date_fin = datetime.now()
        self.observations = observations
        if self.date_debut:
            self.duree_reelle = int((self.date_fin - self.date_debut).total_seconds() / 60)
        return True

    def restituer_vehicule(self):
        """Restitue le véhicule au parking après entretien."""
        if self.statut != "TERMINEE":
            raise ValueError("L'entretien doit être terminé avant restitution")
        return True

    def annuler_entretien(self, raison):
        """Annule la demande d'entretien."""
        if self.statut in ["EN_COURS", "TERMINEE"]:
            raise ValueError("Impossible d'annuler un entretien en cours ou terminé")
        self.statut = "ANNULEE"
        return True

    def modifier_type_entretien(self, nouveau_type):
        """Modifie le type d'entretien demandé."""
        if self.statut in ["EN_COURS", "TERMINEE"]:
            raise ValueError("Impossible de modifier un entretien en cours ou terminé")
        if nouveau_type not in self.TYPES_VALIDES:
            raise ValueError(f"Type invalide. Types acceptés : {self.TYPES_VALIDES}")
        self.type_entretien = nouveau_type
        self.cout = self.TARIFS[nouveau_type]
        self.duree_estimee = self.DUREES[nouveau_type]
        return True

    def get_infos_entretien(self):
        """Récupère toutes les informations de l'entretien."""
        return {
            'id_entretien': self.id_entretien,
            'type_entretien': self.type_entretien,
            'immatriculation': self.voiture.immatriculation,
            'client': f"{self.client.prenom} {self.client.nom}",
            'statut': self.statut,
            'cout': self.cout,
            'observations': self.observations
        }

    def calculer_duree_totale(self):
        """Calcule la durée totale de l'entretien en minutes."""
        if self.date_debut is None:
            return 0
        fin = self.date_fin if self.date_fin else datetime.now()
        return int((fin - self.date_debut).total_seconds() / 60)

    def __str__(self):
        return f"Entretien #{self.id_entretien} - {self.type_entretien} ({self.voiture.immatriculation}) - {self.statut}"
