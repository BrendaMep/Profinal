from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QSlider, QComboBox, QDoubleSpinBox, QPushButton, QSizePolicy
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas)
from scipy.integrate import odeint
import numpy as np
from sklearn import tree

class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.container = QWidget()

        self.main_layout = QHBoxLayout()
        self.lyt_settings = QVBoxLayout()
        self.lyt_graph = QHBoxLayout()

        self.lyt_inicio = QFormLayout()
        self.lyt_destino = QFormLayout()


        self.lbl_inicio = QComboBox()  # para x0
        self.lnedt_inicio = QLineEdit()

        self.lbl_destino = QComboBox()  # para y0
        self.lnedt_destino = QLineEdit()

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Mapa')

        self.lbl_inicio.setText('inicio')
        self.lnedt_inicio.setText("A")
        self.lnedt_inicio.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.lbl_destino.setText('destino')
        self.lnedt_destino.setText("B")
        self.lnedt_destino.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.lyt_inicio.addRow(self.lbl_inicio, self.lnedt_inicio)
        self.lyt_destino.addRow(self.lbl_destino, self.lnedt_destino)

        self.main_layout.addLayout(self.lyt_settings) # objetos que conforman la interfaz
        self.container.setLayout(self.main_layout)

        self.lyt_settings.addLayout(self.lyt_inicio)
        self.lyt_settings.addLayout(self.lyt_destino)

        self.setCentralWidget(self.container)

    # la definicion

if __name__ == '__main__':
    app = QApplication([])     # funcion principal
    window = ProjectWindow()
    window.show()
    app.exec_()


