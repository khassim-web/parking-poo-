import unittest
from model.place import Place
from model.voiture import Voiture
from model.client import Client

class TestPlace(unittest.TestCase):
    
    def test_liberer_place_occupee(self):
        """Test : Libérer une place occupée"""
        # Créer une place et une voiture
        place = Place(1, 101, 0, 5.0, 2.5)
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        
        # Occuper la place
        place.occuper(voiture)
        
        # Libérer
        voiture_liberee = place.liberer()
        
        # Vérifications
        self.assertEqual(voiture_liberee, voiture)
        self.assertTrue(place.est_libre)
        self.assertIsNone(place.voiture_occupante)
    
    def test_liberer_place_deja_libre(self):
        """Test : Refuser de libérer une place déjà libre"""
        place = Place(1, 101, 0, 5.0, 2.5)
        
        # Essayer de libérer une place déjà libre
        with self.assertRaises(ValueError) as context:
            place.liberer()
        
        self.assertIn("déjà libre", str(context.exception))

if __name__ == '__main__':
    unittest.main()