import sys
import matplotlib.pyplot as plt
sys.path.insert(0, '~/Documents/Code/Python/Projet_Math')
from sCSV import *

fichier   = 'toy_incomplet.csv'
personnes = loadAsList(fichier) 

# On cherche à faire la moyenne de notes
# données par deux utilisateurs sur un même item

def bravais_pearson(a, b):
    # Les sets de donnés doivent être de la même longueur
    if len(a)!=len(b): return

    moyennes = []

    for i,j in zip(a,b):
        if i!=-1 and j!=-1:
            moyennes.append([i,j])
    print("Items notés par A et B: "+str(len(moyennes)))

    moy_A = list(map(lambda x: x[0], moyennes))
    moy_A = sum(moy_A)/len(moy_A)

    moy_B = list(map(lambda x: x[1], moyennes))
    moy_B = sum(moy_B)/len(moy_B)

    # Calculer partie gauche + partie droite
    # parties : item - moy (respectivement) 


    print("Moyenne A: " + str(moy_A))
    print("Moyenne B: " + str(moy_B))
    #print("Len a: "+str(len(a)))
    #print("Len b: "+str(len(b)))

#Objectif
# print(sum(list(map(lambda x: len(x), personnes))))
print(bravais_pearson(personnes[0],personnes[1]))