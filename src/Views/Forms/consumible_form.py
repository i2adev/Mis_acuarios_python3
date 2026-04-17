"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad ACUARIO.
"""

import sys

from CustomControls.combo_box import ComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QPlainTextEdit, QPushButton,
                             QVBoxLayout)

from CustomControls.double_line_edit import DoubleLineEdit
from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit


class ConsumibleForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad COSUMIBLE.
    """

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """

        # Layouts
        ## Layout del formulario
        self.layout_form = QVBoxLayout()  # Layout del formulario

        ## Primera línea
        self.layout_first_line = QHBoxLayout()  # Layout de la promera linea
        self.layout_first_line.setContentsMargins(0, 0, 0, 20)
        ### ID
        self.layout_id = QVBoxLayout()
        ### Marca
        self.layout_marca = QVBoxLayout()
        self.layout_combo_marca = QHBoxLayout()
        ### Producto
        self.layout_producto = QVBoxLayout()
        ### Categoría de consumible
        self.layout_categoria = QVBoxLayout()
        self.layout_combo_categoria = QHBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        self.layout_second_line.setContentsMargins(0, 0, 0, 20)
        ### Formato
        self.layout_formato = QVBoxLayout()
        self.layout_combo_formato = QHBoxLayout()
        ### Contenido
        self.layout_contenido = QVBoxLayout()
        ### Unidad
        self.layout_unidad = QVBoxLayout()
        self.layout_h_contenido = QHBoxLayout()

        ## Cuarta línea
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_marca = QLabel("MARCA")
        self.label_producto = QLabel("NOMBRE DEL PRODUCTO")
        self.label_categoria = QLabel("CATEGORÍA DE CONSUMIBLE")
        self.label_formato = QLabel("FORMATO DEL PRODUCTO")
        self.label_contenido = QLabel("CONTENIDO")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")

        self.edit_producto = StrLineEdit(
            control_name="PRODUCTO",
            max_length=32,
        )
        self.edit_producto.setObjectName("edit_producto")
        self.edit_producto.setMinimumWidth(250)
        self.edit_producto.setToolTip(
            """
            <h2>Producto</h2><br>
            En este campo se inserta el nombre comercial del producto.
            """
        )

        self.edit_contenido = DoubleLineEdit(control_name="CONTENIDO",
                                             units=None,
                                             min_value=10,
                                             max_value=2_000)
        self.edit_contenido.setObjectName("edit_contenido")
        self.edit_contenido.setToolTip(
            """
            <h2>Contenido</h2><br>
            En este campo se inserta el volumen/cantidad de 
            liquido/tastillas/tabletas que contiene el envase del producto.
            """
        )

        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setFixedHeight(75)
        self.text_descripcion.setToolTip(
            """ <h2>Descripción del producto</h2><br>
            En este campo se incluirá una breve descripción del producto.
            Se incluirán las características del mismo.
            """
        )

        # Combos
        self.combo_marca = ComboBox("MARCA")
        self.combo_marca.setObjectName("combo_marca")
        self.combo_marca.setEditable(True)
        self.combo_marca.setMinimumWidth(200)
        self.combo_marca.setToolTip(
            """
            <h2>Marca</h2><br>
            En este campo se seleccionará la marca del producto consumible.
            """
        )

        self.combo_categoria = ComboBox("CATEGORÍA DE CONSUMIBLE")
        self.combo_categoria.setMinimumWidth(250)
        self.combo_categoria.setObjectName("combo_categoria")
        self.combo_categoria.setEditable(True)
        self.combo_categoria.setToolTip(
            """
            <h2>Categoría</h2><br>
            En este campo se selecciona la categoría a la que pertenece el 
            producto.
            """
        )

        self.combo_formato = ComboBox("FORMATO DE CONSUMIBLE")
        self.combo_formato.setMinimumWidth(200)
        self.combo_formato.setObjectName("combo_formato")
        self.combo_formato.setEditable(True)
        self.combo_formato.setToolTip(
            """
            <h2>Formato</h2><br>
            En este campo se selecciona el formato en el que se presenta el 
            consumible.
            """
        )

        self.combo_unidad = ComboBox("UNIDAD")
        self.combo_unidad.setMinimumWidth(200)
        self.combo_unidad.setObjectName("combo_unidad")
        self.combo_unidad.setEditable(True)
        self.combo_unidad.setToolTip(
            """
            <h2>Unidad</h2><br>
            En este campo se selecciona la unidad fisica en la que se 
            presenta el producto.
            """
        )

        # Botones
        self.button_insert_marca = QPushButton("<")
        self.button_insert_marca.setObjectName("button_insert_marca")
        self.button_insert_marca.setFixedWidth(30)
        self.button_insert_marca.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_insert_categoria = QPushButton("<")
        self.button_insert_categoria.setObjectName(
            "button_insert_categoria")
        self.button_insert_categoria.setFixedWidth(30)
        self.button_insert_categoria.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_insert_formato = QPushButton("<")
        self.button_insert_formato.setObjectName(
            "button_insert_formato")
        self.button_insert_formato.setFixedWidth(30)
        self.button_insert_formato.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_insert_unidad = QPushButton("<")
        self.button_insert_unidad.setObjectName(
            "button_insert_unidad")
        self.button_insert_unidad.setFixedWidth(30)
        self.button_insert_unidad.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera línea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Marca
        self.layout_combo_marca.addWidget(self.combo_marca)
        self.layout_combo_marca.addWidget(self.button_insert_marca)
        self.layout_marca.addWidget(self.label_marca)
        self.layout_marca.addLayout(self.layout_combo_marca)

        ## Producto
        self.layout_producto.addWidget(self.label_producto)
        self.layout_producto.addWidget(self.edit_producto)

        ## Categoría de consumible
        self.layout_combo_categoria.addWidget(self.combo_categoria)
        self.layout_combo_categoria.addWidget(
            self.button_insert_categoria)
        self.layout_categoria.addWidget(self.label_categoria)
        self.layout_categoria.addLayout(self.layout_combo_categoria)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_marca)
        self.layout_first_line.addLayout(self.layout_producto)
        self.layout_first_line.addLayout(self.layout_categoria)

        # Segunda línea
        ## Formato
        self.layout_combo_formato.addWidget(self.combo_formato)
        self.layout_combo_formato.addWidget(self.button_insert_formato)
        self.layout_formato.addWidget(self.label_formato)
        self.layout_formato.addLayout(self.layout_combo_formato)
        ## Contenido
        self.layout_h_contenido.addWidget(self.edit_contenido)
        self.layout_h_contenido.addWidget(self.combo_unidad)
        self.layout_h_contenido.addWidget(self.button_insert_unidad)
        self.layout_contenido.addWidget(self.label_contenido)
        self.layout_contenido.addLayout(self.layout_h_contenido)
        ## Montamos la segunda línea
        self.layout_second_line.addLayout(self.layout_formato)
        self.layout_second_line.addLayout(self.layout_contenido)

        # Tercera línea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        ## Montamos el formulario
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_descripcion)
        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ConsumibleForm()
    ventana.setFixedWidth(800)
    ventana.setFixedHeight(600)
    ventana.show()

    sys.exit(app.exec())
