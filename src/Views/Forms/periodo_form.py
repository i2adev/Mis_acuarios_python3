"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      06/04/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad
    PERIODO.
"""

import sys

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QApplication, QSpacerItem, QSizePolicy)

from CustomControls.str_line_edit import StrLineEdit


class PeriodoForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad requerimiento 
    de iluminación.
    """

    def __init__(self):
        super().__init__()

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
        ### Periodo
        self.layout_periodo = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_periodo = QLabel("PERIODO")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_periodo = StrLineEdit(
            control_name="PERIODO",
            max_length=32,
        )
        self.edit_periodo.setObjectName("edit_periodo")
        self.edit_periodo.setToolTip(
            """
            <h2>Periodo</h2><br>
            En este campo se inserta el <b>periodo</b> de tiempo.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Periodo
        self.layout_periodo.addWidget(self.label_periodo)
        self.layout_periodo.addWidget(self.edit_periodo)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_periodo)
        self.layout_first_line.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Expanding)
        )

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = PeriodoForm()
    ventana.show()

    sys.exit(app.exec())
