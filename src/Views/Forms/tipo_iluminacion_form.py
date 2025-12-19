"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/12/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad TIPO DE
    ILUMINACIÓN.
"""

import sys

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPlainTextEdit, QApplication,
                             QSpacerItem, QSizePolicy)


class TipoIluminacionForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad tipo de 
    iluminación.
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
        ### Tipo de iluminación
        self.layout_tipo_iluminacion = QVBoxLayout()

        ## Segunda linea
        ### Descripción
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_tipo_iluminacion = QLabel("TIPO DE ILUMINACIÓN")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_tipo_iluminacion = QLineEdit()
        self.edit_tipo_iluminacion.setObjectName("edit_tipo_iluminacion")
        self.edit_tipo_iluminacion.setToolTip(
            """
            <h2>Tipo de iluminación</h2>
            En este campo se inserta el tipo de iluminación Este campo es 
            <b>obligatorio</b>.
            """
        )

        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setFixedHeight(75)
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción del tipo de iluminación</h2>
            En este campo se inserta la descripción del tipo de iluminación.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de iluminación
        self.layout_tipo_iluminacion.addWidget(self.label_tipo_iluminacion)
        self.layout_tipo_iluminacion.addWidget(self.edit_tipo_iluminacion)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_tipo_iluminacion)

        # Segunda linea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_descripcion)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = TipoIluminacionForm()
    ventana.show()

    sys.exit(app.exec())
