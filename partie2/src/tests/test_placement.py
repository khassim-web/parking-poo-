import unittest
from time import sleep
from model.placement import Placement
from model.voiture import Voiture
from model.place import Place
from model.acces import Acces
from model.client import Client

class TestPlacement(unittest.TestCase):
    
    def test_get_duree_placement(self):
        """Test : Calculer la durée de placement"""
        # Setup
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        place = Place(1, 101, 0, 5.0, 2.5)
        acces = Acces(1, "Entrée")
        
        # Créer le placement
        placement = Placement(voiture, place, acces)
        
        # Attendre un peu (simulation)
        sleep(0.1)  # 100ms
        
        # Calculer la durée
        duree = placement.get_duree_placement()
        
        # Vérification : durée >= 0
        self.assertGreaterEqual(duree, 0)
    
    def test_terminer_placement_valide(self):
        """Test : Terminer un placement en cours"""
        # Setup
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        place = Place(1, 101, 0, 5.0, 2.5)
        acces = Acces(1, "Entrée")
        
        placement = Placement(voiture, place, acces)
        
        # Terminer le placement
        placement.terminer_placement()
        
        # Vérifications
        self.assertEqual(placement.statut, "TERMINE")
        self.assertIsNotNone(placement.date_fin)
    
    def test_terminer_placement_deja_termine(self):
        """Test : Refuser de terminer un placement déjà terminé"""
        # Setup
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        place = Place(1, 101, 0, 5.0, 2.5)
        acces = Acces(1, "Entrée")
        
        placement = Placement(voiture, place, acces)
        placement.terminer_placement()
        
        # Essayer de terminer à nouveau
        with self.assertRaises(ValueError) as context:
            placement.terminer_placement()
        
        self.assertIn("déjà terminé", str(context.exception))

if __name__ == '__main__':
    unittest.main()