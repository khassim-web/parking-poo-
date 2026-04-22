"""
Tests unitaires pour la classe Entretien.

Auteur: BARRY FAtimatou
Date: Décembre 2025
Version: 1.0
"""

import unittest
from modele.entretien import Entretien
from modele.voiture import Voiture
from modele.client import Client


class TestEntretien(unittest.TestCase):
    """Tests pour Entretien."""
    
    def setUp(self):
        """Initialisation avant chaque test."""
        pass
    
    def test_init_valide(self):
        """
        Test : Création valide d'un entretien.
        
        Vérifie que l'entretien est créé correctement.
        """
        pass
    
    def test_init_type_invalide(self):
        """
        Test : Création avec type invalide.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
   
    def test_calculer_cout_lavage(self):
        """
        Test : Calcul du coût pour un lavage.
        
        Vérifie que le coût est correct selon le type.
        """
        pass
    
    def test_assigner_prestataire_valide(self):
        """
        Test : Assignation d'un prestataire.
        
        Vérifie que le prestataire est assigné.
        """
        pass
    
    def test_terminer_entretien_valide(self):
        """
        Test : Terminaison avec observations.
        
        Vérifie que les observations sont enregistrées.
        """
        pass


if __name__ == '__main__':
    unittest.main()