"""
Module de gestion des voituriers.

Ce module définit la classe Voiturier qui représente un voiturier
effectuant les services de livraison pour le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

class Voiturier:
    """
    Représente un voiturier du parking DreamPark.

    Attributes:
        id_voiturier (int): Identifiant unique
        nom (str): Nom du voiturier
        prenom (str): Prénom du voiturier
        telephone (str): Numéro de téléphone
        est_disponible (bool): True si le voiturier est libre
        missions_en_cours (list[Livraison]): Livraisons en cours
        historique_missions (list[dict]): Historique des missions
    """

    def __init__(self, id_voiturier, nom, prenom, telephone):
        if not nom or nom.strip() == "":
            raise ValueError("Le nom ne peut pas être vide")
        if not prenom or prenom.strip() == "":
            raise ValueError("Le prénom ne peut pas être vide")

        self.id_voiturier = id_voiturier
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.est_disponible = True
        self.missions_en_cours = []
        self.historique_missions = []

    def assigner_mission(self, livraison):
        """Assigne une livraison au voiturier."""
        if not self.est_disponible:
            raise ValueError("Le voiturier n'est pas disponible")

        self.missions_en_cours.append(livraison)
        self.est_disponible = False
        livraison.voiturier = self
        return True

    def demarrer_mission(self, livraison):
        """Démarre l'exécution d'une livraison."""
        if livraison not in self.missions_en_cours:
            raise ValueError("Cette livraison n'est pas assignée à ce voiturier")
        livraison.demarrer()
        return True

    def terminer_mission(self, livraison):
        """Termine une livraison en cours."""
        if livraison not in self.missions_en_cours:
            raise ValueError("Cette livraison n'est pas assignée à ce voiturier")
        livraison.terminer()
        self.missions_en_cours.remove(livraison)
        self.historique_missions.append({
            'livraison_id': livraison.id_service,
            'voiture': livraison.voiture.immatriculation
        })
        if not self.missions_en_cours:
            self.est_disponible = True
        return True

    def __str__(self):
        etat = "Disponible" if self.est_disponible else "En mission"
        return f"Voiturier: {self.prenom} {self.nom} ({etat})"
