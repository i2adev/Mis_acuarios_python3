"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/04/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad ESPECIE
    VEGETAL.
"""

import sys

from CustomControls.combo_box import ComboBox
from CustomControls.double_line_edit import DoubleLineEdit
from CustomControls.int_line_edit import IntLineEdit
from CustomControls.plain_text_edit import PlainTextEdit
from CustomControls.str_line_edit import StrLineEdit

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
                             QPushButton,
                             QSizePolicy, QSpacerItem, QVBoxLayout)


class EspecieVegetalForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad ESPECIE VEGETAL.
    """

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """

        # Layouts
        ## Layout formulario
        self.layout_form = QVBoxLayout()

        ## Layouts de lineas
        self.layout_first_line = QHBoxLayout()
        self.layout_second_line = QHBoxLayout()
        self.layout_third_line = QHBoxLayout()
        self.layout_fourth_line = QHBoxLayout()

        ## Layout taxonmía
        self.layout_taxonomia = QVBoxLayout()
        self.layout_taxo_first_line = QHBoxLayout()
        self.layout_taxo_second_line = QHBoxLayout()
        self.layout_taxo_third_line = QHBoxLayout()

        ## Layouts parámetros físico-químicos
        self.layout_parametros = QHBoxLayout()
        self.layout_ph = QHBoxLayout()
        self.layout_kh = QHBoxLayout()
        self.layout_gh = QHBoxLayout()
        self.layout_temperatura = QHBoxLayout()

        # Controles del formulario
        ## ID
        self.layout_id = QVBoxLayout()
        self.label_id = QLabel("ID")
        self.edit_id = QLineEdit()
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Reino
        self.layout_reino = QVBoxLayout()
        self.label_reino = QLabel("REINO")
        self.edit_reino = StrLineEdit(
            control_name="REINO",
            max_length=32
        )
        self.edit_reino.setObjectName("edit_reino")
        self.edit_reino.setFixedWidth(150)
        self.edit_reino.setToolTip(
            """
            <h1>Reino</h1>
            Taxonomía: Reino al que pertenece la especie.
            """
        )
        self.layout_reino.addWidget(self.label_reino)
        self.layout_reino.addWidget(self.edit_reino)

        ## División
        self.layout_división = QVBoxLayout()
        self.label_división = QLabel("DIVISIÓN")
        self.edit_division = StrLineEdit(
            control_name="DIVISIÓN",
            max_length=32
        )
        self.edit_division.setObjectName("edit_division")
        self.edit_division.setFixedWidth(150)
        self.edit_division.setToolTip(
            """
            <h1>División</h1>
            Taxonomía: División al que pertenece la especie.
            """
        )
        self.layout_división.addWidget(self.label_división)
        self.layout_división.addWidget(self.edit_division)

        ## Clase
        self.layout_clase = QVBoxLayout()
        self.label_clase = QLabel("CLASE")
        self.edit_clase = StrLineEdit(
            control_name="CLASE",
            max_length=32
        )
        self.edit_clase.setObjectName("edit_clase")
        self.edit_clase.setFixedWidth(150)
        self.edit_clase.setToolTip(
            """
            <h1>Clase</h1>
            Taxonomía: Clase al que pertenece la especie.
            """
        )
        self.layout_clase.addWidget(self.label_clase)
        self.layout_clase.addWidget(self.edit_clase)

        ## Orden
        self.layout_orden = QVBoxLayout()
        self.label_orden = QLabel("ORDEN")
        self.edit_orden = StrLineEdit(
            control_name="ORDEN",
            max_length=32
        )
        self.edit_orden.setObjectName("edit_orden")
        self.edit_orden.setFixedWidth(150)
        self.edit_orden.setToolTip(
            """
            <h1>Clase</h1>
            Taxonomía: Clase al que pertenece la especie.
            """
        )
        self.layout_orden.addWidget(self.label_orden)
        self.layout_orden.addWidget(self.edit_orden)

        ## Familia
        self.layout_familia = QVBoxLayout()
        self.label_familia = QLabel("FAMILIA")
        self.edit_familia = StrLineEdit(
            control_name="FAMILIA",
            max_length=32
        )
        self.edit_familia.setObjectName("edit_familia")
        self.edit_familia.setFixedWidth(150)
        self.edit_familia.setToolTip(
            """
            <h1>Familia</h1>
            Taxonomía: Familia al que pertenece la especie.
            """
        )
        self.layout_familia.addWidget(self.label_familia)
        self.layout_familia.addWidget(self.edit_familia)

        ## Genero
        self.layout_genero = QVBoxLayout()
        self.label_genero = QLabel("GÉNERO")
        self.edit_genero = StrLineEdit(
            control_name="GÉNERO",
            max_length=32
        )
        self.edit_genero.setObjectName("edit_genero")
        self.edit_genero.setFixedWidth(150)
        self.edit_genero.setToolTip(
            """
            <h1>Género</h1>
            Taxonomía: Género al que pertenece la especie.
            """
        )
        self.layout_genero.addWidget(self.label_genero)
        self.layout_genero.addWidget(self.edit_genero)

        ## Especie
        self.layout_especie = QVBoxLayout()
        self.label_especie = QLabel("ESPECIE")
        self.edit_especie = StrLineEdit(
            control_name="ESPECIE",
            max_length=32
        )
        self.edit_especie.setObjectName("edit_genero")
        self.edit_especie.setFixedWidth(150)
        self.edit_especie.setToolTip(
            """
            <h1>Especie</h1>
            Taxonomía: Especie al que pertenece el animal.
            """
        )
        self.layout_especie.addWidget(self.label_especie)
        self.layout_especie.addWidget(self.edit_especie)

        ## Nombre cientifico (Solo lectura)
        self.layout_n_cientifico = QVBoxLayout()
        self.label_n_cientifico = QLabel("NOMBRE CIENTÍFICO")
        self.edit_n_cientifico = StrLineEdit(
            control_name="NOMBRE CIENTÍFICO",
            max_length=32
        )
        self.edit_n_cientifico.setObjectName("edit_n_cientifico")
        self.edit_n_cientifico.setFixedWidth(300)
        self.edit_n_cientifico.setToolTip(
            """
            <h1>Nombre científico</h1>
            En este campo se inserta el <b>nombre científico</b> de la especie.
            """
        )
        self.layout_n_cientifico.addWidget(self.label_n_cientifico)
        self.layout_n_cientifico.addWidget(self.edit_n_cientifico)

        ## Nombre común
        self.layout_n_comun = QVBoxLayout()
        self.label_n_comun = QLabel("NOMBRE COMÚN")
        self.edit_n_comun = StrLineEdit(
            control_name="NOMBRE COMÚN",
            max_length=32
        )
        self.edit_n_comun.setObjectName("edit_n_comun")
        self.edit_n_comun.setFixedWidth(200)
        self.edit_n_comun.setToolTip(
            """
            <h1>Nombre común</h1>
            En este campo se inserta el <b>nombre común</b> con el que se 
            conoce la especie.
            """
        )
        self.layout_n_comun.addWidget(self.label_n_comun)
        self.layout_n_comun.addWidget(self.edit_n_comun)

        ## pH mínimo
        self.layout_ph_min = QVBoxLayout()
        self.label_ph_min = QLabel("MÍN.")
        self.edit_ph_min = DoubleLineEdit(
            control_name="PH MÍNIMO",
            min_value=0.0,
            max_value=14.0,
            units="H+"
        )
        self.edit_ph_min.setObjectName("edit_ph_min")
        self.edit_ph_min.setFixedWidth(50)
        self.edit_ph_min.setToolTip(
            """
            <h1>pH mínimo</h1>
            En este campo se inserta el <b>pH mínimo</b> que tolera la especie.
            """
        )
        self.layout_ph_min.addWidget(self.label_ph_min)
        self.layout_ph_min.addWidget(self.edit_ph_min)

        ## pH máximo
        self.layout_ph_max = QVBoxLayout()
        self.label_ph_max = QLabel("MÁX.")
        self.edit_ph_max = DoubleLineEdit(
            control_name="PH MÁXIMO",
            min_value=0.0,
            max_value=14.0,
            units="H+"
        )
        self.edit_ph_max.setObjectName("edit_ph_min")
        self.edit_ph_max.setFixedWidth(50)
        self.edit_ph_max.setToolTip(
            """
            <h1>pH máximo</h1>
            En este campo se inserta el <b>pH máximo</b> que tolera la especie.
            """
        )
        self.layout_ph_max.addWidget(self.label_ph_max)
        self.layout_ph_max.addWidget(self.edit_ph_max)

        ## KH mínimo
        self.layout_kh_min = QVBoxLayout()
        self.label_kh_min = QLabel("MÍN.")
        self.edit_kh_min = IntLineEdit(
            control_name="KH MÍNIMO",
            min_value=0,
            max_value=30,
            units="GRADOS"
        )
        self.edit_kh_min.setObjectName("edit_kh_min")
        self.edit_kh_min.setFixedWidth(50)
        self.edit_kh_min.setToolTip(
            """
            <h1>KH mínimo</h1>
            En este campo se inserta el <b>KH mínimo</b> que tolera la especie.
            """
        )
        self.layout_kh_min.addWidget(self.label_kh_min)
        self.layout_kh_min.addWidget(self.edit_kh_min)

        ## KH máximo
        self.layout_kh_max = QVBoxLayout()
        self.label_kh_max = QLabel("MÁX.")
        self.edit_kh_max = IntLineEdit(
            control_name="KH MÁXIMO",
            min_value=0,
            max_value=30,
            units="GRADOS"
        )
        self.edit_kh_max.setObjectName("edit_kh_max")
        self.edit_kh_max.setFixedWidth(50)
        self.edit_kh_max.setToolTip(
            """
            <h1>KH máximo</h1>
            En este campo se inserta el <b>KH máximo</b> que tolera la especie.
            """
        )
        self.layout_kh_max.addWidget(self.label_kh_max)
        self.layout_kh_max.addWidget(self.edit_kh_max)

        ## GH mínimo
        self.layout_gh_min = QVBoxLayout()
        self.label_gh_min = QLabel("MÍN.")
        self.edit_gh_min = IntLineEdit(
            control_name="GH MÍNIMO",
            min_value=0,
            max_value=40,
            units="GRADOS"
        )
        self.edit_gh_min.setObjectName("label_gh_min")
        self.edit_gh_min.setFixedWidth(50)
        self.edit_gh_min.setToolTip(
            """
            <h1>GH mínimo</h1>
            En este campo se inserta el <b>GH mínimo</b> que tolera la especie.
            """
        )
        self.layout_gh_min.addWidget(self.label_gh_min)
        self.layout_gh_min.addWidget(self.edit_gh_min)

        ## GH máximo
        self.layout_gh_max = QVBoxLayout()
        self.label_gh_max = QLabel("MÁX.")
        self.edit_gh_max = IntLineEdit(
            control_name="GH MÁXIMO",
            min_value=0,
            max_value=40,
            units="GRADOS"
        )
        self.edit_gh_max.setObjectName("edit_kh_max")
        self.edit_gh_max.setFixedWidth(50)
        self.edit_gh_max.setToolTip(
            """
            <h1>GH máximo</h1>
            En este campo se inserta el <b>GH máximo</b> que tolera la especie.
            """
        )
        self.layout_gh_max.addWidget(self.label_gh_max)
        self.layout_gh_max.addWidget(self.edit_gh_max)

        ## Temperatura mínima
        self.layout_temp_min = QVBoxLayout()
        self.label_temp_min = QLabel("MÍN.")
        self.edit_temp_min = DoubleLineEdit(
            control_name="TEMPERATURA MÍNIMA",
            min_value=15.0,
            max_value=35.0,
            units="°C"
        )
        self.edit_temp_min.setObjectName("edit_kh_max")
        self.edit_temp_min.setFixedWidth(50)
        self.edit_temp_min.setToolTip(
            """
            <h1>Temperatura mínima</h1>
            En este campo se inserta la <b>temperatura mínima</b> que tolera 
            la especie.
            """
        )
        self.layout_temp_min.addWidget(self.label_temp_min)
        self.layout_temp_min.addWidget(self.edit_temp_min)

        ## Temperatura máxima
        self.layout_temp_max = QVBoxLayout()
        self.label_temp_max = QLabel("MÁX.")
        self.edit_temp_max = DoubleLineEdit(
            control_name="TEMPERATURA MÁXIMA",
            min_value=15.0,
            max_value=35.0,
            units="°C"
        )
        self.edit_temp_max.setObjectName("edit_kh_max")
        self.edit_temp_max.setFixedWidth(50)
        self.edit_temp_max.setToolTip(
            """
            <h1>Temperatura máxima</h1>
            En este campo se inserta la <b>temperatura máxima</b> que tolera 
            la especie.
            """
        )
        self.layout_temp_max.addWidget(self.label_temp_max)
        self.layout_temp_max.addWidget(self.edit_temp_max)

        ## Origen
        self.layout_origen = QVBoxLayout()
        self.label_origen = QLabel("ORIGEN")
        self.edit_origen = StrLineEdit(
            control_name="ORIGEN",
            max_length=64
        )
        self.edit_origen.setObjectName("edit_origen")
        self.edit_origen.setFixedWidth(300)
        self.edit_origen.setToolTip(
            """
            <h1>Origen geográfico de la especie</h1>
            En este campo se inserta la procedencia de la especie.
            """
        )
        self.layout_origen.addWidget(self.label_origen)
        self.layout_origen.addWidget(self.edit_origen)

        ## Posición en el acuario
        self.layout_posicion = QVBoxLayout()
        self.layout_combo_posicion = QHBoxLayout()
        self.label_posicion = QLabel("POSICION")
        self.combo_posicion = ComboBox(
            control_name="POSICION"
        )
        self.combo_posicion.setObjectName("combo_posicion")
        self.combo_posicion.setFixedWidth(200)
        self.combo_posicion.setToolTip(
            """
            <h1>Posición</h1>
            En este campo se inserta la <b>posición</b> donde se coloca la 
            planta en el acuario.
            """
        )
        self.button_insert_posicion = QPushButton("<")
        self.button_insert_posicion.setObjectName(
            "button_insert_posicion")
        self.button_insert_posicion.setFixedWidth(30)
        self.button_insert_posicion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_posicion.addWidget(self.combo_posicion)
        self.layout_combo_posicion.addWidget(self.button_insert_posicion)
        self.layout_posicion.addWidget(self.label_posicion)
        self.layout_posicion.addLayout(self.layout_combo_posicion)

        ## Requerimientro de iluminación
        self.layout_req_iluminacion = QVBoxLayout()
        self.layout_combo_req_iluminacion = QHBoxLayout()
        self.label_req_iluminacion = QLabel("REQ. ILUMINACIÓN")
        self.combo_req_iluminacion = ComboBox(
            control_name="REQUERIMIENTO DE ILUMINACIÓN"
        )
        self.combo_req_iluminacion.setObjectName("combo_req_iluminacion")
        self.combo_req_iluminacion.setFixedWidth(200)
        self.combo_req_iluminacion.setToolTip(
            """
            <h1>Reqerimiento de iluminación</h1>
            En este campo se inserta la <b>Requerimiento de iluminación</b> 
            de la planta.
            """
        )
        self.button_insert_req_iuminacion = QPushButton("<")
        self.button_insert_req_iuminacion.setObjectName(
            "button_insert_req_iuminacion")
        self.button_insert_req_iuminacion.setFixedWidth(30)
        self.button_insert_req_iuminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_req_iluminacion.addWidget(self.combo_req_iluminacion)
        self.layout_combo_req_iluminacion.addWidget(
            self.button_insert_req_iuminacion)
        self.layout_req_iluminacion.addWidget(self.label_req_iluminacion)
        self.layout_req_iluminacion.addLayout(
            self.layout_combo_req_iluminacion)

        ## Requerimiento de CO2 
        self.layout_req_co2 = QVBoxLayout()
        self.layout_combo_req_co2 = QHBoxLayout()
        self.label_req_co2 = QLabel("REQ. CO2")
        self.combo_req_co2 = ComboBox(
            control_name="REQUERIMIENTO CO2"
        )
        self.combo_req_co2.setObjectName("combo_crecimiento")
        self.combo_req_co2.setFixedWidth(200)
        self.combo_req_co2.setToolTip(
            """
            <h1>Requerimiento de CO<sub>2</sub></h1>
            En este campo se inserta el <b>requerimiento de CO<sub>2</sub></b> 
            que necesita la planta.
            """
        )
        self.button_insert_req_co2 = QPushButton("<")
        self.button_insert_req_co2.setObjectName(
            "button_insert_req_co2")
        self.button_insert_req_co2.setFixedWidth(30)
        self.button_insert_req_co2.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_req_co2.addWidget(self.combo_req_co2)
        self.layout_combo_req_co2.addWidget(
            self.button_insert_req_co2)
        self.layout_req_co2.addWidget(self.label_req_co2)
        self.layout_req_co2.addLayout(self.layout_combo_req_co2)

        ## Tasa de crecimiento
        self.layout_crecimiento = QVBoxLayout()
        self.layout_combo_crecimiento = QHBoxLayout()
        self.label_crecimiento = QLabel("TASA DE CRECIMIENTO")
        self.combo_crecimiento = ComboBox(
            control_name="TASA DE CRECIMIENTO"
        )
        self.combo_crecimiento.setObjectName("combo_crecimiento")
        self.combo_crecimiento.setFixedWidth(200)
        self.combo_crecimiento.setToolTip(
            """
            <h1>Tasa de crecimiento</h1>
            En este campo se inserta la <b>tasa de crecimiento</b> de la 
            planta.
            """
        )
        self.button_insert_crecimiento = QPushButton("<")
        self.button_insert_crecimiento.setObjectName(
            "button_insert_crecimiento")
        self.button_insert_crecimiento.setFixedWidth(30)
        self.button_insert_crecimiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_crecimiento.addWidget(self.combo_crecimiento)
        self.layout_combo_crecimiento.addWidget(
            self.button_insert_crecimiento)
        self.layout_crecimiento.addWidget(self.label_crecimiento)
        self.layout_crecimiento.addLayout(self.layout_combo_crecimiento)

        ## Dificultad
        self.layout_dificultad = QVBoxLayout()
        self.layout_combo_dificultad = QHBoxLayout()
        self.label_dificultad = QLabel("DIFICULTAD")
        self.combo_dificultad = ComboBox(
            control_name="DIFICULTAD"
        )
        self.combo_dificultad.setObjectName("combo_dificultad")
        self.combo_dificultad.setFixedWidth(200)
        self.combo_dificultad.setToolTip(
            """
            <h1>Dificultad</h1>
            En este campo se inserta la <b>dificultad de mantenimiento</b> 
            de la planta.
            """
        )
        self.button_insert_dificultad = QPushButton("<")
        self.button_insert_dificultad.setObjectName(
            "button_insert_dificultad")
        self.button_insert_dificultad.setFixedWidth(30)
        self.button_insert_dificultad.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_dificultad.addWidget(self.combo_dificultad)
        self.layout_combo_dificultad.addWidget(
            self.button_insert_dificultad)
        self.layout_dificultad.addWidget(self.label_dificultad)
        self.layout_dificultad.addLayout(self.layout_combo_dificultad)

        ## Descripción
        self.layout_descripcion = QVBoxLayout()
        self.label_descripcion = QLabel("DESCRIPTION")
        self.text_descripcion = PlainTextEdit("DESCRIPCIÓN")
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setMinimumHeight(75)
        self.text_descripcion.setToolTip(
            """ 
            <h2>Descripción</h2><br>
            En este campo se incluirá una breve descripción de la especie.
            """
        )
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # GroupBox
        self.group_taxonomia = QGroupBox("TAXONOMÍA DE LA ESPECIE")
        self.group_taxonomia.setLayout(self.layout_taxonomia)

        self.group_ph = QGroupBox("PH")
        self.group_ph.setLayout(self.layout_ph)

        self.group_kh = QGroupBox("KH")
        self.group_kh.setLayout(self.layout_kh)

        self.group_gh = QGroupBox("GH")
        self.group_gh.setLayout(self.layout_gh)

        self.group_temperatura = QGroupBox("TEMPERATURA")
        self.group_temperatura.setLayout(self.layout_temperatura)

        self.group_parametros = QGroupBox("PARÁMETROS FÍSICO-QUÍMICOS")
        self.group_parametros.setLayout(self.layout_parametros)

    def build_layout(self):
        """ Construye el layout del frame. """

        horizontal_spacer = QSpacerItem(
            0, 0,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        # Datos taxonómicos
        ## Montamos la primera línea
        self.layout_taxo_first_line.addLayout(self.layout_id)
        self.layout_taxo_first_line.addLayout(self.layout_reino)
        self.layout_taxo_first_line.addSpacerItem(horizontal_spacer)
        self.layout_taxo_first_line.addLayout(self.layout_división)
        self.layout_taxo_first_line.addSpacerItem(horizontal_spacer)
        self.layout_taxo_first_line.addLayout(self.layout_clase)
        self.layout_taxo_first_line.addSpacerItem(horizontal_spacer)
        self.layout_taxo_first_line.addLayout(self.layout_orden)

        ## Montamos la segunda línea
        self.layout_taxo_second_line.addLayout(self.layout_familia)
        self.layout_taxo_second_line.addSpacerItem(horizontal_spacer)
        self.layout_taxo_second_line.addLayout(self.layout_genero)
        self.layout_taxo_second_line.addSpacerItem(horizontal_spacer)
        self.layout_taxo_second_line.addLayout(self.layout_especie)
        self.layout_taxo_second_line.addSpacerItem(horizontal_spacer)
        self.layout_taxo_second_line.addLayout(self.layout_n_cientifico)

        ## Montamos la tercera línea
        self.layout_taxo_third_line.addLayout(self.layout_n_comun)
        self.layout_taxo_third_line.addSpacerItem(horizontal_spacer)

        ## Montamos los datos taxonómicos
        self.layout_taxonomia.addLayout(self.layout_taxo_first_line)
        self.layout_taxonomia.addSpacing(20)
        self.layout_taxonomia.addLayout(self.layout_taxo_second_line)
        self.layout_taxonomia.addSpacing(20)
        self.layout_taxonomia.addLayout(self.layout_taxo_third_line)

        # Parámetros físico-químicos
        ## Primera linea
        ### PH
        self.layout_ph.addLayout(self.layout_ph_min)
        self.layout_ph.addLayout(self.layout_ph_max)

        ### KH
        self.layout_kh.addLayout(self.layout_kh_min)
        self.layout_kh.addLayout(self.layout_kh_max)

        # Segunda línea
        ### GH
        self.layout_gh.addLayout(self.layout_gh_min)
        self.layout_gh.addLayout(self.layout_gh_max)

        ### Temperatura
        self.layout_temperatura.addLayout(self.layout_temp_min)
        self.layout_temperatura.addLayout(self.layout_temp_max)

        ## Montamos la segunda línea
        self.layout_parametros.addWidget(self.group_ph)
        self.layout_parametros.addSpacerItem(horizontal_spacer)
        self.layout_parametros.addWidget(self.group_kh)
        self.layout_parametros.addSpacerItem(horizontal_spacer)
        self.layout_parametros.addWidget(self.group_gh)
        self.layout_parametros.addSpacerItem(horizontal_spacer)
        self.layout_parametros.addWidget(self.group_temperatura)

        ## Montamos la tercera línea
        self.layout_third_line.addLayout(self.layout_origen)
        self.layout_third_line.addSpacerItem(horizontal_spacer)
        self.layout_third_line.addSpacerItem(horizontal_spacer)
        self.layout_third_line.addLayout(self.layout_posicion)
        self.layout_third_line.addSpacerItem(horizontal_spacer)
        self.layout_third_line.addLayout(self.layout_req_iluminacion)

        ## Montamos la cuarta línea
        self.layout_fourth_line.addLayout(self.layout_req_co2)
        self.layout_fourth_line.addSpacerItem(horizontal_spacer)
        self.layout_fourth_line.addLayout(self.layout_crecimiento)
        self.layout_fourth_line.addSpacerItem(horizontal_spacer)
        self.layout_fourth_line.addLayout(self.layout_dificultad)

        # Montamos el layout
        self.layout_form.addWidget(self.group_taxonomia)  # 1ª línea
        self.layout_form.addSpacing(20)
        self.layout_form.addWidget(self.group_parametros)  # 2ª línea
        self.layout_form.addSpacing(20)
        self.layout_form.addLayout(self.layout_third_line)  # 3ª línea
        self.layout_form.addSpacing(20)
        self.layout_form.addLayout(self.layout_fourth_line)  # 3ª línea
        self.layout_form.addSpacing(20)
        self.layout_form.addLayout(self.layout_descripcion)  # 4ª línea

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = EspecieVegetalForm()
    # ventana.setFixedWidth(800)
    # ventana.setFixedHeight(600)
    ventana.show()

    sys.exit(app.exec())
