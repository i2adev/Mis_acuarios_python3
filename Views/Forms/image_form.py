"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      08/08/2025
Commentarios:
    Módulo que contiene los controles para la inserción de imagenes.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QApplication, QHBoxLayout, \
    QLabel, QSizePolicy, QPushButton, QSpacerItem


class ImageForm(QFrame):
    """
    Clase que contiene los controles para gestionar imagenes.
    """

    def __init__(self):
        """ Constructor de clase. """

        super().__init__()

        self.setMinimumWidth(150)

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Crea los widgets. """

        # Layouts
        ## Layout principal
        self.layout_form = QVBoxLayout()

        ## Layout controles
        self.layout_controls = QHBoxLayout()

        # Primera línea
        ## Label de la imagen
        self.label_image = QLabel()
        self.label_image.setObjectName("label_image")
        self.label_image.setSizePolicy(
            QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored
        )

        # Segunda línea
        ## Botón add
        self.button_add = QPushButton("+")
        self.button_add.setObjectName("button_add")
        self.button_add.setFixedWidth(20)
        ## Botón Remove
        self.button_remove = QPushButton("-")
        self.button_remove.setObjectName("button_remove")
        self.button_remove.setFixedWidth(20)
        ## Botón previo
        self.button_prev = QPushButton("<")
        self.button_prev.setObjectName("button_prev")
        self.button_prev.setFixedWidth(20)
        ## Label numero de imagen
        self.label_num_imagen = QLabel()
        self.label_num_imagen.setFixedWidth(30)
        self.label_num_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_num_imagen.setObjectName("label_num_imagen")
        ## Label DE
        self.label_de = QLabel(" DE ")
        self.label_de.setObjectName("DE")
        self.label_de.setFixedWidth(50)
        self.label_de.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ## Label número total de imagenes
        self.label_num_total_imegenes = QLabel()
        self.label_num_total_imegenes.setFixedWidth(30)
        self.label_num_total_imegenes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_num_total_imegenes.setObjectName("label_num_total_imegenes")
        ## Botón siguiente
        self.button_next = QPushButton(">")
        self.button_next.setObjectName("button_next")
        self.button_next.setFixedWidth(20)

    def build_layout(self):
        """ Construye el layout. """

        # Controles
        self.layout_controls.addWidget(self.button_add)
        self.layout_controls.addWidget(self.button_remove)
        self.layout_controls.addSpacerItem(
            QSpacerItem(50,10, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Fixed)
        )
        self.layout_controls.addWidget(self.button_prev)
        self.layout_controls.addWidget(self.label_num_imagen)
        self.layout_controls.addWidget(self.label_de)
        self.layout_controls.addWidget(self.label_num_total_imegenes)
        self.layout_controls.addWidget(self.button_next)

        # Montar el layout
        self.layout_form.addWidget(self.label_image)
        self.layout_form.addLayout(self.layout_controls)

        self.setLayout(self.layout_form)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ImageForm()
    ventana.show()

    sys.exit(app.exec())