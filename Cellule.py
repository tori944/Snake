from init import *
from random import *

class Cellule :
    global NbColumn, NbRow, vitesse, vit, running, startInit

    listeCellules = []

    listeCellulesSnake = []     # Id des celules formant le serpent

    direction = 3               # 0 : haut / 1 : bas / 2 : gauche / 3 : droite

    length = 1                  # taille du serpent en cellule

    start = 0   # 0 : en attente de commencer / 1 : en jeu / 2 : perdu, fin

    PremirerPomme = None
    PremierSerpent = None

    
    def __init__(self, coA, coB, row, column):
        Cellule.listeCellules.append(self)

        self.id = Cellule.listeCellules.index(self)

        self.row = row
        self.column = column

        self.coA = coA
        self.coB = coB

        self.etat = 0  # 0 -> mort / 1 -> serpent / 2 -> pomme

        self.rec = canvas.create_rectangle(coA+1, coB+1, coA+sizeCel+1, coB+sizeCel+1, fill='black', outline="gray")

        if self.row == (NbRow // 2) and self.column == (NbColumn // 2):  # première cellule du serpent au centre du canvas
            self.set_etat(1) 
            self.listeCellulesSnake.append(self.id)
            Cellule.idPremierSerpent = self
            

        if self.row == (NbRow // 2) and self.column == (NbColumn // 2) + 10:  # première pomme
            self.set_etat(2)
            Cellule.idPremirerPomme = self

        canvas.focus_set()
        canvas.bind("<Key>", Cellule.clavier)

#############
#### get ####

    def get_id (self):
        return self.id 
    
    # def get_row (self):
    #     return self.row
    
    def get_column (self):
        return self.column
    
    def get_etat (self):
        return self.etat
    
    def get_direction():
        return Cellule.direction
    
    def get_start():
        return Cellule.start

    def get_length():
        return Cellule.length
    

#### set ####

    def set_etat (self, val):
        self.etat = val
        if val == 1 :# serpent
            canvas.itemconfig(self.rec, fill="green", outline="")
        elif val == 0 : # rien
            canvas.itemconfig(self.rec, fill="black", outline="gray")
        elif val == 2: # pomme
            canvas.itemconfig(self.rec, fill="red", outline="")

    def set_length():
        Cellule.length += 1
    
    def set_direction(val):
        Cellule.direction = val
    
    def set_start(val):
        Cellule.start = val

#############

            
    def end ():
        global running, startInit 
        # print("perdu")
        canvas.create_text(400, 250, text="Perdu !", fill="pink", font=("", 70), tags="message")
        # startInit = 2
        Cellule.set_start(2)
        # running = False
    
    def poser_pomme ():
        cel = choice(Cellule.listeCellules)
        if cel in Cellule.listeCellulesSnake:
            Cellule.poser_pomme()
        cel.set_etat(2)    

    def avance ():
        global NbColumn

        val = Cellule.get_direction()

        idVoisineDirecte = [-NbColumn, NbColumn, -1, 1]  # haut / bas / gauche / droite

        # prendre l'id de la celulle tête du Serpent
        idCel = Cellule.listeCellulesSnake[-1]
        tete = Cellule.listeCellules[idCel] 

        if (tete.get_column() == 0 and Cellule.direction == 2) or (tete.get_column() == NbColumn-1 and Cellule.direction == 3): 
            # si le serpent ce cogne à gauche ou a droite
            Cellule.end()
            return

        # id de la voisine qui va devenir tête est compris entre 0 et la taille de la liste de cellule, donc ne dépasse ni en haut, ni en bas
        if 0 <= (idCel+idVoisineDirecte[val]) <= len(Cellule.listeCellules):

            cel = Cellule.listeCellules[idCel+idVoisineDirecte[val]]  # Cellule suivante va devenir tête

            # if cel.get_column() == 0:
            #     Cellule.end()
            #     return
            
            if cel.get_etat() == 2 :#si c'est une pomme
                Cellule.set_length() #ajouter 1 à la taille
                Cellule.poser_pomme()
                taille.set(Cellule.get_length())

            Cellule.listeCellulesSnake.append(cel.get_id())
            cel.set_etat(1)
            
            
            if len(Cellule.listeCellulesSnake) > Cellule.get_length(): #Cellule.get_length(): # si on a atteint la taille du serpent (de 4)
                cel = Cellule.listeCellules[Cellule.listeCellulesSnake[0]]
                cel.set_etat(0)
                del Cellule.listeCellulesSnake[0]
            
        else: 
            Cellule.end()


    def clavier(event):
        touche = event.keysym

        if Cellule.get_start() == 0:    # si on clic pour la première fois
            Cellule.set_start(1)

        if touche == "Down":
            Cellule.set_direction(1)
            
        elif touche == "Right":
            Cellule.set_direction(3)

        elif touche == "Left":
            Cellule.set_direction(2)
            
        elif touche == "Up":
            Cellule.set_direction(0)
