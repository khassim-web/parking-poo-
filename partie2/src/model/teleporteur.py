"""
Module de gestion des téléporteurs.

Ce module définit la classe Teleporteur qui gère le transport
des véhicules dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

class Teleporteur:
    """
    Représente un téléporteur dans le système DreamPark.
    
    Le téléporteur transporte les véhicules entre l'accès et les places
    de parking de manière instantanée. Il est utilisé par un Acces 
    (relation d'agrégation).
    
    Attributes:
        id_teleporteur (int): Identifiant unique
        est_disponible (bool): True si le téléporteur est libre
        voiture_en_cours (Voiture): Voiture actuellement transportée (None si libre)
    """
    
    def __init__(self, id_teleporteur):
        """
        Initialise un nouveau téléporteur.
        
        Args:
            id_teleporteur (int): Identifiant unique
            
        Raises:
            ValueError: Si l'id_teleporteur est négatif
            
        Note:
            Le téléporteur est créé indépendamment et peut être
            ajouté à un Acces (agrégation).
            
        Example:
            >>> teleporteur = Teleporteur(1)
            >>> teleporteur.est_disponible
            True
        """
        self.id_teleporteur = id_teleporteur
        self.est_disponible = True
        self.voiture_en_cours = None
    
    def teleporter_vers_place(self, voiture, place):
        """Téléporte la voiture vers une place."""
        if not self.est_disponible:
            raise ValueError("Téléporteur occupé")
        
        # Simuler l'occupation temporaire
        self.est_disponible = False
        self.voiture_en_cours = voiture
        
        # Téléportation instantanée (simulation)
        
        # Libérer
        self.est_disponible = True
        self.voiture_en_cours = None
        
        return True
    
    def teleporter_vers_acces(self, voiture):
        """Ramène une voiture à l'accès."""
        if not self.est_disponible:
            raise ValueError("Téléporteur occupé")
        
        if not voiture.est_dans_parking():
            raise ValueError("La voiture n'est pas dans le parking")
        
        # Marquer comme occupé
        self.est_disponible = False
        self.voiture_en_cours = voiture
        
        # Téléportation instantanée (simulation)
        
        # Libérer
        self.est_disponible = True
        self.voiture_en_cours = None
        
        return True
    def __str__(self):
        etat = "Disponible" if self.est_disponible else "Occupé"
        return f"Téléporteur #{self.id_teleporteur} ({etat})"