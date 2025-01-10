class Laby:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur #largeur du laby
        self.hauteur = hauteur #hauteur du laby
        # Grille remplie de murs : sous forme de matrice
        self.labyrinthe = [['#' for _ in range(largeur)] for _ in range(hauteur)]

    def generer(self): #Pour faire le laby
        #Placer le départ (D)
        depart_x = random.randrange(1, self.largeur, 2) # 2 pour s'assurer qu'il ne tombe pas sur un bord
        depart_y = random.randrange(1, self.hauteur, 2) # 2 pour s'assurer qu'il ne tombe pas sur un bord
        self.labyrinthe[depart_x][depart_y] #Place le départ (D) sur le laby
    
    def afficher(self):
        # Affiche le laby
        for ligne in self.labyrinthe:
          print(''.join(ligne))

largeur = 31
hauteur = 41
# (Parce que ça fait 3141 : 3,141)
labyrinthe = Laby(largeur, hauteur)

labyrinth.generer()
labyrinth.afficher()
