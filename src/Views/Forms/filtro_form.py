"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      25/11/2025
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


class FiltroForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad FILTRO.
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
        ### Tipo de filtro
        self.layout_tipo_filtro = QVBoxLayout()
        self.layout_combo_tipo_filtro = QHBoxLayout()

        ### Termofiltro
        self.layout_termofiltro = QVBoxLayout()

        ### Marca de filtro
        self.layout_marca = QVBoxLayout()
        self.layout_combo_marca = QHBoxLayout()
        ### Modelo
        self.layout_modelo = QVBoxLayout()
        ### Número de serie
        self.layout_num_serie = QVBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        self.layout_volumenes_acuario_filtro = QHBoxLayout()
        self.layout_consumos_acuario_filtro = QHBoxLayout()
        self.layout_dimensiones_filtro = QHBoxLayout()
        self.layout_second_line.setContentsMargins(0, 0, 0, 20)
        ### Volumen mínimo del acuario
        self.layout_vol_min_acuario = QVBoxLayout()
        ### Volumen máximo del acuario
        self.layout_vol_max_acuario = QVBoxLayout()
        ### Consumo del filtro
        self.layout_consumo_filtro = QVBoxLayout()
        ### Consumo del calentador
        self.layout_consumo_calentador = QVBoxLayout()
        ### Ancho
        self.layout_ancho = QVBoxLayout()
        ### Fondo
        self.layout_fondo = QVBoxLayout()
        ### Alto
        self.layout_alto = QVBoxLayout()

        ## Tercera línea
        self.layout_third_line = QHBoxLayout()
        self.layout_third_line.setContentsMargins(0, 0, 0, 20)
        ### Volumen filtrante
        self.layout_volumen_material = QVBoxLayout()
        ### Altura máxima de bombeo
        self.layout_altura_maxima_bombeo = QVBoxLayout()
        ### Caudal del filtro
        self.layout_caudal = QVBoxLayout()

        ## Cuarta línea
        self.layout_fouth_line = QHBoxLayout()
        ### Fecha compra
        self.layout_fecha_compra = QVBoxLayout()
        ### Fecha baja
        self.layout_fecha_baja = QVBoxLayout()
        ### Motivo de baja
        self.layout_motivo_baja = QVBoxLayout()

        ## Quinta línea
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_tipo_proyecto = QLabel("TIPO DE FILTRO")
        self.label_termofiltro = QLabel("")
        self.label_marca = QLabel("MARCA")
        self.label_modelo = QLabel("MODELO")
        self.label_num_serie = QLabel("NÚMERO DE SERIE")
        self.label_vol_min_acuario = QLabel("MÍNIMO")
        self.label_vol_max_acuario = QLabel("MÁXIMO")
        self.label_consumo_filtro = QLabel("FILTRO")
        self.label_consumo_calentador = QLabel("CALENTADOR")
        self.label_ancho = QLabel("ANCHO")
        self.label_fondo = QLabel("FONDO")
        self.label_Alto = QLabel("ALTO")
        self.label_vol_material = QLabel("VOL. MAT.")
        self.label_altura_maxima = QLabel("ALT. MAX.")
        self.label_caudal = QLabel("CAUDAL")
        self.label_fecha_compra = QLabel("FECHA COMPRA")
        self.label_fecha_baja = QLabel("FECHA BAJA")
        self.label_motivo_baja = QLabel("MOTIVO BAJA")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")

        self.edit_modelo = QLineEdit()
        self.edit_modelo.setObjectName("edit_modelo")

        self.edit_num_serie = QLineEdit()
        self.edit_num_serie.setObjectName("edit_num_serie")

        self.edit_vol_min_acuario = QLineEdit()
        self.edit_vol_min_acuario.setObjectName("edit_vol_min_acuario")
        self.edit_vol_min_acuario.setValidator(QIntValidator())

        self.edit_vol_max_acuario = QLineEdit()
        self.edit_vol_max_acuario.setObjectName("edit_vol_max_acuario")
        self.edit_vol_max_acuario.setValidator(QIntValidator())

        self.edit_consumo_filtro = QLineEdit()
        self.edit_consumo_filtro.setObjectName("edit_consumo_filtro")
        self.edit_consumo_filtro.setValidator(QIntValidator())

        self.edit_consumo_calentador = QLineEdit()
        self.edit_consumo_calentador.setObjectName("edit_consumo_calentador")
        self.edit_consumo_calentador.setValidator(QIntValidator())

        self.edit_vol_material = QLineEdit()
        self.edit_vol_material.setObjectName("edit_vol_material")
        self.edit_vol_material.setFixedWidth(80)
        self.edit_vol_material.setValidator(QDoubleValidator())

        self.edit_altura_max_bombeo = QLineEdit()
        self.edit_altura_max_bombeo.setObjectName("edit_altura_max_bombeo")
        self.edit_altura_max_bombeo.setFixedWidth(80)
        self.edit_altura_max_bombeo.setValidator(QDoubleValidator())

        self.edit_caudal = QLineEdit()
        self.edit_caudal.setObjectName("edit_caudal")
        self.edit_caudal.setFixedWidth(80)
        self.edit_caudal.setValidator(QIntValidator())

        self.edit_ancho = QLineEdit()
        self.edit_ancho.setObjectName("edit_ancho")
        self.edit_ancho.setValidator(QIntValidator())

        self.edit_fondo = QLineEdit()
        self.edit_fondo.setObjectName("edit_fondo")
        self.edit_fondo.setValidator(QIntValidator())

        self.edit_alto = QLineEdit()
        self.edit_alto.setObjectName("edit_alto")
        self.edit_alto.setValidator(QIntValidator())

        self.edit_motivo_baja = QLineEdit()
        self.edit_motivo_baja.setObjectName("edit_motivo_baja")

        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setMinimumHeight(75)

        # Combos
        self.combo_tipo_filtro = QComboBox()
        self.combo_tipo_filtro.setObjectName("combo_tipo_filtro")
        self.combo_tipo_filtro.setMinimumWidth(250)
        self.combo_tipo_filtro.setEditable(True)

        self.combo_marca = QComboBox()
        self.combo_marca.setMinimumWidth(250)
        self.combo_marca.setObjectName("combo_marca")
        self.combo_marca.setEditable(True)

        # Checkboxes
        self.check_termofiltro = QCheckBox("TERMO.")
        self.check_termofiltro.setObjectName("check_termofiltro")
        self.check_termofiltro.setChecked(False)

        # Date pickers
        self.fecha_compra = NullableDateEdit()
        self.fecha_compra.setObjectName("fecha_compra")

        self.fecha_baja = NullableDateEdit()
        self.fecha_baja.setObjectName("fecha_baja")

        # Botones
        self.button_insert_tipo_filtro = QPushButton("<")
        self.button_insert_tipo_filtro.setObjectName(
            "button_insert_tipo_filtro")
        self.button_insert_tipo_filtro.setFixedWidth(30)
        self.button_insert_tipo_filtro.setCursor(
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
        self.group_volumen = QGroupBox("VOLUMEN DE ACUARIOS (Litros)")
        self.group_consumo = QGroupBox("CONSUMOS (w)")
        self.group_dimensiones = QGroupBox("DIMENSIONES DEL FILTRO (cm)")

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera línea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Tipo de filtro
        self.layout_combo_tipo_filtro.addWidget(self.combo_tipo_filtro)
        self.layout_combo_tipo_filtro.addWidget(self.button_insert_tipo_filtro)
        self.layout_tipo_filtro.addWidget(self.label_tipo_proyecto)
        self.layout_tipo_filtro.addLayout(self.layout_combo_tipo_filtro)

        ## Termofiltro
        self.layout_termofiltro.addWidget(self.label_termofiltro)
        self.layout_termofiltro.addWidget(self.check_termofiltro)

        ## Marca comercial
        self.layout_combo_marca.addWidget(self.combo_marca)
        self.layout_combo_marca.addWidget(self.button_insert_marca)
        self.layout_marca.addWidget(self.label_marca)
        self.layout_marca.addLayout(self.layout_combo_marca)

        ## Modelo
        self.layout_modelo.addWidget(self.label_modelo)
        self.layout_modelo.addWidget(self.edit_modelo)

        ## Número de serie
        self.layout_num_serie.addWidget(self.label_num_serie)
        self.layout_num_serie.addWidget(self.edit_num_serie)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_tipo_filtro)
        self.layout_first_line.addLayout(self.layout_termofiltro)
        self.layout_first_line.addLayout(self.layout_marca)
        self.layout_first_line.addLayout(self.layout_modelo)
        self.layout_first_line.addLayout(self.layout_num_serie)

        # Segunda línea
        ## Volumen mínimo
        self.layout_vol_min_acuario.addWidget(self.label_vol_min_acuario)
        self.layout_vol_min_acuario.addWidget(self.edit_vol_min_acuario)

        ## Volumen máximo
        self.layout_vol_max_acuario.addWidget(self.label_vol_max_acuario)
        self.layout_vol_max_acuario.addWidget(self.edit_vol_max_acuario)

        ## Consumo del filtro
        self.layout_consumo_filtro.addWidget(self.label_consumo_filtro)
        self.layout_consumo_filtro.addWidget(self.edit_consumo_filtro)

        ## Consumo calentador
        self.layout_consumo_calentador.addWidget(self.label_consumo_calentador)
        self.layout_consumo_calentador.addWidget(self.edit_consumo_calentador)

        ## Ancho
        self.layout_ancho.addWidget(self.label_ancho)
        self.layout_ancho.addWidget(self.edit_ancho)

        ## Fondo
        self.layout_fondo.addWidget(self.label_fondo)
        self.layout_fondo.addWidget(self.edit_fondo)

        ## Alto
        self.layout_alto.addWidget(self.label_Alto)
        self.layout_alto.addWidget(self.edit_alto)

        ## Montamos la segunda línea
        self.layout_volumenes_acuario_filtro.addLayout(
            self.layout_vol_min_acuario)
        self.layout_volumenes_acuario_filtro.addLayout(
            self.layout_vol_max_acuario)
        self.group_volumen.setLayout(self.layout_volumenes_acuario_filtro)

        self.layout_consumos_acuario_filtro.addLayout(
            self.layout_consumo_filtro)
        self.layout_consumos_acuario_filtro.addLayout(
            self.layout_consumo_calentador)
        self.group_consumo.setLayout(self.layout_consumos_acuario_filtro)

        self.layout_dimensiones_filtro.addLayout(self.layout_ancho)
        self.layout_dimensiones_filtro.addLayout(self.layout_fondo)
        self.layout_dimensiones_filtro.addLayout(self.layout_alto)
        self.group_dimensiones.setLayout(self.layout_dimensiones_filtro)

        self.layout_second_line.addWidget(self.group_volumen)
        self.layout_second_line.addWidget(self.group_consumo)
        self.layout_second_line.addWidget(self.group_dimensiones)

        # Tercera línea
        ## Volumen material filtrante
        self.layout_volumen_material.addWidget(self.label_vol_material)
        self.layout_volumen_material.addWidget(self.edit_vol_material)

        ## Altura máxima de bombeo
        self.layout_altura_maxima_bombeo.addWidget(self.label_altura_maxima)
        self.layout_altura_maxima_bombeo.addWidget(self.edit_altura_max_bombeo)

        ## Caudal del filtro
        self.layout_caudal.addWidget(self.label_caudal)
        self.layout_caudal.addWidget(self.edit_caudal)

        ## Fecha de compra
        self.layout_fecha_compra.addWidget(self.label_fecha_compra)
        self.layout_fecha_compra.addWidget(self.fecha_compra)

        ## Fecha de baja
        self.layout_fecha_baja.addWidget(self.label_fecha_baja)
        self.layout_fecha_baja.addWidget(self.fecha_baja)

        ## Motivo de baja
        self.layout_motivo_baja.addWidget(self.label_motivo_baja)
        self.layout_motivo_baja.addWidget(self.edit_motivo_baja)

        ## Montaje tercera linea
        self.layout_third_line.addLayout(self.layout_volumen_material)
        self.layout_third_line.addLayout(self.layout_altura_maxima_bombeo)
        self.layout_third_line.addLayout(self.layout_caudal)
        self.layout_third_line.addLayout(self.layout_fecha_compra)
        self.layout_third_line.addLayout(self.layout_fecha_baja)
        self.layout_third_line.addLayout(self.layout_motivo_baja)

        # Cuarta línea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        ## Montamos el formulario
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_third_line)
        self.layout_form.addLayout(self.layout_descripcion)
        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = FiltroForm()
    ventana.show()

    sys.exit(app.exec())
