#A = 'acayucan'
#B = 'boca del rio'
#C = 'coatzacoalcos'
#D = 'agua dulce'
#E = 'jimenez'
#F = 'Flores'
#G = 'vega de la torre'
#H = 'huatusco'
#I = 'joachin'
#M = 'minatitlan'
#N = 'nigromante'
#O = 'otatitlan'
#P = 'papantla'
#S = 'san andres'
#T = 'tecolutla'
#U = 'teuxitlan'
#V = 'alvarado'
#L = 'xalapa'
#R = 'yanga'
#Z = 'zempoala'

#recorrido = [[A,None], [Z,A],[T,A],[S,A],[O,S],[F,S],[R,S],[C,R],[P,R],[B,P],[U,O]]

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
print(mapa[11])

def profundidad(mapa, inicio, destino):
    arbol = []
    recorrido = []
    arbol.append(inicio)
    recorrido.append([inicio, None])
    while len(arbol) != 0:
        ciudad = arbol[len(arbol) - 1]
        arbol.remove(arbol[len(arbol)-1])
        if ciudad == destino:
            print(recorrido)
            ru = ruta(recorrido)
            return ru
        else:
            vecinos = mapa[ciudades.index(ciudad)]
            for vecino in vecinos:
                acceso = 0
                for ndo in recorrido:
                    print(ndo)
                    if (vecino == ndo[0]) or (vecino == ndo[1]):
                        acceso += 1
                if acceso == 0:
                    arbol.append(vecino)
                    recorrido.append([vecino, ciudad])
#X = profundidad(mapa,C,T)
#print(X)