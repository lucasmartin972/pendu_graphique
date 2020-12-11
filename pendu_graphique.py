# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:03:55 2020

@author: lucas
"""
#header
#Faire un pendu dans une version graphique
#11/12/2020
#Martin Lucas
#To Do: 
    
from tkinter import Tk, Label, Button , Frame
mw = Tk()
mw.title('Jeu du Pendu')
mw['bg']=''
mw.geometry('640x360+400+200')
labelHello = Label(mw, text = "petite partie de pendu?!!", fg = 'blue')
labelHello.pack()


FrameAffichageMot = Frame(mw,relief='groove')
FrameAffichageMot.pack(side='top',padx=10,pady=10)




def NouvellePartie():
    
    from fonctions import jeu
    fichier=open("mots.txt",'r')
    liste_mots=[]
    for ligne in fichier:
        liste_mots.append(ligne)

    fichier.close()

    mots_pendu=liste_mots[0].split(" ")
    #on initialise le score max
    score_max=0

    #le jeu commence
    jeu(mots_pendu,score_max)


Label(FrameAffichageMot, text = 'iugdziugdhz').pack(padx=10, pady=10)

BoutonProposer = Button(FrameAffichageMot, text ='Proposer', command=NouvellePartie)
BoutonProposer.pack(side='right',padx=1,pady=1)
    

mw.mainloop()