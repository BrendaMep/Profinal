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
ciudades= [A, B, C, D, E, F, G, H, J, M, N, O, P, S, T, U, V, X, Y, Z]
mapa_ej = [[M, S, N], [Z, V, J, X], [M, D, S], [C], [O, F], [Y, H, E], [T, P, Z, X], [F, X],
           [Y, B, O], [C, A], [O, A], [J, N, V, E], [T, G, U], [V, A, C], [G, P], [X, P],
           [B, S, O], [Z, U, B, H, G], [F, J], [B, X, G]]
#print(mapa_ej[7])

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
    rut.reverse()
    return rut


def profundidad(mapa, inicio, destino):
    arbol = []
    recorrido = []
    arbol.append(inicio)
    recorrido.append([inicio, None])
    while len(arbol) != 0:
        ciudad = arbol[len(arbol) - 1]
        #print(ciudad)
        #print(arbol)
        arbol.remove(arbol[len(arbol)-1])
        if ciudad == destino:
            #print(recorrido)
            ru = ruta(recorrido)
            return ru
        else:
            vecinos = mapa[ciudades.index(ciudad)]
            for vecino in vecinos:
                acceso = 0
                for ndo in recorrido:
                    if (vecino == ndo[0] or vecino == ndo[1]):
                        acceso += 1
                if acceso == 0:
                    arbol.append(vecino)
                    recorrido.append([vecino, ciudad])
print(profundidad(mapa_ej,A,B))
