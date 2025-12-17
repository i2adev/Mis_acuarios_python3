"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      17/12/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad ACUARIO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QIntValidator, QDoubleValidator
from PyQt6.QtWidgets import QFrame, QLabel, QLineEdit, QPlainTextEdit, \
    QVBoxLayout, QHBoxLayout, QApplication, QComboBox, QPushButton, QGroupBox, \
    QCheckBox

from CustomControls.nullable_date_edit import NullableDateEdit


class EquipamientoForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad EQUIPAMIENTO.
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
        self.layout_first_line = QHBoxLayout()
        self.layout_first_line.setContentsMargins(0, 0, 0, 20)

        ### ID
        self.layout_id = QVBoxLayout()

        ### Categoría de equipamiento
        self.layout_categoria_equipamiento = QVBoxLayout()
        self.layout_combo_categoria_equipamiento = QHBoxLayout()

        ### Marca del equipo
        self.layout_marca = QVBoxLayout()
        self.layout_combo_marca = QHBoxLayout()

        ### Modelo
        self.layout_modelo = QVBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        self.layout_volumenes_acuario_filtro = QHBoxLayout()
        self.layout_consumos_acuario_filtro = QHBoxLayout()
        self.layout_dimensiones_filtro = QHBoxLayout()
        self.layout_second_line.setContentsMargins(0, 0, 0, 20)

        ### Número de serie
        self.layout_num_serie = QVBoxLayout()

        ### Fecha alta
        self.layout_fecha_alta = QVBoxLayout()

        ### Fecha baja
        self.layout_fecha_baja = QVBoxLayout()

        ### Motivo de baja
        self.layout_motivo_baja = QVBoxLayout()

        ## Tercera línea
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_categoria_equipamiento = QLabel("CATEGORÍA")
        self.label_marca = QLabel("MARCA")
        self.label_modelo = QLabel("MODELO")
        self.label_num_serie = QLabel("NÚMERO DE SERIE")
        self.label_fecha_alta = QLabel("ALTA")
        self.label_fecha_baja = QLabel("BAJA")
        self.label_motivo_baja = QLabel("MOTIVO DE LA BAJA")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")

        self.edit_modelo = QLineEdit()
        self.edit_modelo.setMinimumWidth(250)
        self.edit_modelo.setObjectName("edit_modelo")
        self.edit_modelo.setToolTip(
            """
            <h2>Modelo deL equipo</h2><br>
            En este campo se inserta el modelo del equipo. Este es un campo 
            <b>obligatorio</b>.
            """
        )

        self.edit_num_serie = QLineEdit()
        self.edit_num_serie.setMinimumWidth(250)
        self.edit_num_serie.setObjectName("edit_num_serie")
        self.edit_num_serie.setToolTip(
            """
            <h2>Número de serie</h2><br>
            En este campo se inserta el número de serie del equipo. Este es un 
            campo <b>obligatorio</b>.
            """
        )

        self.edit_motivo_baja = QLineEdit()
        self.edit_motivo_baja.setObjectName("edit_motivo_baja")
        self.edit_motivo_baja.setToolTip(
            """
            <h2>Motivo baja del equipo</h2>
            En este campo se inserta el motivo por el que se le ha dado de 
            baja al equipo. En caso de que se encuentre en tono rojo, 
            el control está deshabilitado porque no se ha insertado una 
            fecha de baja.
            """
        )

        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setMinimumHeight(75)
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción del equipo</h2>
            En este campo se inserta la descripción del equipo, asi como las 
            carácteristicas mas relevantes.
            """
        )

        # Combos
        self.combo_categoria_equipamiento = QComboBox()
        self.combo_categoria_equipamiento.setObjectName(
            "combo_categoria_equipamiento")
        self.combo_categoria_equipamiento.setMinimumWidth(250)
        self.combo_categoria_equipamiento.setEditable(True)
        self.combo_categoria_equipamiento.setToolTip(
            """
            <h2>Categoría de equipamiento</h2>
            En este campo se selecciona la categoría a la que pertenece este 
            equipo. Este es un campo <b>obligatorio<b>.
            """
        )

        self.combo_marca = QComboBox()
        self.combo_marca.setMinimumWidth(250)
        self.combo_marca.setObjectName("combo_marca")
        self.combo_marca.setEditable(True)
        self.combo_marca.setToolTip(
            """
            <h2>Marca del equipo</h2>
            En este campo se selecciona la marca del equipo (EHEIM, JBL, 
            Aquael, etc). Si la marca del equipo no se encuentra en la 
            lista, puedes insertar uno pulsando en el botón de la 
            derecha. Este es un campo <b>obligatorio<b>.
            """
        )

        # Date pickers
        self.fecha_alta = NullableDateEdit()
        self.fecha_alta.setObjectName("fecha_alta")
        self.fecha_alta.setToolTip(
            """
            <h2>Fecha de alta</h2>
            En este campo se inserta la fecha den la que se da de alta el 
            equipo. Este es un campo <b>obligatorio<b>.
            """
        )

        self.fecha_baja = NullableDateEdit()
        self.fecha_baja.setObjectName("fecha_baja")
        self.fecha_baja.setToolTip(
            """
            <h2>Fecha de baja</h2>
            En este campo se inserta la fecha en la que se da de baja al 
            equipo.
            """
        )

        # Botones
        self.button_insert_cat_equipamiento = QPushButton("<")
        self.button_insert_cat_equipamiento.setObjectName(
            "button_insert_cat_equipamiento")
        self.button_insert_cat_equipamiento.setFixedWidth(30)
        self.button_insert_cat_equipamiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_insert_marca = QPushButton("<")
        self.button_insert_marca.setObjectName(
            "button_insert_marca")
        self.button_insert_marca.setFixedWidth(30)
        self.button_insert_marca.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        # GroupBox
        self.group_fechas = QGroupBox("FECHAS")

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera línea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Categoría del equipamiento
        self.layout_combo_categoria_equipamiento.addWidget(
            self.combo_categoria_equipamiento)
        self.layout_combo_categoria_equipamiento.addWidget(
            self.button_insert_cat_equipamiento)
        self.layout_categoria_equipamiento.addWidget(
            self.label_categoria_equipamiento)
        self.layout_categoria_equipamiento.addLayout(
            self.layout_combo_categoria_equipamiento)

        ## Marca comercial
        self.layout_combo_marca.addWidget(self.combo_marca)
        self.layout_combo_marca.addWidget(self.button_insert_marca)
        self.layout_marca.addWidget(self.label_marca)
        self.layout_marca.addLayout(self.layout_combo_marca)

        ## Modelo
        self.layout_modelo.addWidget(self.label_modelo)
        self.layout_modelo.addWidget(self.edit_modelo)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_categoria_equipamiento)
        self.layout_first_line.addLayout(self.layout_marca)
        self.layout_first_line.addLayout(self.layout_marca)
        self.layout_first_line.addLayout(self.layout_modelo)

        # Segunda línea
        self.layout_fechas = QHBoxLayout()

        ## Número de serie
        self.layout_num_serie.addWidget(self.label_num_serie)
        self.layout_num_serie.addWidget(self.edit_num_serie)

        ## Fecha de alta
        self.layout_fecha_alta.addWidget(self.label_fecha_alta)
        self.layout_fecha_alta.addWidget(self.fecha_alta)

        ## Fecha de baja
        self.layout_fecha_baja.addWidget(self.label_fecha_baja)
        self.layout_fecha_baja.addWidget(self.fecha_baja)

        ## Motivo de baja
        self.layout_motivo_baja.addWidget(self.label_motivo_baja)
        self.layout_motivo_baja.addWidget(self.edit_motivo_baja)

        ## Montamos la segunda línea
        self.layout_second_line.addLayout(self.layout_num_serie)

        self.layout_fechas.addLayout(self.layout_fecha_alta)
        self.layout_fechas.addLayout(self.layout_fecha_baja)
        self.group_fechas.setLayout(self.layout_fechas)
        self.layout_second_line.addWidget(self.group_fechas)
        self.layout_second_line.addLayout(self.layout_motivo_baja)

        # Tercera línea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        ## Monta el formulario
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_descripcion)
        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = EquipamientoForm()
    ventana.show()

    sys.exit(app.exec())
