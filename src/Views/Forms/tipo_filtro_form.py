"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      21/07/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad TIPO DE
    FILTRO.
"""

import sys

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPlainTextEdit, QApplication, QSpacerItem, QSizePolicy


class TipoFiltroForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad categoría
    de acuario.
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
        ### Tipo filtro
        self.layout_tipo_filtro = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_tipo_filtro = QLabel("TIPO FILTRO")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_tipo_filtro = QLineEdit()
        self.edit_tipo_filtro.setObjectName("edit_tipo_filtro")
        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_descripcion")
        self.text_observaciones.setFixedHeight(75)

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de filtro
        self.layout_tipo_filtro.addWidget(self.label_tipo_filtro)
        self.layout_tipo_filtro.addWidget(self.edit_tipo_filtro)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_tipo_filtro)
        self.layout_first_line.addSpacerItem(
            QSpacerItem(100, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Fixed)
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

    ventana = TipoFiltroForm()
    ventana.show()

    sys.exit(app.exec())
