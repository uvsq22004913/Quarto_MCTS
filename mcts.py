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
def expansion(noeud):
    for p_jouée in noeud.p_reste:
        for index_x, x in enumerate(noeud.plateau):
            [nouv_noeud(noeud, p_jouée, index_x, index_y) for index_y, y in enumerate(x) if y == None]
    return random.choice(noeud.enfants)


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


# entrée : noeud parent, p_jouée, coordonnées sur le plateau(x,y)
# sortie : noeud parent
def nouv_noeud(noeud_p, pièce, x, y):
    plateau = noeud_p.plateau.copy()
    plateau[x][y] = pièce
    reste = noeud_p.p_reste.copy()
    [reste.pop(p) for p in reste if p == pièce]
    noeud_e = Noeud(plateau, None, noeud_p, reste)
    noeud_p.enfants.append(noeud_e)
    return noeud_p


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
    
    if plateau[x][3-x] == None:
        if sum_grand == 0 or sum_grand == 4:
            return True
        if sum_plein == 0 or sum_plein == 4:
            return True
        if sum_clair == 0 or sum_clair == 4:
            return True
        if sum_carre == 0 or sum_carre == 4:
            return True
    
    return False

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
