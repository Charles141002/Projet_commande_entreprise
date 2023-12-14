from points import Point
import numpy as np

class FrontPareto:

    def __init__(self, bruit, dimension, valeur_inf, valeur_sup, nb_points):
        self.liste_points = [Point(bruit, dimension, valeur_inf, valeur_sup) for _ in range(nb_points)]
        self.liste_points_pareto = []

    def createCoPoints_1surx(self):
        for point in self.liste_points:
            point.creationCoordonnees_1surx()

    def findParetoPoints_1surx(self):
        self.createCoPoints_1surx()
        points = [point.liste_coordonees for point in self.liste_points]
        n = len(points)
        indices_population = np.arange(n)
        front_pareto = np.ones(n, dtype=bool)
        # Calcul du front de Pareto
        for i in range(n):
            for j in range(n):
                if all(points[j] <= points[i]) and any(points[j] < points[i]):
                    front_pareto[i] = False
                    break
        return np.array(points)[front_pareto]

    def createCoPoints_random(self):
        for point in self.liste_points:
            point.creationCoordonnees_random()
    
    def findParetoPoints_random(self):
        self.createCoPoints_random()
        points = [point.liste_coordonees for point in self.liste_points]
        n = len(points)
        indices_population = np.arange(n)
        front_pareto = np.ones(n, dtype=bool)
        # Calcul du front de Pareto
        for i in range(n):
            for j in range(n):
                if all(points[j] <= points[i]) and any(points[j] < points[i]):
                    front_pareto[i] = False
                    break
        return np.array(points)[front_pareto]

if __name__ == "__main__":
    # Exemple d'utilisation
    bruit = 0.1
    dimension = 5
    valeur_inf = 1
    valeur_sup = 10
    nb_points = 100

    front_pareto_obj = FrontPareto(bruit, dimension, valeur_inf, valeur_sup, nb_points)
    pareto_points = front_pareto_obj.findParetoPoints_1surx()

    print("Indices des points de Pareto:", pareto_points)
    print('nb_points', len(pareto_points) )