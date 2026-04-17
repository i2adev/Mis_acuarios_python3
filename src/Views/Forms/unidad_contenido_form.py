"""
Autor: Inigo Iturriagaetxebarria
Fecha: 05/03/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad 
    UNIDAD DE CONTENIDO.
"""

import sys

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, \
    QLineEdit, \
    QPlainTextEdit, QApplication, QSpacerItem, QSizePolicy

from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit


class UnidadContenidoForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad unidad de 
    contenido.
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
        self.layout_unidad_contenido = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_unidad_contenido = QLabel("UNIDAD DE CONTENIDO")
        self.label_descripcion = QLabel("DESCRIPCION")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_unidad_contenido = StrLineEdit(
            control_name="UNIDAD DE CONTENIDO",
            max_length=32,
        )
        self.edit_unidad_contenido.setObjectName(
            "edit_unidad_contenido")
        self.edit_unidad_contenido.setToolTip(
            """
            <h2>Unidad de contenido</h2><br>
            En este campo se inserta la unidad en la que está tasada el 
            contenido del consumible.
            """
        )

        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción</h2><br>
            En este campo se insertan la descripción de la unidad del 
            contenido.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de filtro
        self.layout_unidad_contenido.addWidget(
            self.label_unidad_contenido)
        self.layout_unidad_contenido.addWidget(
            self.edit_unidad_contenido)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_unidad_contenido)
        self.layout_first_line.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Expanding)
        )

        # Segunda linea
        self.layout_observaciones.addWidget(self.label_descripcion)
        self.layout_observaciones.addWidget(self.text_descripcion)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = UnidadContenidoForm()
    ventana.show()

    sys.exit(app.exec())
