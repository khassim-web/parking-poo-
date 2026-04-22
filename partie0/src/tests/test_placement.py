"""
Tests unitaires pour la classe Placement.

Auteur: BARRY FAtimatou
Date: Décembre 2025
Version: 1.0
"""

import unittest
from modele.placement import Placement
from modele.voiture import Voiture
from modele.place import Place
from modele.acces import Acces


class TestPlacement(unittest.TestCase):
    """Tests pour Placement (classe d'association)."""
    
    def setUp(self):
        """Initialisation avant chaque test."""
        pass
    
    
    def test_init_valide(self):
        """
        Test : Création valide d'un placement.
        
        Vérifie que le placement est créé avec statut EN_COURS.
        """
        pass
    
    def test_init_place_non_compatible(self):
        """
        Test : Création avec place incompatible.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
   
    def test_verifier_compatibilite_ok(self):
        """
        Test : Compatibilité voiture-place.
        
        Vérifie que retourne True.
        """
        pass
    
    
    def test_get_duree_placement(self):
        """
        Test : Calcul de la durée.
        
        Vérifie que la durée en minutes est correcte.
        """
        pass
    
    def test_terminer_placement_valide(self):
        """
        Test : Terminer un placement en cours.
        
        Vérifie que statut devient TERMINE.
        """
        pass
    
    def test_terminer_placement_deja_termine(self):
        """
        Test : Terminer un placement déjà terminé.
        
        Vérifie qu'une ValueError est levée.
        """
        pass


if __name__ == '__main__':
    unittest.main()