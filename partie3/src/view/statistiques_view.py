import os
from datetime import datetime
class StatistiquesView:
    """
    Composant 'Vue' chargé de la représentation visuelle des statistiques du parking.
    
    Cette classe implémente la logique d'affichage demandée par le cahier des charges :
    - Affichage textuel pour une consultation rapide en console.
    - Génération de documents HTML pour une étude de marché approfondie.
    - Aide à l'identification des clients réguliers pour la fidélisation.

    Auteur: ABOULKHASSIM Abdallah
    Date: Décembre 2025
    """
    
    def afficher_rapport_texte(self, donnees):
        """
        Génère une vue textuelle simplifiée des performances du parking dans la console.
        
        Affiche le chiffre d'affaires, la fréquentation par service et une liste 
        des clients réguliers identifiés par le système.

        Args:
            donnees (dict): Dictionnaire contenant les métriques calculées par le contrôleur.
        """
        print("\n" + "="*40)
        print("   RAPPORT D'ACTIVITÉ - DREAMPARK")
        print("="*40)
        print(f"Chiffre d'affaires total : {donnees['ca_total']:.2f}€")
        print("\nRépartition par service :")
        for service, nb in donnees['frequentation'].items():
            print(f" - {service}: {nb} passage(s)")
        
        print("\nClients réguliers à fidéliser :")
        if not donnees['clients_reguliers']:
            print(" Aucun pour le moment.")
        for immat, nb in donnees['clients_reguliers'].items():
            print(f" - Voiture {immat}: {nb} visites")
        print("="*40 + "\n")

    def exporter_html(self, donnees, nom_fichier="rapport_stats.html"):
        """
        Produit un rapport au format HTML professionnel pour l'administrateur.
        
        Génère un document structuré incluant un résumé financier et un tableau 
        récapitulatif de l'historique des passages (immatriculation, place occupée, durée).

        Args:
            donnees (dict): Données formatées à insérer dans le modèle HTML.
            nom_fichier (str): Chemin de destination du fichier généré.
        """
        html_content = f"""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <title>Statistiques DreamPark</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background-color: #f4f7f6; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 25px; }}
                h2 {{ color: #2980b9; margin-top: 0; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 15px; background-color: white; }}
                th, td {{ border: 1px solid #dee2e6; padding: 12px; text-align: left; }}
                th {{ background-color: #3498db; color: white; text-transform: uppercase; font-size: 0.9em; }}
                tr:nth-child(even) {{ background-color: #f8f9fa; }}
                tr:hover {{ background-color: #e9ecef; }}
                .stat-value {{ font-size: 1.2em; color: #27ae60; font-weight: bold; }}
            </style>
        </head>
        <body>
            <h1>Rapport d'Activité - Parking DreamPark</h1>
            
            <div class="card">
                <h2>Résumé Global</h2>
                <p><strong>Chiffre d'Affaires Total :</strong> <span class="stat-value">{donnees['ca_total']:.2f} €</span></p>
                <p><em>Données générées le : {datetime.now().strftime('%d/%m/%Y à %H:%M')}</em></p>
            </div>

            <div class="card">
                <h2>Historique détaillé des Passages </h2>
                <table>
                    <thead>
                        <tr>
                            <th>Véhicule (Immat)</th>
                            <th>Place assignée</th>
                            <th>Durée de stationnement</th>
                            <th>Statut final</th>
                        </tr>
                    </thead>
                    <tbody>
        """
        
        # Injection dynamique des traces de passage
        for p in donnees['liste_passages']:
            html_content += f"""
                        <tr>
                            <td><strong>{p['voiture']}</strong></td>
                            <td>Place n°{p['place']}</td>
                            <td>{p['duree_minutes']} min</td>
                            <td>{p['statut']}</td>
                        </tr>
            """

        html_content += """
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """
        
        try:
            with open(nom_fichier, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Rapport HTML généré avec succès : {os.path.abspath(nom_fichier)}")
        except Exception as e:
            print(f" Erreur lors de la génération du document HTML : {e}")