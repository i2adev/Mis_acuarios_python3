"""
Autor: Inigo Iturriagaetxebarria
Fecha: 08/10/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad ESTADO
    DE PROYECTO.
"""

import sys

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPlainTextEdit, QApplication, QSpacerItem, QSizePolicy


class EstadoProyectoForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad categoría
    de acuario.
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
        self.layout_estado_proyecto = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_estado_proyecto = QLabel("ESTADO DEL PROYECTO")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_estado_proyecto = QLineEdit()
        self.edit_estado_proyecto.setObjectName("edit_estado_proyecto")
        self.edit_estado_proyecto.setToolTip(
            """
            <h2>Estado del proyecto</h2><br>
            En este campo se inserta el estado que puede tomar un proyecto (
            Planificación, en curso, finalizado, cancelado, etc).
            """
        )

        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_descripcion")
        self.text_observaciones.setToolTip(
            """
            <h2>Observaciones</h2><br>
            En este campo se insertan las observaciones sobre el estado del 
            proyecto.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de filtro
        self.layout_estado_proyecto.addWidget(self.label_estado_proyecto)
        self.layout_estado_proyecto.addWidget(self.edit_estado_proyecto)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_estado_proyecto)
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

    ventana = EstadoProyectoForm()
    ventana.show()

    sys.exit(app.exec())
