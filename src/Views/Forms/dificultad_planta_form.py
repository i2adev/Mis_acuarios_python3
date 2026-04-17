"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      13/03/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad
    DIFICULTAD DE PLANTAS.
"""

import sys

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPlainTextEdit, QApplication,
                             QSpacerItem, QSizePolicy)

from CustomControls.int_line_edit import IntLineEdit
from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit


class DificultadPlantaForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad
    dieta de fauna.
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
        ### Nivel
        self.layout_nivel = QVBoxLayout()
        ### Dificultad
        self.layout_dificultad = QVBoxLayout()

        ## Segunda linea
        ### Descripción
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_nivel = QLabel("NIVEL")
        self.label_dificultad = QLabel("DIFICULTAD")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_nivel = IntLineEdit(
            control_name="NIVEL",
            min_value=1,
            max_value=10,
        )
        self.edit_nivel.setFixedWidth(50)
        self.edit_nivel.setObjectName("edit_nivel")
        self.edit_nivel.setToolTip(
            """
            <h2>Nivel</h2><br>
            En este campo se inserta el indice numérico que representa la 
            <b>dificultad de mantenimiento</b> de la planta.
            """
        )

        self.edit_dificultad = StrLineEdit(
            control_name="DIFICULTAD",
            max_length=15,
        )
        self.edit_dificultad.setObjectName("edit_dificultad")
        self.edit_dificultad.setToolTip(
            """
            <h2>Dificultad de mantenimiento</h2><br>
            En este campo se inserta la <b>dificultad</b> de mantenimiento 
            de la planta.
            """
        )

        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción</h2><br>
            En este campo se insertan la <b>descripción</b> de la 
            dificultad de mantenimiento.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Nivel
        self.layout_nivel.addWidget(self.label_nivel)
        self.layout_nivel.addWidget(self.edit_nivel)

        ## Comportamiento del animal
        self.layout_dificultad.addWidget(self.label_dificultad)
        self.layout_dificultad.addWidget(self.edit_dificultad)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_nivel)
        self.layout_first_line.addLayout(self.layout_dificultad)
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

    ventana = DietaFaunaForm()
    ventana.show()

    sys.exit(app.exec())
