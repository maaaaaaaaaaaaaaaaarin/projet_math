import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
sys.path.insert(0, '~/Documents/Code/Python/Projet_Math')
from sCSV import *
from math import sqrt
from numpy import array, linspace, sum as npsum

def cov(a, b):
    x = array(a)
    y = array(b)
    return ((1/len(x))*npsum(x*y)) - (npsum(x)/len(x))*(npsum(y)/len(y))

def bravais_pearson(a, b, log=False, limit=-1):
    # Les sets de donnés doivent être de la même longueur
    # if len(a)!=len(b): return

    moyennes = []

    for i,j in zip(a,b):
        if i!=-1 and j!=-1:
            moyennes.append([i,j])
    if log:
        print("\n\nItems notés par A et B: "+str(len(moyennes)))


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
        print("\n"*3)
        print("moyenne de A: "+str(moy_A))
        print("moyenne de B: "+str(moy_B))
        print("\nu   = "+ "+".join(stru) + "\nu   ± "+str(u))
        print("\n√ll = " +str(sqrt(ll)))
        print("√lr = " +str(sqrt(lr)))
        print("\n√ll * √lr ± "+str(sqrt(ll)*sqrt(lr)))
    r = (
        u/(sqrt(ll)*sqrt(lr))
        # note to self, division happens before multiplication
        # i have autism
    )
    if log:
        print("\nr = u/(√ll * √lr) = " + str(r))
        print()

    return r

# extra
def like(a,b):
    for i in range(a,b):
        r = bravais_pearson(personnes[i-1],personnes[i])
        if r > 0.9:
            print("{}&{} --> très similaires ({:3.3})".format(i-1,i,r))
        #print()

#print(bravais_pearson(personnes[0],personnes[1]))

def colonne(n,ignorem1=True):
    return list(map(lambda x: x[n], list(filter(lambda x: True, personnes))))

def invert(list2D):
    return list(map(list, zip(*list2D)))




def prédireNote(utilisateur, item, invert=False):
    
    # Récupération p[0]: (ctx dépend de l'application de `invert`)
    # - notes données par l'utilisateur 0
    # ou
    # - notes reçues par l'objet 0

    ctx = p if not invert else q
    line = ctx[0]

    return line





def prédire_new(utilisateur, item, log=False):
    p = personnes[utilisateur]
    m = sum(p)/len(p)

    #print(str(nUtilisateur)+": "+str(p[item]))
    # on filtre les personnes qui n'ont pas notées l'objet n°item
    filtré = list(filter(lambda x: x[item] != -1, personnes))

    if log:
        print("\nIl y a " + str(len(filtré))+" utilisateurs qui ont noté l'objet "+str(item))
        print("\nL'utilisateur "+str(nUtilisateur)+" ", end="")
    if p[item] == -1:
        if log:
            print("n'a pas noté l'objet "+str(item)+". ("+str(p[item])+")")
    else:
        if log:
            print("a noté l'objet "+str(item)+". ("+str(p[item])+")")
    if log:
        print()


    u = 0
    d = 0
    for i in list(filtré):

        r = bravais_pearson(p,i)
        if r >= 0.8:
            if log:
                print(str(r) + "\t"+str(i[item]))
            u +=  r * (i[item]-(sum(i)/len(i)))
            d += abs(r)
    return m + (u/d)


def prédire(nUtilisateur, item, log=False):
    test=invert(personnes)
    p = personnes[nUtilisateur]
    #p = invert(test)[utilisateur]
    m = sum(p)/len(p)

    #print(str(nUtilisateur)+": "+str(p[item]))
    # on filtre les personnes qui n'ont pas notées l'objet n°item
    filtré = list(filter(lambda x: x[item] != -1, personnes))
    if log:
        print("\nIl y a " + str(len(filtré))+" utilisateurs qui ont noté l'objet "+str(item))
        print("\nL'utilisateur "+str(nUtilisateur)+" ", end="")
    if p[item] == -1:
        if log:
            print("n'a pas noté l'objet "+str(item)+". ("+str(p[item])+")")
    else:
        if log:
            print("a noté l'objet "+str(item)+". ("+str(p[item])+")")
    if log:
        print()


    u = 0
    d = 0
    for i in list(filtré):
        # r * objet donné moins moyenne utilisateur
        r = bravais_pearson(p,i)
        if r >= 0.8:
            if log:
                print(str(r) + "\t"+str(i[item]))
            u +=  r * (i[item]-(sum(i)/len(i)))
            d += abs(r)
    return m + (u/d)
        
        
#print(bravais_pearson(colonne(0),colonne(1)))
def calcCol(a,b, log=False):
    if log:
        print("A\tB\n"+("–"*10).format(a,b))


    # on doit trouver les colonnes ayant reçu des notes au mêmes endroits que la colonne donnée
    # on fait la moyenne en colonne des notes filtrées communes 
    # on soustrait la moyenne à la note donnée par l'utilisateur dont on cherche à déterminer la note
    #
    # ex:           item 1      item 2      item 3
    # personne 1      x           2           3
    # personne 2      4           4           5
    # 
    # 2 - 3 
    # 3 = (2+4)/2

    notes_communes = [[], []]

    for i, j in zip(colonne(a), colonne(b)):
        if log:
            print("{}\t{}".format(i, j), end="")
        
        if (i == -1 or j == -1 ):
            if log:
                print("\t--> x ",end="")
        else:
            notes_communes[0].append(i)
            notes_communes[1].append(j)
        
        if log:
            print()
    
    moy_A = sum(notes_communes[0])/len(notes_communes[0])
    moy_B = sum(notes_communes[1])/len(notes_communes[1])

    return [moy_A, moy_B]

