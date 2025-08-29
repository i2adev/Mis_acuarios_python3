"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Commentarios:
    Módulo que contiene los controles del formulario de la entidad TIPO DE
    ACUARIO.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QFrame, QLabel, QLineEdit, QPlainTextEdit, \
    QVBoxLayout, QHBoxLayout, QApplication, QComboBox, QPushButton

class SubcategoriaIncidenciaForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad subtipo de 
    incidencia.
    """

    def __init__(self):
        super().__init__()

        self.setFixedHeight(150)

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """

        # Layouts
        ## Layout principal
        self.layout_form = QVBoxLayout()

        ## Layout primera linea
        self.layout_first_line = QHBoxLayout()
        ### ID
        self.layout_id = QVBoxLayout()
        ### Categoría acuario
        self.layout_categoria_incidencia = QVBoxLayout()
        self.layout_combo_categoria_incidencia = QHBoxLayout()
        ### Subtipo acuario
        self.layout_subcategoria_incidencia = QVBoxLayout()

        ## Segunda linea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_categoria_incidencia = QLabel("CATEGORÍA INCIDENCIA")
        self.label_subcategoria_incidencia = QLabel("SUBCATEGORÍA INCIDENCIA")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_subcategoria_incidencia = QLineEdit()
        self.edit_subcategoria_incidencia.setObjectName(
            "edit_subcategoria_incidencia"
        )
        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_descripcion")

        # Combos
        self.combo_categoria_incidencia = QComboBox()
        self.combo_categoria_incidencia.setMinimumWidth(200)
        self.combo_categoria_incidencia.setEditable(True)
        self.combo_categoria_incidencia.setObjectName(
            "combo_subcategoria_acuario"
        )

        # Botones
        self.button_insert_categoria_incidencia = QPushButton("<")
        self.button_insert_categoria_incidencia.setFixedWidth(30)
        self.button_insert_categoria_incidencia.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de incidencia
        self.layout_combo_categoria_incidencia.addWidget(
            self.combo_categoria_incidencia
        )
        self.layout_combo_categoria_incidencia.addWidget(
            self.button_insert_categoria_incidencia
        )
        self.layout_categoria_incidencia.addWidget(self.label_categoria_incidencia)
        self.layout_categoria_incidencia.addLayout(
            self.layout_combo_categoria_incidencia
        )
        self.layout_subcategoria_incidencia.addWidget(
            self.label_subcategoria_incidencia
        )
        self.layout_subcategoria_incidencia.addWidget(
            self.edit_subcategoria_incidencia
        )

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_categoria_incidencia)
        self.layout_first_line.addLayout(self.layout_subcategoria_incidencia)

        # Segunda linea
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_observaciones)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = SubcategoriaIncidenciaForm()
    ventana.show()

    sys.exit(app.exec())