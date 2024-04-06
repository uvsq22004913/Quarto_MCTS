# TOUT ECRIRE EN FRANCAIS!!!!
# égalité = défaite

# 1 = True, 0 = False
piece = {"grand" : 1,
         "plein" : 1,
         "clair" : 1,
         "carré" : 1}


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

# initialisation d'un plateau vide
plateau = [
            [],
            [],
            [],
            []
          ]