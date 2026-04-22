"""
Module de gestion des accès du parking.

Ce module définit la classe Acces qui représente un point d'entrée/sortie
du parking DreamPark avec ses équipements.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

class Acces:
    """
    Représente un accès (entrée/sortie) du parking DreamPark.
    
    Chaque accès est équipé d'une caméra, d'une borne à tickets-paiement,
    de deux téléporteurs et d'un panneau d'affichage (AGRÉGATION).
    
    Attributes:
        id_acces (int): Identifiant unique de l'accès
        nom (str): Nom de l'accès (ex: "Nord", "Sud")
        camera (Camera): Caméra de l'accès (agrégation)
        borne (Borne_Ticket): Borne à tickets-paiement (agrégation)
        teleporteurs (list[Teleporteur]): Liste des 2 téléporteurs (agrégation)
        panneau (Panneau_Affichage): Panneau d'affichage (agrégation)
        est_actif (bool): True si l'accès est opérationnel
    """
 
    def __init__(self, id_acces, nom):
        self.id_acces = id_acces
        self.nom = nom
        self.camera = None
        self.borne = None
        self.teleporteurs = []
        self.panneau = None
        self.est_actif = True
    
    def installer_camera(self, camera):
        """Installe une caméra."""
        if self.camera is not None:
            raise ValueError("Une caméra est déjà installée")
        self.camera = camera
        return True
    
    def installer_borne(self, borne):
        """Installe une borne."""
        if self.borne is not None:
            raise ValueError("Une borne est déjà installée")
        self.borne = borne
        return True
    
    def ajouter_teleporteur(self, teleporteur):
        """Ajoute un téléporteur."""
        if len(self.teleporteurs) >= 2:
            raise ValueError("Maximum 2 téléporteurs par accès")
        self.teleporteurs.append(teleporteur)
        return True
    
    def installer_panneau(self, panneau):
        """Installe un panneau."""
        if self.panneau is not None:
            raise ValueError("Un panneau est déjà installé")
        self.panneau = panneau
        return True
    
    def teleporter_vers_place(self, voiture, place):
        """Téléporte la voiture vers une place."""
        # Trouver un téléporteur disponible
        teleporteur_dispo = None
        for t in self.teleporteurs:
            if t.est_disponible:
                teleporteur_dispo = t
                break
        
        if not teleporteur_dispo:
            raise ValueError("Aucun téléporteur disponible")
        
        return teleporteur_dispo.teleporter_vers_place(voiture, place)
    
    def teleporter_vers_acces(self, voiture):
        """Ramène une voiture à l'accès."""
        # Trouver un téléporteur disponible
        teleporteur_dispo = None
        for t in self.teleporteurs:
            if t.est_disponible:
                teleporteur_dispo = t
                break
        
        if not teleporteur_dispo:
            raise ValueError("Aucun téléporteur disponible")
        
        return teleporteur_dispo.teleporter_vers_acces(voiture)
    
    def retirer_camera(self):
        """Retire la caméra de l'accès (agrégation)."""
        if self.camera is None:
            raise ValueError("Cet accès n'a pas de caméra")
        camera = self.camera
        self.camera = None
        return camera

    def retirer_teleporteur(self, teleporteur):
        """Retire un téléporteur de l'accès (agrégation)."""
        if teleporteur not in self.teleporteurs:
            raise ValueError("Ce téléporteur n'appartient pas à cet accès")
        self.teleporteurs.remove(teleporteur)
        return True

    def capturer_vehicule(self, voiture):
        """Capture les informations du véhicule via la caméra."""
        if self.camera is None:
            raise ValueError("Cet accès n'a pas de caméra installée")
        return self.camera.capturer_image(voiture)

    def activer(self):
        """Active l'accès."""
        self.est_actif = True
        return True

    def desactiver(self):
        """Désactive l'accès."""
        self.est_actif = False
        return True

    def __str__(self):
        etat = "Actif" if self.est_actif else "Inactif"
        equip = []
        if self.camera:
            equip.append("Camera")
        if self.borne:
            equip.append("Borne")
        if self.teleporteurs:
            equip.append(f"{len(self.teleporteurs)} Téléporteur(s)")
        if self.panneau:
            equip.append("Panneau")
        equipements = ", ".join(equip) if equip else "Aucun"
        return f"Accès {self.nom} ({etat}) - Équipements: {equipements}"