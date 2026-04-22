"""
Module de gestion des caméras.

Ce module définit la classe Camera qui gère la capture d'informations
sur les véhicules dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

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
        """
        Initialise une nouvelle caméra.
        
        Args:
            id_camera (int): Identifiant unique
            
        Raises:
            ValueError: Si l'id_camera est négatif
            
        Note:
            La caméra est créée indépendamment et peut être
            installée sur un Acces (agrégation).
            
        Example:
            >>> camera = Camera(1)
            >>> camera.est_active
            True
        """
        pass
    
    def capturer_image(self, voiture):
        """
        Capture une image du véhicule.
        
        Args:
            voiture (Voiture): La voiture à capturer
            
        Returns:
            dict: Informations capturées
                - timestamp: datetime
                - immatriculation: str
                - longueur: float
                - hauteur: float
                
        Raises:
            TypeError: Si l'argument n'est pas une instance de Voiture
            ValueError: Si la caméra est inactive
            
        Example:
            >>> camera = Camera(1)
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> capture = camera.capturer_image(voiture)
        """
        pass
    
    def extraire_immatriculation(self, image):
        """
        Extrait l'immatriculation depuis une capture.
        
        Args:
            image (dict): Données de l'image capturée
            
        Returns:
            str: Numéro d'immatriculation extrait
            
        Example:
            >>> camera = Camera(1)
            >>> image = {"data": "..."}
            >>> immat = camera.extraire_immatriculation(image)
        """
        pass
    
    def mesurer_dimensions(self, voiture):
        """
        Mesure les dimensions d'un véhicule.
        
        Args:
            voiture (Voiture): La voiture à mesurer
            
        Returns:
            dict: Dimensions mesurées
                - longueur: float
                - hauteur: float
                
        Raises:
            TypeError: Si l'argument n'est pas une instance de Voiture
            
        Example:
            >>> camera = Camera(1)
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> dimensions = camera.mesurer_dimensions(voiture)
        """
        pass
    
    def activer(self):
        """
        Active la caméra.
        
        Returns:
            bool: True si l'activation a réussi
            
        Example:
            >>> camera = Camera(1)
            >>> camera.activer()
            True
        """
        pass
    
    def desactiver(self):
        """
        Désactive la caméra.
        
        Returns:
            bool: True si la désactivation a réussi
            
        Example:
            >>> camera = Camera(1)
            >>> camera.desactiver()
            True
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la caméra.
        
        Returns:
            str: Description de la caméra
            
        Example:
            >>> camera = Camera(1)
            >>> print(camera)
            Caméra #1 (Active)
        """
        pass