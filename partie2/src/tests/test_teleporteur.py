import unittest
from model.teleporteur import Teleporteur
from model.voiture import Voiture
from model.place import Place
from model.client import Client

class TestTeleporteur(unittest.TestCase):
    
    def test_teleporter_vers_acces_valide(self):
        """Test : Téléporter une voiture vers l'accès"""
        # Setup
        teleporteur = Teleporteur(1)
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        place = Place(1, 101, 0, 5.0, 2.5)
        
        # Garer la voiture (simuler qu'elle est dans le parking)
        voiture.garer(place)
        
        # Téléporter vers l'accès
        resultat = teleporteur.teleporter_vers_acces(voiture)
        
        # Vérifications
        self.assertTrue(resultat)
        self.assertTrue(teleporteur.est_disponible)
        self.assertIsNone(teleporteur.voiture_en_cours)
    
    def test_teleporter_vers_acces_voiture_non_garee(self):
        """Test : Refuser de téléporter une voiture non garée"""
        teleporteur = Teleporteur(1)
        client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
        
        # Essayer de téléporter sans être garée
        with self.assertRaises(ValueError) as context:
            teleporteur.teleporter_vers_acces(voiture)
        
        self.assertIn("pas dans le parking", str(context.exception))

if __name__ == '__main__':
    unittest.main()