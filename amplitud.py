# las ciudades que estan a los lados
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

# ciudades vecinas de cada una de las ciudades
ciudades_ej = [A, B, C, D, E, F, G, H, J, M, N, O, P, S, T, U, V, X, Y, Z]
mapa_ej = [[M, S, N], [Z, V, J, X], [M, D, S], [C], [O, F], [Y, H, E], [T, P, Z, X], [F, X],
           [Y, B, O], [C, A], [O, A], [J, N, V, E], [T, G, U], [V, A, C], [G, P], [X, P],
           [B, S, O], [Z, U, B, H, G], [F, J], [B, X, G]]

# Aqui se obtiene cada ciudad vecina de una en especifico.
"""
for i in range(20):
    for j in range(len(mapa_ej[i])):
        print(ciudades[i] ,mapa_ej[i][j])

"""


def recursive(list_tup,coso):
    rta = []
    rta.append(list_tup[0][0])
    extra = []
    last = coso
    for i in range(1,len(list_tup)):
        ant_last = list_tup[len(list_tup) - i][0]
        if ant_last == last:
            extra.append(ant_last)
            last = list_tup[len(list_tup) - i][1]
    for i in range(1,len(extra)+1):
        rta.append(extra[(len(extra) - i)])
    return (rta)


def fcn_amplitud(ciudades, mapa, origen, destino):
    arbol = []
    recorrido = []
    arbol.append(origen)
    nodo = [origen, None]
    recorrido.append(nodo)
    while len(arbol) != 0:
        ciudad = arbol[0]
        arbol.remove(arbol[0])
        if ciudad == destino:
            #print(recorrido)
            ruta = recursive(recorrido,destino)
            return ruta
        else:
            vecinos = mapa[ciudades.index(ciudad)]
            for vecino in vecinos:
                acceso = 0
                for ndo in recorrido:
                    if (vecino == ndo[0]) or (vecino == ndo[1]):
                        acceso += 1
                if acceso == 0:
                    arbol.append(vecino)
                    nodo = [vecino, ciudad]
                    recorrido.append(nodo)
X = fcn_amplitud(ciudades_ej,mapa_ej, C,F)
print(X)