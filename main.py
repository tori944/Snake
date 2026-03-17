from Cellule import *

for i in range (NbRow):
    for j in range (NbColumn):
        Cellule(j*sizeCel, i*sizeCel, i, j)

varChange = 0 # var qui augmente lorqusque qu'on change la vitesse

def GO ():
    global vit, varChange

    if Cellule.get_start() == 1:
        Cellule.avance()

        if vit > 40 :
            if Cellule.get_length() % 5 == 0 and varChange != Cellule.get_length():
                vit -= 5
                varChange += 5
                vitesse.set(vit)

        root.after(vitesse.get(), GO)

    elif Cellule.get_start() == 2:
        return

def onCommence ():

    if Cellule.get_start() == 1:
        GO()
    else:
        root.after(50, onCommence)

def rejouer (): 
    global taille, vit, vitesse, varChange

    if Cellule.get_start() == 0:
        return
    else:
        Cellule.direction = 3
        Cellule.length = 1
        Cellule.start = 0

        # taille.set(Cellule.get_length())

        for cel in Cellule.listeCellules:
            if cel.get_etat() != 0:
                cel.set_etat(0)

        celS = Cellule.idPremierSerpent
        celS.set_etat(1)

        Cellule.listeCellulesSnake = []
        Cellule.listeCellulesSnake.append(celS.get_id())

        celP = Cellule.idPremirerPomme
        celP.set_etat(2)

        taille.set(Cellule.get_length()) # = 1

        canvas.delete("message")

        vitesse.set(100)
        vit = 100
        varChange = 0



    onCommence()


onCommence()

frame = Frame(root)
frame.grid(sticky=EW, padx=10, pady=10)

frame.columnconfigure([0, 1, 2], weight=1)

frame2 = Frame(frame)
frame2.grid(column=0, row=0, pady=10)

frame3 = Frame(frame)
frame3.grid(column=1, row=0, pady=10)

btn = Button(frame, text="Rejouer", font=("",15), command=rejouer)
btn.grid(column=2, row=0, pady=10)

LabelAa = Label(frame2, text="Taille :", font=("",15))
LabelAa.grid()
labelAb = Label(frame2, textvariable=taille, font=("",15))
labelAb. grid()

labelA = Label(frame3, text="Vitesse : ", font=("",15))
labelA. grid()
labelAb = Label(frame3, textvariable=vitesse, font=("",15))
labelAb. grid()


root.mainloop()