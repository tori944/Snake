from tkinter import *

NbRow = 25          # nombre de colones
NbColumn = 40       # nombre de ligne

sizeCel = 20        # taille de la cellule

root = Tk()
root.title("Snake")

taille = IntVar()
taille.set(1)


# vitesse en fonction du nombre de pomme avalé ou du temps passé ?

vit = 150

vitesse = IntVar()
vitesse.set(vit)

canvas = Canvas(root, width=800, height=500, bg="light yellow", highlightthickness=2, highlightbackground="black", bd=0)
canvas.grid(padx=25, pady=25)

