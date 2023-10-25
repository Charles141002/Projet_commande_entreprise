# Importation des bibliothèques
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

# Fonction qui trouve les indices (dans le tableau de points) des points appartenants au front de pareto 
def front_de_pareto(points):
    n = points.shape[0]
    indices_population = np.arange(n)
    front_pareto = np.ones(n, dtype=bool)
    
    # Calcul du front de Pareto
    for i in range(n):
        for j in range(n):
            if all(points[j] <= points[i]) and any(points[j] < points[i]):
                front_pareto[i] = 0
                break
    return indices_population[front_pareto]  # Creation d'un tableau numpy où il ne reste que les indices des points i pour lequel front_pareto[i] est True. Les autres sont "éliminés"

# Définission de l'ensemble de points
# Plage de valeurs pour la distribution uniforme
#low_x = 1.0  # Borne inférieure pour x
#high_x = 5.0  # Borne supérieure pour x

#low_y = 2.0  # Borne inférieure pour y
#high_y = 6.0  # Borne supérieure pour y


#x = [(random.gauss(4,1)+random.uniform(low_x, high_x)) for _ in range(4000)]
#y = [(random.gauss(4,2)+random.uniform(low_y, high_y)) for _ in range(4000)]



#points = np.array([x, y]).T


# Nombre de points
n_points = 10000

# Générer des points aléatoires
x = np.random.uniform(1, 10, n_points)  # Plage de valeurs pour x
y = 1 / x  # Calculez les valeurs de y en utilisant la fonction 1/x

# Ajouter un peu de bruit aléatoire pour rendre les points plus aléatoires
noise = np.random.normal(0, 0.1, n_points)  # Ajout de bruit gaussien
y += noise

# Créer un tableau NumPy à partir de x et y
points = np.array([x, y]).T


#points = np.array([[55, 77], [70, 65], [40, 30], [30, 40], [20, 60], [60, 50], [30, 1], [60, 40], [70, 25], [55, 55], [55, 10], [8, 30], [10, 23], [45, 75], [72, 60], [42, 32], [35, 42], [23, 61], [63, 51], [22, 22], [32, 3], [65, 45], [75, 22], [47, 65], [58, 57], [57, 12], [7, 35], [13, 24], [33, 70], [6, 88], [15, 90], [17, 95], [72, 75], [41, 32], [38, 41], [25, 69], [67, 55], [27, 22], [37, 2], [66, 42], [79, 28], [59, 59], [59, 8], [9, 38], [14, 22], [32, 44], [10, 66], [51, 44], [53, 51], [55, 50], [53, 33], [32, 50], [32, 40], [32, 30], [21, 60], [63, 50], [22, 12], [35, 5], [64, 45], [73, 26], [49, 64], [52, 55], [51, 12], [9, 45], [19, 21], [36, 5], [21, 73], [11, 66], [17, 25], [28, 30], [43, 62], [55, 59], [54, 10], [4, 30], [72, 42], [75, 25], [49, 62], [52, 56], [50, 5], [8, 30], [16, 23], [37, 2], [12, 67], [18, 23], [24, 38], [56, 55], [58, 15], [6, 38], [14, 26], [39, 5], [3, 47], [26, 72], [13, 68], [29, 22], [33, 35], [44, 62], [57, 58], [59, 14], [8, 40], [78, 42], [15, 28], [7, 46], [20, 74], [10, 67], [19, 27], [23, 33], [46, 61], [55, 57], [57, 18], [5, 36], [77, 41], [12, 29], [6, 43], [22, 74], [11, 65], [20, 24], [29, 32], [42, 61], [54, 56], [56, 20], [4, 35]])


# Creaction d'un tableau Numpy des indices des points appartenant au front de pareto
indices_pareto = front_de_pareto(points)
# Creation d'un tableau Numpy où il y a seulement les points appartenants au front de pareto
front_pareto = points[indices_pareto]

# Trie des points du front de pareto, avec les abscisses croissantes : Pour éviter de tracer un front de pareto qui fait des trucs bizarres, la le front de pareto ira de gauche à droite sans croisements
data = pd.DataFrame(front_pareto)
data.sort_values(0, inplace=True)
front_pareto = data.values

# Traçage du front de Pareto
x = points[:, 0]
y = points[:, 1]
x_pareto = front_pareto[:, 0]
y_pareto = front_pareto[:, 1]

#plt.scatter(x, y, marker='x', s=10, alpha=0.5, c='b')  # Utilisation de 'x' comme marqueur
plt.scatter(x_pareto, y_pareto, marker='x', c='r')  # Utilisation de 'x' comme marqueur

plt.title("Graphique de l'ensemble de points et de leur front de Pareto")
plt.plot(x_pareto, y_pareto, color='g') # Traçage du front de pareto
plt.xlabel('Axe x')
plt.ylabel('Axe y')
plt.show()