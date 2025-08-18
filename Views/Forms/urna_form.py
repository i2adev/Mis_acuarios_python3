"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Commentarios:
    Módulo que contiene los controles del formulario de la entidad ACUARIO.
"""

import sys

from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QFrame, QLabel, QLineEdit, QPlainTextEdit, \
    QVBoxLayout, QHBoxLayout, QApplication, QComboBox, QPushButton, QSpacerItem, \
    QSizePolicy


class UrnaForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad acuario.
    """

    def __init__(self):
        super().__init__()

        # self.setFixedHeight(275)

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """

        # Layouts
        ## Layout principal
        self.layout_main = QHBoxLayout()

        ## Layout del formulario
        self.layout_form = QVBoxLayout()

        ## Primera línea
        self.layout_first_line = QHBoxLayout()
        ### ID
        self.layout_id = QVBoxLayout()
        ## Marca
        self.layout_marca = QVBoxLayout()
        self.layout_combo_marca = QHBoxLayout()
        ## Modelo
        self.layout_modelo = QVBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        ### Ancho
        self.layout_ancho = QVBoxLayout()
        ### Profundo
        self.layout_profundo = QVBoxLayout()
        ### Alto
        self.layout_alto = QVBoxLayout()

        ## Tercera línea
        self.layout_third_line = QHBoxLayout()
        ### Grosor del cristal
        self.layout_grosor = QVBoxLayout()
        ### Volumen del tanque
        self.layout_volumen = QVBoxLayout()
        ### Material de la urna
        self.layout_material = QVBoxLayout()
        self.layout_combo_material = QHBoxLayout()

        ## Cuarta línea
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_marca = QLabel("MARCA ACUARIO")
        self.label_modelo = QLabel("MODELO ACUARIO")
        self.label_ancho = QLabel("ANCHO")
        self.label_profundo = QLabel("PROFUNDIDAD")
        self.label_alto = QLabel("ALTO")
        self.label_grosor = QLabel("GROSOR CRISTAL")
        self.label_volumen = QLabel("VOLUMEN TANQUE")
        self.label_material = QLabel("MATERIAL DE LA URNA")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")
        self.edit_modelo = QLineEdit()
        self.edit_modelo.setObjectName("edit_modelo")
        self.edit_ancho = QLineEdit()
        self.edit_ancho.setObjectName("edit_ancho")
        self.edit_ancho.setValidator(QIntValidator())
        self.edit_profundo = QLineEdit()
        self.edit_profundo.setObjectName("edit_profundo")
        self.edit_profundo.setValidator(QIntValidator())
        self.edit_alto = QLineEdit()
        self.edit_alto.setObjectName("edit_alto")
        self.edit_alto.setValidator(QIntValidator())
        self.edit_grosor = QLineEdit()
        self.edit_grosor.setObjectName("edit_grosor")
        self.edit_grosor.setValidator(QIntValidator())
        self.edit_volumen = QLineEdit()
        self.edit_volumen.setObjectName("edit_volumen")
        self.edit_volumen.setValidator(QIntValidator())
        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")

        # Combos
        self.combo_marca = QComboBox()
        self.combo_marca.setMinimumWidth(250)
        self.combo_marca.setObjectName("combo_marca")
        self.combo_material = QComboBox()
        self.combo_material.setMinimumWidth(250)
        self.combo_material.setObjectName("combo_material")

        # Botones
        self.button_insert_marca = QPushButton("<")
        self.button_insert_marca.setObjectName("button_insert_marca")
        self.button_insert_marca.setFixedWidth(30)
        self.button_insert_material = QPushButton("<")
        self.button_insert_material.setObjectName("button_insert_material")
        self.button_insert_material.setFixedWidth(30)

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera línea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Marca de acuario
        self.layout_combo_marca.addWidget(self.combo_marca)
        self.layout_combo_marca.addWidget(self.button_insert_marca)
        self.layout_marca.addWidget(self.label_marca)
        self.layout_marca.addLayout(self.layout_combo_marca)

        ## Modelo de acuario
        self.layout_modelo.addWidget(self.label_modelo)
        self.layout_modelo.addWidget(self.edit_modelo)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_marca)
        self.layout_first_line.addLayout(self.layout_modelo)

        # Segunda línea
        ## Ancho acuario
        self.layout_ancho.addWidget(self.label_ancho)
        self.layout_ancho.addWidget(self.edit_ancho)

        ## Profundidad acuario
        self.layout_profundo.addWidget(self.label_profundo)
        self.layout_profundo.addWidget(self.edit_profundo)

        ## Alto acuario
        self.layout_alto.addWidget(self.label_alto)
        self.layout_alto.addWidget(self.edit_alto)

        ## Montamos la segunda línea
        self.layout_second_line.addLayout(self.layout_ancho)
        self.layout_second_line.addLayout(self.layout_profundo)
        self.layout_second_line.addLayout(self.layout_alto)

        # Tercera línea
        ## Grosor del cristal
        self.layout_grosor.addWidget(self.label_grosor)
        self.layout_grosor.addWidget(self.edit_grosor)

        ## Volumen del tanque
        self.layout_volumen.addWidget(self.label_volumen)
        self.layout_volumen.addWidget(self.edit_volumen)

        ## Material urna
        self.layout_combo_material.addWidget(self.combo_material)
        self.layout_combo_material.addWidget(self.button_insert_material)
        self.layout_material.addWidget(self.label_material)
        self.layout_material.addLayout(self.layout_combo_material)

        ## Montamos la tercera línea
        self.layout_third_line.addLayout(self.layout_grosor)
        self.layout_third_line.addLayout(self.layout_volumen)
        self.layout_third_line.addLayout(self.layout_material)

        # Cuarta línea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        ## Montamos el formulario
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_third_line)
        self.layout_form.addLayout(self.layout_descripcion)
        self.layout_main.addLayout(self.layout_form)

        self.setLayout(self.layout_main)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = UrnaForm()
    ventana.setFixedWidth(800)
    ventana.setFixedHeight(600)
    ventana.show()

    sys.exit(app.exec())
