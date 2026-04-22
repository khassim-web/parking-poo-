"""
Tests unitaires pour la classe Voiture.

Auteur: BARRY FAtimatou
Date: Décembre 2025
Version: 1.0
"""

import unittest
from modele.voiture import Voiture
from modele.place import Place


class TestVoiture(unittest.TestCase):
    """Tests pour Voiture."""
    
    def setUp(self):
        """Initialisation avant chaque test."""
        pass

    def test_init_valide(self):
        """
        Test : Création valide d'une voiture.
        
        Vérifie que la voiture est créée avec les bons attributs.
        """
        pass
    
    def test_init_immatriculation_vide(self):
        """
        Test : Création avec immatriculation vide.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_init_dimensions_negatives(self):
        """
        Test : Création avec dimensions négatives.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
  
    def test_est_dans_parking_false(self):
        """
        Test : Voiture hors parking.
        
        Vérifie que retourne False si place_actuelle est None.
        """
        pass
    
    def test_est_dans_parking_true(self):
        """
        Test : Voiture dans parking.
        
        Vérifie que retourne True si place_actuelle existe.
        """
        pass
    
    def test_garer_voiture(self):
        """
        Test : Garer une voiture.
        
        Vérifie que place_actuelle est assignée.
        """
        pass
    
    def test_garer_voiture_deja_garee(self):
        """
        Test : Garer une voiture déjà garée.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_retirer_voiture_garee(self):
        """
        Test : Retirer une voiture garée.
        
        Vérifie que la place est retournée et place_actuelle devient None.
        """
        pass
    
    def test_retirer_voiture_non_garee(self):
        """
        Test : Retirer une voiture non garée.
        
        Vérifie qu'une ValueError est levée.
        """
        pass


if __name__ == '__main__':
    unittest.main()