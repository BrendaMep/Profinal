from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QSlider, QDial, QDoubleSpinBox, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy


class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.container = QWidget()

        self.main_layout = QHBoxLayout()
        self.lyt_settings = QVBoxLayout()
        self.lyt_graph = QHBoxLayout()

        self.lyt_x0 = QFormLayout()
        self.lyt_y0 = QFormLayout()

        self.lbl_x0 = QLabel()
        self.lnedt_x0 = QLineEdit()

        self.lbl_y0 = QLabel()
        self.lnedt_y0 = QLineEdit()

        self.btn_graph = QPushButton()



        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Proyecto Busquedas")

        self.lbl_x0.setText('Inicio')
        self.lnedt_x0.setText('A')
        self.lbl_x0.setFixedWidth(50)
        self.lnedt_x0.setFixedWidth(100)
        self.lbl_x0.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.lnedt_x0.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.lbl_y0.setText('Final')
        self.lnedt_y0.setText('B')
        self.lbl_y0.setFixedWidth(50)
        self.lnedt_y0.setFixedWidth(100)
        self.lbl_y0.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.lnedt_y0.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        self.btn_graph.setText('Trazar ruta')
        self.btn_graph.setFixedWidth(165)
        self.btn_graph.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Functionality
        self.lyt_x0.addRow(self.lbl_x0, self.lnedt_x0)
        self.lyt_y0.addRow(self.lbl_y0, self.lnedt_y0)

        self.main_layout.addLayout(self.lyt_settings)
        self.main_layout.addLayout(self.lyt_graph)
        self.container.setLayout(self.main_layout)

        self.lyt_settings.addLayout(self.lyt_x0)
        self.lyt_settings.addLayout(self.lyt_y0)
        self.lyt_settings.addWidget(self.btn_graph)


        self.setCentralWidget(self.container)



if __name__ == '__main__':
    app = QApplication([])
    window = ProjectWindow()
    window.show()
    app.exec_()