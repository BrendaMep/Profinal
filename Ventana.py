from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QSlider, QDial, QDoubleSpinBox, QPushButton, QSizePolicy, QComboBox
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from scipy.integrate import odeint
import numpy as np

class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.container = QWidget()

        self.main_layout = QHBoxLayout()
        self.lyt_settings = QVBoxLayout()
        self.lyt_graph = QHBoxLayout()


        self.lyt_sigma = QFormLayout()
        self.lyt_rho = QFormLayout()
        self.lyt_beta = QFormLayout()

        self.lbl_sigma = QLabel()
        self.sld_sigma = QComboBox()
        #self.lnedt_sigma = QLineEdit()

        self.lbl_rho = QLabel()
        self.sld_rho = QComboBox()
        #self.lnedt_rho = QLineEdit()

        self.lbl_beta = QLabel()
        self.sld_beta = QComboBox()
        #self.lnedt_beta = QLineEdit()

        self.btn_graph = QPushButton()


        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Viaje')
        mensaje = QLabel("Bienvenido")

        self.lbl_sigma.setText('Salida')
        self.lbl_sigma.setFixedWidth(50)
        #self.lbl_sigma.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        #self.sld_sigma.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.lbl_rho.setText('Destino')
        self.lbl_rho.setFixedWidth(65)
        # self.lbl_sigma.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        # self.sld_sigma.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        descripcion1 = QLabel("Rapida, es la ruta mas corta de llegar al destino")
        descripcion2 = QLabel("Bajo, es la ruta con menos costo")
        descripcion3 = QLabel("Larga, es la ruta mas grande")

        self.lbl_beta.setText('Modo de viaje')
        self.lbl_beta.setFixedWidth(110)
        # self.lbl_sigma.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        # self.sld_sigma.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.btn_graph.setText('Trazar ruta')
        self.btn_graph.setFixedWidth(105)

        self.main_layout.addLayout(self.lyt_settings) # objetos que conforman la interfaz
        self.main_layout.addLayout(self.lyt_graph)
        self.container.setLayout(self.main_layout)

        self.lyt_settings.addWidget(mensaje)

        self.lyt_settings.addWidget(self.lbl_sigma)
        self.lyt_sigma.addRow(self.sld_sigma)  #, self.lnedt_sigma)
        self.lyt_settings.addLayout(self.lyt_sigma)

        self.lyt_settings.addWidget(self.lbl_rho)
        self.lyt_rho.addRow(self.sld_rho)   #, self.lnedt_rho)
        self.lyt_settings.addLayout(self.lyt_rho)

        self.lyt_settings.addWidget(self.lbl_beta)
        self.lyt_beta.addRow(self.sld_beta)    #, self.lnedt_beta)
        self.lyt_settings.addLayout(self.lyt_beta)

        self.lyt_settings.addWidget(self.btn_graph)

        self.setCentralWidget(self.container)


if __name__ == '__main__':
    app = QApplication([])     # funcion principal
    window = ProjectWindow()
    window.show()
    app.exec_()



