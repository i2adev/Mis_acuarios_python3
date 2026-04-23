"""
Autor: Inigo Iturriagaetxebarria
Fecha: 04/03/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad 
    FORMATO DE CONSUMIBLE.
"""

import sys

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPlainTextEdit, QApplication,
                             QSpacerItem, QSizePolicy)

import globales
from CustomControls.int_line_edit import IntLineEdit
from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit


class FormatoCunsumibleForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad formato
    de consumible.
    """

    def __init__(self):
        super().__init__()

        self.setFixedHeight(200)

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
        ### Tipo filtro
        self.layout_formato_consumible = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_formato_consumible = QLabel("FORMATO DE CONSUMIBLE")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = IntLineEdit(
            control_name="ID",
            min_value=0,
            max_value=globales.INT32_MAX_VALUE
        )
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_formato_consumible = StrLineEdit(
            control_name="FORMATO DE CONSUMIBLE",
            max_length=32,
        )
        self.edit_formato_consumible.setObjectName(
            "edit_formato_consumible")
        self.edit_formato_consumible.setToolTip(
            """
            <h2>Formato de consumible</h2><br>
            En este campo se inserta el formato en el que viene el consumible.
            """
        )

        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción</h2><br>
            En este campo se insertan la descripción sobre la categoría de 
            consumible.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Formato de consumible
        self.layout_formato_consumible.addWidget(
            self.label_formato_consumible)
        self.layout_formato_consumible.addWidget(
            self.edit_formato_consumible)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_formato_consumible)
        self.layout_first_line.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Expanding)
        )

        # Segunda linea
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_descripcion)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = FormatoCunsumibleForm()
    ventana.show()

    sys.exit(app.exec())
