from init import *
from random import *

class Cellule :
    global NbColumn, NbRow, vitesse, vit

    listeCellules = []

    listeCellulesSnake = [] # Id des celules formant le serpent

    direction = 3

    length = 1

    start = 0

    #pomme = None  # Id de la pomme ?

    
    def __init__(self, coA, coB, row, column):
        Cellule.listeCellules.append(self)

        self.id = Cellule.listeCellules.index(self)

        self.row = row
        self.column = column

        self.coA = coA
        self.coB = coB


        self.etat = 0  # 0 -> mort / 1 -> serpent / 2 -> pomme

        self.rec = canvas.create_rectangle(coA+1, coB+1, coA+sizeCel+1, coB+sizeCel+1, fill='black', outline="gray")

        if self.row == (NbRow // 2) and self.column == (NbColumn // 2):
            #self.etat = 1
            self.set_etat(1)
            self.listeCellulesSnake.append(self.id)
            #canvas.itemconfig(self.rec, fill="green")
        else:
            self.etat = 0

        if self.row == (NbRow // 2) and self.column == (NbColumn // 2) + 10:
            self.set_etat(2)

        #canvas.tag_bind(self.rec, "<Button-1>", self.clicG)
        # canvas.tag_bind(self.rec, "<Button-3>", self.clicD)
        canvas.focus_set()
        canvas.bind("<Key>", Cellule.clavier)


    def get_id (self):
        return self.id 
    
    def get_row (self):
        return self.row
    
    def get_column (self):
        return self.column
    
    def get_etat (self):
        return self.etat
    
    def get_direction():
        return Cellule.direction
    
    def set_direction(val):
        Cellule.direction = val
    
    def set_etat (self, val):
        self.etat = val
        if val == 1 :
            canvas.itemconfig(self.rec, fill="green", outline="")
        elif val == 0 :
            canvas.itemconfig(self.rec, fill="black", outline="gray")
        elif val == 2: # deviens pomme
            canvas.itemconfig(self.rec, fill="red", outline="")

    
    def get_length():
        return Cellule.length

    def set_length():
        Cellule.length += 1
    
    def get_start():
        return Cellule.start
    
    def set_start(val):
        Cellule.start = val
    
    # def set_vitess ():
    #     global vit
    #     if vitesse.get() > 20:
    #         if Cellule.get_length() % 5 == 0:
    #             vit -= 10
    #             vitesse.set(vit)

    # def set_vitess():
    #     global vit
    #     # if vitesse.get() > 20:
    #         # if (Cellule.get_length() % 5) == 0:

    #     vit -= 10
    #     vitesse.set(vit)
            
    def end ():
        print("perdu")
        canvas.create_text(400, 250, text="Perdu !", fill="pink", font=("", 70), tags="LesIndices")
    
    def poser_pomme ():
        cel = choice(Cellule.listeCellules)
        if cel in Cellule.listeCellulesSnake:
            Cellule.poser_pomme()
        cel.set_etat(2)    

    def avence ():

        val = Cellule.get_direction()
        # dire à la voisine du haut
        # -NbColum

        idVoisineDirecte = [-NbColumn, NbColumn, -1, 1]  # haut / bas / gauche / droite

        # prendre l'id de la celulle tête du Serpent
        idCel = Cellule.listeCellulesSnake[-1]

        # id de la voisine qui va devenir tête est compris entre 0 et la taille de la liste de cellule, donc ne déâsse ni en heut, ni en bas
        if 0 <= (idCel+idVoisineDirecte[val]) <= len(Cellule.listeCellules):

            cel = Cellule.listeCellules[idCel+idVoisineDirecte[val]]  # Cellule suivante devient tête
            
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

            # if (Cellule.get_length() % 5) == 0:
            #     if vitesse.get() > 20:
                
            #         Cellule.set_vitess()
            
        else:
            Cellule.end()


    def clavier(event):
        global start2, start3
        touche = event.keysym
        
        # print("avant if", start2.get())

        if Cellule.get_start() == 0:
            Cellule.set_start(1)

        if touche == "Down":
            Cellule.set_direction(1)
            
        elif touche == "Right":
            Cellule.set_direction(3)

        elif touche == "Left":
            Cellule.set_direction(2)    
            
        elif touche == "Up":
            Cellule.set_direction(0)




  