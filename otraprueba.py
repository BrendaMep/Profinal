from amplitud import fcn_amplitud
#from uniforme import costo
from ignoren import costo
from BusquedasProfundidad import profundidad
from ignoren import mapa1
from mapa2 import mapa
from mapa2 import ciudades
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QSlider, QDial, QDoubleSpinBox, QPushButton, QSizePolicy, QComboBox


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

lista = ['Acayucan', 'Boca del Rio', 'Coatzacualcos', 'Agua Dulce', 'Huautla de Jimenez', 'Fortin Flores',
         'Vega de Alatorre', 'Huatusco', 'Joachin', 'Minatitlan', 'Nigromante', 'Otatitlan', 'Papantla',
         'San Andres Tuxtla', 'Tecolutla', 'Teziutlan', 'Alvarado', 'Xalapa', 'Yanga', 'Zempoala']
lista2 = ['Aplitud', 'Costo', 'Profundidad']

def cam(palabra):
    for i in range(20):
        if palabra == ciudades[i]:
            m = ciudades[i]
            return m


def f(inicio, fin, modo):
    if modo == 'Ampliud':
        recor = fcn_amplitud(ciudades, mapa, inicio, fin)
        return recor
    else:
        if modo == 'Costo':
            recor = costo(mapa1, inicio, fin)
            return recor
        else:
            recor = profundidad(mapa, inicio, fin)
            return recor

