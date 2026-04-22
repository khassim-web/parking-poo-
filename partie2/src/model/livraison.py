"""
Module de gestion des livraisons.

Ce module définit la classe Livraison qui hérite de Service.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime
from .service import Service

class Livraison(Service):
    """
    Service de livraison de véhicule.

    Attributes (hérités + spécifiques):
        type_livraison (str): Type ('RECUPERATION', 'LIVRAISON_VEHICULE')
        adresse (str): Adresse de livraison/récupération
        heure_demandee (datetime): Heure souhaitée
        heure_effective (datetime): Heure effective
        voiturier (Voiturier): Voiturier assigné
    """

    TYPES_VALIDES = ['RECUPERATION', 'LIVRAISON_VEHICULE']
    TARIF = 25.0

    def __init__(self, id_service, voiture, client, type_livraison, adresse, heure_demandee):
        if type_livraison not in self.TYPES_VALIDES:
            raise ValueError(f"Type invalide. Types acceptés : {self.TYPES_VALIDES}")
        if not adresse or adresse.strip() == "":
            raise ValueError("L'adresse ne peut pas être vide")

        super().__init__(id_service, voiture, client)
        self.type_livraison = type_livraison
        self.adresse = adresse
        self.heure_demandee = heure_demandee
        self.heure_effective = None
        self.voiturier = None

    def calculer_cout(self):
        """Calcule le coût de la livraison (25€ par défaut)."""
        return self.TARIF

    def executer(self):
        """Exécute le service de livraison."""
        self.demarrer()
        self.heure_effective = datetime.now()
        self.terminer()
        return True

    def assigner_voiturier(self, voiturier):
        """Assigne un voiturier à la livraison."""
        if not voiturier.est_disponible:
            raise ValueError("Le voiturier n'est pas disponible")
        self.voiturier = voiturier
        voiturier.est_disponible = False
        return True

    def modifier_horaire(self, nouvelle_heure):
        """Modifie l'heure de livraison."""
        if nouvelle_heure < datetime.now():
            raise ValueError("La nouvelle heure ne peut pas être dans le passé")
        self.heure_demandee = nouvelle_heure
        return True

    def modifier_adresse(self, nouvelle_adresse):
        """Modifie l'adresse de livraison."""
        if not nouvelle_adresse or nouvelle_adresse.strip() == "":
            raise ValueError("L'adresse ne peut pas être vide")
        self.adresse = nouvelle_adresse
        return True

    def __str__(self):
        return f"Livraison #{self.id_service} - {self.type_livraison} ({self.voiture.immatriculation}) → {self.adresse}"
