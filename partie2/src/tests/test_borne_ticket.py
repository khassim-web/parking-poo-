import unittest
from datetime import datetime, timedelta
from model.borne_ticket import Borne_Ticket
from model.voiture import Voiture
from model.client import Client

class TestBorneTicket(unittest.TestCase):
    
    def setUp(self):
        """Prépare les objets pour les tests"""
        self.borne = Borne_Ticket(1)
        self.client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        self.voiture = Voiture("AB-123-CD", 4.5, 1.8, self.client)
    
    def test_lire_ticket_existant(self):
        """Test : Lire un ticket existant"""
        # Générer un ticket
        ticket = self.borne.generer_ticket(self.voiture, self.client, False)
        
        # Lire le ticket
        ticket_lu = self.borne.lire_ticket(ticket['numero'])
        
        # Vérifications
        self.assertIsNotNone(ticket_lu)
        self.assertEqual(ticket_lu['numero'], ticket['numero'])
        self.assertEqual(ticket_lu['immatriculation'], "AB-123-CD")
    
    def test_lire_ticket_inexistant(self):
        """Test : Refuser de lire un ticket inexistant"""
        with self.assertRaises(ValueError) as context:
            self.borne.lire_ticket("T9999")
        
        self.assertIn("introuvable", str(context.exception))
    
    def test_calculer_montant_moins_30min(self):
        """Test : Gratuit pour moins de 30 minutes"""
        # Créer un ticket récent (< 30 min)
        ticket = self.borne.generer_ticket(self.voiture, self.client, False)
        
        # Calculer le montant
        montant = self.borne.calculer_montant_du(ticket)
        
        # Vérification : gratuit
        self.assertEqual(montant, 0.0)
    
    def test_calculer_montant_2_heures(self):
        """Test : Calculer le montant pour 2 heures"""
        # Créer un ticket avec date d'entrée il y a 2h
        ticket = {
            'numero': 'T001',
            'date_entree': datetime.now() - timedelta(hours=2),
            'client_abonne': False
        }
        self.borne.tickets_emis.append(ticket)
        
        # Calculer le montant
        montant = self.borne.calculer_montant_du(ticket)
        
        # Vérification : 2h - 0.5h = 1.5h * 2€/h = 3€
        self.assertAlmostEqual(montant, 3.0, places=1)
    
    def test_calculer_montant_abonne_gratuit(self):
        """Test : Gratuit pour les abonnés"""
        # Créer un ticket abonné avec date d'entrée il y a 2h
        ticket = {
            'numero': 'T001',
            'date_entree': datetime.now() - timedelta(hours=2),
            'client_abonne': True
        }
        self.borne.tickets_emis.append(ticket)
        
        # Calculer le montant
        montant = self.borne.calculer_montant_du(ticket)
        
        # Vérification : gratuit pour abonné
        self.assertEqual(montant, 0.0)
    
    def test_traiter_paiement_cb(self):
        """Test : Paiement par CB"""
        resultat = self.borne.traiter_paiement(10.0, "CB")
        self.assertTrue(resultat)
    
    def test_traiter_paiement_especes(self):
        """Test : Paiement en espèces"""
        resultat = self.borne.traiter_paiement(10.0, "ESPECES")
        self.assertTrue(resultat)
    
    def test_traiter_paiement_mode_invalide(self):
        """Test : Refuser un mode de paiement invalide"""
        with self.assertRaises(ValueError) as context:
            self.borne.traiter_paiement(10.0, "CHEQUE")
        
        self.assertIn("invalide", str(context.exception))

if __name__ == '__main__':
    unittest.main()