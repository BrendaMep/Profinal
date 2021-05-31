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

mapa = {
    'A': ['Z', 'T', 'S'],
    'B': ['F', 'P', 'G', 'U'],
    'C': ['D', 'P', 'R'],
    'D': ['M', 'C'],
    'E': ['H'],
    'F': ['S', 'B'],
    'G': ['B'],
    'H': ['U', 'E'],
    'I': ['N', 'V'],
    'L': ['T', 'M'],
    'M': ['L', 'D'],
    'N': ['I'],
    'O': ['Z', 'S'],
    'P': ['R', 'C', 'B'],
    'R': ['S', 'C', 'P'],
    'S': ['A', 'O', 'F', 'R'],
    'T': ['A', 'L'],
    'U': ['B', 'V', 'H'],
    'V': ['U', 'I'],
    'Z': ['O', 'A']
}


def costo(mapa, inicio, final):
    ruta = []
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
            inicio = vecinos2[0]



