"""
Tests unitaires pour la classe Client.

Auteur: BARRY FAtimatou
Date: Décembre 2025
Version: 1.0
"""

import unittest
from modele.client import Client
from modele.voiture import Voiture


class TestClient(unittest.TestCase):
    """Tests pour Client."""
    
    def setUp(self):
        """Initialisation avant chaque test."""
        pass
    
    def test_init_valide(self):
        """
        Test : Création valide d'un client.
        
        Vérifie que le client est créé avec les bons attributs.
        """
        pass
    
    def test_init_nom_vide(self):
        """
        Test : Création avec nom vide.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_init_email_invalide(self):
        """
        Test : Création avec email invalide.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_ajouter_voiture_valide(self):
        """
        Test : Ajout d'une voiture valide.
        
        Vérifie que la voiture est ajoutée à la liste.
        """
        pass
    
    def test_ajouter_voiture_doublon(self):
        """
        Test : Ajout d'une voiture déjà existante.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_ajouter_voiture_type_invalide(self):
        """
        Test : Ajout d'un objet non-Voiture.
        
        Vérifie qu'une TypeError est levée.
        """
        pass
   
    def test_est_client_regulier_true(self):
        """
        Test : Client avec assez de passages.
        
        Vérifie que retourne True si passages >= seuil.
        """
        pass
    
    def test_est_client_regulier_false(self):
        """
        Test : Client avec peu de passages.
        
        Vérifie que retourne False.
        """
        pass


if __name__ == '__main__':
    unittest.main()