﻿"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Commentarios:
    Módulo que contiene los controles del formulario de la entidad CATE-
    GORÍA DE ACUARIO.
"""
import sys

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPlainTextEdit, QApplication

class CategoriaAcuarioForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad categoría
    de acuario.
    """

    def __init__(self):
        super().__init__()

        self.setFixedHeight(150)

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """
        # Layouts
        ## Layout principal
        self.layout_form = QVBoxLayout()

        ## Layout primera linea
        self.layout_first_line = QHBoxLayout()
        ### ID
        self.layout_id = QVBoxLayout()
        ### Tipo acuario
        self.layout_tipo_acuario = QVBoxLayout()
        ### Subtipo acuario
        self.layout_subtipo_acuario = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_tipo_acuario = QLabel("TIPO ACUARIO")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_categoria_acuario = QLineEdit()
        self.edit_categoria_acuario.setObjectName("edit_categoria_acuario")
        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_observaciones")

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de acuario
        self.layout_tipo_acuario.addWidget(self.label_tipo_acuario)
        self.layout_tipo_acuario.addWidget(self.edit_categoria_acuario)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_tipo_acuario)

        # Segunda linea
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_observaciones)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = CategoriaAcuarioForm()
    ventana.show()

    sys.exit(app.exec())