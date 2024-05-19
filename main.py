import tkinter as tk
from random import randint
import interface
import mcts

IMAGE_PLATEAU = "images/p-1.jpg"

def piece_selected_callback(piece):
    # Afficher ou utiliser la pièce sélectionnée
    print("Pièce sélectionnée:", piece)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = interface.Fenetre(root)
    
    # Enregistrer le callback
    app.set_piece_selected_callback(piece_selected_callback)
    
    # Affichage du plateau et des pièces
    app.creer_plateau()
    app.creation_pieces()

    # Initialisation de la racine de l'arbre
    plateau_vide = [[None for _ in range(4)] for _ in range(4)]
    racine = mcts.Noeud(plateau_vide)

    # 0 Joueur ; 1 ordi
    tour = randint(0, 1)
    tour = 0
    # joueur commence
    if tour == 0:
        print("Tour du joueur.")
        app.affiche_piece("A vous de me choisir une pièce.", IMAGE_PLATEAU)
        # La pièce sera imprimée via le callback lorsqu'elle est sélectionnée
        
    # ordi commence
    else:
        print("Tour de l'ordi.")
        piece_choisie = mcts.choisir_piece(racine)
        app.affiche_piece("A vous de placer cette pièce.", IMAGE_PLATEAU)

    root.mainloop()
