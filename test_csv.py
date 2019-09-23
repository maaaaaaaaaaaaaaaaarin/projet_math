import sys
sys.path.insert(0, '~/Documents/Code/Python/Projet_Math')

from sCSV import *

fichier  = 'toy_incomplet.csv'
resultat = loadAsList(fichier) 

# Indice de resultat (resultat[n]) donne les notes de l'utilisateur n

print(resultat[0])