# es el de profundidad.
from sklearn import tree



mapa ={'A':['Z','T','S'], 'B':['F','P','G','U'],
       'C':['D','P','R'],'D':['M','C'],
       'E':['H'], 'F':['S','B'],'G':['B'],
       'H':['U','E'], 'I':['N','V'],'L':['T','M'],
       'M':['L','D'], 'N':['I'], 'O':['Z','S'],
       'P':['R','C','B'], 'R':['S','C','P'],
       'S':['A','O','F','R'], 'T':['A','L'], 'U':['B','V','H'],
       'V':['U','I'], 'Z':['O','A']}


def profundidad(mapa, inicio, destino):
    arbol = set(inicio)
    recorrido = set(inicio,None)
    while len(arbol) != 0:
        ciudad = set(inicio)
        arbol.remove(inicio)
        if ciudad == destino:
            return
        for vecino in ciudad:
            if vecino not in recorrido:
                arbol.add(vecino)
                recorrido.__add__(vecino,ciudad)
            #break
        #break
    #break
profundidad(mapa,A ,B)