from datetime import datetime, timedelta
from model.parking import Parking
from model.place import Place
from model.voiture import Voiture
from model.client import Client
from model.acces import Acces
from model.placement import Placement
from model.statistiques import Statistiques
from controller.statistiques_controller import StatistiquesController
from view.statistiques_view import StatistiquesView

def main():
    print("=" * 70)
    print("DREAMPARK - DÉMONSTRATION GESTION DES STATISTIQUES (PARTIE 3)")
    print("=" * 70)

    # 1. Initialisation du Système
    modele_stats = Statistiques()
    vue_stats = StatistiquesView()
    controleur = StatistiquesController(modele_stats, vue_stats)
    
    parking = Parking("DreamPark", 100)
    acces = Acces(1, "Entrée Nord")
    place = Place(1, 101, 0, 5.0, 2.5)

    # 2. Simulation de plusieurs passages pour peupler les stats
    # Nous simulons des voitures qui sont déjà sorties
    passages_simules = [
        {"immat": "AA-111-AA", "nom": "Dupont", "tarif": 5.0, "service": "Standard"},
        {"immat": "BB-222-BB", "nom": "Durand", "tarif": 12.0, "service": "Maintenance"},
        {"immat": "AA-111-AA", "nom": "Dupont", "tarif": 8.0, "service": "Standard"}, # Client régulier
        {"immat": "CC-333-CC", "nom": "Martin", "tarif": 25.0, "service": "Livraison"}
    ]

    print(f"\n Simulation de {len(passages_simules)} passages de véhicules...")

    for p in passages_simules:
        client = Client(99, p['nom'], "Test", "0600000000", "test@test.com")
        voiture = Voiture(p['immat'], 4.0, 1.5, client)
        
        # Création et fin du placement
        placement = Placement(voiture, place, acces)
        # Simulation d'une durée (on recule la date de placement)
        placement.date_placement = datetime.now() - timedelta(hours=2)
        
        # On termine le placement avec les données de la Partie 3
        placement.terminer_placement(
            montant=p['tarif'], 
            mode_paiement="CB", 
            type_service=p['service']
        )
        
        # Archivage dans le modèle de statistiques
        modele_stats.ajouter_passage(placement)
        print(f" > Passage enregistré : {p['immat']} ({p['service']}) - {p['tarif']}€")

    # 3. Génération des rapports via le Contrôleur (Patron MVC)
    print("\n" + "=" * 70)
    print(" GÉNÉRATION DES RAPPORTS")
    print("=" * 70)

    # Rapport Console (Texte)
    controleur.generer_rapport_texte()

    # Rapport HTML (Fichier)
    controleur.generer_rapport_html("rapport_final_dreampark.html")

if __name__ == "__main__":
    main()