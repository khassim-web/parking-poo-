"""
Module de gestion du parking DreamPark.

Ce module définit la classe Parking qui est le gestionnaire central
du système de gestion de parking.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""
from datetime import datetime

class Parking:
    """
    Gestionnaire central du système de parking DreamPark.
    
    Le parking gère l'ensemble des places, des accès, et coordonne
    toutes les opérations (entrée, sortie, réservations, statistiques).
    
    Attributes:
        nom (str): Nom du parking
        places (list[Place]): Liste de toutes les places du parking
        acces (list[Acces]): Liste des accès (exactement 2)
        nb_places_totales (int): Nombre total de places
        nb_places_disponibles (int): Nombre de places actuellement libres
        historique_passages (list[dict]): Historique de tous les passages
        services_actifs (list[Service]): Liste des services en cours d'exécution
    """
    
    def __init__(self, nom, nb_places):
        """Initialise un parking."""
        if nb_places < 0:
            raise ValueError("Le nombre de places ne peut pas être négatif")
        
        self.nom = nom
        self.nb_places_totales = nb_places
        self.nb_places_disponibles = 0  # Au début, aucune place ajoutée
        self.places = []
        self.acces = [] 
        self.historique_passages = []
        self.services_actifs = []    
    
    def ajouter_place(self, place):
        """Ajoute une place au parking."""
        if any(p.id_place == place.id_place for p in self.places):
            raise ValueError("Une place avec cet ID existe déjà")
        
        self.places.append(place)
        self.nb_places_totales += 1
        self.nb_places_disponibles += 1
        return True
    
    def ajouter_acces(self, acces):
        """Ajoute un accès au parking."""
        if len(self.acces) >= 2:
            raise ValueError("Le parking ne peut avoir que 2 accès maximum")
        
        self.acces.append(acces)
        return True
    
    def chercher_place_disponible(self, voiture):
        """Cherche une place disponible compatible."""
        for place in self.places:
            if place.est_libre and place.est_compatible(voiture):
                return place
        return None
    
    def affecter_place(self, voiture, place):
        """Affecte une place à une voiture."""
        if not place.est_libre:
            raise ValueError("La place n'est pas libre")
        
        if place not in self.places:
            raise ValueError("Cette place n'appartient pas au parking")
        
        # Occuper la place
        place.occuper(voiture)
        voiture.garer(place)
        
        # Mettre à jour les compteurs
        self.nb_places_disponibles -= 1
        
        # Historique
        self.historique_passages.append({
            'action': 'ENTREE',
            'voiture': voiture.immatriculation,
            'place': place.numero,
            'date': datetime.now()
        })
        
        return True
    
    def liberer_place(self, place):
        """Libère une place occupée."""
        if place not in self.places:
            raise ValueError("Cette place n'appartient pas au parking")
        
        if place.est_libre:
            raise ValueError("La place est déjà libre")
        
        # Libérer la place
        voiture = place.liberer()
        
        # Mettre à jour les compteurs
        self.nb_places_disponibles += 1
        
        # Historique
        self.historique_passages.append({
            'action': 'SORTIE',
            'voiture': voiture.immatriculation,
            'place': place.numero,
            'date': datetime.now()
        })
        
        return voiture
    
    def est_plein(self):
        """Vérifie si le parking est plein."""
        return self.nb_places_disponibles == 0
    
    def get_taux_occupation(self):
        """Calcule le taux d'occupation."""
        if self.nb_places_totales == 0:
            return 0.0
        
        places_occupees = self.nb_places_totales - self.nb_places_disponibles
        return (places_occupees / self.nb_places_totales) * 100
    
    
    def enregistrer_passage(self, voiture, type_passage, acces, place=None):
        """Enregistre un passage (entrée ou sortie) dans l'historique."""
        if type_passage not in ('ENTREE', 'SORTIE'):
            raise ValueError("type_passage doit être 'ENTREE' ou 'SORTIE'")

        enregistrement = {
            'action': type_passage,
            'voiture': voiture.immatriculation,
            'acces': acces.nom,
            'place': place.numero if place else None,
            'date': datetime.now()
        }
        self.historique_passages.append(enregistrement)
        return enregistrement

    def get_statistiques(self, date_debut=None, date_fin=None):
        """Génère des statistiques sur l'activité du parking."""
        passages = self.historique_passages
        if date_debut:
            passages = [p for p in passages if p['date'] >= date_debut]
        if date_fin:
            passages = [p for p in passages if p['date'] <= date_fin]

        nb_entrees = sum(1 for p in passages if p['action'] == 'ENTREE')
        nb_sorties = sum(1 for p in passages if p['action'] == 'SORTIE')

        return {
            'nb_passages_total': len(passages),
            'nb_entrees': nb_entrees,
            'nb_sorties': nb_sorties,
            'taux_occupation_actuel': self.get_taux_occupation(),
            'nb_places_disponibles': self.nb_places_disponibles,
            'nb_places_totales': self.nb_places_totales
        }

    def ajouter_service(self, service):
        """Ajoute un service en cours au parking."""
        self.services_actifs.append(service)
        return True

    def __str__(self):
        return f"Parking {self.nom} - {self.nb_places_totales} places ({self.nb_places_disponibles} disponibles)"