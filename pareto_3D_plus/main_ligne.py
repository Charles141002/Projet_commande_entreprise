from flask import Flask, render_template, request, redirect, url_for
from clustering import Clustering
from radar import Radar
import matplotlib
matplotlib.use('Agg')
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        bruit = float(request.form['bruit'])
        dimension = int(request.form['dimension'])
        valeur_inf = float(request.form['valeur_inf'])
        valeur_sup = float(request.form['valeur_sup'])
        nb_points = int(request.form['nb_points'])
        n_clusters = int(request.form['n_clusters'])
        # Effectuer le clustering
        clustering_result = Clustering(bruit, dimension, valeur_inf, valeur_sup, nb_points, n_clusters).clusteriser()
        closest_points, labels = clustering_result
        # Générer le graphique radar
        radar_chart = Radar.vue_radar(closest_points)
        print(radar_chart)
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
