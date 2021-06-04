import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import os

lista = ['Acayucan','Boca del Rio','Coatzacualcos','Agua Dulce','Huautla de Jimenez','Fortin Flores',
         'Vega de Alatorre','Huatusco','Joachin','Minatitlan','Nigromante','Otatitlan','Papantla',
         'San Andres Tuxtla','Tecolutla','Teziutlan','Alvarado','Xalapa','Yanga','Zempoala']
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
        #self.lnedt_sigma = QLineEdit()

        self.lbl_destino = QLabel()
        self.sld_destino = QComboBox()
        #self.lnedt_rho = QLineEdit()

        self.descripcion1 = QLabel()
        self.descripcion2 = QLabel()
        self.descripcion3 = QLabel()

        self.lbl_modo = QLabel()
        self.sld_modo = QComboBox()
        #self.lnedt_beta = QLineEdit()

        self.btn_graph = QPushButton()

        # graficas

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Viaje')
        self.mensaje = QLabel("Bienvenido")

        self.lbl_salida.setText('Salida')
        self.lbl_salida.setFixedWidth(50)
        self.sld_salida.addItems(lista)
        self.lbl_salida.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.sld_salida.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.lbl_destino.setText('Destino')
        self.lbl_destino.setFixedWidth(65)
        self.sld_destino.addItems(lista)
        self.lbl_destino.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.sld_destino.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.descripcion1 = QLabel("Rapida, es la ruta mas corta de llegar al destino.")
        self.descripcion2 = QLabel("Bajo, es la ruta con menos costo.")
        self.descripcion3 = QLabel("Larga, es la ruta donde viajaras por mas ciudades.")


        #mapa de html
        self.html_view = QWebEngineView()
        self.lyt_graph.addWidget(self.html_view)

        self.html_view.load(QUrl.fromLocalFile(os.path.abspath('index.html')))



        self.lbl_modo.setText('Modo de viaje')
        self.lbl_modo.setFixedWidth(110)
        self.sld_modo.addItems(lista2)
        self.lbl_modo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.sld_modo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.btn_graph.setText('Trazar ruta')
        self.btn_graph.setFixedWidth(105)

        self.main_layout.addLayout(self.lyt_settings) # objetos que conforman la interfaz
        self.main_layout.addLayout(self.lyt_graph)
        self.container.setLayout(self.main_layout)

        self.lyt_settings.addWidget(self.mensaje)

        self.lyt_settings.addWidget(self.lbl_salida)
        self.lyt_salida.addRow(self.sld_salida)  #, self.lnedt_sigma)
        self.lyt_settings.addLayout(self.lyt_salida)

        self.lyt_settings.addWidget(self.lbl_destino)
        self.lyt_destino.addRow(self.sld_destino)   #, self.lnedt_rho)
        self.lyt_settings.addLayout(self.lyt_destino)

        self.lyt_settings.addWidget(self.descripcion1)
        self.lyt_settings.addWidget(self.descripcion2)
        self.lyt_settings.addWidget(self.descripcion3)

        self.lyt_settings.addWidget(self.lbl_modo)
        self.lyt_modo.addRow(self.sld_modo)    #, self.lnedt_beta)
        self.lyt_settings.addLayout(self.lyt_modo)

        self.lyt_settings.addWidget(self.btn_graph)










        self.setCentralWidget(self.container)






if __name__ == '__main__':
    app = QApplication([])     # funcion principal
    window = ProjectWindow()
    window.show()
    app.exec_()



