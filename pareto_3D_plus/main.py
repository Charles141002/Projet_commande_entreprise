from clustering import Clustering
from radar import Radar


# Utilisation
bruit = 0.1
dimension = 4
valeur_inf = 1
valeur_sup = 10
nb_points = 100
n_clusters = 5

clustering_result = Clustering(bruit, dimension, valeur_inf, valeur_sup, nb_points, n_clusters).clusteriser()
closest_points, labels = clustering_result

Radar.vue_radar(closest_points)