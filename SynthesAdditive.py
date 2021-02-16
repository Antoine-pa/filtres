from tkinter import *

fenetre=Tk() # la fenêtre principale
fenetre.title("ISN d'Estournelles de Constant : synthèse additive des couleurs.")
fenetre.geometry("800x650") # Sa taille

f1=Frame(fenetre,height=100) # Un cadre dans la fenêtre principale
f1.pack(side=TOP) # Position du cadre dans la fenêtre.

can1=Canvas(f1,width=50,height=50,bg='black') # Un Canvas dans le panneau 1 : pour illustrer la couleur obtenue par mélange des 3
can1.grid(row=1, column=1) # En seconde ligne. En première: curseurs...


f2=Frame(fenetre,height=700) # cadre 2 pour contenir cadre de mélange des couleurs.
f2.pack(side=TOP)

can2=Canvas(f2,width=250,height=200,bg='black') # Un canvas qui contiendra les carrés.
can2.grid(row=0)

can3=Canvas(f2,width=700,height=281,bg='grey') # Un canvas qui contiendra une image d'explication de la synthèse.
imageExplication=PhotoImage(file='explication.png')
can3.create_image(350,140,image=imageExplication)
can3.grid(row=1)


rouge,vert,bleu=255,255,255

rectangle1=can2.create_rectangle(30,20,130,120,fill='red',width=0)
rectangle2=can2.create_rectangle(100,10,200,110,fill='green',width=0)
rectangle3=can2.create_rectangle(75,75,175,175,fill='blue',width=0)

couleur4 = '#%02x%02x%02x' % (rouge, vert, 0)
rectangle4=can2.create_rectangle(100,20,130,75,fill=couleur4,width=0)

couleur5 = '#%02x%02x%02x' % (rouge, 0, bleu)
rectangle5=can2.create_rectangle(75,75,100,120,fill=couleur5,width=0)
rectangle5bis=can2.create_rectangle(100,110,130,120,fill=couleur5,width=0)

couleur6 = '#%02x%02x%02x' % (rouge, vert, bleu)
rectangle6=can2.create_rectangle(100,75,130,110,fill=couleur6,width=0)

couleur7 = '#%02x%02x%02x' % (0, vert, bleu)
rectangle7=can2.create_rectangle(130,75,175,110,fill=couleur7,width=0)


def affichage1(x):
    global rouge,vert,bleu
    rouge=int(x)
    couleur1 = '#%02x%02x%02x' % (rouge, vert, bleu)
    couleur2='#%02x%02x%02x' % (rouge, 0, 0)
    couleur4 = '#%02x%02x%02x' % (rouge, vert, 0)
    couleur5 = '#%02x%02x%02x' % (rouge, 0, bleu)

    can1.configure(bg=couleur1) # La couleur mélange des 3
    can2.itemconfigure(rectangle1,fill=couleur2) # Le carré rouge
    curseur1.configure(troughcolor=couleur2) # La couleur du curseur

    can2.itemconfigure(rectangle4,fill=couleur4)
    can2.itemconfigure(rectangle5,fill=couleur5)
    can2.itemconfigure(rectangle5bis,fill=couleur5)
    can2.itemconfigure(rectangle6,fill=couleur1)

def affichage2(x):
    global rouge,vert,bleu
    vert=int(x)
    couleur1= '#%02x%02x%02x' % (rouge, vert, bleu)
    couleur2='#%02x%02x%02x' % (0, vert, 0)
    couleur4 = '#%02x%02x%02x' % (rouge, vert, 0)
    couleur7 = '#%02x%02x%02x' % (0, vert, bleu)

    can1.configure(bg=couleur1)
    can2.itemconfigure(rectangle2,fill=couleur2)
    curseur2.configure(troughcolor=couleur2) # La couleur du curseur

    can2.itemconfigure(rectangle4,fill=couleur4)
    can2.itemconfigure(rectangle6,fill=couleur1)
    can2.itemconfigure(rectangle7,fill=couleur7)


def affichage3(x):
    global rouge,vert,bleu
    bleu=int(x)

    couleur1= '#%02x%02x%02x' % (rouge, vert, bleu)
    couleur2='#%02x%02x%02x' % (0, 0, bleu)
    couleur5 = '#%02x%02x%02x' % (rouge, 0, bleu)
    couleur7 = '#%02x%02x%02x' % (0, vert, bleu)

    can1.configure(bg=couleur1)
    can2.itemconfigure(rectangle3,fill=couleur2)
    curseur3.configure(troughcolor=couleur2) # La couleur du curseur

    can2.itemconfigure(rectangle5,fill=couleur5)
    can2.itemconfigure(rectangle5bis,fill=couleur5)
    can2.itemconfigure(rectangle6,fill=couleur1)
    can2.itemconfigure(rectangle7,fill=couleur7)



curseur1=Scale(f1,length=150, orient=HORIZONTAL, label='Rouge', troughcolor='red',sliderlength=10, showvalue=1, from_=0, to=255, tickinterval=50, command=affichage1)
curseur1.grid(row=0, column=0, sticky=W)
curseur1.set(255)

curseur2=Scale(f1,length=150, orient=HORIZONTAL, label='Vert', troughcolor='green',sliderlength=10, showvalue=1, from_=0, to=255, tickinterval=50, command=affichage2)
curseur2.grid(row=0, column=1, sticky=W)
curseur2.set(255)

curseur3=Scale(f1,length=150, orient=HORIZONTAL, label='Bleu', troughcolor='blue',sliderlength=10, showvalue=1, from_=0, to=255, tickinterval=50, command=affichage3)
curseur3.grid(row=0, column=2, sticky=W)
curseur3.set(255)


fenetre.mainloop()







