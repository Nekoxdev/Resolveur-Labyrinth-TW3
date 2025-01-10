import random 

class Laby:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur #largeur du laby
        self.hauteur = hauteur #hauteur du laby
        # Grille remplie de murs : sous forme de matrice
        self.labyrinthe = [['#' for _ in range(largeur)] for _ in range(hauteur)]

    def generer(self): #Pour faire le laby
        #Placer le départ (D)
        depart_x = random.randrange(1, self.largeur - 1, 2) # 2 pour s'assurer qu'il ne tombe pas sur un bord
        depart_y = random.randrange(1, self.hauteur - 1, 2) # 2 pour s'assurer qu'il ne tombe pas sur un bord
        self.labyrinthe[depart_y][depart_x] = 'D' #Place le départ (D) sur le laby

        cellules_quil_reste_a_explorer_oui_je_sais_le_nom_de_la_liste_est_long_mais_je_fais_ce_que_je_veux = [(depart_x, depart_y)] # Initialisation (nan c pas une récurrence...) pour générer un laby faisable

        #Générer le laby
        while cellules_quil_reste_a_explorer_oui_je_sais_le_nom_de_la_liste_est_long_mais_je_fais_ce_que_je_veux:
            x, y = cellules_quil_reste_a_explorer_oui_je_sais_le_nom_de_la_liste_est_long_mais_je_fais_ce_que_je_veux[-1] #Prend la dernière cellule
            voisins = [] #On va lister les voisins de cette cellule dans... une liste
            #On défini les directions possibles pour les voisins (haut, bas, gauche, droite)
            directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.largeur - 1 and 1 <= ny < self.hauteur - 1 and self.labyrinthe[ny][nx] == '#': #Sécurité pour vérif qu'on est bien dans les bordures et que c bien un mur
                    voisins.append((nx, ny))

            if voisins: #Permet de vérifier s'il a des voisins murs, miskin s'il en a pas, lol
                nx, ny = random.choice(voisins) #C assez explicite je pense
                self.labyrinthe[ny][nx] = ' ' #Transformer le mur en passage
                self.labyrinthe[(y + ny) // 2][(x + nx) // 2] = ' ' #Lier la cellule avec la voisine choisit, bah oui on comptait de 2 en 2...
                cellules_quil_reste_a_explorer_oui_je_sais_le_nom_de_la_liste_est_long_mais_je_fais_ce_que_je_veux.append((nx, ny))
            else:
                cellules_quil_reste_a_explorer_oui_je_sais_le_nom_de_la_liste_est_long_mais_je_fais_ce_que_je_veux.pop() #enlève le dernier élément de la liste a explorer et refait si aucun voisin mur
        
        #Mettre une bordure 
        for i in range(self.largeur):
            self.labyrinthe[0][i] = '#'
            self.labyrinthe[self.hauteur - 1][i] = '#'
        for i in range(self.hauteur):
            self.labyrinthe[i][0] = '#'
            self.labyrinthe[i][self.largeur - 1] = '#'
    
        #Mettre l'arrivée (A)
        arrivee_x = random.randrange(1, self.largeur, 2)
        arrivee_y = random.randrange(1, self.hauteur, 2)
        while self.labyrinthe[arrivee_y][arrivee_x] != ' ': #Pour ne pas avoir l'arrivée sur un mur, ca serait balo. Mais plutôt sur un des chemins qu'on a crée plus tôt
            arrivee_x = random.randrange(1, self.largeur, 2)
            arrivee_y = random.randrange(1, self.hauteur, 2)
        self.labyrinthe[arrivee_y][arrivee_x] = 'A' #Marqué l'arrivée

    def afficher(self):
        # Affiche le laby
        for ligne in self.labyrinthe:
          print(''.join(ligne))

largeur = 31 #Mettre des nombres impaires
hauteur = 41 #Mettre des nombres impaires
# (Parce que ça fait 3141 : 3,141)
labyrinthe = Laby(largeur, hauteur)

labyrinthe.generer()
labyrinthe.afficher()
