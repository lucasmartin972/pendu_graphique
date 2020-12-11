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
mw.geometry('1000x360+400+200')




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
    
    
chance=8






#codage de l'avancement du bonhomme
if chance == 8:
    photo="bonhomme8.gif"
elif chance == 7:
    photo="bonhomme7.gif"
elif chance == 6:
    photo="bonhomme6.gif"
elif chance == 5:
    photo="bonhomme5gif"
elif chance == 4:
    photo="bonhomme4.gif"
elif chance == 3:
    photo="bonhomme3.gif"
elif chance == 2:
    photo="bonhomme2.gif"
elif chance == 1:
    photo="bonhomme1.gif"
elif chance == 0:
    photo="bonhomme0.gif"

  
    
    


Label(FrameAffichageMot, text = 'Proposez une lettre').pack(padx=0, pady=0)





BoutonNouvellePartie = Button(mw, text ='Nouvelle Partie?', command=NouvellePartie)
BoutonNouvellePartie.pack(padx=1,pady=1)





    
#création d'un canvas
Canevas= Canvas(mw,width=300,height=300, bg ='#3D4042')
photo=PhotoImage(file=photo)
item=Canevas.create_image(0,0,anchor=NW,image=photo)
Canevas.pack(side='right',padx=40)                                           



















mw.mainloop()