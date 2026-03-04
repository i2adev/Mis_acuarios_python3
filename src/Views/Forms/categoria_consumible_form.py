"""
Autor: Inigo Iturriagaetxebarria
Fecha: 04/03/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad 
    CATEGORÍA DE CONSUMIBLE.
"""

import sys

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, \
    QLineEdit, \
    QPlainTextEdit, QApplication, QSpacerItem, QSizePolicy

from CustomControls.str_line_edit import StrLineEdit


class CategoriaCunsumibleForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad categoría
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
        self.layout_categoria_consumible = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_categoria_consumible = QLabel("CATEGORÍA DE CONSUMIBLE")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_categoria_consumible = StrLineEdit(
            control_name="CATEGORÍA DE CONSUMIBLE",
            max_length=32,
        )
        self.edit_categoria_consumible.setObjectName(
            "edit_categoria_consumible")
        self.edit_categoria_consumible.setToolTip(
            """
            <h2>Categoría de consumible</h2><br>
            En este campo se inserta la categoría a la que pertenece un 
            consumible.
            """
        )

        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_descripcion")
        self.text_observaciones.setToolTip(
            """
            <h2>Observaciones</h2><br>
            En este campo se insertan las observaciones sobre la 
            categoría de consumible.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de filtro
        self.layout_categoria_consumible.addWidget(
            self.label_categoria_consumible)
        self.layout_categoria_consumible.addWidget(
            self.edit_categoria_consumible)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_categoria_consumible)
        self.layout_first_line.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Expanding)
        )

        # Segunda linea
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_observaciones)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = CategoriaCunsumibleForm()
    ventana.show()

    sys.exit(app.exec())
