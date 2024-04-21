from math import sqrt
from math import log

# TOUT ECRIRE EN FRANCAIS!!!!
# égalité = défaite

# 1 = True, 0 = False
piece = {"grand" : 1,
         "plein" : 1,
         "clair" : 1,
         "carré" : 1}

# Constantes
INFINIE = -1

def calcul_uct(noeud, parent):
    """
        * Calcule et retourne la valeur UCT du noeud en entrée
    """

    C = sqrt(2)
    global INFINIE

    if noeud.get_simulation() != 0:
        return (noeud.get_victoire() / noeud.get_simulation()) + (C * sqrt ( log(parent.get_simulation()) / noeud.get_simulation()))
    else:
        return INFINIE


# entrée : racine (1)
# sortie : noeud sélectionné (2)
def selection(noeud):
    global INFINIE
    enfants = noeud.get_enfants()
    uct_max = 0
    position = 0

    for i,enfant in enumerate(enfants):
        uct = calcul_uct(enfant, noeud)
        
        if uct != INFINIE:
            if uct > uct_max:
                uct_max  = uct
                position = i
        else:
            position = i
    
    return enfants[position]


# entrée : noeud sélectionné (2)
# sortie : noeud sélectionné (3)
def expansion():
    pass


# entrée : noeud sélectionné (3)
# sortie : résultat
def simulation():
    pass


# entrée : résultat, noeud sélectionné (3)
# sortie : racine (1)
def retropropagation():
    pass


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
    
    def get_plataeu(self):
        return self.plateau
    
    def get_simulation(self):
        return self.simulation

# initialisation d'un plateau vide
plateau = [
            [],
            [],
            [],
            []
          ]

#racine = Noeud(plateau, [], , )