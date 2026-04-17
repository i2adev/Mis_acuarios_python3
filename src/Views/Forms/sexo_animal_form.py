"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/04/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad
    SEXO DEL ANIMAL.
"""

import sys

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPlainTextEdit, QApplication,
                             QSpacerItem, QSizePolicy)

from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit


class SexoAnimalForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad sexo del animal.
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
        ### Sexo del animal
        self.layout_sexo = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_sexo = QLabel("SEXO")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_sexo = StrLineEdit(
            control_name="SEXO",
            max_length=32,
        )
        self.edit_sexo.setObjectName("edit_sexo")
        self.edit_sexo.setToolTip(
            """
            <h2>Sexo</h2><br>
            En este campo se inserta el <b>sexo</b> del animal.
            """
        )

        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción</h2><br>
            En este campo se inserta la <b>descripción</b> del sexo.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Sexo del animal
        self.layout_sexo.addWidget(self.label_sexo)
        self.layout_sexo.addWidget(self.edit_sexo)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_sexo)
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

    ventana = SexoAnimalForm()
    ventana.show()

    sys.exit(app.exec())
