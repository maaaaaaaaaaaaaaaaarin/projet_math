import sys
import matplotlib.pyplot as plt
sys.path.insert(0, '~/Documents/Code/Python/Projet_Math')
from sCSV import *

fichier  = 'toy_incomplet.csv'
resultat = loadAsList(fichier) 

print(list(filter(lambda x: x=='5', resultat[0])))


tracés = []
def plotUtilisateur(numéro,couleur,offset=0.0,show=False,ignorer_absence=True):
  y = list(map(lambda x: int(x), resultat[numéro]))

  if ignorer_absence:
    y = list(filter(lambda x: x!=-1.0, y))

  y = list(map(lambda x: x+offset, y))

  x = range(1,len(y)+1) # Décalage de 1

  tracés.append(plt.scatter(x, y, c = couleur))
  #plt.legend(str(numéro))
  #plt.title("Utilisateur n°"+str(numéro))
  if show:
    plt.show()

colors = ["blue","red","yellow","green","orange","purple"]
for i in range(6):
  plotUtilisateur(i, colors[i], 0+i/10)

plt.subplots_adjust(bottom=0.15)
plt.legend(tracés, range(len(tracés)),loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
plt.show()
#plotUtilisateur(0,'red')
#plotUtilisateur(1,'blue',0.1)
