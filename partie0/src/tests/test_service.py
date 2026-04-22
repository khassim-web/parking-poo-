"""
Tests unitaires pour la classe Service (abstraite).

Auteur: BARRY FAtimatou
Date: Décembre 2025
Version: 1.0
"""

import unittest
from modele.service import Service
from modele.voiture import Voiture
from modele.client import Client


class ServiceConcret(Service):
    """Classe concrète pour tester Service."""
    
    def calculer_cout(self):
        """Implémentation test."""
        return 10.0
    
    def executer(self):
        """Implémentation test."""
        return True


class TestService(unittest.TestCase):
    """Tests pour Service (classe abstraite)."""
    
    def setUp(self):
        """Initialisation avant chaque test."""
        pass
   
    def test_init_valide(self):
        """
        Test : Création d'un service concret.
        
        Vérifie que le service est créé avec statut EN_ATTENTE.
        """
        pass
    
    def test_init_client_non_abonne(self):
        """
        Test : Création avec client non abonné.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_verifier_eligibilite_client_abonne(self):
        """
        Test : Vérification client abonné.
        
        Vérifie que retourne True.
        """
        pass
    
    def test_verifier_eligibilite_client_non_abonne(self):
        """
        Test : Vérification client non abonné.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_demarrer_service(self):
        """
        Test : Démarrage d'un service.
        
        Vérifie que statut devient EN_COURS et date_debut est définie.
        """
        pass
    
    def test_demarrer_service_deja_en_cours(self):
        """
        Test : Démarrage d'un service déjà en cours.
        
        Vérifie qu'une ValueError est levée.
        """
        pass
    
    def test_terminer_service(self):
        """
        Test : Terminaison d'un service.
        
        Vérifie que statut devient TERMINEE et date_fin est définie.
        """
        pass
    
    def test_annuler_service(self):
        """
        Test : Annulation d'un service.
        
        Vérifie que statut devient ANNULEE.
        """
        pass


if __name__ == '__main__':
    unittest.main()