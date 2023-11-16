# Importation des modules nécessaires
from flask import Flask, render_template, request
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Activation du mode non interactif de Matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min



# Création de l'application Flask

app = Flask(__name__)

# __ FONCTIONS __
# Fonction qui trouve les indices (dans le tableau de points) des points appartenants au front de Pareto 

def front_de_pareto(points):
    n = points.shape[0]
    print(points)
    indices_population = np.arange(n)
    front_pareto = np.ones(n, dtype=bool)
    # Calcul du front de Pareto
    for i in range(n):
        for j in range(n):
            if all(points[j] <= points[i]) and any(points[j] < points[i]):
                front_pareto[i] = 0
                break
    return indices_population[front_pareto]  # Crée un tableau NumPy où il ne reste que les indices des points i pour lesquels front_pareto[i] est True. Les autres sont "éliminés"

# Fonction pour générer des points aléatoires
def generer_points_aleatoires(n):
    x = np.random.uniform(2, 50, n)  # Plage de valeurs pour x
    y = 1/x + 1# Calculez les valeurs de y en utilisant la fonction 1/x +1
    noise = np.random.normal(0, 0.015, n)  # Ajout de bruit gaussien
    y += noise
    return np.column_stack((x, y))

#Fonction pour faire les clusters
def generer_clusters(data):
    # Spécifier le nombre de clusters souhaité
    n_clusters = 5
    # Créer un modèle K-Means
    kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    kmeans.fit(data)
    # Obtenir les étiquettes de cluster attribuées à chaque point de données
    labels = kmeans.labels_
    # Initialiser une liste vide pour stocker les points les plus proches de chaque cluster
    closest_points = []
    # Itérer sur chaque cluster
    for cluster_label in range(n_clusters):
        # Sélectionner les points appartenant à ce cluster
        cluster_points = data[labels == cluster_label]
        # Calculer la distance de chaque point par rapport au centre du cluster
        distances = np.linalg.norm(cluster_points - kmeans.cluster_centers_[cluster_label], axis=1)
        # Trouver l'indice du point le plus proche
        closest_point_index = np.argmin(distances)
        # Ajouter le point le plus proche à la liste
        closest_points.append(cluster_points[closest_point_index])
    # Convertir la liste en un tableau NumPy
    closest_points = np.array(closest_points)
    return closest_points, labels

# __ EN LIGNE __

# Définition de la route principale de l'application
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'afficher' in request.form:
            # Générer des points aléatoires
            points = generer_points_aleatoires(4000)
        else:
            return "Veuillez cliquer sur le bouton 'Afficher' pour générer des données aléatoires."
        # Calculer le front de Pareto
        indices_pareto = front_de_pareto(points)
        front_pareto = points[indices_pareto]
        # Trier les points du front de Pareto par abscisses croissantes
        front_pareto = front_pareto[np.argsort(front_pareto[:, 0])]
        # Créer le premier graphique
        x_pareto = front_pareto[:, 0]
        y_pareto = front_pareto[:, 1]
        plt.clf()
        plt.scatter(points[:, 0], points[:, 1])
        plt.plot(x_pareto, y_pareto, color='g')
        plt.title("Graphique de l'ensemble de points et de leur front de Pareto")
        plt.xlabel('Axe x')
        plt.ylabel('Axe y')
        # Convertir le premier graphique en une image base64
        img_data = BytesIO()
        plt.savefig(img_data, format='png')
        # Effacer le graphique pour préparer le deuxième
        plt.clf()
        # Créer le deuxième graphique
        plt.scatter(x_pareto, y_pareto)
        plt.plot(x_pareto, y_pareto, color='g')
        plt.title("Graphique des points du front de Pareto et de leur front de Pareto")
        plt.xlabel('Axe x')
        plt.ylabel('Axe y')
        # Convertir le deuxième graphique en une image base64
        img_data2 = BytesIO()
        plt.savefig(img_data2, format='png')
        # Créer un nouveau graphique pour afficher les clusters
        plt.clf()
        # Adapter le modèle aux données
        closest_points, labels = generer_clusters(front_pareto)
        # Afficher les résultats
        plt.scatter(closest_points[:, 0], closest_points[:, 1,], c='red', marker='x')
        plt.title('K-Means Clustering')
        plt.xlabel('Axe x')
        plt.ylabel('Axe y')
        plt.show()
        # Convertir le graphique en une image base64
        img_data_clusters = BytesIO()
        plt.savefig(img_data_clusters, format='png')
        img_data_clusters.seek(0)
        img_base64_clusters = base64.b64encode(img_data_clusters.read()).decode()
        img_url_clusters = f'data:image/png;base64,{img_base64_clusters}'
        img_data.seek(0)
        img_base64 = base64.b64encode(img_data.read()).decode()
        img_url = f'data:image/png;base64,{img_base64}'
        img_data2.seek(0)
        img_base642 = base64.b64encode(img_data2.read()).decode()
        img_url2 = f'data:image/png;base64,{img_base642}'
        # Rendre le modèle HTML avec les deux images et les points Pareto
        return render_template('result2D.html', img_url=img_url, img_url2=img_url2, points_pareto=front_pareto, img_url_clusters=img_url_clusters)
    # Si la méthode est GET (premier chargement de la page), afficher le modèle de base
    return render_template('index2D.html')


# Point d'entrée de l'application
if __name__ == '__main__':
    app.run(debug=True)
