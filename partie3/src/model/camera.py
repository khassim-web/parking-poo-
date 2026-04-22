"""
Module de gestion des caméras.

Ce module définit la classe Camera qui gère la capture d'informations
sur les véhicules dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime

class Camera:
    """
    Représente une caméra de surveillance et de capture d'informations.

    La caméra capture l'immatriculation, la hauteur et la longueur
    des véhicules. Elle est utilisée par un Acces (relation d'agrégation).

    Attributes:
        id_camera (int): Identifiant unique
        est_active (bool): True si la caméra est en fonctionnement
        images_capturees (list[dict]): Historique des captures
    """

    def __init__(self, id_camera):
        self.id_camera = id_camera
        self.est_active = True
        self.images_capturees = []

    def capturer_image(self, voiture):
        """Capture une image du véhicule."""
        if not self.est_active:
            raise ValueError("La caméra est inactive")

        image = {
            'timestamp': datetime.now(),
            'immatriculation': voiture.immatriculation,
            'longueur': voiture.longueur,
            'hauteur': voiture.hauteur
        }
        self.images_capturees.append(image)
        return image

    def extraire_immatriculation(self, image):
        """Extrait l'immatriculation depuis une capture."""
        return image['immatriculation']

    def mesurer_dimensions(self, voiture):
        """Mesure les dimensions d'un véhicule."""
        return {'longueur': voiture.longueur, 'hauteur': voiture.hauteur}

    def activer(self):
        """Active la caméra."""
        self.est_active = True
        return True

    def desactiver(self):
        """Désactive la caméra."""
        self.est_active = False
        return True

    def __str__(self):
        etat = "Active" if self.est_active else "Inactive"
        return f"Caméra #{self.id_camera} ({etat})"
