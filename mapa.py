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
ciudades = [A,B,C,D,E,F,G,H,J,M,N,O,P,S,T,U,V,X,Y,Z]
mapa = [[M, S, N], [Z, V, J, X], [M, D, S], [C], [O, F], [Y, H, E], [T, P, Z, X], [F, X],
        [Y, B, O], [C, A], [O,A], [J, N, V, E], [T, G, U], [V, A, C], [G, P], [X, P],
        [B, S, O], [Z, U, B, H, G], [F, J], [B, X, G]]

print(len(mapa))


#Aqui se obtiene cada ciudad vecina de una en especifico.

for i in range(20):
    for j in range(len(mapa[i])):
        print(ciudades[i] ,mapa[i][j])