from frontPareto import FrontPareto
import numpy as np
from sklearn.cluster import KMeans


class ClusteringRandom :

    def __init__(self, bruit, dimension, valeur_inf, valeur_sup, nb_points, n_clusters):
        self.liste_points_pareto = FrontPareto(bruit, dimension, valeur_inf, valeur_sup, nb_points).findParetoPoints_random()
        self.n_clusters = n_clusters

    def clusteriser(self):
        # Créer un modèle K-Means
        kmeans = KMeans(n_clusters=self.n_clusters, n_init=10)
        kmeans.fit(self.liste_points_pareto)
        # Obtenir les étiquettes de cluster attribuées à chaque point de données
        labels = kmeans.labels_
        # Initialiser une liste vide pour stocker les points les plus proches de chaque cluster
        closest_points = []
        # Itérer sur chaque cluster
        for cluster_label in range(self.n_clusters):
            # Sélectionner les points appartenant à ce cluster
            cluster_points = self.liste_points_pareto[labels == cluster_label]
            # Calculer la distance de chaque point par rapport au centre du cluster
            distances = np.linalg.norm(cluster_points - kmeans.cluster_centers_[cluster_label], axis=1)
            # Trouver l'indice du point le plus proche
            closest_point_index = np.argmin(distances)
            # Ajouter le point le plus proche à la liste
            closest_points.append(cluster_points[closest_point_index])
        # Convertir la liste en un tableau NumPy
        closest_points = np.array(closest_points)
        return closest_points, labels
        

if __name__ == "__main__":
    # Paramètres
    bruit = 0.1
    dimension = 5
    valeur_inf = 1
    valeur_sup = 10
    nb_points = 100
    n_clusters = 3

    clustering_result = ClusteringRandom(bruit, dimension, valeur_inf, valeur_sup, nb_points, n_clusters).clusteriser()
    closest_points, labels = clustering_result

    print(closest_points)
    print(len(closest_points))