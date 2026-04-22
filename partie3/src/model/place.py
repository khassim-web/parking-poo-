"""
Module de gestion des places de parking.

Ce module définit la classe Place qui représente une place de stationnement
dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""


class Place:
    """
    Représente une place de parking dans le système DreamPark.
    
    Une place possède un identifiant unique, des dimensions (longueur, hauteur),
    un niveau et un état (libre ou occupée).
    
    Attributes:
        id_place (int): Identifiant unique de la place dans le système
        numero (int): Numéro affiché de la place
        niveau (int): Niveau/étage où se trouve la place (0 pour rez-de-chaussée)
        longueur (float): Longueur de la place en mètres
        hauteur (float): Hauteur maximale autorisée en mètres
        est_libre (bool): État de disponibilité de la place
        voiture_occupante (Optional[Voiture]): Référence vers la voiture garée
    """
    
    def __init__(self, id_place, numero, niveau, longueur, hauteur):
        """Initialise une place."""
        if longueur <= 0 or hauteur <= 0:
            raise ValueError("Les dimensions doivent être positives")
        
        self.id_place = id_place
        self.numero = numero
        self.niveau = niveau
        self.longueur = longueur
        self.hauteur = hauteur
        self.est_libre = True
        self.voiture_occupante = None
    
    def est_compatible(self, voiture):
        """Vérifie si une voiture est compatible avec la place."""
        return (voiture.longueur <= self.longueur and 
                voiture.hauteur <= self.hauteur)
    
    def occuper(self, voiture):
        """Occupe la place avec une voiture."""
        if not self.est_libre:
            raise ValueError("La place est déjà occupée")
        
        if not self.est_compatible(voiture):
            raise ValueError("La voiture n'est pas compatible avec cette place")
        
        self.est_libre = False
        self.voiture_occupante = voiture
    
    def liberer(self):
        """Libère la place."""
        if self.est_libre:
            raise ValueError("La place est déjà libre")
        
        voiture = self.voiture_occupante
        self.voiture_occupante = None
        self.est_libre = True
        return voiture
    
    def __str__(self):
        etat = "Libre" if self.est_libre else "Occupée"
        return f"Place {self.numero} (Niveau {self.niveau}) - {self.longueur}m x {self.hauteur}m - {etat}"