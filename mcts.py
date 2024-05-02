import random
from math import log
from math import sqrt
from copy import deepcopy

# TOUT ECRIRE EN FRANCAIS!!!!
# égalité = défaite

# 1 = True, 0 = False
piece = {"grand" : 1,
        "plein" : 1,
        "clair" : 1,
        "carre" : 1}

# Constantes
INFINIE = -1
DUREE = 300
C = sqrt(2)
LISTES_PIECES = [{"grand" : 1, "plein" : 1, "clair" : 1, "carre" : 1},
                 {"grand" : 1, "plein" : 0, "clair" : 1, "carre" : 1},
                 {"grand" : 0, "plein" : 1, "clair" : 1, "carre" : 1},
                 {"grand" : 0, "plein" : 0, "clair" : 1, "carre" : 1},
                 {"grand" : 1, "plein" : 1, "clair" : 1, "carre" : 0},
                 {"grand" : 1, "plein" : 0, "clair" : 1, "carre" : 0},
                 {"grand" : 0, "plein" : 1, "clair" : 1, "carre" : 0},
                 {"grand" : 0, "plein" : 0, "clair" : 1, "carre" : 0},
                 {"grand" : 1, "plein" : 1, "clair" : 0, "carre" : 1},
                 {"grand" : 1, "plein" : 0, "clair" : 0, "carre" : 1},
                 {"grand" : 0, "plein" : 1, "clair" : 0, "carre" : 1},
                 {"grand" : 0, "plein" : 0, "clair" : 0, "carre" : 1},
                 {"grand" : 1, "plein" : 1, "clair" : 0, "carre" : 0},
                 {"grand" : 1, "plein" : 0, "clair" : 0, "carre" : 0},
                 {"grand" : 0, "plein" : 1, "clair" : 0, "carre" : 0},
                 {"grand" : 0, "plein" : 0, "clair" : 0, "carre" : 0}]

# initialisation d'un plateau vide
plateau = [[None for _ in range(4)] for _ in range(4)]

# Tour du joueur : 0 Joueur ; 1 ordi
tour_joueur = 0
 
# entrée : racine (1)
# sortie : noeud sélectionné (2)
def selection(noeud):
    while noeud.enfants:
        noeud = noeud.meilleur_enfant()
    return noeud


# entrée : noeud sélectionné (2)
# sortie : noeud sélectionné (3)
def expansion(noeud):

    pieces_restantes = deepcopy(noeud.get_p_reste())
    plateau = deepcopy(noeud.get_plateau())

    # Parcoure la liste des pièces restantes
    for piece in noeud.get_p_reste():
        # Parcoure les lignes du plateau
        for i in range(4):
            # Parcoure les colonnes du plateau
            for j in range(4):
                if plateau[i][j] == None:
                    plateau[i][j] = piece
                    pieces_restantes.remove(piece)
                    fils = Noeud(plateau, noeud, pieces_restantes)
                    noeud.enfants.append(fils)
                    plateau = deepcopy(noeud.get_plateau())
                    pieces_restantes = deepcopy(noeud.get_p_reste())
    return noeud.enfants[0]
                

# entrée : noeud sélectionné (3)
# sortie : résultat
def simulation(noeud, tour_joueur):
    plateau = deepcopy(noeud.plateau)
    p_reste = deepcopy(noeud.p_reste)
    while not quarto(plateau) and p_reste:
        ligne, colonne = choix_case(plateau)
        random.shuffle(p_reste)
        if plateau[ligne][colonne] is None:
            plateau[ligne][colonne] = p_reste.pop()
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
        noeud.calcul_uct()
        noeud = noeud.parent


# entrée : noeud parent, p_jouée, coordonnées sur le plateau(x,y)
# sortie : noeud parent
def nouv_noeud(noeud_p, pièce, x, y):
    plateau = noeud_p.plateau.copy()
    plateau[x][y] = pièce
    reste = noeud_p.p_reste.copy()
    [reste.pop(p) for p in reste if p == pièce]
    noeud_e = Noeud(plateau, noeud_p, reste)
    noeud_p.enfants.append(noeud_e)
    return noeud_p


# entrée : plateau
# sortie : (i, j) coordonnée de la case choisie
def choix_case(plateau):
    cases_vide = list()
    for i in range(4):
        for j in range(4):
            if plateau[i][j] == None:
                cases_vide.append((i,j))
    return random.choice(cases_vide)


