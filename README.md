# Projet_commande_entreprise


# README

## Visualisation d'un Front de Pareto avec Clustering

Ce programme permet de générer un front de Pareto en utilisant deux méthodes de création de points : "Points 1/x" et "Points aléatoires". Ensuite, il effectue une clustering sur le front de Pareto généré en utilisant l'algorithme K-Means.

### Fichiers principaux

1. **clustering_1surx.py et clustering_random.py:** Ces fichiers contiennent deux classes, `Clustering1surX` et `ClusteringRandom`, qui effectuent la clustering sur les fronts de Pareto générés par les méthodes "Points 1/x" et "Points aléatoires", respectivement.

2. **frontPareto.py:** Ce fichier contient la classe `FrontPareto` qui génère un front de Pareto en utilisant deux méthodes : "Points 1/x" et "Points aléatoires".

3. **points.py:** Ce fichier contient la classe `Point` qui représente un point dans l'espace.

4. **radar.py:** Ce fichier contient la classe `Radar` qui génère des graphiques radar ou des visualisations t-SNE à partir des points de Pareto.

5. **app.py:** Ce fichier contient l'application Flask qui permet à l'utilisateur de spécifier les paramètres, de choisir la méthode de génération des points et de visualiser le résultat.

### Comment exécuter le programme

1. Installez les dépendances nécessaires en utilisant la commande suivante :
   ```
   pip install Flask scikit-learn matplotlib numpy
   ```

2. Exécutez l'application Flask en utilisant la commande :
   ```
   python pareto_....py
   ```

3. Ouvrez votre navigateur et accédez à l'URL [http://127.0.0.1:5000/](http://127.0.0.1:5000/) pour utiliser l'interface utilisateur.

4. Remplissez le formulaire avec les paramètres souhaités, choisissez la méthode de génération des points et la présentation (radar ou t-SNE), puis cliquez sur "Soumettre".

5. Visualisez le résultat sur la page suivante.

### Structure des fichiers HTML

1. **index.html:** Page d'accueil avec le formulaire pour spécifier les paramètres.

2. **result.html:** Page affichant le résultat sous forme de graphique radar ou de visualisation t-SNE.

### Dossiers

1. **static:** Contient le fichier CSS pour le style de l'interface utilisateur et les images générées.

### Remarques

- Le graphique généré sera sauvegardé dans le dossier `static` sous le nom de fichier `radar_chart.png`.

- Les paramètres tels que le bruit, la dimension, les valeurs inférieure et supérieure, le nombre de points, et le nombre de clusters peuvent être modifiés dans le fichier `app.py`.