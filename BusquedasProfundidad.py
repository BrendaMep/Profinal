# las ciudades que estan a los lados
A = 'acayucan'
B = 'boca del rio'
C = 'coatzacoalcos'
D = 'agua dulce'
E = 'jimenez'
F = 'Flores'
G = 'vega de la torre'
H = 'huatusco'
I = 'joachin'
M = 'minatitlan'
N = 'nigromante'
O = 'otatitlan'
P = 'papantla'
S = 'san andres'
T = 'tecolutla'
U = 'teuxitlan'
V = 'alvarado'
L = 'xalapa'
R = 'yanga'
Z = 'zempoala'

ciudades = [A, B, C, D, E, F, G, H, I, L, M, N, O, P, R, S, T, U, V, Z]
mapa = [[Z, T, S], [F, P, G, U], [D, P, R], [M, C], [H], [S, B], [B], [U, E], [N, V], [T, M], [L, D],
        [I], [Z, S], [R, C, B], [S, C, P], [A, O, F, R], [A, L], [B, V, H], [U, I], [O, A]]


def ruta(recor):
    x = len(recor)
    rut = []
    rut.append(recor[x-1][0])
    rut.append(recor[x-1][1])
    m = len(rut)
    while m < x:
        for i in range(x):
            j = len(rut) - 1
            if rut[j] == recor[i][0]:
                if recor[i][1] is not rut:
                    rut.append(recor[i][1])
                    break
        m = m+1
    return rut


def profundidad(mapa, inicio, destino):
    arbol = list()
    recorrido = list()
    arbol.append(inicio)
    recorrido.append([inicio, None])
    x = len(arbol)
    while x != 0:
        ciudad = arbol[x-1]
        arbol.remove(ciudad)
        if ciudad == destino:
            print(ruta(recorrido))
            return
        else:
            vecinos = mapa[ciudades.index(ciudad)]
            for vecino in vecinos:
                if vecino is not recorrido:
                    arbol.append(vecino)
                    recorrido.append([vecino,ciudad])
        x = x+1


print(profundidad(mapa,A,B))
