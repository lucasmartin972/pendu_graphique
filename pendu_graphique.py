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
    
    
#Création fenetre principale
from tkinter import *
from fonctions import *
mw = Tk()
mw.title('Jeu du Pendu')
mw['bg']='#3D4042'
mw.geometry('640x360+400+200')




#Création Frame interface utilisateur
FrameAffichageMot =Frame(mw,relief='groove')
FrameAffichageMot.pack(side='left',padx=10,pady=10)


#input de l'utilisateur
LettreEntre = StringVar()
Champ=Entry(FrameAffichageMot, textvariable='LettreEntre')
Champ.focus_set(); #on met le focus des entrées utilisaterur sur le champ
Champ.pack(side='bottom',padx=5,pady=5)








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
    
    
    
  
    
    


Label(FrameAffichageMot, text = 'Proposez une lettre').pack(padx=10, pady=10)





BoutonNouvellePartie = Button(mw, text ='Nouvelle Partie?', command=NouvellePartie)
BoutonNouvellePartie.pack(side='top',padx=1,pady=1)





    
#création d'un canvas
Canevas= Canvas(mw,width=300,height=300, bg ='#3D4042')
photo=PhotoImage(file="bonhomme1.gif")
Canevas.create_image(0,0,anchor=NW,image=photo)
Canevas.pack()                                             



















mw.mainloop()