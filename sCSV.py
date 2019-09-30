#import sys
#sys.path.insert(0, '~/Documents/Code/Python/Projet_Math')
from csv import reader

def loadAsList(file='toy_complet.csv', type='int'):
    with open(file) as csvF:
        if type == 'int':
                return list(map(lambda x: list(map(lambda y: int(y), x[0].split())), list(reader(csvF))))
        elif type == 'str':
                return list(map(lambda x: x[0].split(), list(reader(csvF))))