# entrée : plateau
# sortie : booléen
def quarto(plateau):
    # vérification des lignes
    for x in range(4):
        sum_grand = 0
        sum_plein = 0
        sum_clair = 0
        sum_carre = 0
        for y in range(4):
           if plateau[x][y] == None: break
           sum_grand += (plateau[x][y])["grand"]
           sum_plein += (plateau[x][y])["plein"]
           sum_clair += (plateau[x][y])["clair"]
           sum_carre += (plateau[x][y])["carre"]
        if plateau[x][y] == None: continue
        if sum_grand == 0 or sum_grand == 4:
            return True
        if sum_plein == 0 or sum_plein == 4:
            return True
        if sum_clair == 0 or sum_clair == 4:
            return True
        if sum_carre == 0 or sum_carre == 4:
            return True
    # vérification des colonnes
    for x in range(4):
        sum_grand = 0
        sum_plein = 0
        sum_clair = 0
        sum_carre = 0
        for y in range(4):
           if plateau[y][x] == None: break
           sum_grand += (plateau[y][x])["grand"]
           sum_plein += (plateau[y][x])["plein"]
           sum_clair += (plateau[y][x])["clair"]
           sum_carre += (plateau[y][x])["carre"]
        if plateau[y][x] == None: continue
        if sum_grand == 0 or sum_grand == 4:
            return True
        if sum_plein == 0 or sum_plein == 4:
            return True
        if sum_clair == 0 or sum_clair == 4:
            return True
        if sum_carre == 0 or sum_carre == 4:
            return True
    # vérification première diagonale
    sum_grand = 0
    sum_plein = 0
    sum_clair = 0
    sum_carre = 0
    for x in range(4):
        if plateau[x][x] == None: break
        sum_grand += (plateau[x][x])["grand"]
        sum_plein += (plateau[x][x])["plein"]
        sum_clair += (plateau[x][x])["clair"]
        sum_carre += (plateau[x][x])["carre"]
    
    if not plateau[x][x] == None:
        if sum_grand == 0 or sum_grand == 4:
            return True
        if sum_plein == 0 or sum_plein == 4:
            return True
        if sum_clair == 0 or sum_clair == 4:
            return True
        if sum_carre == 0 or sum_carre == 4:
            return True
    # vérification seconde diagonale
    sum_grand = 0
    sum_plein = 0
    sum_clair = 0
    sum_carre = 0
    for x in range(4):
        if plateau[x][3-x] == None: break
        sum_grand += (plateau[x][3-x])["grand"]
        sum_plein += (plateau[x][3-x])["plein"]
        sum_clair += (plateau[x][3-x])["clair"]
        sum_carre += (plateau[x][3-x])["carre"]

    if not plateau[x][3-x] == None:
        if sum_grand == 0 or sum_grand == 4:
            return True
        if sum_plein == 0 or sum_plein == 4:
            return True
        if sum_clair == 0 or sum_clair == 4:
            return True
        if sum_carre == 0 or sum_carre == 4:
            return True

    return False


def nouvelle_partie():
    for i in range(4):
        for j in range(4):
            plateau[i][j] = None
    if tour_joueur == 1:
        changement_joueur()


def changement_joueur():
    global tour_joueur
    tour_joueur = 1 - tour_joueur


#Structure de l'arbre
class Noeud:
    def __init__(self, plateau, parent=None, p_reste=LISTES_PIECES):
        self.plateau    = plateau
        self.enfants    = []
        self.parent     = parent
        self.p_reste    = p_reste
        self.uct        = INFINIE      # uct = -1 représente uct --> infinie
        self.simulation = 0
        self.victoire   = 0

    def get_parent(self):
        return self.parent

    def get_enfants(self):
        return self.enfants

    def get_plateau(self):
        return self.plateau
    
    def get_simulation(self):
        return self.simulation

    def get_p_reste(self):
        return self.p_reste

    def add_simul(self, res):
        self.simulation += 1
        self.victoire += res

    """
    def calcul_uct(self):
         * Calcule et renvoie la valeur UCT du noeud en entrée 
        C = sqrt(2)

        if self.get_simulation() != 0 and self.parent.get_simulation() != 0:
            if log(self.parent.get_simulation() / self.get_simulation()) >= 0:
                self.uct = ((self.victoire / self.get_simulation()) + (C * sqrt(log(self.parent.get_simulation() / self.get_simulation())))) 
        else:
            self.uct = INFINIE
    """

    def calcul_uct(self):
        """  * Calcule et renvoie la valeur UCT du noeud en entrée  """
        global INFINIE
        global C
        Wi = self.victoire
        Ni = self.parent.simulation
        ni = self.simulation

        if ni == 0 or Ni == 0:
            self.uct = INFINIE
        else: 
            self.uct = (Wi / ni) + C * (sqrt (log(Ni) / ni))

    # entrée : noeud
    # sortie : noeud enfant avec le meilleur score UCT
    def meilleur_enfant(self):
        if not self.enfants :
            return self
        uct_max = 0
        for enfant in self.enfants:
            if enfant.uct == INFINIE:
                return enfant
            if enfant.uct > uct_max:
                uct_max = enfant.uct
                enfant_max = enfant
        return enfant_max
    
    def piece_choisie(self):
        if self.parent != None:
            plateau_parent = self.parent.plateau
            for i in range(4):
                for j in range(4):
                    if self.plateau[i][j] != plateau_parent[i][j]:
                        piece_choisie = self.plateau[i][j]
                        position = (i, j)
                        return [piece_choisie, position]
        else:
            return "Cette méthode n'est pas définie pour la racine."


# Check si il y a quarto et plateau vide
def depose_piece(racine):
    for _ in range(DUREE):
        noeud_selectione = selection(racine)

        if noeud_selectione.uct != INFINIE:
            noeud_selectione = expansion(noeud_selectione)
    
        resultat = simulation(noeud_selectione, tour_joueur)
        noeud_final = retropropagation(noeud_selectione, resultat)
        
    for enfant in racine.enfants:
        print(enfant.simulation, enfant.victoire)
    noeud_final = noeud_final.meilleur_enfant()
    
    return noeud_final.piece_choisie()
