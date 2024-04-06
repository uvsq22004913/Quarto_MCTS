# TOUT ECRIRE EN FRANCAIS!!!!
# égalité = défaite

# 1 = True, 0 = False
piece = {"grand" : 1,
         "plein" : 1,
         "clair" : 1,
         "carré" : 1}

plateau = [
            [],
            [],
            [],
            []
          ]

def placer_une_piece (plateau, piece , position):
    """
        @paramètres:
            
piece est la piece a placer sur le plateau est de la forme [b0, b1, b2, b3] avec bi des 0 ou des 1
position est la position ou il faut placer la pièce elle de la forme (ligne, colonne)
le plateau sur lequel on place la pièce

        @retour:
            
Le plateau avec la pièce placée"""
  pass


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
   def __init__(self, plateau, enfants, parent, p_reste, UCT, nbr_éssaies, victoire):

