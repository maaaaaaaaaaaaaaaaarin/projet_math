import sys
import matplotlib.pyplot as plt
sys.path.insert(0, '~/Documents/Code/Python/Projet_Math')
from sCSV import *
from math import sqrt

fichier   = 'toy_incomplet.csv'
personnes = loadAsList(fichier) 

# On cherche à faire la moyenne de notes
# données par deux utilisateurs sur un même item

def bravais_pearson(a, b, log=False, limit=-1):
    # Les sets de donnés doivent être de la même longueur
    # if len(a)!=len(b): return

    moyennes = []

    for i,j in zip(a,b):
        if i!=-1 and j!=-1:
            moyennes.append([i,j])
    if log:
        print("Items notés par A et B: "+str(len(moyennes)))


    # séparer listes + calcul moyennes (numérique)
    list_A = list(map(lambda x: x[0], moyennes))
    moy_A = sum(list_A)/len(list_A)

    list_B = list(map(lambda x: x[1], moyennes))
    moy_B = sum(list_B)/len(list_B)

    u  = 0  # upper component
    ll = 0  # lower left hand c.
    lr = 0  # lower right hand c.

    # logging var
    stru = []
    
    if limit == -1:
        limit = len(list_A)

    for i, j in zip(list_A, list_B):
        if limit != 0:
            u+=(i-moy_A)*(j-moy_B)
            ll+=(i-moy_A)**2
            lr+=(j-moy_B)**2

            if log:
                stru.append("({}-{:2.2})*({}-{:2.2})".format(i,moy_A,j,moy_B))
                print("\nll = ll + ({}-{:3.3})^2\t ll = {}".format(i,moy_A,ll))
                print("lr = lr + ({}-{:3.3})^2\t lr = {}".format(j,moy_B, lr))
            limit-=1
    
    if log:
        print("\nu   = "+ "+".join(stru) + "\nu   ± "+str(u))
        print("√ll = " +str(sqrt(ll)))
        print("√lr = " +str(sqrt(lr)))
        print("√ll * √lr ± "+str(sqrt(ll)*sqrt(lr)))
    r = (
        u/(sqrt(ll)*sqrt(lr))
        # note to self, division happens before multiplication
        # i have autism
    )

    return r

# extra
def like(a,b):
    for i in range(a,b):
        r = bravais_pearson(personnes[i-1],personnes[i])
        if r > 0.9:
            print("{}&{} --> très similaires ({:3.3})".format(i-1,i,r))
        #print()

#print(bravais_pearson(personnes[0],personnes[1]))

def colonne(n):
    return list(map(lambda x: x[n], list(filter(lambda x: x[n] != -1, personnes))))

"""
    nUtilisateur    : int
    item            : int

    return          : int
"""
def prédire(nUtilisateur, item, approche="item"):
    if approche == "utilisateur":
        p = personnes[nUtilisateur]
        m = sum(p)/len(p)

        #print(str(nUtilisateur)+": "+str(p[item]))
        # on filtre les personnes qui n'ont pas notées l'objet n°item
        filtré = list(filter(lambda x: x[item] != -1, personnes))
        
        print("\nIl y a " + str(len(filtré))+" utilisateurs qui ont noté l'objet "+str(item))
        print("\nL'utilisateur "+str(nUtilisateur)+" ", end="")
        if p[item] == -1:
            print("n'a pas noté l'objet "+str(item)+". ("+str(p[item])+")")
        else:
            print("a noté l'objet "+str(item)+". ("+str(p[item])+")")
        print()


        u = 0
        d = 0
        for i in list(filtré):
            # r * objet donné moins moyenne utilisateur
            r = bravais_pearson(p,i)
            if r >= 0.8:
                print(str(r) + "\t"+str(i[item]))
                u +=  r * (i[item]-(sum(i)/len(i)))
                d += abs(r)
        return m + (u/d)
    
    if approche == "item":
        p = personnes[nUtilisateur]
        i = colonne(0)
        m = sum(i) / len(i)





print(colonne(0))
print(colonne(1)) #FIXME


#d = prédire(0, 3)
#print("La note est " + str(round(d)) + " ( "+str(d)+" )")
#Objectif
# print(sum(list(map(lambda x: len(x), personnes))))
for i in range(1,10):
    print(bravais_pearson(colonne(i-1), colonne(i)))
#print(bravais_pearson(personnes[0],personnes[1]))
