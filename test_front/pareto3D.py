from flask import Flask, render_template, request, send_file
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Fonction qui obtient les points de Pareto
def pareto_simple(Points):
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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        input_data = request.form['points']
        print(input_data)
        
        # Diviser les lignes en un tableau
        lines = input_data.split('\n')
        
        # Traiter les données pour obtenir un tableau NumPy
        points = []
        for line in lines:
            # Ignorer les lignes vides
            if line.strip():
                values = list(map(int, line.split(",")))
                if len(values) == 3:  # Assurez-vous que le nombre de colonnes est correct
                    points.append(values)

        if len(points) < 3:
            return "Veuillez entrer au moins trois points valides."

        points = np.array(points)
        points_de_pareto, _ = pareto_simple(points)

        # Tracer le front de Pareto
        fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        ax.scatter(*points_de_pareto.T, color='green', label='Front de Pareto')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Convertir le graphique en une image
        img_data = BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        img_base64 = base64.b64encode(img_data.read()).decode()
        img_url = f'data:image/png;base64,{img_base64}'

        return render_template('result3D.html', img_url=img_url)

    return render_template('index3D.html')

if __name__ == '__main__':
    app.run(debug=True)
