import mcts
import tkinter as tk
from PIL import ImageTk, Image
import re

"""
IMAGE_PLATEAU = "images/p-1.jpg"
CHEMINS_IMAGES = ["images/p0.jpg", "images/p1.jpg", "images/p2.jpg", "images/p3.jpg", "images/p4.jpg", "images/p5.jpg", "images/p6.jpg", "images/p7.jpg", 
                  "images/p8.jpg", "images/p9.jpg", "images/p10.jpg", "images/p11.jpg", "images/p12.jpg", "images/p13.jpg", "images/p14.jpg", "images/p15.jpg"]

image_selectionnee = ""

def selectionner_une_piece(image):
    global image_selectionnee
    if image_selectionnee == "":
        image_selectionnee = image
        pieces[image].destroy()
        pieces.pop(image)
        piece_actuel(image)
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
        piece = mcts.LISTES_PIECES[num_piece]
        piece_actuel()
        mcts.plateau[row][column] = piece
        if mcts.quarto(mcts.plateau):
            fin_partie()


def creation_plateau():
    frame_plateau = tk.Frame(fenetre, bg="black")
    frame_plateau.grid(row=1, pady=50)
    image_pil = Image.open(IMAGE_PLATEAU)
    for row in range(4):
        for column in range(4):
            image_tk = ImageTk.PhotoImage(image_pil)
            label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
            label_image.image = image_tk
            label_image.grid(row=row, column=column, padx=20, pady=20)
            label_image.bind("<Button>", lambda event, row=row, column=column: deposer_une_piece(row, column))
    return frame_plateau

def creation_pieces():
    frame_pieces = tk.Frame(fenetre, bg="black")
    frame_pieces.grid(row=3, pady=50)
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
    return frame_pieces, pieces


def piece_actuel(image=None):
    if image is not None:
        image_pil = Image.open(image)
        image_tk = ImageTk.PhotoImage(image_pil)
        text = 'A vous de poser cette pièce : ' if mcts.tour_joueur == 0 else "A moi de poser cette pièce : "
        label_actuel.config(text=text, image=image_tk)
        label_actuel.image = image_tk
    else:
        text = 'A vous de choisir une pièce.' if mcts.tour_joueur == 0 else "A moi de choisir une pièce."
        label_actuel.config(text=text, image=label_actuel.image_vide)


def fin_partie():
    for label in pieces.values():
        label.unbind("<Button>")
    text = "Quarto! Vous avez gagné!" if mcts.tour_joueur == 0 else "Quarto! J'ai gagné!"
    label_actuel.config(text=text, image='')
    boutton = tk.Button(frame_tour, text='Rejouer ?', command= lambda: nouvelle_partie(boutton))
    boutton.grid(row=2, column=2)


def nouvelle_partie(boutton):
    # Changer les frames global et reinnitialiser les pieces
    global frame_pieces, frame_plateau, pieces
    mcts.nouvelle_partie()
    boutton.destroy()
    frame_pieces.destroy()
    frame_plateau.destroy()
    frame_plateau = creation_plateau()
    frame_pieces, pieces = creation_pieces()
    label_actuel.config(text="A vous de choisir une pièce.", image=label_actuel.image_vide)



fenetre = tk.Tk()
fenetre.title("Quarto")
fenetre.configure(bg="black")
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_columnconfigure(0, weight=1)

LARGEUR_ECRAN = fenetre.winfo_screenwidth()
HAUTEUR_ECRAN = fenetre.winfo_screenheight()
fenetre.maxsize(width=LARGEUR_ECRAN, height=HAUTEUR_ECRAN)
fenetre.minsize(width=550, height=800)

label = tk.Label(fenetre, text="Quarto", font=("Arial", 25), bg="black", fg="red")
label.grid(row=0)

case_vide = Image.open("images/vide.jpg")
case_vide = ImageTk.PhotoImage(case_vide)
frame_tour = tk.Frame(fenetre, bg="black")
frame_tour.grid(row=2)
label_actuel = tk.Label(frame_tour, text="A vous de choisir une pièce.", font=("Arial", 25), bg="black", fg="white", compound='right', image=case_vide)
label_actuel.grid(row=2)
label_actuel.image_vide = case_vide


frame_plateau = creation_plateau()
frame_pieces, pieces = creation_pieces()

# Démarrage de la boucle principale de Tkinter
fenetre.mainloop()
"""

################################################################

