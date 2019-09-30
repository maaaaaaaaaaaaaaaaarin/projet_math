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
    if len(a)!=len(b): return

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

print(bravais_pearson(personnes[0],personnes[1]))

    #print("Moyenne A: " + str(moy_A))
    #print("Moyenne B: " + str(moy_B))
    #print("diff: " + str(max([moy_A, moy_B])-min([moy_A, moy_B])))
    #print("Len a: "+str(len(a)))
    #print("Len b: "+str(len(b)))

#Objectif
# print(sum(list(map(lambda x: len(x), personnes))))
#for i in range(1,10):
#    print(bravais_pearson(personnes[i-1],personnes[i]))
#print(bravais_pearson(personnes[0],personnes[1]))
