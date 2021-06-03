A = 'Acayucan'
B = 'Boca del Rio'
C = 'Coatzacualcos'
D = 'Agua Dulce'
E = 'Huautla de Jimenez'
F = 'Fortin Flores'
G = 'Vega de Alatorre'
H = 'Huatusco'
J = 'Joachin'
M = 'Minatitlan'
N = 'Nigromante'
O = 'Otatitlan'
P = 'Papantla'
S = 'San Andres Tuxtla'
T = 'Tecolutla'
U = 'Teziutlan'
V = 'Alvarado'
X = 'Xalapa'
Y = 'Yanga'
Z = 'Zempoala'

mapa1 = {
    'A': ['M', 'S', 'N'],
    'B': ['Z', 'V', 'J', 'X'],
    'C': ['M', 'D', 'S'],
    'D': ['C'],
    'E': ['O', 'F'],
    'F': ['Y', 'H', 'E'],
    'G': ['T', 'P', 'Z', 'X'],
    'H': ['F', 'X'],
    'J': ['Y', 'B', 'O'],
    'M': ['C', 'A'],
    'N': ['O', 'A'],
    'O': ['J', 'N', 'V', 'E'],
    'P': ['T', 'G', 'U'],
    'S': ['V', 'A', 'C'],
    'T': ['G', 'P'],
    'U': ['X', 'P'],
    'V': ['B', 'S', 'O'],
    'X': ['Z', 'U', 'B', 'H', 'G'],
    'Y': ['F', 'J'],
    'Z': ['B', 'X', 'G']
}


def costo(mapa, inicio, final):
    ruta = []
    ciclo = 0
    while inicio != final:
        vecinos = mapa[inicio]
        ruta.append(inicio)
        vecinos2 = list()
        if final in vecinos:
            inicio = final
            ruta.append(final)
            return ruta
        else:
            for ciudad in vecinos:
                if ciudad not in ruta:
                    vecinos2.append(ciudad)
            if len(vecinos2) != 0:
                inicio = vecinos2[0]
            else:
                inicio = ruta[len(ruta) - 1]
                ruta.remove(inicio)
                for ciudades in mapa:
                    if inicio in mapa[ciudades]:
                        mapa[ciudades].remove(inicio)
                del mapa[inicio]
                inicio = ruta[len(ruta) -1]
                ruta.remove(inicio)
X = costo(mapa1, A,B)
print(X)


