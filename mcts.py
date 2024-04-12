import random

# TOUT ECRIRE EN FRANCAIS!!!!
# égalité = défaite

# 1 = True, 0 = False
piece = {"grand" : 1,
        "plein" : 1,
        "clair" : 1,
        "carré" : 1}

# initialisation d'un plateau vide
plateau = [[None for _ in range(4)] for _ in range(4)]

# Tour du joueur : 0 Joueur 1 ; 1 Joueur 2
tour_joueur = 0

# entrée : racine (1)
# sortie : noeud sélectionné (2)
def selection():
    pass


# entrée : noeud sélectionné (2)
# sortie : noeud sélectionné (3)
def expansion():
    pass


# entrée : noeud sélectionné (3)
# sortie : résultat
def simulation(noeud, tour_joueur):
    plateau = noeud.plateau
    p_reste = noeud.p_reste
    while not quarto(plateau):
        i, j = choix_case(plateau)
        p_reste = random.shuffle(p_reste)
        plateau[i][j] = p_reste.pop()
        #placer_piece(plateau, i, j, p_reste.pop())
        tour_joueur = 1 - tour_joueur
    return 1 - tour_joueur


# entrée : résultat, noeud sélectionné (3)
# sortie : racine (1)
def retropropagation(noeud, res):
    while True:
        if noeud.parent is None:
            noeud.add_simul(res)
            return noeud
        noeud.add_simul(res)
        noeud = noeud.parent
    return noeud


# entrée : plateau
# sortie : (i, j) coordonnée de la case choisie
def choix_case(plateau):
    cases = list()
    for i in range(4):
        for j in range(4):
            if plateau[i][j] is None:
                cases.append((i,j))
    return random.choice(cases)


# entrée : plateau
# sortie : booléen
def quarto():
   pass

#Structure de l'arbre
class Noeud:
    def __init__(self, plateau, enfants, parent, p_reste):
        self.plateau    = plateau
        self.enfants    = enfants
        self.parent     = parent
        self.p_reste    = p_reste
        self.uct        = -1      # uct = -1 représente uct --> infinie
        self.simulation = 0
        self.victoire   = 0

    def get_parent(self):
        return self.parent

    def get_enfants(self):
        return self.enfants

    def get_plateau(self):
        return self.plateau

    def add_simul(self, res):
        self._simulation += 1
        self._victoire += res
