from Cellule import *

for i in range (NbRow):
    for j in range (NbColumn):
        Cellule(j*sizeCel, i*sizeCel, i, j)
    

def GO ():
    Cellule.avence()
    root.after(vitesse.get(), GO)

def onCommence ():
    if Cellule.get_start() == 1:
        GO()
    else:
        root.after(50, onCommence)

onCommence()

    

frame = Frame(root)
frame.grid(sticky=EW, padx=10, pady=10)

frame.columnconfigure([0, 1, 2], weight=1)

frame2 = Frame(frame)
frame2.grid(column=0, row=0, pady=10)

frame3 = Frame(frame)
frame3.grid(column=1, row=0, pady=10)

btn = Button(frame, text="un bouton qui ne sert à rien", font=("",15))
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