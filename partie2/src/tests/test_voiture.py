import unittest
from model.voiture import Voiture
from model.place import Place
from model.client import Client

class TestVoiture(unittest.TestCase):
    
    def test_retirer_voiture_garee(self):
        """Test : Retirer une voiture garée"""
        # Setup
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        place = Place(1, 101, 0, 5.0, 2.5)
        
        # Garer la voiture
        voiture.garer(place)
        self.assertTrue(voiture.est_dans_parking())
        
        # Retirer la voiture
        place_liberee = voiture.retirer()
        
        # Vérifications
        self.assertEqual(place_liberee, place)
        self.assertFalse(voiture.est_dans_parking())
        self.assertIsNone(voiture.place_actuelle)
    
    def test_retirer_voiture_non_garee(self):
        """Test : Refuser de retirer une voiture non garée"""
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        
        # Essayer de retirer sans être garée
        with self.assertRaises(ValueError) as context:
            voiture.retirer()
        
        self.assertIn("pas dans le parking", str(context.exception))

if __name__ == '__main__':
    unittest.main()