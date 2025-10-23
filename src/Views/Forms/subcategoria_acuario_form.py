"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/06/2025
Commentarios:
    Módulo que contiene los controles del formulario de la entidad TIPO DE
    ACUARIO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QFrame, QLabel, QLineEdit, QPlainTextEdit, \
    QVBoxLayout, QHBoxLayout, QApplication, QComboBox, QPushButton

class SubcategoriaAcuarioForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad tipo de acuario.
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
        ### Categoría acuario
        self.layout_categoria_acuario = QVBoxLayout()
        self.layout_edit_categoria_acuario = QHBoxLayout()
        ### Subtipo acuario
        self.layout_subcategoria_acuario = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_categoria_acuario = QLabel("CATEGORÍA ACUARIO")
        self.label_subcategoria_acuario = QLabel("SUBCATEGORÍA ACUARIO")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_subcategoria_acuario = QLineEdit()
        self.edit_subcategoria_acuario.setObjectName("edit_subcategoria_acuario")
        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_descripcion")

        # Combos
        self.combo_categoria_acuario = QComboBox()
        self.combo_categoria_acuario.setMinimumWidth(200)
        self.combo_categoria_acuario.setEditable(True)
        self.combo_categoria_acuario.setObjectName("combo_subcategoria_acuario")

        # Botones
        self.button_insert_categoria_acuario = QPushButton("<")
        self.button_insert_categoria_acuario.setFixedWidth(30)
        self.button_insert_categoria_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de acuario
        self.layout_edit_categoria_acuario.addWidget(
            self.combo_categoria_acuario
        )

        self.layout_edit_categoria_acuario.addWidget(
            self.button_insert_categoria_acuario
        )

        self.layout_categoria_acuario.addWidget(self.label_categoria_acuario)
        self.layout_categoria_acuario.addLayout(
            self.layout_edit_categoria_acuario
        )

        self.layout_subcategoria_acuario.addWidget(
            self.label_subcategoria_acuario
        )

        self.layout_subcategoria_acuario.addWidget(
            self.edit_subcategoria_acuario
        )

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_categoria_acuario)
        self.layout_first_line.addLayout(self.layout_subcategoria_acuario)

        # Segunda linea
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_observaciones)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = SubcategoriaAcuarioForm()
    ventana.show()

    sys.exit(app.exec())