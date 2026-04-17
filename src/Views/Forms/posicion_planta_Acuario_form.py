"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/03/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad
    POSICIÓN PLANTA ACUARIO.
"""

import sys

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPlainTextEdit, QApplication,
                             QSpacerItem, QSizePolicy)

from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit


class PosicionPlantaAcuarioForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad
    posición de planta en el acuario.
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
        self.layout_psicion = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_posicion = QLabel("POSICIÓN")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_posicion = StrLineEdit(
            control_name="POSICIÓN",
            max_length=32,
        )
        self.edit_posicion.setObjectName("edit_posicion")
        self.edit_posicion.setToolTip(
            """
            <h2>Posición</h2><br>
            En este campo se inserta la <b>posición de la planta</b> en el 
            acuario.
            """
        )

        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción</h2><br>
            En este campo se inserta la <b>descripción</b> de la posición de la 
            planta en el acuario.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Comportamiento del animal
        self.layout_psicion.addWidget(self.label_posicion)
        self.layout_psicion.addWidget(self.edit_posicion)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_psicion)
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

    ventana = PosicionPlantaAcuarioForm()
    ventana.show()

    sys.exit(app.exec())
