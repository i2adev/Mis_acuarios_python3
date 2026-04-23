"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/03/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad
    REQUERIMIENTO DE CO2.
"""

import sys

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPlainTextEdit, QApplication,
                             QSpacerItem, QSizePolicy)

import globales
from CustomControls.int_line_edit import IntLineEdit
from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit


class RequerimientoCO2Form(QFrame):
    """
    Clase que contiene los controles de edición de la entidad requerimiento 
    de CO2.
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
        ### Posicion de la planta en el acuario
        self.layout_requerimiento = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_requerimiento = QLabel("REQUERIMIENTO CO2")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = IntLineEdit(
            control_name="ID",
            min_value=0,
            max_value=globales.INT32_MAX_VALUE
        )
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_requerimiento = StrLineEdit(
            control_name="REQUERIMIENTO CO2",
            max_length=32,
        )
        self.edit_requerimiento.setObjectName("edit_requerimiento")
        self.edit_requerimiento.setToolTip(
            """
            <h2>Requerimiento de CO<sub>2</sub></h2><br>
            En este campo se inserta el <b>requerimiento</b> de CO<sub>2</sub>.
            """
        )

        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción</h2><br>
            En este campo se inserta la <b>descripción</b> del requerimiento.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Comportamiento del animal
        self.layout_requerimiento.addWidget(self.label_requerimiento)
        self.layout_requerimiento.addWidget(self.edit_requerimiento)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_requerimiento)
        self.layout_first_line.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Expanding)
        )

        # Segunda linea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_descripcion)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = RequerimientoCO2Form()
    ventana.show()

    sys.exit(app.exec())
