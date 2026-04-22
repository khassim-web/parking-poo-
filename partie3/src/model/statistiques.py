class Statistiques:
    """
    Modèle gérant l'historique des passages du parking DreamPark. 
    
    Cette classe est responsable de la persistance en mémoire des données de 
    fréquentation afin de permettre l'édition de rapports d'activité. 
    Elle permet notamment d'identifier les usages par service et les clients 
    les plus réguliers. 

    Attributes:
        historique_placements (list): Collection d'objets Placement terminés 
            représentant la trace de passage des voitures. 

    Auteur: ABOULKHASSIM Abdallah 
    Date: Décembre 2025
    """

    def __init__(self):
        """
        Initialise un nouveau gestionnaire de statistiques avec un historique vide.
        """
        self.historique_placements = []

    def ajouter_passage(self, placement):
        """
        Ajoute un placement finalisé à l'historique du système. 

        Args:
            placement (Placement): L'objet placement contenant les infos de 
                la voiture, de la place et du paiement. 

        Raises:
            ValueError: Si le placement n'est pas dans l'état 'TERMINE'.
        """
        if placement.statut != "TERMINE":
            raise ValueError("Seuls les placements terminés peuvent être archivés.")
        self.historique_placements.append(placement)

    def get_chiffre_affaires_total(self):
        """
        Calcule la somme totale des revenus générés par le parking. 

        Returns:
            float: Le montant total cumulé de tous les paiements encaissés.
        """
        return sum(p.montant_paye for p in self.historique_placements)

    def get_frequentation_par_service(self):
        """
        Analyse l'activité du parking selon les différents types de services. 
        
        Permet de distinguer l'activité standard des services d'entretien, 
        de maintenance ou de livraison. 

        Returns:
            dict: Un dictionnaire associant le nom du service au nombre de passages.
        """
        stats = {}
        for p in self.historique_placements:
            stats[p.type_service] = stats.get(p.type_service, 0) + 1
        return stats

    def identifier_clients_reguliers(self, seuil=3):
        """
        Identifie les véhicules fréquents pour la politique de fidélisation. 
        
        Cette méthode permet d'extraire les immatriculations des clients 
        dépassant un certain nombre de passages afin de leur proposer 
        des abonnements ou le pack garanti. 

        Args:
            seuil (int): Le nombre minimum de passages pour être considéré régulier.

        Returns:
            dict: Un dictionnaire {immatriculation: nombre_de_passages}.
        """
        frequence = {}
        for p in self.historique_placements:
            immat = p.voiture.immatriculation
            frequence[immat] = frequence.get(immat, 0) + 1
        
        return {immat: nb for immat, nb in frequence.items() if nb >= seuil}