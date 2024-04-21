import mcts
import tkinter as tk
from PIL import ImageTk, Image

IMAGE_PLATEAU = "images/p-1.jpg"
CHEMINS_IMAGES = ["images/p0.jpg", "images/p1.jpg", "images/p2.jpg", "images/p3.jpg", "images/p4.jpg", "images/p5.jpg", "images/p6.jpg", "images/p7.jpg", 
                  "images/p8.jpg", "images/p9.jpg", "images/p10.jpg", "images/p11.jpg", "images/p12.jpg", "images/p13.jpg", "images/p14.jpg", "images/p15.jpg"]
LISTES_PIECES = [{"grand" : 1, "plein" : 1, "clair" : 1, "carré" : 1},
                {"grand" : 1, "plein" : 0, "clair" : 1, "carré" : 1},
                {"grand" : 0, "plein" : 1, "clair" : 1, "carré" : 1},
                {"grand" : 0, "plein" : 0, "clair" : 1, "carré" : 1},
                {"grand" : 1, "plein" : 1, "clair" : 1, "carré" : 0},
                {"grand" : 1, "plein" : 0, "clair" : 1, "carré" : 0},
                {"grand" : 0, "plein" : 1, "clair" : 1, "carré" : 0},
                {"grand" : 1, "plein" : 0, "clair" : 1, "carré" : 0},
                {"grand" : 1, "plein" : 1, "clair" : 0, "carré" : 1},
                {"grand" : 1, "plein" : 0, "clair" : 0, "carré" : 1},
                {"grand" : 0, "plein" : 1, "clair" : 0, "carré" : 1},
                {"grand" : 0, "plein" : 0, "clair" : 0, "carré" : 1},
                {"grand" : 1, "plein" : 1, "clair" : 0, "carré" : 0},
                {"grand" : 1, "plein" : 0, "clair" : 0, "carré" : 0},
                {"grand" : 0, "plein" : 1, "clair" : 0, "carré" : 0},
                {"grand" : 1, "plein" : 0, "clair" : 0, "carré" : 0}]


image_selectionnee = ""

def selectionner_une_piece(image):
    global image_selectionnee
    if image_selectionnee == "":
        image_selectionnee = image
        pieces[image].destroy()
        mcts.tour_joueur = 1 - mcts.tour_joueur


def deposer_une_piece(row, column):
    global image_selectionnee
    if image_selectionnee != "":
        image_pil = Image.open(image_selectionnee)
        image_tk = ImageTk.PhotoImage(image_pil)
        label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
        label_image.image = image_tk 
        label_image.grid(row=row, column=column, padx=20, pady=20)
        image_selectionnee = ""
        num_piece = (row + 1) * (column + 1) - 1
        piece = LISTES_PIECES[num_piece]
        mcts.place_piece(row, column, piece)
        #if quarto(mcts.plateau):
        #    fin_partie()



fenetre = tk.Tk()
fenetre.title("Quarto")
fenetre.configure(bg="black")

LARGEUR_ECRAN = fenetre.winfo_screenwidth()
HAUTEUR_ECRAN = fenetre.winfo_screenheight()
fenetre.maxsize(width=LARGEUR_ECRAN, height=HAUTEUR_ECRAN)
fenetre.minsize(width=500, height=800)

label = tk.Label(fenetre, text="Quarto", font=("Arial", 25), bg="black", fg="red")
label.pack(padx=200, pady=25)

frame_plateau = tk.Frame(fenetre)
frame_plateau.configure(bg="black")
frame_plateau.pack(expand=True)

frame_pieces = tk.Frame(fenetre, bg="black")
frame_pieces.pack(padx=50, pady=50)



def creation_plateau():
    image_pil = Image.open(IMAGE_PLATEAU)
    for row in range(4):
        for column in range(4):
            image_tk = ImageTk.PhotoImage(image_pil)
            label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
            label_image.image = image_tk
            label_image.grid(row=row, column=column, padx=20, pady=20)
            label_image.bind("<Button>", lambda event, row=row, column=column: deposer_une_piece(row, column))


def creation_pieces():
    pieces = {}
    i = 0
    for chemin in CHEMINS_IMAGES:
        image_pil = Image.open(chemin)
        image_tk = ImageTk.PhotoImage(image_pil)
        label_image = tk.Label(frame_pieces, image=image_tk, borderwidth=0, highlightthickness=0)
        label_image.image = image_tk
        label_image.grid(row=i//8, column=i%8, padx=5, pady=0)
        label_image.bind("<Button>",  lambda event, chemin=chemin: selectionner_une_piece(chemin))
        pieces[chemin] = label_image
        i += 1
    return pieces


"""
# Création d'un frame pour les images
frame_plateau = tk.Frame(fenetre)
frame_plateau.configure(bg="black")
frame_plateau.pack(expand=True)

IMAGE_PLATEAU = "images/p-1.jpg"
max_columns = 4 
for i in range(16):
    image_pil = Image.open(IMAGE_PLATEAU)
    image_tk = ImageTk.PhotoImage(image_pil)
    label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
    label_image.image = image_tk
    row = i // max_columns
    column = i % max_columns 
    label_image.grid(row=row, column=column, padx=20, pady=20)
    label_image.bind("<Button>", lambda event, row=row, column=column: deposer_une_piece(row, column))

frame_pieces = tk.Frame(fenetre, bg="black")
frame_pieces.pack(padx=50, pady=50)


pieces = {}

# Charger et afficher chaque image
max_columns = 8  # Nombre maximal de colonnes
for i, chemin in enumerate(CHEMINS_IMAGES):
    # Charger l'image avec PIL
    image_pil = Image.open(chemin)

    # Convertir l'image pour l'afficher avec Tkinter
    image_tk = ImageTk.PhotoImage(image_pil)

    # Créer un label pour afficher l'image
    label_image = tk.Label(frame_pieces, image=image_tk, borderwidth=0, highlightthickness=0)
    
    label_image.image = image_tk  # Garder une référence à l'image pour éviter sa suppression
    # Placer le label dans la grille

    row = i // max_columns  # Ligne de la grille
    column = i % max_columns  # Colonne de la grille
    label_image.grid(row=row, column=column, padx=5, pady=0)

    label_image.bind("<Button>",  lambda event, chemin=chemin: selectionner_une_piece(chemin))
    pieces[chemin] = label_image
"""
creation_plateau()
pieces = creation_pieces()

# Démarrage de la boucle principale de Tkinter
fenetre.mainloop()


# TODO : Affichage fin de partie
# TODO : Initialisation début de partie
# TODO : 2 ème arbre pour choix des pièces

def fin_partie():
    pass

