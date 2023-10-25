# Importation des bibliothèques nécessaires
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fonction qui obtient les points de Pareto
def pareto_3D(Points):
    # Crée un ensemble pour stocker les points de Pareto
    points_de_pareto = set()
    # Initialise le numéro de ligne du candidat à 0
    numero_ligne_candidat = 0
    # Crée un ensemble pour stocker les points dominés
    points_dominants = set()
    # Début de la boucle principale
    while True:
        # Récupère la ligne candidat à partir de la liste des points
        ligne_candidat = Points[numero_ligne_candidat]
        # Retire la ligne candidat de la liste des points
        Points.remove(ligne_candidat)
        # Initialise le numéro de ligne à 0
        numero_ligne = 0
        # Initialise la variable pour indiquer si la ligne candidat est non dominée
        non_dominant = True
        # Boucle pour comparer la ligne candidat aux autres lignes
        while len(Points) != 0 and numero_ligne < len(Points):
            # Récupère la ligne actuelle à comparer
            ligne = Points[numero_ligne]
            # Vérifie si la ligne candidat domine la ligne actuelle
            if domine(ligne_candidat, ligne):
                # Si c'est le cas, retire la ligne actuelle des points
                Points.remove(ligne)
                # Ajoute la ligne actuelle aux points dominants
                points_de_pareto.add(tuple(ligne))
            # Vérifie si la ligne actuelle domine la ligne candidat
            elif domine(ligne, ligne_candidat):
                # Si c'est le cas, la ligne candidat n'est pas non dominante
                non_dominant = False
                # Ajoute la ligne candidat aux points dominants
                points_de_pareto.add(tuple(ligne_candidat))
                # Passe à la ligne suivante
                numero_ligne += 1
            else:
                # Si aucune domination n'est détectée, passe à la ligne suivante
                numero_ligne += 1
        # Si la ligne candidat est non dominée, ajoute-la aux points de Pareto
        if non_dominant:
            points_dominants.add(tuple(ligne_candidat))
        # Si la liste des points est vide, la boucle se termine
        if len(Points) == 0:
            break
    # Retourne l'ensemble des points de Pareto et l'ensemble des points dominés
    return points_de_pareto, points_dominants


# Fonction qui vérifie si une ligne domine une autre
def domine(ligne, ligne_candidat):
    return sum([ligne[x] >= ligne_candidat[x] for x in range(len(ligne))]) == len(ligne)

# Placez votre ensemble de points ici
# Exemples de points
Points = [[97, 23, 25], [55, 77, 35], [34, 76, 29], [80, 60, 42], [99, 4, 28], [81, 5, 76], [5, 81, 56], [30, 79, 24], [15, 80, 42], [70, 65, 74], [90, 40, 36], [40, 30, 94], [30, 40, 5], [20, 60, 42], [60, 50, 4], [20, 20, 49], [30, 1, 73], [60, 40, 55], [70, 25, 42], [44, 62, 37], [55, 55, 49], [55, 10, 18], [15, 45, 72], [83, 22, 29], [76, 46, 10], [56, 32, 27], [45, 55, 88], [10, 70, 26], [10, 30, 44], [79, 50, 40]]
#Points = [[97, 23, 25], [55, 77, 35],[34, 76, 29], [99, 4, 28]]

points_de_pareto, points_dominants = pareto_3D(Points)

# Tracé du front de Pareto en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points_dominants_array = np.array(list(points_dominants))
points_de_pareto_array = np.array(list(points_de_pareto))
plt.title('Front de Pareto')
ax.scatter(points_dominants_array[:,0], points_dominants_array[:,1], points_dominants_array[:,2], color='red')
ax.scatter(points_de_pareto_array[:,0], points_de_pareto_array[:,1], points_de_pareto_array[:,2], color='green')

print(points_dominants_array)




plt.show()
