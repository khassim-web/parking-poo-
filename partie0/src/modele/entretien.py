"""
Module de gestion de l'entretien des véhicules.

Ce module définit la classe Entretien qui représente un service
d'entretien courant pour les véhicules dans le parking DreamPark.

Auteur: ABOULKHASSIM Abdallah
Date: Décembre 2025
Version: 1.0
"""

from datetime import datetime
from .service import Service

class Entretien:
    """
    Représente un service d'entretien de véhicule.
    
    L'entretien permet aux abonnés de faire effectuer des opérations
    d'entretien courant sur leur véhicule (lavage, nettoyage intérieur,
    contrôles basiques, etc.). Le système prend en charge le véhicule
    et le restitue après intervention.
    
    Attributes:
        id_entretien (int): Identifiant unique
        voiture (Voiture): Voiture concernée
        client (Client): Client demandeur
        type_entretien (str): Type d'entretien ('LAVAGE', 'NETTOYAGE_INTERIEUR', 'LAVAGE_COMPLET', 'CONTROLE_BASIQUE')
        description (str): Description détaillée de l'entretien
        date_demande (datetime): Date de la demande
        date_debut (datetime): Date de début effective
        date_fin (datetime): Date de fin effective
        duree_estimee (int): Durée estimée en minutes
        duree_reelle (int): Durée réelle en minutes
        cout (float): Coût du service en euros
        statut (str): Statut ('EN_ATTENTE', 'EN_COURS', 'TERMINEE', 'ANNULEE')
        prestataire (str): Nom du prestataire
        observations (str): Observations après entretien
    """
    
    def __init__(self, id_entretien, voiture, client, type_entretien, description=""):
        """
        Initialise une nouvelle demande d'entretien.
        
        Args:
            id_entretien (int): Identifiant unique
            voiture (Voiture): Voiture à entretenir
            client (Client): Client demandeur
            type_entretien (str): Type d'entretien
            description (str, optional): Description complémentaire
            
        Raises:
            ValueError: Si l'id_entretien est négatif
            TypeError: Si les arguments ne sont pas du bon type
            ValueError: Si le type_entretien n'est pas reconnu
            ValueError: Si le client n'est pas abonné
            
        Example:
            >>> voiture = Voiture("AB-123-CD", 4.5, 1.8)
            >>> client = Client(1, "Dupont", "Jean", "0612345678", "jean@email.com")
            >>> entretien = Entretien(
            ...     1, voiture, client, "LAVAGE_COMPLET",
            ...     "Lavage extérieur + intérieur complet"
            ... )
        """
        pass
    
    def verifier_eligibilite_client(self):
        """
        Vérifie si le client est éligible au service d'entretien.
        
        Seuls les clients abonnés peuvent bénéficier de ce service.
        
        Returns:
            bool: True si le client est abonné
            
        Raises:
            ValueError: Si le client n'est pas abonné
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> entretien.verifier_eligibilite_client()
            True
        """
        pass
    
    def calculer_cout_et_duree(self):
        """
        Calcule le coût et la durée de l'entretien.
        
        Le calcul dépend du type d'entretien demandé.
        
        Returns:
            dict: Coût et durée
                - cout: float (en euros)
                - duree_estimee: int (en minutes)
                
        Note:
            Pour certains abonnements, l'entretien peut être inclus (coût = 0).
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> estimation = entretien.calculer_cout_et_duree()
            >>> print(estimation['cout'])
        """
        pass
    
    def assigner_prestataire(self, nom_prestataire):
        """
        Assigne un prestataire à l'entretien.
        
        Args:
            nom_prestataire (str): Nom du prestataire
            
        Returns:
            bool: True si l'assignation a réussi
            
        Raises:
            ValueError: Si le nom du prestataire est vide
            ValueError: Si un prestataire est déjà assigné
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> entretien.assigner_prestataire("Station Lavage Express")
            True
        """
        pass
    
    def prendre_en_charge_vehicule(self):
        """
        Prend en charge le véhicule pour l'entretien.
        
        Le système récupère le véhicule de sa place et le prépare
        pour le transfert au prestataire.
        
        Returns:
            bool: True si la prise en charge a réussi
            
        Raises:
            ValueError: Si aucun prestataire n'est assigné
            ValueError: Si la voiture n'est pas dans le parking
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> entretien.assigner_prestataire("Station Lavage Express")
            >>> entretien.prendre_en_charge_vehicule()
            True
        """
        pass
    
    def demarrer_entretien(self):
        """
        Démarre l'entretien du véhicule.
        
        Enregistre la date de début et met à jour le statut.
        
        Returns:
            bool: True si le démarrage a réussi
            
        Raises:
            ValueError: Si le véhicule n'est pas pris en charge
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> entretien.prendre_en_charge_vehicule()
            >>> entretien.demarrer_entretien()
            True
        """
        pass
    
    def terminer_entretien(self, observations=""):
        """
        Termine l'entretien et enregistre les observations.
        
        Args:
            observations (str, optional): Observations du prestataire
            
        Returns:
            bool: True si la clôture a réussi
            
        Raises:
            ValueError: Si l'entretien n'est pas en cours
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> entretien.demarrer_entretien()
            >>> entretien.terminer_entretien("Véhicule lavé et nettoyé - RAS")
            True
        """
        pass
    
    def restituer_vehicule(self):
        """
        Restitue le véhicule au parking après entretien.
        
        Le système récupère le véhicule du prestataire et le replace
        automatiquement dans le parking.
        
        Returns:
            bool: True si la restitution a réussi
            
        Raises:
            ValueError: Si l'entretien n'est pas terminé
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> entretien.terminer_entretien()
            >>> entretien.restituer_vehicule()
            True
        """
        pass
    
    def annuler_entretien(self, raison):
        """
        Annule la demande d'entretien.
        
        Args:
            raison (str): Raison de l'annulation
            
        Returns:
            bool: True si l'annulation a réussi
            
        Raises:
            ValueError: Si l'entretien est déjà en cours ou terminé
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> entretien.annuler_entretien("Client ne souhaite plus le service")
            True
        """
        pass
    
    def modifier_type_entretien(self, nouveau_type):
        """
        Modifie le type d'entretien demandé.
        
        Permet la flexibilité mentionnée dans le cahier des charges
        (changement d'options sur simple coup de fil).
        
        Args:
            nouveau_type (str): Nouveau type d'entretien
            
        Returns:
            bool: True si la modification a réussi
            
        Raises:
            ValueError: Si l'entretien est déjà en cours ou terminé
            ValueError: Si le nouveau type n'est pas reconnu
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE")
            >>> entretien.modifier_type_entretien("LAVAGE_COMPLET")
            True
        """
        pass
    
    def get_infos_entretien(self):
        """
        Récupère toutes les informations de l'entretien.
        
        Returns:
            dict: Informations complètes
                - id_entretien: int
                - type_entretien: str
                - immatriculation: str
                - client: str
                - statut: str
                - cout: float
                - observations: str
                
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> infos = entretien.get_infos_entretien()
        """
        pass
    
    def calculer_duree_totale(self):
        """
        Calcule la durée totale de l'entretien.
        
        Returns:
            int: Durée en minutes
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> duree = entretien.calculer_duree_totale()
        """
        pass
    
    def __str__(self):
        """
        Retourne une représentation textuelle de l'entretien.
        
        Returns:
            str: Description de l'entretien
            
        Example:
            >>> entretien = Entretien(1, voiture, client, "LAVAGE_COMPLET")
            >>> print(entretien)
            Entretien #1 - LAVAGE_COMPLET (AB-123-CD) - EN_ATTENTE
        """
        pass