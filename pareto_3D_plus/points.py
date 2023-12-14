import random
import numpy as np


class Point:

    def __init__(self, bruit, dimension, valeur_inf, valeur_sup):
        self.bruit = bruit
        self.dimension = dimension
        self.liste_coordonees = np.zeros(dimension, dtype = float)
        self.valeur_inf = valeur_inf
        self.valeur_sup = valeur_sup

    def creationCoordonnees_1surx(self):

        for i in range(self.dimension):
            x = random.uniform(self.valeur_inf, self.valeur_sup)  # Plage de valeurs pour une coordonnee
            noise = random.gauss(0, self.bruit)  # Bruit gaussien
            self.liste_coordonees[i] = 1/x + noise +1
        print(self.liste_coordonees)

    def creationCoordonnees_random(self):

        for i in range(self.dimension):
            x = random.uniform(self.valeur_inf, self.valeur_sup)  # Plage de valeurs pour une coordonnee
            noise = random.gauss(0, x)  # Bruit gaussien
            self.liste_coordonees[i] = x + noise +1