from amplitud import fcn_amplitud
from uniforme import costo
from BusquedasProfundidad import profundidad
from uniforme import mapa1
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
lista2 = ['Rapida', 'Bajo', 'Larga']


class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.container = QWidget()

        self.main_layout = QHBoxLayout()
        self.lyt_settings = QVBoxLayout()
        self.lyt_graph = QHBoxLayout()

        self.mensaje = QFormLayout()
        self.lyt_salida = QFormLayout()
        self.lyt_destino = QFormLayout()
        self.descripcion1 = QFormLayout()
        self.descripcion2 = QFormLayout()
        self.descripcion3 = QFormLayout()
        self.lyt_modo = QFormLayout()

        self.mensaje = QLabel()

        self.lbl_salida = QLabel()
        self.sld_salida = QComboBox()
        # self.lnedt_sigma = QLineEdit()

        self.lbl_destino = QLabel()
        self.sld_destino = QComboBox()
        # self.lnedt_rho = QLineEdit()

        self.descripcion1 = QLabel()
        self.descripcion2 = QLabel()
        self.descripcion3 = QLabel()

        self.lbl_modo = QLabel()
        self.sld_modo = QComboBox()
        # self.lnedt_beta = QLineEdit()

        self.btn_graph = QPushButton()

        # graficas

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Viaje')

        self.mensaje = QLabel("Bienvenido")

        self.lbl_salida.setText('Salida')
        self.lbl_salida.setFixedWidth(50)
        for i in lista:
            self.sld_salida.addItem(i)
        self.lbl_salida.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.sld_salida.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.lbl_destino.setText('Destino')
        self.lbl_destino.setFixedWidth(65)
        for i in lista:
            self.sld_destino.addItem(i)
        self.lbl_destino.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.sld_destino.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.descripcion1 = QLabel("Rapida, es la ruta mas corta de llegar al destino.")
        self.descripcion2 = QLabel("Bajo, es la ruta con menos costo.")
        self.descripcion3 = QLabel("Larga, es la ruta donde viajaras por mas ciudades.")

        self.lbl_modo.setText('Modo de viaje')
        self.lbl_modo.setFixedWidth(110)
        for i in lista2:
            self.sld_modo.addItem(i)
        self.lbl_modo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.sld_modo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.btn_graph.setText('Trazar ruta')
        self.btn_graph.setFixedWidth(105)

        # Funcionabilidad
        self.sld_salida.currentTextChanged.connect(self.plot_datas)
        self.sld_destino.currentTextChanged.connect(self.plot_datas)
        self.sld_modo.currentTextChanged.connect(self.plot_datas)

        self.main_layout.addLayout(self.lyt_settings)  # objetos que conforman la interfaz
        self.main_layout.addLayout(self.lyt_graph)
        self.container.setLayout(self.main_layout)

        self.lyt_settings.addWidget(self.mensaje)

        self.lyt_settings.addWidget(self.lbl_salida)
        self.lyt_salida.addRow(self.sld_salida)  # , self.lnedt_sigma)
        self.lyt_settings.addLayout(self.lyt_salida)

        self.lyt_settings.addWidget(self.lbl_destino)
        self.lyt_destino.addRow(self.sld_destino)  # , self.lnedt_rho)
        self.lyt_settings.addLayout(self.lyt_destino)

        self.lyt_settings.addWidget(self.descripcion1)
        self.lyt_settings.addWidget(self.descripcion2)
        self.lyt_settings.addWidget(self.descripcion3)

        self.lyt_settings.addWidget(self.lbl_modo)
        self.lyt_modo.addRow(self.sld_modo)  # , self.lnedt_beta)
        self.lyt_settings.addLayout(self.lyt_modo)

        self.lyt_settings.addWidget(self.btn_graph)

        self.setCentralWidget(self.container)

    def f(self, inicio, fin, modo):
        if self.sld_modo.value() == 'Rapida':
            recor = fcn_amplitud(ciudades, mapa, inicio, fin)
            return recor
        # if modo == 'Bajo':
        # recor = costo(mapa1,inicio,fin)
        else:
            recor = profundidad(mapa, inicio, fin)
            return recor


    def plot_datas(self):
        print(self.sld_salida.value())
        print(self.sld_destino.value())
        print(self.sld_modo.value())


if __name__ == '__main__':
    app = QApplication([])     # funcion principal
    window = ProjectWindow()
    window.show()
    app.exec_()



