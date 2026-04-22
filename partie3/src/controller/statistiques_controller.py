from model.statistiques import Statistiques
from view.statistiques_view import StatistiquesView

class StatistiquesController:
    """
    Composant 'Contrôleur' du module de statistiques (Patron MVC).
    
    Cette classe assure l'interface entre le modèle de données (Statistiques) 
    et les différents formats de sortie (Vue). Elle orchestre la récupération 
    des indicateurs de performance (CA, fréquentation) et pilote les demandes 
    d'édition de rapports pour l'administrateur du parking.

    Attributes:
        modele (Statistiques): Référence au modèle gérant la persistance des passages.
        vue (StatistiquesView): Référence à la vue gérant les exports (Texte, HTML).

    Auteur: ABOULKHASSIM Abdallah
    Date: Décembre 2025
    """
    
    def __init__(self, modele_stats, vue_stats):
        """
        Initialise le contrôleur avec ses composants de données et d'affichage.

        Args:
            modele_stats (Statistiques): Le gestionnaire d'historique du parking.
            vue_stats (StatistiquesView): Le gestionnaire d'affichage des rapports.
        """
        self.modele = modele_stats
        self.vue = vue_stats

    def collecter_donnees(self):
        """
        Récupère et structure les métriques métier pour l'édition.
        
        Cette méthode centralise l'accès aux données du modèle pour construire 
        un dictionnaire de synthèse prêt à être consommé par la vue. Elle inclut 
        le chiffre d'affaires, la fréquentation par service et la liste des 
        clients réguliers à fidéliser.

        Returns:
            dict: Un dictionnaire contenant l'ensemble des indicateurs calculés.
        """
        donnees = {
            "ca_total": self.modele.get_chiffre_affaires_total(),
            "frequentation": self.modele.get_frequentation_par_service(),
            "clients_reguliers": self.modele.identifier_clients_reguliers(seuil=2),
            "liste_passages": [p.get_infos_placement() for p in self.modele.historique_placements]
        }
        return donnees

    def generer_rapport_texte(self):
        """
        Pilote la génération du rapport d'activité au format console (Texte).
        
        Demande à la vue d'afficher les informations essentielles pour une 
        lecture rapide par l'administrateur.
        """
        donnees = self.collecter_donnees()
        self.vue.afficher_rapport_texte(donnees)

    def generer_rapport_html(self, nom_fichier="rapport_stats.html"):
        """
        Pilote la création du document d'étude de marché au format HTML.
        
        Permet d'exporter l'activité complète du parking dans un fichier 
        externe structuré et stylisé.

        Args:
            nom_fichier (str): Le nom ou chemin du fichier HTML à générer.
        """
        donnees = self.collecter_donnees()
        self.vue.exporter_html(donnees, nom_fichier)