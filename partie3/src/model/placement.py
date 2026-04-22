"""
Module de gestion du placement des véhicules.

Ce module définit la classe Placement qui est une classe d'association
entre Voiture et Place.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime

class Placement:
    """
    Classe d'association entre Voiture et Place.
    
    Cette classe représente la relation entre une voiture et une place
    dans le parking, avec les attributs de cette relation.
    
    Attributes:
        voiture (Voiture): Voiture placée (extrémité de l'association)
        place (Place): Place assignée (extrémité de l'association)
        date_placement (datetime): Date et heure du placement
        acces_utilise (Acces): Accès par lequel le véhicule est entré
        statut (str): Statut du placement ('EN_COURS', 'TERMINE')
        ticket (dict): Ticket associé au placement
    """
    
    def __init__(self, voiture, place, acces):
        # Pas d'ID !
        self.voiture = voiture
        self.place = place
        self.date_placement = datetime.now()
        self.acces_utilise = acces
        self.statut = "EN_COURS"
        self.ticket = None
        self.date_fin = None
    
    def verifier_compatibilite(self):
        """Vérifie la compatibilité."""
        return self.place.est_compatible(self.voiture)
    
    def get_duree_placement(self):
        """Retourne la durée en minutes."""
        if self.statut == "TERMINE":
            duree_secondes = (self.date_fin - self.date_placement).total_seconds()
        else:
            duree_secondes = (datetime.now() - self.date_placement).total_seconds()
        
        return int(duree_secondes / 60)
    
    def terminer_placement(self, montant=0.0, mode_paiement=None, type_service="Standard"):
        """
        Termine le placement en enregistrant les infos de paiement et de service.
        Indispensable pour la Partie 3 : Gestion des statistiques.
        """
        if self.statut == "TERMINE":
            raise ValueError("Le placement est déjà terminé")
        
        self.statut = "TERMINE"
        self.date_fin = datetime.now()
        
        # Nouvelles données pour les statistiques 
        self.montant_paye = montant
        self.mode_paiement = mode_paiement
        self.type_service = type_service
    
    def get_infos_placement(self):
        """Retourne les infos du placement."""
        return {
            'voiture': self.voiture.immatriculation,
            'place': self.place.numero,
            'date_placement': self.date_placement,
            'duree_minutes': self.get_duree_placement(),
            'statut': self.statut
        }
    
    def __str__(self):
        place_num = self.place.numero if self.place else "N/A"
        return f"Placement: {self.voiture.immatriculation} → Place {place_num} ({self.statut})"