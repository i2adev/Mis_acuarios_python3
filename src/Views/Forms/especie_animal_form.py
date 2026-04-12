"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      20/03/2026
Comentarios:
    Módulo que contiene los controles del formulario de la entidad ESPECIE 
    ANIMAL.
"""

import sys

from CustomControls.combo_box import ComboBox
from CustomControls.double_line_edit import DoubleLineEdit
from CustomControls.int_line_edit import IntLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
                             QPushButton,
                             QSizePolicy, QSpacerItem, QVBoxLayout)

from CustomControls.str_line_edit import StrLineEdit


class EspecieAnimalForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad ESPECIE ANIMAL.
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

        ## Filo
        self.layout_filo = QVBoxLayout()
        self.label_filo = QLabel("FILO")
        self.edit_filo = StrLineEdit(
            control_name="FILO",
            max_length=32
        )
        self.edit_filo.setObjectName("edit_filo")
        self.edit_filo.setFixedWidth(150)
        self.edit_filo.setToolTip(
            """
            <h1>Filo</h1>
            Taxonomía: Filo al que pertenece la especie.
            """
        )
        self.layout_filo.addWidget(self.label_filo)
        self.layout_filo.addWidget(self.edit_filo)

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

        ## Especie hibridada
        self.layout_hibrido = QHBoxLayout()
        self.layout_n_e_hibrida = QVBoxLayout()
        self.check_hibrida = QCheckBox(" ESPECIE HÍBRIDA")
        self.check_hibrida.setObjectName("check_hibrida")
        self.check_hibrida.setChecked(False)
        self.check_hibrida.setToolTip(
            """
            <h1>Especie híbrida</h1>
            En este campo se especifica sí la especie es el resultado de la 
            cria artificial.
            """
        )
        self.label_n_e_hibrida = QLabel("NOMBRE HÍBRIDO")
        self.edit_n_e_hibrida = StrLineEdit(
            control_name="NOMBRE COMÚN",
            max_length=32
        )
        self.edit_n_e_hibrida.setObjectName("edit_n_e_hibrida")
        self.edit_n_e_hibrida.setFixedWidth(150)
        self.edit_n_e_hibrida.setToolTip(
            """
            <h1>Nombre de la especie híbrida</h1>
            En este campo se inserta el nombre que se le ha dado a la 
            especie híbrida.
            """
        )
        self.layout_n_e_hibrida.addWidget(self.label_n_e_hibrida)
        self.layout_n_e_hibrida.addWidget(self.edit_n_e_hibrida)
        self.layout_hibrido.addWidget(self.check_hibrida)
        self.layout_hibrido.addSpacing(20)
        self.layout_hibrido.addLayout(self.layout_n_e_hibrida)

        ## Grupo taxonómico
        self.layout_grupo_taxo = QVBoxLayout()
        self.layout_combo_grupo_taxo = QHBoxLayout()
        self.label_grupo_taxo = QLabel("GRUPO TAXONÓMICO")
        self.combo_grupo_taxo = ComboBox(
            control_name="GRUPO TAXONÓMICO"
        )
        self.combo_grupo_taxo.setObjectName("combo_grupo_taxo")
        self.combo_grupo_taxo.setFixedWidth(150)
        self.combo_grupo_taxo.setToolTip(
            """
            <h1>Grupo taxonómico</h1>
            En este campo se inserta el <b>grupo taxonómico</b> al que 
            pertenece la especie.
            """
        )
        self.button_insert_grupo_taxo = QPushButton("<")
        self.button_insert_grupo_taxo.setObjectName(
            "button_insert_grupo_taxo")
        self.button_insert_grupo_taxo.setFixedWidth(30)
        self.button_insert_grupo_taxo.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_grupo_taxo.addWidget(self.combo_grupo_taxo)
        self.layout_combo_grupo_taxo.addWidget(self.button_insert_grupo_taxo)
        self.layout_grupo_taxo.addWidget(self.label_grupo_taxo)
        self.layout_grupo_taxo.addLayout(self.layout_combo_grupo_taxo)

        ## Origen
        self.layout_origen = QVBoxLayout()
        self.label_origen = QLabel("ORIGEN")
        self.edit_origen = StrLineEdit(
            control_name="ORIGEN",
            max_length=64
        )
        self.edit_origen.setObjectName("edit_origen")
        self.edit_origen.setFixedWidth(150)
        self.edit_origen.setToolTip(
            """
            <h1>Origen geográfico de la especie</h1>
            En este campo se inserta la procedencia de la especie.
            """
        )
        self.layout_origen.addWidget(self.label_origen)
        self.layout_origen.addWidget(self.edit_origen)

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

        ## Tamaño
        self.layout_tamano = QVBoxLayout()
        self.label_tamano = QLabel("TAMAÑO")
        self.edit_tamano = IntLineEdit(
            control_name="TAMAÑO",
            min_value=1,
            max_value=200,
            units="CMS"
        )
        self.edit_tamano.setObjectName("edit_tamano")
        self.edit_tamano.setFixedWidth(50)
        self.edit_tamano.setToolTip(
            """
            <h1>Tamaño</h1>
            En este campo se inserta el <b>tamaño máximo</b> que que alcanza 
            la especie cuando llega a edad adulta.
            """
        )
        self.layout_tamano.addWidget(self.label_tamano)
        self.layout_tamano.addWidget(self.edit_tamano)

        ## Comportamiento
        self.layout_comportamiento = QVBoxLayout()
        self.layout_combo_comportamiento = QHBoxLayout()
        self.label_comportamiento = QLabel("COMPORTAMIENTO")
        self.combo_comportamiento = ComboBox(
            control_name="COMPORTAMIENTO"
        )
        self.combo_comportamiento.setObjectName("combo_comportamioento")
        self.combo_comportamiento.setFixedWidth(150)
        self.combo_comportamiento.setToolTip(
            """
            <h1>Comportamiento</h1>
            En este campo se inserta el <b>comportamiento</b> que exhibe la 
            especie en el acuario.
            """
        )
        self.button_insert_comportamiento = QPushButton("<")
        self.button_insert_comportamiento.setObjectName(
            "button_insert_grupo_taxo")
        self.button_insert_comportamiento.setFixedWidth(30)
        self.button_insert_comportamiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_comportamiento.addWidget(self.combo_comportamiento)
        self.layout_combo_comportamiento.addWidget(
            self.button_insert_comportamiento)
        self.layout_comportamiento.addWidget(self.label_comportamiento)
        self.layout_comportamiento.addLayout(self.layout_combo_comportamiento)

        ## Dieta
        self.layout_dieta = QVBoxLayout()
        self.layout_combo_dieta = QHBoxLayout()
        self.label_dieta = QLabel("DIETA")
        self.combo_dieta = ComboBox(
            control_name="DIETA"
        )
        self.combo_dieta.setObjectName("combo_dieta")
        self.combo_dieta.setFixedWidth(150)
        self.combo_dieta.setToolTip(
            """
            <h1>Dieta</h1>
            En este campo se inserta la <b>dieta</b> con la que se alimenta 
            la especie.
            """
        )
        self.button_insert_dieta = QPushButton("<")
        self.button_insert_dieta.setObjectName(
            "button_insert_dieta")
        self.button_insert_dieta.setFixedWidth(30)
        self.button_insert_dieta.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_dieta.addWidget(self.combo_dieta)
        self.layout_combo_dieta.addWidget(
            self.button_insert_dieta)
        self.layout_dieta.addWidget(self.label_dieta)
        self.layout_dieta.addLayout(self.layout_combo_dieta)

        ## Nivel de nado
        self.layout_nivel_nado = QVBoxLayout()
        self.layout_combo_nivel_nado = QHBoxLayout()
        self.label_nivel_nado = QLabel("NIVEL DE NADO")
        self.combo_nivel_nado = ComboBox(
            control_name="NIVEL DE NADO"
        )
        self.combo_nivel_nado.setObjectName("combo_nivel_nado")
        self.combo_nivel_nado.setFixedWidth(150)
        self.combo_nivel_nado.setToolTip(
            """
            <h1>Nivel de nado</h1>
            En este campo se inserta el <b>nivel</b> por el que se mueve la 
            espècie en el acuario.
            """
        )
        self.button_insert_nivel_nado = QPushButton("<")
        self.button_insert_nivel_nado.setObjectName(
            "button_insert_nivel_nado")
        self.button_insert_nivel_nado.setFixedWidth(30)
        self.button_insert_nivel_nado.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.layout_combo_nivel_nado.addWidget(self.combo_nivel_nado)
        self.layout_combo_nivel_nado.addWidget(
            self.button_insert_nivel_nado)
        self.layout_nivel_nado.addWidget(self.label_nivel_nado)
        self.layout_nivel_nado.addLayout(self.layout_combo_nivel_nado)

        ## Descripción
        self.layout_descripcion = QVBoxLayout()
        self.label_descripcion = QLabel("DESCRIPTION")
        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setMinimumHeight(75)
        self.text_descripcion.setToolTip(
            """ <h2>Descripción</h2><br>
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
        self.layout_taxo_first_line.addLayout(self.layout_filo)
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
        self.layout_taxo_third_line.addLayout(self.layout_hibrido)
        self.layout_taxo_third_line.addSpacerItem(horizontal_spacer)
        self.layout_taxo_third_line.addLayout(self.layout_grupo_taxo)

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
        self.layout_third_line.addLayout(self.layout_tamano)
        self.layout_third_line.addSpacerItem(horizontal_spacer)
        self.layout_third_line.addLayout(self.layout_comportamiento)
        self.layout_third_line.addSpacerItem(horizontal_spacer)
        self.layout_third_line.addLayout(self.layout_dieta)
        self.layout_third_line.addLayout(self.layout_nivel_nado)

        # Montamos el layout
        self.layout_form.addWidget(self.group_taxonomia)  # 1ª línea
        self.layout_form.addSpacing(20)
        self.layout_form.addWidget(self.group_parametros)  # 2ª línea
        self.layout_form.addSpacing(20)
        self.layout_form.addLayout(self.layout_third_line)  # 3ª línea
        self.layout_form.addSpacing(20)
        self.layout_form.addLayout(self.layout_descripcion)  # 4ª línea

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = EspecieAnimalForm()
    # ventana.setFixedWidth(800)
    # ventana.setFixedHeight(600)
    ventana.show()

    sys.exit(app.exec())
