from PIL import ImageTk, Image
import tkinter as tk

class Fenetre:
    IMAGE_PLATEAU = "images/p-1.jpg"
    CHEMINS_IMAGES = ["images/p0.jpg", "images/p1.jpg", "images/p2.jpg", "images/p3.jpg", "images/p4.jpg", "images/p5.jpg", "images/p6.jpg", "images/p7.jpg", 
                      "images/p8.jpg", "images/p9.jpg", "images/p10.jpg", "images/p11.jpg", "images/p12.jpg", "images/p13.jpg", "images/p14.jpg", "images/p15.jpg"]
    IMAGES_PIECES = {"images/p0.jpg": {"grand" : 1, "plein" : 1, "clair" : 1, "carre" : 1}, 
                     "images/p1.jpg": {"grand" : 1, "plein" : 0, "clair" : 1, "carre" : 1}, 
                     "images/p2.jpg": {"grand" : 0, "plein" : 1, "clair" : 1, "carre" : 1}, 
                     "images/p3.jpg": {"grand" : 0, "plein" : 0, "clair" : 1, "carre" : 1}, 
                     "images/p4.jpg": {"grand" : 1, "plein" : 1, "clair" : 1, "carre" : 0}, 
                     "images/p5.jpg": {"grand" : 1, "plein" : 0, "clair" : 1, "carre" : 0}, 
                     "images/p6.jpg": {"grand" : 0, "plein" : 1, "clair" : 1, "carre" : 0}, 
                     "images/p7.jpg": {"grand" : 0, "plein" : 0, "clair" : 1, "carre" : 0}, 
                     "images/p8.jpg": {"grand" : 1, "plein" : 1, "clair" : 0, "carre" : 1}, 
                     "images/p9.jpg": {"grand" : 1, "plein" : 0, "clair" : 0, "carre" : 1}, 
                     "images/p10.jpg": {"grand" : 0, "plein" : 1, "clair" : 0, "carre" : 1}, 
                     "images/p11.jpg": {"grand" : 0, "plein" : 0, "clair" : 0, "carre" : 1}, 
                     "images/p12.jpg": {"grand" : 1, "plein" : 1, "clair" : 0, "carre" : 0}, 
                     "images/p13.jpg": {"grand" : 1, "plein" : 0, "clair" : 0, "carre" : 0}, 
                     "images/p14.jpg": {"grand" : 0, "plein" : 1, "clair" : 0, "carre" : 0}, 
                     "images/p15.jpg": {"grand" : 0, "plein" : 0, "clair" : 0, "carre" : 0}
                    }
    image_selectionnee = ""
    pieces = {}

    def __init__(self, root):
        self.root = root
        self.root.title("Quarto")
        self.root.geometry("400x300")
        self.root.configure(bg="black")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.piece_choisie = None
        LARGEUR_ECRAN = self.root.winfo_screenwidth()
        HAUTEUR_ECRAN = self.root.winfo_screenheight()
        self.root.geometry(f"{LARGEUR_ECRAN}x{HAUTEUR_ECRAN}")
        label_texte = tk.Label(text="Quarto", font=("Helvetica", 20, "bold"), bg="black", fg="white")
        label_texte.place(x=700, y=100)
        
        # Initialize images to avoid garbage collection
        self.images_pieces = []
        self.image_plateau = None
        self.piece_selected_callback = None  # Initialize callback to None

    def get_piece_choisie(self):
        return self.piece_choisie

    def set_piece_selected_callback(self, callback):
        self.piece_selected_callback = callback

    def deposer_une_piece(self, row, column, frame_plateau):
        if Fenetre.image_selectionnee != "":
            image_pil = Image.open(Fenetre.image_selectionnee)
            image_tk = ImageTk.PhotoImage(image_pil)
            label_image = tk.Label(frame_plateau, image=image_tk, borderwidth=0, highlightthickness=0)
            label_image.image = image_tk 
            label_image.grid(row=row, column=column, padx=20, pady=20)
            Fenetre.image_selectionnee = ""
            
            self.affiche_piece("sélecionnez une images", Fenetre.IMAGE_PLATEAU)

    def creer_plateau(self):
        frame_plateau = tk.Frame(bg="black")
        frame_plateau.place(x=200, y=200)

        image_pil = Image.open(Fenetre.IMAGE_PLATEAU)
        self.image_plateau = ImageTk.PhotoImage(image_pil)  # Store the image reference

        for row in range(4):
            for column in range(4):
                label_image = tk.Label(frame_plateau, image=self.image_plateau, borderwidth=0, highlightthickness=0)
                label_image.grid(row=row, column=column, padx=30, pady=20)
                label_image.bind("<Button>", lambda event, row=row, column=column: self.deposer_une_piece(row, column, frame_plateau))
        return frame_plateau
    
    def creation_pieces(self):
        frame_pieces = tk.Frame(bg="black")
        frame_pieces.place(x=800, y=400)

        self.pieces = {}
        for i, chemin in enumerate(Fenetre.CHEMINS_IMAGES):
            image_pil = Image.open(chemin)
            image_tk = ImageTk.PhotoImage(image_pil)
            self.images_pieces.append(image_tk)  # Store the image reference
            label_image = tk.Label(frame_pieces, image=image_tk, borderwidth=0, highlightthickness=0)
            label_image.grid(row=i // 8, column=i % 8, padx=10, pady=10)
            label_image.bind("<Button-1>", lambda event, chemin=chemin, r=i//8, c=i%8: self.selectionner("Image selectionée", chemin, frame_pieces, r, c))
            self.pieces[chemin] = label_image
        return frame_pieces
      
    def affiche_piece(self, texte, chemin):
        Fenetre.image_selectionnee = chemin
        label_texte = tk.Label(text=texte, font=("Arial", 15), bg="black", fg="white", compound='left')
        label_texte.place(x=900, y=300)
        
        image = Image.open(chemin)
        photo = ImageTk.PhotoImage(image)
        self.image_for_button = photo  # Store the image reference

        button = tk.Label(image=photo, borderwidth=0, highlightthickness=0)
        button.place(x=1200, y=270)

    def selectionner(self, texte, chemin, frame_pieces, row, column):
        self.affiche_piece(texte, chemin)
        self.piece_choisie = Fenetre.IMAGES_PIECES[chemin]
        image_pil = Image.open("images/vide.jpg")
        image_tk = ImageTk.PhotoImage(image_pil)
        self.images_pieces.append(image_tk)  # Store the image reference
        label_image = tk.Label(frame_pieces, image=image_tk, borderwidth=0, highlightthickness=0)
        label_image.grid(row=row, column=column, padx=10, pady=10)

        # Appeler le callback lorsque la pièce est sélectionnée
        if self.piece_selected_callback:
            self.piece_selected_callback(self.piece_choisie)
