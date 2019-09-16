#import sys
#sys.path.insert(0, '~/Documents/Code/Python/Projet_Math')
from csv import reader

def loadAsList(file='toy_complet.csv'):
    with open(file) as csvF:
        return list(map(lambda x: x[0].split(), list(reader(csvF))))