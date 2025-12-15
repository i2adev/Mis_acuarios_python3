"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      11/12/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad 
    ATEGORÍA DE EQUIPAMIENTO.
"""

import sys

from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, \
    QLineEdit, QPlainTextEdit, QVBoxLayout


class CategoriaEquipamientoForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad categoría
    de equipamiento.
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
        ### Categoría de equipamiento
        self.layout_categoria_equipamiento = QVBoxLayout()

        ## Segunda linea
        ### Descripción
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_categoria_equipamiento = QLabel("CATEGORÍA DE EQUIPAMIENTO")
        self.label_observaciones = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_categoria_equipamiento = QLineEdit()
        self.edit_categoria_equipamiento.setObjectName(
            "edit_categoria_equipamiento")
        self.edit_categoria_equipamiento.setToolTip(
            """
            <h2>Categoría de equipamiento</h2>
            En este campo se inserta la categoría a la que pertenece el 
            equipamiento. Este campo es <b>obligatorio</b>.
            """
        )

        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setFixedHeight(75)
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción de la categoría</h2>
            En este campo se inserta la descripción de la categoría del 
            equipamiento.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de filtro
        self.layout_categoria_equipamiento.addWidget(
            self.label_categoria_equipamiento)
        self.layout_categoria_equipamiento.addWidget(
            self.edit_categoria_equipamiento)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_categoria_equipamiento)

        # Segunda linea
        self.layout_descripcion.addWidget(self.label_observaciones)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_descripcion)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = CategoriaEquipamientoForm()
    ventana.show()

    sys.exit(app.exec())
