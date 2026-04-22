"""
Script de démonstration du use case : Reprendre la voiture
"""
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


def main():
    print("=" * 70)
    print("DREAMPARK - DÉMONSTRATION USE CASE : REPRENDRE LA VOITURE")
    print("=" * 70)
    print()
    
    # === SETUP : Simulation d'une voiture déjà garée (Partie 1) ===
    print(" SETUP : Préparation du parking...")
    
    # Créer le parking
    parking = Parking("DreamPark", 100)
    print(f" Parking '{parking.nom}' créé")
    
    # Créer l'accès
    acces = Acces(1, "Sortie Principale")
    parking.ajouter_acces(acces)
    print(f" Accès '{acces.nom}' créé")
    
    # Installer les équipements
    acces.installer_camera(Camera(1))
    acces.installer_borne(Borne_Ticket(1))
    acces.ajouter_teleporteur(Teleporteur(1))
    acces.ajouter_teleporteur(Teleporteur(2))
    acces.installer_panneau(Panneau_Affichage(1))
    print(" Équipements installés (caméra, borne, 2 téléporteurs, panneau)")
    
    # Créer une place
    place = Place(1, 101, 0, 5.0, 2.5)
    parking.ajouter_place(place)
    print(f" Place n°{place.numero} ajoutée (5.0m x 2.5m)")
    
    # Créer client et voiture
    client = Client(1, "ABOULKHASSIM", "Abdallah", "0612345678", "A.aboulkhassim@univ-tlse2.fr")
    voiture = Voiture("AB-123-CD", 4.5, 1.8, client)
    print(f" Client : {client.prenom} {client.nom}")
    print(f" Voiture : {voiture.immatriculation} ({voiture.longueur}m x {voiture.hauteur}m)")
    
    # Garer la voiture (simuler Partie 1)
    parking.affecter_place(voiture, place)
    print(f" Voiture garée sur la place n°{place.numero}")
    
    # Générer un ticket (avec date d'entrée il y a 2h)
    ticket = acces.borne.generer_ticket(voiture, client, False)
    ticket['date_entree'] = datetime.now() - timedelta(hours=2)
    print(f"Ticket généré : {ticket['numero']} (entrée il y a 2h)")
    
    # Panneau décrémenter
    acces.panneau.afficher(1)
    acces.panneau.decrementer()
    print(f"Panneau : {acces.panneau.nb_places_affiche} place(s) disponible(s)")
    
    # Créer le placement
    placement = Placement(voiture, place, acces)
    print(f"Placement créé\n")
    
    # === USE CASE : Reprendre la voiture ===
    print("=" * 70)
    print(" USE CASE : REPRENDRE LA VOITURE")
    print("=" * 70)
    print()
    
    
    # ÉTAPE 1 : Client arrive
    print("1️  Le client arrive à l'accès de sortie...")
    print(f"   → Accès : {acces.nom}")
    print(f"   → Statut : {'Actif' if acces.est_actif else 'Inactif'}")
    print()
    
    # ÉTAPE 2 : Client insère son ticket
    print("2️  Le client insère son ticket à la borne...")
    ticket_lu = acces.borne.lire_ticket(ticket['numero'])
    print(f"    Ticket trouvé : {ticket_lu['numero']}")
    print(f"   → Immatriculation : {ticket_lu['immatriculation']}")
    print(f"   → Client : {ticket_lu['client_nom']}")
    print(f"   → Abonné : {'Oui' if ticket_lu['client_abonne'] else 'Non'}")
    print()
    
    # ÉTAPE 3 : Calcul du montant
    print("3️ Calcul du montant à payer...")
    montant = acces.borne.calculer_montant_du(ticket_lu)
    print(f" Montant dû : {montant}€")
    if montant == 0:
        print("   → (30 premières minutes gratuites)")
    else:
        print(f"   → Durée de stationnement : ~2 heures")
        print(f"   → Tarif : 2€/heure après les 30 premières minutes")
    print()
    
    # ÉTAPE 4 : Paiement
    print("4️  Le client paie par carte bancaire...")
    paiement_ok = acces.borne.traiter_paiement(montant, "CB")
    if paiement_ok:
        print(" Paiement accepté")
    print()
    
    # ÉTAPE 5 : Téléportation
    print("5️ Téléportation de la voiture vers l'accès...")
    print(f"   → Voiture actuellement sur la place n°{place.numero}")
    teleportation_ok = acces.teleporter_vers_acces(voiture)
    if teleportation_ok:
        print("    Voiture téléportée à l'accès de sortie")
    print()
    
    # ÉTAPE 6 : Libération
    print("6️  Libération de la place...")
    nb_places_avant = parking.nb_places_disponibles
    voiture_liberee = parking.liberer_place(place)
    print(f"   Place n°{place.numero} libérée")
    print(f"   → Places disponibles : {nb_places_avant} → {parking.nb_places_disponibles}")
    
    # Retirer la voiture du système
    place_liberee = voiture.retirer()
    print(f"    Voiture {voiture.immatriculation} retirée du système")
    
    # Terminer le placement
    placement.terminer_placement()
    duree = placement.get_duree_placement()
    print(f"    Placement terminé (durée totale : {duree} minutes)")
    print()
    
    # ÉTAPE 7 : Mise à jour du panneau
    print("7️  Mise à jour du panneau d'affichage...")
    nouveau_nb = acces.panneau.incrementer()
    print(f"    Panneau mis à jour : {nouveau_nb} place(s) disponible(s)")
    print()
    
    # === VÉRIFICATIONS FINALES ===
    print("=" * 70)
    print("VÉRIFICATIONS FINALES")
    print("=" * 70)
    print()
    
    print(f" La voiture n'est plus dans le parking : {not voiture.est_dans_parking()}")
    print(f" La place est libre : {place.est_libre}")
    print(f" La place n'a plus de voiture occupante : {place.voiture_occupante is None}")
    print(f" Places disponibles : {parking.nb_places_disponibles}/{parking.nb_places_totales}")
    print(f" Statut du placement : {placement.statut}")
    print()
    
    print("=" * 70)
    print(" USE CASE 'REPRENDRE LA VOITURE' : SUCCÈS !")
    print("=" * 70)


if __name__ == "__main__":
    main()
