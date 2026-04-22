import unittest
import sys
import os
from datetime import datetime

# Configuration du chemin pour importer le modèle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model.statistiques import Statistiques
from model.placement import Placement
from model.voiture import Voiture
from model.client import Client

class TestStatistiques(unittest.TestCase):
    def setUp(self):
        """Initialisation des objets pour les tests."""
        self.stats = Statistiques()
        self.client = Client(1, "Test", "User", "0102030405", "test@univ.fr")
        self.voiture = Voiture("AB-123-CD", 4.0, 1.8, self.client)
        # On simule un accès et une place pour le placement
        self.placement = Placement(self.voiture, None, None) 
        self.placement.terminer_placement(montant=10.0, type_service="Standard")

    def test_ajouter_passage(self):
        """Vérifie que l'ajout d'un passage fonctionne."""
        self.stats.ajouter_passage(self.placement)
        self.assertEqual(len(self.stats.historique_placements), 1)

    def test_calcul_chiffre_affaires(self):
        """Vérifie le calcul du CA total."""
        self.stats.ajouter_passage(self.placement)
        # Ajout d'un deuxième passage
        p2 = Placement(self.voiture, None, None)
        p2.terminer_placement(montant=15.5, type_service="Maintenance")
        self.stats.ajouter_passage(p2)
        
        self.assertEqual(self.stats.get_chiffre_affaires_total(), 25.5)

    def test_frequentation_services(self):
        """Vérifie la répartition par service."""
        self.stats.ajouter_passage(self.placement)
        repartition = self.stats.get_frequentation_par_service()
        self.assertEqual(repartition["Standard"], 1)

    def test_identification_reguliers(self):
        """Vérifie la détection des clients fréquents."""
        # On ajoute 3 fois la même voiture
        for _ in range(3):
            p = Placement(self.voiture, None, None)
            p.terminer_placement(montant=5.0)
            self.stats.ajouter_passage(p)
        
        reguliers = self.stats.identifier_clients_reguliers(seuil=3)
        self.assertIn("AB-123-CD", reguliers)

if __name__ == '__main__':
    unittest.main()