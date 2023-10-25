from flask import Flask, render_template, request
import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('Agg')  # Activation du mode non interactif de Matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        input_data = request.form['points']
        # Diviser les lignes en un tableau
        lines = input_data.split('\n')
        
        # Traiter les données pour obtenir un tableau NumPy
        points = []
        for line in lines:
            # Ignorer les lignes vides
            if line.strip():
                values = list(map(int, line.split(',')))
                if len(values) == 2:
                    points.append(values)

        if len(points) < 2:
            return "Veuillez entrer au moins deux points valides."

        points = np.array(points)
        
        # Calculer le front de Pareto
        indices_pareto = front_de_pareto(points)
        front_pareto = points[indices_pareto]

        # Trier les points du front de Pareto par abscisses croissantes
        front_pareto = front_pareto[np.argsort(front_pareto[:, 0])]

        
        # Créer le graphique
        x_pareto = front_pareto[:, 0]
        y_pareto = front_pareto[:, 1]

        plt.scatter(points[:, 0], points[:, 1])
        plt.plot(x_pareto, y_pareto, color='g')
        plt.title("Graphique de l'ensemble de points et de leur front de Pareto")
        plt.xlabel('Axe x')
        plt.ylabel('Axe y')
        
        # Convertir le graphique en une image base64
        img_data = BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        img_base64 = base64.b64encode(img_data.read()).decode()
        img_url = f'data:image/png;base64,{img_base64}'
        return render_template('/result2D.html', img_url=img_url , points_pareto = front_pareto)
    return render_template('index2D.html')


if __name__ == '__main__':
    app.run(debug=True)
