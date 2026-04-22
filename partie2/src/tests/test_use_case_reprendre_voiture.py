import unittest
from datetime import datetime, timedelta
from model.parking import Parking
from model.place import Place
from model.voiture import Voiture
from model.client import Client
from model.acces import Acces
from model.camera import Camera
from model.borne_ticket import Borne_Ticket
from model.teleporteur import Teleporteur
from model.panneau_affichage import Panneau_Affichage
from model.placement import Placement

class TestUseCaseReprendreVoiture(unittest.TestCase):
    
    def setUp(self):
        """
        Prépare un parking avec une voiture déjà garée.
        Simule l'état après la Partie 1 (use case "Se garer").
        """
        # Créer le parking
        self.parking = Parking("DreamPark", 100)
        
        # Créer l'accès (sortie)
        self.acces = Acces(1, "Sortie")
        self.parking.ajouter_acces(self.acces)
        
        # Installer les équipements
        self.acces.installer_camera(Camera(1))
        self.acces.installer_borne(Borne_Ticket(1))
        self.acces.ajouter_teleporteur(Teleporteur(1))
        self.acces.ajouter_teleporteur(Teleporteur(2))
        self.acces.installer_panneau(Panneau_Affichage(1))
        
        # Créer une place
        self.place = Place(1, 101, 0, 5.0, 2.5)
        self.parking.ajouter_place(self.place)
        
        # Créer client et voiture
        self.client = Client(1, "Barry", "Fatimatou", "0612345678", "f.barry@univ-tlse2.fr")
        self.voiture = Voiture("AB-123-CD", 4.5, 1.8, self.client)
        
        # === SIMULER QUE LA VOITURE EST DÉJÀ GARÉE (Partie 1) ===
        self.parking.affecter_place(self.voiture, self.place)
        
        # Générer un ticket (avec date d'entrée il y a 2h pour tester la tarification)
        self.ticket = self.acces.borne.generer_ticket(self.voiture, self.client, False)
        # Modifier la date d'entrée pour simuler 2h de stationnement
        self.ticket['date_entree'] = datetime.now() - timedelta(hours=2)
        
        # Décrémenter le panneau (simuler l'entrée)
        self.acces.panneau.afficher(1)
        self.acces.panneau.decrementer()
        
        # Créer le placement
        self.placement = Placement(self.voiture, self.place, self.acces)
    
    def test_use_case_reprendre_voiture_complet(self):
        """
        TEST PRINCIPAL : Scénario complet de récupération de voiture
        """
        print("\n" + "="*60)
        print("USE CASE : Reprendre la voiture")
        print("="*60)
        
        # === ÉTAPE 1 : Client arrive à l'accès ===
        print("\n1. Client arrive à l'accès...")
        self.assertTrue(self.acces.est_actif)
        print("   ✅ Accès actif")
        
        # === ÉTAPE 2 : Client insère son ticket ===
        print("\n2. Client insère son ticket...")
        ticket_lu = self.acces.borne.lire_ticket(self.ticket['numero'])
        self.assertIsNotNone(ticket_lu)
        self.assertEqual(ticket_lu['numero'], self.ticket['numero'])
        print(f"   ✅ Ticket trouvé : {ticket_lu['numero']}")
        
        # === ÉTAPE 3 : Calcul du montant ===
        print("\n3. Calcul du montant à payer...")
        montant = self.acces.borne.calculer_montant_du(ticket_lu)
        self.assertGreaterEqual(montant, 0)
        # Pour 2h de stationnement : (2h - 0.5h) * 2€/h = 3€
        self.assertAlmostEqual(montant, 3.0, places=1)
        print(f"   💰 Montant dû : {montant}€")
        
        # === ÉTAPE 4 : Paiement ===
        print("\n4. Client paie par CB...")
        paiement_ok = self.acces.borne.traiter_paiement(montant, "CB")
        self.assertTrue(paiement_ok)
        print("   ✅ Paiement accepté")
        
        # === ÉTAPE 5 : Téléportation vers l'accès ===
        print("\n5. Téléportation de la voiture vers l'accès...")
        self.assertTrue(self.voiture.est_dans_parking())
        teleportation_ok = self.acces.teleporter_vers_acces(self.voiture)
        self.assertTrue(teleportation_ok)
        print("   ✅ Voiture ramenée à l'accès")
        
        # === ÉTAPE 6 : Libération de la place ===
        print("\n6. Libération de la place...")
        nb_dispo_avant = self.parking.nb_places_disponibles
        voiture_liberee = self.parking.liberer_place(self.place)
        self.assertEqual(voiture_liberee, self.voiture)
        self.assertEqual(self.parking.nb_places_disponibles, nb_dispo_avant + 1)
        print("   ✅ Place libérée")
        
        # Retirer la voiture du parking
        place_liberee = self.voiture.retirer()
        self.assertEqual(place_liberee, self.place)
        print("   ✅ Voiture retirée du système")
        
        # Terminer le placement
        self.placement.terminer_placement()
        self.assertEqual(self.placement.statut, "TERMINE")
        duree = self.placement.get_duree_placement()
        print(f"   📊 Durée totale : {duree} minutes")
        
        # === ÉTAPE 7 : Mise à jour du panneau ===
        print("\n7. Mise à jour du panneau d'affichage...")
        nouveau_nb = self.acces.panneau.incrementer()
        self.assertEqual(nouveau_nb, 1)
        print(f"   ✅ Places disponibles : {nouveau_nb}")
        
        # === VÉRIFICATIONS FINALES ===
        print("\n" + "="*60)
        print("VÉRIFICATIONS FINALES")
        print("="*60)
        
        self.assertFalse(self.voiture.est_dans_parking())
        print("✅ La voiture n'est plus dans le parking")
        
        self.assertTrue(self.place.est_libre)
        print("✅ La place est libre")
        
        self.assertIsNone(self.place.voiture_occupante)
        print("✅ La place n'a plus de voiture occupante")
        
        self.assertEqual(self.parking.nb_places_disponibles, 1)
        print("✅ Le parking a mis à jour ses places disponibles")
        
        self.assertEqual(self.placement.statut, "TERMINE")
        print("✅ Le placement est terminé")
        
        print("\n" + "="*60)
        print("✅ USE CASE 'REPRENDRE LA VOITURE' : SUCCÈS !")
        print("="*60 + "\n")

if __name__ == '__main__':
    unittest.main(verbosity=2)