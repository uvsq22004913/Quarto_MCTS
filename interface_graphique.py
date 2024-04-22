import mcts
import tkinter as tk
from PIL import ImageTk, Image
import re

IMAGE_PLATEAU = "images/p-1.jpg"
CHEMINS_IMAGES = ["images/p0.jpg", "images/p1.jpg", "images/p2.jpg", "images/p3.jpg", "images/p4.jpg", "images/p5.jpg", "images/p6.jpg", "images/p7.jpg", 
                  "images/p8.jpg", "images/p9.jpg", "images/p10.jpg", "images/p11.jpg", "images/p12.jpg", "images/p13.jpg", "images/p14.jpg", "images/p15.jpg"]
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


image_selectionnee = ""

def selectionner_une_piece(image):
    global image_selectionnee
    if image_selectionnee == "":
        image_selectionnee = image
        pieces[image].destroy()
        mcts.changement_joueur()


def deposer_une_piece(row, column):
    global image_selectionnee
    if image_selectionnee != "":
        image_pil = Image.open(image_selectionnee)
        image_tk = ImageTk.PhotoImage(image_pil)
        label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
        label_image.image = image_tk 
        label_image.grid(row=row, column=column, padx=20, pady=20)
        num_piece = int(re.findall(r"\d+", image_selectionnee)[0])
        image_selectionnee = ""
        piece = LISTES_PIECES[num_piece]
        #mcts.place_piece(row, column, piece)
        mcts.plateau[row][column] = piece
        #print(mcts.plateau)
        if mcts.quarto(mcts.plateau):
            #fin_partie()
            print("fin partie")
        mcts.changement_joueur()



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


creation_plateau()
pieces = creation_pieces()

# Démarrage de la boucle principale de Tkinter
fenetre.mainloop()

def fin_partie():
    pass

