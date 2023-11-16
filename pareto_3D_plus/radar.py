import random
import numpy as np
import matplotlib.pyplot as plt
from clustering import Clustering

class Radar:

    def to_liste2(pareto):
        pareto = list(pareto)
        for i in range(len(pareto)):
            pareto[i] = list(pareto[i])
        return pareto

    def vue_radar(pareto):
        pareto = Radar.to_liste2(pareto)
        # data
        categories = [f"Critère {i}" for i in range(1, len(pareto[0]) + 1)]
        categories.append("Critère 1")
        # to close the radar shape add the first list element to the end of the list or concatenate
        for point in pareto:
            point.append(point[0])
        label_placement = np.linspace(start=0, stop=2 * np.pi, num=len(pareto[0]))
        # create matplotlib figure and polar plot with labels, title, and legend
        fig = plt.figure(figsize=(8, 8))
        point_sublists = [pareto[i:min(i + 5, len(pareto))] for i in range(0, len(pareto), 5)]
        i = 1
        for sublist in point_sublists:
            # Le nombre de colonnes dans la figure (1 pour une seule colonne)
            num_rows = 1

            # Calculez le nombre de lignes en fonction du nombre de sous-plots par colonne
            num_cols = len(point_sublists) // num_rows + (len(point_sublists) % num_rows > 0)
            ax = fig.add_subplot(num_rows, num_cols, i, polar=True)
            i += 1
            lines, labels = plt.thetagrids(np.degrees(label_placement), labels=categories)
            for point in sublist:
                ax.plot(label_placement, point)
            ax.legend(labels=[f"Point{(i - 2) * 5 + j + 1}" for j in range(len(sublist))], loc='lower right', fontsize=5)
        fig.suptitle('Compare pareto front Point', fontsize=22)
        plt.savefig('static/radar_chart.png')  # Sauvegarder le graphique comme fichier image
        plt.show()

if __name__ == "__main__":
    # Utilisation
    bruit = 0.1
    dimension = 5
    valeur_inf = 1
    valeur_sup = 10
    nb_points = 100
    n_clusters = 5

    clustering_result = Clustering(bruit, dimension, valeur_inf, valeur_sup, nb_points, n_clusters).clusteriser()
    closest_points, labels = clustering_result

    Radar.vue_radar(closest_points)