def predireItems(utilisateur, item):
    elements  = set([i for i in range(len(personnes))])
    elements -= set([item])

    index=0
    u=0
    l=0
    moy_item=calcCol(item,item)[0]
    #print("Moyenne selon calcCol de {} : {}".format(item, calcCol(item,item)[0]))
    for i in personnes[utilisateur]:
        if i != -1:
            # r * (i - moy(i)) + ...
            r = bravais_pearson(colonne(item), colonne(index))
            u+= r *(i-calcCol(item, index)[1])
            l+= abs(r)
            #print("Moyenne colonne "+str(index)+" = "+str(calcCol(item, index, log=False)[1]))
        else:
            pass
            #print("Colonne "+str(index)+ " -1")
        index+=1
    return (moy_item+(u/l))

def plotDifferences(utilisateur, start_end, predictor):
    
    if type(start_end) == list:
        start = start_end[0]
        end   = start_end[1]
    elif type(start_end) == int:
        start = start_end
        end   = start+1
    
    predictions  = []
    notesReelles = realNotes[utilisateur][start:end]
    differences  = []
    xrange       = list(range(end-start))
    rot          = -90

    #print("notesRéelles: {}\n len nr: {}".format(notesReelles, len(notesReelles)))
    #print("xrange: {}\n len xr: {}".format(xrange, len(xrange)))    
    
    # Plot du haut
    # notes prédites et notes réelles
    # + calcul des différences entre prédites et réelles

    plt.subplot(2,1,1)

    for i in xrange:
        
        prediction = predictor(utilisateur, i-1)
        predictions.append(prediction)

        differences.append(abs(notesReelles[i-1] - prediction))
    
    tracés = []
    print("notesRéelles: {}\n len nr: {}".format(notesReelles, len(notesReelles)))
    print("differences: {}\n len diff: {}".format(differences, len(differences)))
    x = range(len(notesReelles))
    tracés.append(
        plt.errorbar(x, notesReelles, c="orange", fmt='o', yerr=differences)
    )
    tracés.append(
        plt.scatter(x, predictions, c="blue")
    )
    
    plt.subplots_adjust(bottom=0.15)
    plt.legend(tracés, ["Notes réelles","Notes prédites"],loc='upper center',
    bbox_to_anchor=(0.5, 1.25),fancybox=True, shadow=True, ncol=5)
    plt.xticks(x, range(start, end), rotation=rot)
    # Second plot, illustrant les différences entre chaque notes
    # et l'erreur moyenne de celles-ci

    plt.subplot(2,1,2)
    
    erreurMoyenne = sum(differences)/len(differences)
    
    plt.hlines(erreurMoyenne, 0, len(x), colors='red')
    plt.bar(x, differences)
    plt.text(0,-1.25, "Erreur moyenne: {:.3}".format(erreurMoyenne), horizontalalignment='left')
    plt.xticks(x, range(start, end, 3), rotation=rot)
#     import numpy as np
# import matplotlib.pyplot as plt

# x = [0,5,9,10,15]
# y = [0,1,2,3,4]
# plt.plot(x,y)
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
# plt.show()

    plt.show()

# def plotDifferences(utilisateur, start=0, end=50, comp=predireItems):
#     preds=[]
#     notes=realNotes[utilisateur][:end]
#     print(len(notes))
#     tracés = []
#     diff = []
#     plt.subplot(2,1,1)
#     for i in range(start, end):
#         pred = comp(utilisateur, i)
#         preds.append(pred)
#         diff.append(abs(notes[i]-pred))

#     # yerr=diff
#     tracés.append(plt.errorbar(range(len(notes)), notes, c="orange", fmt='o'))
    
#     tracés.append(plt.scatter(range(len(preds)), preds, c="blue"))

#     print(sum(diff))
#     print(len(diff))
#     moy_err = sum(diff)/len(diff)
#     print("Erreur moyenne = " + str(moy_err))

#     plt.subplots_adjust(bottom=0.15)
#     plt.legend(tracés, ["Notes réelles","Notes prédites"],loc='upper center', bbox_to_anchor=(0.5, -0.05),
#     fancybox=True, shadow=True, ncol=5)

#     plt.subplot(2,1,2)
#     plt.hlines(moy_err, 0, end, colors='red')
#     plt.bar(range(len(diff)), diff)


fichier   = 'toy_incomplet.csv'
personnes = loadAsList(fichier)
p         = personnes
q         = invert(p)

realNotes = loadAsList('toy_complet.csv')

print(prédireNote(0,0))


#     plt.show()

    #print("toy_complet = {}, prédiction = {:.5f},\tdiff = {:>5}".format(float(tc), float(pred), float(diff)))
# plotDifferences(0,[0,101], prédire)
#print(personnes[0])
#print(colonne(0))
#print(invert(personnes)[0])
# print(colonne(0))
# print(colonne(1))
#x=[44,62,71,73,87]
#y=[40,57,59,65,77]

#xx = [0,1,2,2,2,3,4,5,5,5,6,7,8,8,9,10]
#yy = [4,5,5,3,5,3,4,4,4,6,6,5,9,8,8,7]
#print("cov = "+str(cov(xx,yy)))
#print("r = "+str(bravais_pearson(xx,yy)))