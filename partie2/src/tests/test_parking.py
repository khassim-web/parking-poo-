import unittest
from model.parking import Parking
from model.place import Place
from model.voiture import Voiture
from model.client import Client

class TestParking(unittest.TestCase):
    
    def test_liberer_place_valide(self):
        """Test : Libérer une place occupée"""
        # Setup
        parking = Parking("DreamPark", 100)
        place = Place(1, 101, 0, 5.0, 2.5)
        parking.ajouter_place(place)
        
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        
        # Affecter la place
        parking.affecter_place(voiture, place)
        nb_dispo_avant = parking.nb_places_disponibles
        
        # Libérer
        voiture_liberee = parking.liberer_place(place)
        
        # Vérifications
        self.assertEqual(voiture_liberee, voiture)
        self.assertEqual(parking.nb_places_disponibles, nb_dispo_avant + 1)
        self.assertTrue(place.est_libre)
    
    def test_liberer_place_deja_libre(self):
        """Test : Refuser de libérer une place déjà libre"""
        parking = Parking("DreamPark", 100)
        place = Place(1, 101, 0, 5.0, 2.5)
        parking.ajouter_place(place)
        
        # Essayer de libérer une place déjà libre
        with self.assertRaises(ValueError) as context:
            parking.liberer_place(place)
        
        self.assertIn("déjà libre", str(context.exception))

if __name__ == '__main__':
    unittest.main()