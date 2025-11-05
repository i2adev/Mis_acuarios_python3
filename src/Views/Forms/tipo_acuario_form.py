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


class TipoAcuarioForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad tipo de acuario.
    """

    def __init__(self):
        super().__init__()

        # self.setFixedHeight(150)

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """
        # Layouts
        ## Layout principal
        self.layout_form = QVBoxLayout()

        ## Layout primera linea
        self.layout_first_line = QHBoxLayout()
        self.layout_first_line.setContentsMargins(0, 0, 0, 20)
        ### ID
        self.layout_id = QVBoxLayout()
        ### Tipo acuario
        self.layout_tipo_acuario = QVBoxLayout()
        self.layout_edit_tipo_acuario = QHBoxLayout()
        ### Subtipo acuario
        self.layout_subtipo_acuario = QVBoxLayout()
        self.layout_edit_subtipo_acuario = QHBoxLayout()

        ## Segunda linea
        # self.layout_second_line = QVBoxLayout()
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_tipo_acuario = QLabel("TIPO ACUARIO")
        self.label_subtipo_acuario = QLabel("SUBTIPO ACUARIO")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_descripcion")
        self.text_observaciones.setFixedHeight(75)

        # Combos
        self.combo_categoria_acuario = QComboBox()
        self.combo_categoria_acuario.setEditable(True)
        self.combo_categoria_acuario.setObjectName("combo_categoria_acuario")
        self.button_insert_tipo_acuario = QPushButton("<")
        self.button_insert_tipo_acuario.setFixedWidth(30)
        self.button_insert_tipo_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.combo_subcategoria_acuario = QComboBox()
        self.combo_subcategoria_acuario.setEditable(True)
        self.combo_subcategoria_acuario.setObjectName(
            "combo_subcategoria_acuario"
        )
        self.button_insert_subtipo_acuario = QPushButton("<")
        self.button_insert_subtipo_acuario.setFixedWidth(30)
        self.button_insert_subtipo_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de acuario
        self.layout_edit_tipo_acuario.addWidget(self.combo_categoria_acuario)
        self.layout_edit_tipo_acuario.addWidget(self.button_insert_tipo_acuario)
        self.layout_tipo_acuario.addWidget(self.label_tipo_acuario)
        self.layout_tipo_acuario.addLayout(self.layout_edit_tipo_acuario)

        ## Subtipo acuario
        self.layout_edit_subtipo_acuario.addWidget(
            self.combo_subcategoria_acuario
        )
        self.layout_edit_subtipo_acuario.addWidget(
            self.button_insert_subtipo_acuario
        )
        self.layout_subtipo_acuario.addWidget(self.label_subtipo_acuario)
        self.layout_subtipo_acuario.addLayout(self.layout_edit_subtipo_acuario)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_tipo_acuario)
        self.layout_first_line.addLayout(self.layout_subtipo_acuario)

        # Segunda linea
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_observaciones)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = TipoAcuarioForm()
    ventana.show()

    sys.exit(app.exec())
