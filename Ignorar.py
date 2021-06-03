from amplitud import fcn_amplitud
#from uniforme import costo
from BusquedasProfundidad import profundidad
#from uniforme import mapa1
from mapa1 import mapa
from mapa1 import ciudades
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

print(fcn_amplitud(ciudades,mapa,A,B))
#print(costo(mapa1,A,B))
print(profundidad(mapa,A,B))