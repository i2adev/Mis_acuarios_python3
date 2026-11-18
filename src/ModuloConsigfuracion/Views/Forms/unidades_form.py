"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      06/10/2026
Comentarios:
    Frame que contiene los datos de las unidades.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
                             QGroupBox,
                             QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, )

import globales
from CustomControls.combo_box import ComboBox
from CustomControls.int_line_edit import IntLineEdit
from CustomControls.str_line_edit import StrLineEdit


class UnidadesForm(QFrame):
    """
    Clase que contiene los controles de la cuenta de usuario.
    """

    def __init__(self):
        super().__init__()

        # Política de expansión del control
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """Se encarga de crear los controles del formulario."""

        # Layouts
        self.layout_form = QGridLayout(self)
        self.layout_form.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de unidades dimensionales
        self.unidades_dim_group_box = QGroupBox("UNIDADES DIMENSIONALES")
        self.layout_gr_unidades_dim = QVBoxLayout(self.unidades_dim_group_box)
        self.layout_gr_unidades_dim.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de unidades de potencia y energía
        self.unidades_pot_group_box = QGroupBox("UNIDADES DE POTENCIA Y "
                                                "ENERGIA")
        self.layout_gr_unidades_pot = QHBoxLayout(self.unidades_pot_group_box)
        self.layout_gr_unidades_pot.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de unidades de volumen
        self.unidades_vol_group_box = QGroupBox("UNIDADES DE VOLUMEN")
        self.layout_gr_unidades_vol = QVBoxLayout(self.unidades_vol_group_box)
        self.layout_gr_unidades_vol.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de unidades de masa
        self.unidades_masa_group_box = QGroupBox("UNIDADES DE MASA")
        self.layout_gr_unidades_masa = QVBoxLayout(
            self.unidades_masa_group_box)
        self.layout_gr_unidades_masa.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de unidades de temperatura
        self.unidades_temp_group_box = QGroupBox("UNIDADES DE TEMPERATURA")
        self.layout_gr_unidades_temp = QVBoxLayout(
            self.unidades_temp_group_box)
        self.layout_gr_unidades_temp.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de unidades de iluminación
        self.unidades_ilum_group_box = QGroupBox("UNIDADES DE ILUMINACIÓN")
        self.layout_gr_unidades_ilum = QVBoxLayout(
            self.unidades_ilum_group_box)
        self.layout_gr_unidades_ilum.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de caudal y presión
        self.unidades_caudal_group_box = QGroupBox("UNIDADES DE CAUDAL Y "
                                                   "PRESIÓN")
        self.layout_gr_unidades_caudal = QHBoxLayout(
            self.unidades_caudal_group_box)
        self.layout_gr_unidades_caudal.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Grupo de química
        self.unidades_quimica_group_box = QGroupBox("UNIDADES DE PARÁMETROS "
                                                    "FÍSICO-QUÍMICOS")
        self.layout_gr_unidades_quimica = QGridLayout(
            self.unidades_quimica_group_box)
        self.layout_gr_unidades_quimica.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Dimensiones
        self.label_dim_urna = QLabel("DIMENSIONES")
        self.combo_dimensiones = ComboBox("combo_dimensiones")
        self.combo_dimensiones.setToolTip(
            """
            <h2>Unidad dimensional</h2>
            En este campo se selecciona la unidad de los campos dimensionales.
            """
        )
        self.layout_dimensiones = QVBoxLayout()

        # Unidades de potencia
        self.label_potencia = QLabel("POTENCIA")
        self.combo_potencia = ComboBox("combo_potencia")
        self.combo_potencia.setToolTip(
            """
            <h2>Unidad de potencia</h2>
            En este campo se selecciona la unidad de potencia.
            """
        )
        self.layout_potencia = QVBoxLayout()

        # Unidades de energía
        self.label_energia = QLabel("ENERGÍA")
        self.combo_energia = ComboBox("combo_energia")
        self.combo_energia.setToolTip(
            """
            <h2>Unidad de energía</h2>
            En este campo se selecciona la unidad de energía.
            """
        )
        self.layout_energia = QVBoxLayout()

        # Unidades de volumen
        self.label_volumen = QLabel("VOLUMEN")
        self.combo_volumen = ComboBox("combo_volumen")
        self.combo_volumen.setToolTip(
            """
            <h2>Unidad de volumen</h2>
            En este campo se selecciona la unidad de volumen.
            """
        )
        self.layout_volumen = QVBoxLayout()

        # Unidades de concentración
        self.label_concentracion = QLabel("CONCENTRACIÓN")
        self.combo_concentracion = ComboBox("combo_concentracion")
        self.combo_concentracion.setToolTip(
            """
            <h2>Unidad de concentración</h2>
            En este campo se selecciona la unidad de concentración.
            """
        )
        self.layout_concentracion = QVBoxLayout()

        # Unidades de Kh
        self.label_kh = QLabel("KH")
        self.combo_kh = ComboBox("combo_kh")
        self.combo_kh.setToolTip(
            """
            <h2>Unidad de medición de KH</h2>
            En este campo se selecciona la unidad de medición de KH.
            """
        )
        self.layout_kh = QVBoxLayout()

        # Unidades de GH
        self.label_gh = QLabel("GH")
        self.combo_gh = ComboBox("combo_gh")
        self.combo_gh.setToolTip(
            """
            <h2>Unidad de medición de GH</h2>
            En este campo se selecciona la unidad de medición de GH.
            """
        )
        self.layout_gh = QVBoxLayout()

        # Unidades de conductividad
        self.label_cond = QLabel("CONDUCTIVIDAD")
        self.combo_cond = ComboBox("combo_cond")
        self.combo_cond.setToolTip(
            """
            <h2>Unidad de medición de la conductividad eléctrica (EC).</h2>
            En este campo se selecciona la unidad de la conductividad eléctrica.
            """
        )
        self.layout_cond = QVBoxLayout()

        # Unidades de salinidad
        self.label_sal = QLabel("SALINIDAD")
        self.combo_sal = ComboBox("combo_sal")
        self.combo_sal.setToolTip(
            """
            <h2>Unidad de medición de la salinidad.</h2>
            En este campo se selecciona la unidad de la salinidad.
            """
        )
        self.layout_sal = QVBoxLayout()

        # Unidades de densidad del agua
        self.label_densidad = QLabel("DENSIDAD")
        self.combo_densidad = ComboBox("combo_densidad")
        self.combo_densidad.setToolTip(
            """
            <h2>Unidad de medición de la densidad del agua.</h2>
            En este campo se selecciona la unidad de la densidad del agua.
            """
        )
        self.layout_densidad = QVBoxLayout()

        # Unidades de masa
        self.label_masa = QLabel("MASA")
        self.combo_masa = ComboBox("combo_masa")
        self.combo_masa.setToolTip(
            """
            <h2>Unidad de masa</h2>
            En este campo se selecciona la unidad de masa.
            """
        )
        self.layout_masa = QVBoxLayout()

        # Unidades de temperatura
        self.label_temp = QLabel("TEMPERATURA")
        self.combo_temp = ComboBox("combo_temp")
        self.combo_temp.setToolTip(
            """
            <h2>Unidad de temperatura</h2>
            En este campo se selecciona la unidad de temperatura.
            """
        )
        self.layout_temp = QVBoxLayout()

        # Unidades de caudal
        self.label_caudal = QLabel("CAUDAL")
        self.combo_caudal = ComboBox("combo_caudal")
        self.combo_caudal.setToolTip(
            """
            <h2>Unidad de caudal</h2>
            En este campo se selecciona la unidad de caudal.
            """
        )
        self.layout_caudal = QVBoxLayout()

        # Unidades de presión
        self.label_presion = QLabel("PRESIÓN")
        self.combo_presion = ComboBox("combo_presion")
        self.combo_presion.setToolTip(
            """
            <h2>Unidad de presión</h2>
            En este campo se selecciona la unidad de presión.
            """
        )
        self.layout_presion = QVBoxLayout()

        # Unidades de iluminación
        self.label_iluminacion = QLabel("ILUMINACIÓN")
        self.combo_iluminacion = ComboBox("combo_iluminacion")
        self.combo_iluminacion.setToolTip(
            """
            <h2>Unidad de iluminación</h2>
            En este campo se selecciona la unidad de iluminación.
            """
        )
        self.layout_iluminacion = QVBoxLayout()

    def build_layout(self):
        """Monta el layout del formulario."""

        # Unidades dimensionales
        self.layout_dimensiones.addWidget(self.label_dim_urna)
        self.layout_dimensiones.addWidget(self.combo_dimensiones)

        ## Añadir al layout de unidades
        self.layout_gr_unidades_dim.addLayout(self.layout_dimensiones)

        # Unidades de potencia y energia
        self.layout_potencia.addWidget(self.label_potencia)
        self.layout_potencia.addWidget(self.combo_potencia)
        self.layout_energia.addWidget(self.label_energia)
        self.layout_energia.addWidget(self.combo_energia)

        ## Añadir el layout unidades de potencia y energia
        self.layout_gr_unidades_pot.addLayout(self.layout_potencia)
        self.layout_gr_unidades_pot.addLayout(self.layout_energia)

        # Unidades de caudal y presión
        self.layout_caudal.addWidget(self.label_caudal)
        self.layout_caudal.addWidget(self.combo_caudal)
        self.layout_presion.addWidget(self.label_presion)
        self.layout_presion.addWidget(self.combo_presion)

        ## Añadir el layout unidades de caudal y presión
        self.layout_gr_unidades_caudal.addLayout(self.layout_caudal)
        self.layout_gr_unidades_caudal.addLayout(self.layout_presion)

        # Unidades de volumen
        self.layout_volumen.addWidget(self.label_volumen)
        self.layout_volumen.addWidget(self.combo_volumen)

        # Añadir el layout de unidades de volumen
        self.layout_gr_unidades_vol.addLayout(self.layout_volumen)

        # Unidades de iluminacion
        self.layout_iluminacion.addWidget(self.label_iluminacion)
        self.layout_iluminacion.addWidget(self.combo_iluminacion)

        # Añadir el layout de unidades de iluminación
        self.layout_gr_unidades_ilum.addLayout(self.layout_iluminacion)

        # Unidades de masa
        self.layout_masa.addWidget(self.label_masa)
        self.layout_masa.addWidget(self.combo_masa)

        # Unidades de parámetros físico-químicos
        ## Densidad
        self.layout_densidad.addWidget(self.label_densidad)
        self.layout_densidad.addWidget(self.combo_densidad)
        self.layout_densidad.setContentsMargins(0, 10, 0, 0)

        ## Salinidad
        self.layout_sal.addWidget(self.label_sal)
        self.layout_sal.addWidget(self.combo_sal)
        self.layout_sal.setContentsMargins(0, 10, 0, 0)

        ## Conductividad
        self.layout_cond.addWidget(self.label_cond)
        self.layout_cond.addWidget(self.combo_cond)
        self.layout_cond.setContentsMargins(0, 10, 0, 0)

        ## GH
        self.layout_gh.addWidget(self.label_gh)
        self.layout_gh.addWidget(self.combo_gh)
        self.layout_gh.setContentsMargins(0, 10, 0, 0)

        ## KH
        self.layout_kh.addWidget(self.label_kh)
        self.layout_kh.addWidget(self.combo_kh)

        ## Concentración
        self.layout_concentracion.addWidget(self.label_concentracion)
        self.layout_concentracion.addWidget(self.combo_concentracion)

        ## Añadir al layout de química
        self.layout_gr_unidades_quimica.addLayout(self.layout_concentracion,
                                                  0, 0)
        self.layout_gr_unidades_quimica.addLayout(self.layout_kh,
                                                  0, 1)
        self.layout_gr_unidades_quimica.addLayout(self.layout_gh,
                                                  1, 0)
        self.layout_gr_unidades_quimica.addLayout(self.layout_cond,
                                                  1, 1)
        self.layout_gr_unidades_quimica.addLayout(self.layout_sal,
                                                  2, 0)
        self.layout_gr_unidades_quimica.addLayout(self.layout_densidad,
                                                  2, 1)

        # Unidades de temperatura
        self.layout_temp.addWidget(self.label_temp)
        self.layout_temp.addWidget(self.combo_temp)

        # Añadir el layout de unidades de temperatura
        self.layout_gr_unidades_temp.addLayout(self.layout_temp)

        # Unidades de temperatura
        self.layout_temp.addWidget(self.label_temp)
        self.layout_temp.addWidget(self.combo_temp)

        # Añadir el layout de unidades de masa
        self.layout_gr_unidades_masa.addLayout(self.layout_masa)

        # Añadir el layout de unidades de volumen
        self.layout_gr_unidades_vol.addLayout(self.layout_volumen)

        # Añadir los grupos al layout principal
        self.layout_form.addWidget(self.unidades_dim_group_box, 0, 0)
        self.layout_form.addWidget(self.unidades_vol_group_box, 0, 1)
        self.layout_form.addWidget(self.unidades_masa_group_box, 1, 0)
        self.layout_form.addWidget(self.unidades_temp_group_box, 1, 1)
        self.layout_form.addWidget(self.unidades_pot_group_box, 2, 0, 1, 2)
        self.layout_form.addWidget(self.unidades_caudal_group_box, 3, 0, 1, 2)
        self.layout_form.addWidget(self.unidades_ilum_group_box, 4, 0)
        self.layout_form.addWidget(self.unidades_quimica_group_box, 5, 0, 1, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = UnidadesForm()
    ventana.show()

    sys.exit(app.exec())
