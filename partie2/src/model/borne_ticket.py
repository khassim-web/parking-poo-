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
        self.id_borne = id_borne
        self.tickets_emis = []
        self.est_operationnelle = True
    
    def generer_ticket(self, voiture, client, est_abonne):
        """Génère un ticket (stub minimal pour Partie 1)."""
        if not self.est_operationnelle:
            raise ValueError("La borne n'est pas opérationnelle")
        
        ticket = {
            'numero': f"T{len(self.tickets_emis) + 1:04d}",
            'immatriculation': voiture.immatriculation,
            'client_nom': client.nom,
            'client_abonne': est_abonne,
            'date_entree': datetime.now()
        }
        
        self.tickets_emis.append(ticket)
        return ticket
    
    def lire_ticket(self, numero_ticket):
        """Lit un ticket existant."""
        if not self.est_operationnelle:
            raise ValueError("La borne n'est pas opérationnelle")
        
        # Chercher le ticket
        for ticket in self.tickets_emis:
            if ticket['numero'] == numero_ticket:
                return ticket
        
        raise ValueError(f"Ticket {numero_ticket} introuvable")
    
    def calculer_montant_du(self, ticket):
        """Calcule le montant dû."""
        # Durée de stationnement en minutes
        duree_minutes = (datetime.now() - ticket['date_entree']).total_seconds() / 60
        
        # Tarif : 2€/heure
        # 30 premières minutes gratuites
        if duree_minutes <= 30:
            return 0.0
        
        # Si abonné = gratuit
        if ticket.get('client_abonne', False):
            return 0.0
        
        # Calcul
        heures = (duree_minutes - 30) / 60
        montant = heures * 2.0
        
        return round(montant, 2)
    
    def traiter_paiement(self, montant, mode_paiement):
        """Traite le paiement."""
        if not self.est_operationnelle:
            raise ValueError("La borne n'est pas opérationnelle")
        
        # Modes acceptés
        modes_valides = ["CB", "ESPECES", "BADGE"]
        
        if mode_paiement not in modes_valides:
            raise ValueError(f"Mode de paiement invalide. Modes acceptés : {modes_valides}")
        
        # Simulation du paiement (toujours succès)
        # Dans une vraie implémentation, on contacterait une API bancaire
        return True
    
    def __str__(self):
        etat = "Opérationnelle" if self.est_operationnelle else "Hors service"
        return f"Borne #{self.id_borne} ({etat})"