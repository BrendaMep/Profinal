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
    for j in range(len(rut)):
        for i in range(x):
            if rut[j] == recor[i][0]:
                rut.append(recor[i][1])
    rut = list(set(rut))
    rut.reverse()


def profundidad(mapa, inicio, destino):
    arbol = list()
    arbol.append(inicio)
    recorrido = [[inicio, None]]
    while len(arbol) != 0:
        x = len(arbol)
        ciudad = arbol[x-1]
        arbol.remove(ciudad)
        if ciudad == destino:
            return ruta(recorrido)
        for i in range(20):
            if inicio == ciudades[i]:
                for j in mapa[i]:
                    if j not in recorrido:
                        arbol.append(j)
                        recorrido.append([j, ciudad])
                break
        print(arbol)
        print(recorrido)
        print(ciudad)
        print(len(recorrido))
        #arbol = arbol
        break

print(profundidad(mapa,A,B))
