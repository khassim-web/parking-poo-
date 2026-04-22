import unittest
from model.panneau_affichage import Panneau_Affichage

class TestPanneauAffichage(unittest.TestCase):
    
    def test_incrementer_valide(self):
        """Test : Incrémenter le panneau"""
        panneau = Panneau_Affichage(1)
        panneau.afficher(5)
        
        # Incrémenter
        nouveau_nb = panneau.incrementer()
        
        # Vérifications
        self.assertEqual(nouveau_nb, 6)
        self.assertEqual(panneau.nb_places_affiche, 6)
    
    def test_incrementer_depuis_zero(self):
        """Test : Incrémenter depuis 0"""
        panneau = Panneau_Affichage(1)
        panneau.afficher(0)
        
        # Incrémenter
        nouveau_nb = panneau.incrementer()
        
        # Vérifications
        self.assertEqual(nouveau_nb, 1)

if __name__ == '__main__':
    unittest.main()