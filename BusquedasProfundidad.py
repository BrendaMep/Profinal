# las ciudades que estan a los lados
A = 'acayucan'
B = 'boca del rio'
C = 'coatzacualco'
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

ciudades = [A,B,C,D,E,F,G,H,I,L,M,N,O,P,R,S,T,U,V,Z]
mapa = [[Z, T,S],[F,P,G,U],[D, P,R],[M,C],[H],[S,B],[B],[U,E],[N,V],[T,M],[L,D],
        [I],[Z,S],[R,C,B],[S,C,P],[A,O,F,R],[A,L],[B,V,H],[U,I],[O,A]]

#for i in range(20):
 #   for j in range(len(mapa[i])):
  #      print(ciudades[i] ,mapa[i][j])

def profundidad(mapa, inicio, destino):
    arbol = list()
    arbol.append(inicio)
    recorrido = [[inicio, None]]
    ciudad = list()
    while len(arbol) != 0:
        ciudad.append(arbol[0])
        arbol.remove(inicio)
        if ciudad == destino:
            return

        for i in range(20):
            if inicio == ciudades[i]:
                for j in mapa[i]:
                    if j not in recorrido:
                        arbol.append(j)
                        recorrido.append([j, ciudad])
                break
            break
        break

#print(profundidad(mapa, A,B))

for i in range(20):
    if A == ciudades[i]:
        for j in mapa[i]:
            print(j)
        break
    break
