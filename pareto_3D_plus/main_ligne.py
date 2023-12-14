from flask import Flask, render_template, request, redirect, url_for
from clustering_1surx import Clustering1surX
from clustering_random import ClusteringRandom
from radar import Radar
import matplotlib
matplotlib.use('Agg')
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        bruit = 0.1
        dimension = int(request.form['dimension'])
        valeur_inf = 1
        valeur_sup = 10
        nb_points = int(request.form['nb_points'])
        n_clusters = int(request.form['n_clusters'])
        n_clusters = int(request.form['n_clusters'])
        choix_multiple = request.form.getlist('choixMultiple')[0]
        choix_presentation = request.form.getlist('choixPresentation')[0]
        print(choix_multiple)
        # Effectuer le clustering
        if choix_multiple == "1surx":
            clustering_result = Clustering1surX(bruit, dimension, valeur_inf, valeur_sup, nb_points, n_clusters).clusteriser()
            closest_points, labels = clustering_result
            if choix_presentation == "radar":
                radar_chart = Radar.vue_radar(closest_points)
            else:
                radar_chart = Radar.tsne(closest_points)

        else:
            clustering_result = ClusteringRandom(bruit, dimension, valeur_inf, valeur_sup, nb_points, n_clusters).clusteriser()
            closest_points, labels = clustering_result
            if choix_presentation == "radar":
                radar_chart = Radar.vue_radar(closest_points)
            else:
                radar_chart = Radar.tsne(closest_points)
        # Rediriger vers la nouvelle page avec les résultats
        return redirect(url_for('result', radar_chart=radar_chart))
    
    return render_template('index.html')

@app.route('/result')
def result():
    # Récupérer le graphique radar depuis les arguments de l'URL
    radar_chart = request.args.get('radar_chart', '')
    # Afficher les résultats sur une nouvelle page
    return render_template('result.html', radar_chart=radar_chart)

if __name__ == '__main__':
    app.run(debug=True)
