# las ciudades que estan a los lados
A = 'acayucan'
B = 'boca del rio'
C = 'coatzacualco'
D = 'agua dulce'
E = 'jimenez'
F = 'Flores'
G = 'vega de la torre'
H = 'huatusco'
J = 'joachin'
M = 'minatitlan'
N = 'nigromante'
O = 'otatitlan'
P = 'papantla'
S = 'san andres'
T = 'tecolutla'
U = 'teuxitlan'
V = 'alvarado'
X = 'xalapa'
Y = 'yanga'
Z = 'zempoala'

# ciudades vecinas de cada una de las ciudades
ciudades = [A,B,C,D,E,F,G,H,J,M,N,O,P,S,T,U,V,X,Y,Z]
mapa = [[M, N, S],[J, V, X, Z],[D, M, S],[C],[F,O],[E,H,Y],[P,T,X,Z],[F,X],[B,O,Y],[A,C],
        [A,O],[E,N,V],[G,T,U],[A,C,V],[G,P],[P,X],[B,O,S],[B,G,H,U,Z],[F,J],[B,G,X]]
print(len(mapa))


#Aqui se obtiene cada ciudad vecina de una en especifico.

for i in range(20):
    for j in range(len(mapa[i])):
        print(ciudades[i] ,mapa[i][j])