IMAGE_PLATEAU = "images/p-1.jpg"
CHEMINS_IMAGES = ["images/p0.jpg", "images/p1.jpg", "images/p2.jpg", "images/p3.jpg", "images/p4.jpg", "images/p5.jpg", "images/p6.jpg", "images/p7.jpg", 
                  "images/p8.jpg", "images/p9.jpg", "images/p10.jpg", "images/p11.jpg", "images/p12.jpg", "images/p13.jpg", "images/p14.jpg", "images/p15.jpg"]

image_selectionnee = ""
pieces = {}

def selectionner_une_piece(image):
    global image_selectionnee, pieces
    if image_selectionnee == "":
        image_selectionnee = image
        pieces[image].destroy()
        pieces.pop(image)
        piece_actuel(image)

def deposer_une_piece(row, column, frame_plateau):
    global image_selectionnee, pieces
    if image_selectionnee != "":
        image_pil = Image.open(image_selectionnee)
        image_tk = ImageTk.PhotoImage(image_pil)
        label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
        label_image.image = image_tk 
        label_image.grid(row=row, column=column, padx=20, pady=20)
        num_piece = int(re.findall(r"\d+", image_selectionnee)[0])
        image_selectionnee = ""
        piece = mcts.LISTES_PIECES[num_piece]
        piece_actuel()
        mcts.plateau[row][column] = piece
        if mcts.quarto(mcts.plateau):
            fin_partie()

def creation_plateau(fenetre):
    global mcts
    frame_plateau = tk.Frame(fenetre, bg="black")
    frame_plateau.grid(row=1, pady=50)
    image_pil = Image.open(IMAGE_PLATEAU)
    for row in range(4):
        for column in range(4):
            image_tk = ImageTk.PhotoImage(image_pil)
            label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
            label_image.image = image_tk
            label_image.grid(row=row, column=column, padx=20, pady=20)
            label_image.bind("<Button>", lambda event, row=row, column=column: deposer_une_piece(row, column, frame_plateau))
    return frame_plateau

def creation_pieces(fenetre):
    global pieces
    frame_pieces = tk.Frame(fenetre, bg="black")
    frame_pieces.grid(row=3, pady=50)
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
    return frame_pieces

def piece_actuel(image=None):
    global label_actuel
    if image is not None:
        image_pil = Image.open(image)
        image_tk = ImageTk.PhotoImage(image_pil)
        text = 'A vous de poser cette pièce : ' if mcts.tour_joueur == 0 else "A moi de poser cette pièce : "
        label_actuel.config(text=text, image=image_tk)
        label_actuel.image = image_tk
    else:
        text = 'A vous de choisir une pièce.' if mcts.tour_joueur == 0 else "A moi de choisir une pièce."
        label_actuel.config(text=text, image=label_actuel.image_vide)

def fin_partie():
    global pieces
    for label in pieces.values():
        label.unbind("<Button>")
    text = "Quarto! Vous avez gagné!" if mcts.tour_joueur == 0 else "Quarto! J'ai gagné!"
    label_actuel.config(text=text, image='')
    boutton = tk.Button(frame_tour, text='Rejouer ?', command= lambda: nouvelle_partie(boutton, frame_pieces, frame_plateau))
    boutton.grid(row=2, column=2)

def nouvelle_partie(boutton, frame_pieces, frame_plateau):
    global pieces
    mcts.nouvelle_partie()
    boutton.destroy()
    frame_pieces.destroy()
    frame_plateau.destroy()
    frame_plateau = creation_plateau(fenetre)
    frame_pieces = creation_pieces(fenetre)
    label_actuel.config(text="A vous de choisir une pièce.", image=label_actuel.image_vide)

if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Quarto")
    fenetre.configure(bg="black")
    fenetre.grid_rowconfigure(0, weight=1)
    fenetre.grid_columnconfigure(0, weight=1)

    LARGEUR_ECRAN = fenetre.winfo_screenwidth()
    HAUTEUR_ECRAN = fenetre.winfo_screenheight()
    fenetre.maxsize(width=LARGEUR_ECRAN, height=HAUTEUR_ECRAN)
    fenetre.minsize(width=550, height=800)

    label = tk.Label(fenetre, text="Quarto", font=("Arial", 25), bg="black", fg="red")
    label.grid(row=0)

    case_vide = Image.open("images/vide.jpg")
    case_vide = ImageTk.PhotoImage(case_vide)
    frame_tour = tk.Frame(fenetre, bg="black")
    frame_tour.grid(row=2)
    label_actuel = tk.Label(frame_tour, text="A vous de choisir une pièce.", font=("Arial", 25), bg="black", fg="white", compound='right', image=case_vide)
    label_actuel.grid(row=2)
    label_actuel.image_vide = case_vide

    frame_plateau = creation_plateau(fenetre)
    frame_pieces = creation_pieces(fenetre)

    fenetre.mainloop()
