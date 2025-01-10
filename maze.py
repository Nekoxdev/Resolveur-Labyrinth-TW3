class Laby:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        # Grille remplie de murs
        self.labyrinthe = [['#' for _ in range(largeur)] for _ in range(hauteur)]

  def afficher(self):
    # Affiche le laby
    for ligne in self.labyrinthe:
      print(''.join(ligne))

largeur = 31
hauteur = 41
# (Parce que ça fait 3141 : 3,141)
labyrinthe = Laby(largeur, hauteur)

labyrinth.afficher()
