import tkinter as tk
from PIL import ImageTk, Image

image_selectionnee = ""

def selectioner_une_piece(image):
    global image_selectionnee
    image_selectionnee = image

def deposer_une_piece(row, column):
    global image_selectionnee
    if image_selectionnee != "":
        image_pil = Image.open(image_selectionnee)
        image_tk = ImageTk.PhotoImage(image_pil)
        label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
        label_image.image = image_tk 
        label_image.grid(row=row, column=column, padx=20, pady=20)
        image_selectionnee = ""
      
fenetre = tk.Tk()
fenetre.title("Quarto")
fenetre.configure(bg="black")
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()
fenetre.minsize(width= largeur_ecran, height= hauteur_ecran)

label = tk.Label(fenetre, text="Quarto", font=("Arial", 25), bg="black", fg="red")
label.pack(padx=200, pady=50)

# Création d'un frame pour les images
frame_plateau = tk.Frame(fenetre)
frame_plateau.configure(bg="black")
frame_plateau.pack(fill=tk.BOTH, expand=True)

image_plateau = "images/p-1.jpg"
max_columns = 4 
for i in range(16):
    image_pil = Image.open(image_plateau)
    image_tk = ImageTk.PhotoImage(image_pil)
    label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
    label_image.image = image_tk 
    row = i // max_columns  
    column = i % max_columns 
    label_image.grid(row=row, column=column, padx=30, pady=30)
    label_image.bind("<Button>", lambda event, row=row, column=column: deposer_une_piece(row, column))

frame_pieces = tk.Frame(fenetre)
frame_pieces.configure(bg="black")
frame_pieces.pack(padx=150, pady=50)

chemins_images = ["images/p0.jpg", "images/p1.jpg", "images/p2.jpg", "images/p3.jpg", "images/p4.jpg", "images/p5.jpg", "images/p6.jpg", "images/p7.jpg", 
                  "images/p8.jpg", "images/p9.jpg", "images/p10.jpg", "images/p11.jpg", "images/p12.jpg", "images/p13.jpg", "images/p14.jpg", "images/p15.jpg"]

# Charger et afficher chaque image
max_columns = 8  # Nombre maximal de colonnes
for i, chemin in enumerate(chemins_images):
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

    label_image.bind("<Button>",  lambda event, chemin=chemin: selectioner_une_piece(chemin))

# Démarrage de la boucle principale de Tkinter
fenetre.mainloop()