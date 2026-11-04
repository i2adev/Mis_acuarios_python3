"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/10/2026
Comentarios:
    Clase que contiene los controles de los parámetros a configurar.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
                             QHBoxLayout,
                             QLabel,
                             QTabWidget, QVBoxLayout, QWidget)

import globales
from CustomControls.combo_box import ComboBox
from ModuloMaestro.Views.Forms.usuario_form import UsuarioFOrm


class ConfiguracionForm(QFrame):
    """
    Clase que contiene los controles de los parámetros a configurar.
    """

    def __init__(self):
        super().__init__()

        self.setFixedHeight(200)

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """

        self.layout_form = QVBoxLayout()
        self.layout_form.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.tab_widget = QTabWidget()

        # Pestaña usuario
        self.tab_usuario = QWidget()

        ## Datos de usuario
        self.layout_gr_usuario = QHBoxLayout()
        self.layout_gr_usuario.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.usuario_group_box = QGroupBox("USUARIO")
        self.usuario_group_box.setLayout(self.layout_gr_usuario)

        self.form_usuario = UsuarioFOrm()

        ## Grupo de proyecto y acuario
        self.layout_gr_proyecto = QHBoxLayout()
        self.layout_gr_proyecto.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.proyectro_group_box = QGroupBox("PROYECTO Y ACUARIO")
        self.proyectro_group_box.setLayout(self.layout_gr_proyecto)

        self.label_proyecto = QLabel("PROYECTO POR DEFECTO")
        self.combo_proyecto = ComboBox("PROYECTO POR DEFECTO")
        self.layout_proyecto = QVBoxLayout()

        self.label_acuario = QLabel("ACUARIO POR DEFECTO")
        self.combo_acuario = ComboBox("ACUARIO POR DEFECTO")
        self.layout_acuario = QVBoxLayout()

        self.layout_usuario = QVBoxLayout(self.tab_usuario)

        # Pestaña unidades
        self.tab_unidades = QWidget()

        ## Grupo de unidades dimensionales
        self.layout_gr_domensiones = QVBoxLayout()
        self.layout_gr_domensiones.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.dimensiones_group_box = QGroupBox("UNIDADES DIMENSIONALES")
        self.dimensiones_group_box.setLayout(self.layout_gr_domensiones)

        self.label_dim_urna = QLabel("DIMENSIONES URNA")
        self.combo_dim_urna = ComboBox("DIMENSIONES URNA")
        self.layout_dim_urna = QVBoxLayout()

        self.label_grosor_cristal = QLabel("GROSOR CRISTAL")
        self.combo_grosor_cristal = ComboBox("GROSOR CRISTAL")
        self.layout_grosor_cristal = QVBoxLayout()

        self.label_dim_filtro = QLabel("DIMENSIONES FILTRO")
        self.combo_dim_filtro = ComboBox("DIMENSIONES FILTRO")
        self.layout_dim_filtro = QVBoxLayout()

        self.label_dim_iluminacion = QLabel("DIMENSIONES LUMINARIA")
        self.combo_dim_iluminacion = ComboBox("DIMENSIONES LUMINARIA")
        self.layout_dim_iluminacion = QVBoxLayout()

        self.label_dim_talla = QLabel("DIMENSIONES TALLA PEZ")
        self.combo_dim_talla = ComboBox("DIMENSIONES TALLA PEZ")
        self.layout_dim_talla = QVBoxLayout()

        ## Grupo unidades de potencia
        self.layout_gr_potencia = QVBoxLayout()
        self.layout_gr_potencia.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.potencia_group_box = QGroupBox("UNIDADES DE POTENCIA")
        self.potencia_group_box.setLayout(self.layout_gr_potencia)

        self.label_potencia_filtro = QLabel("POTENCIA DE FILTRO")
        self.combo_potencia_filtro = ComboBox("POTENCIA DE FILTRO")
        self.layout_potencia_filtro = QVBoxLayout()

        self.label_potencia_calentador = QLabel("POTENCIA DEL CALENTADOR")
        self.combo_potencia_calentador = ComboBox("POTENCIA DEL CALENTADOR")
        self.layout_potencia_calentador = QVBoxLayout()

        self.label_potencia_luminaria = QLabel("POTENCIA DE LA LUMINARIA")
        self.combo_potencia_luminaria = ComboBox("POTENCIA DE LA LUMINARIA")
        self.layout_potencia_luminaria = QVBoxLayout()

        self.layout_unidades = QGridLayout(self.tab_unidades)

    def build_layout(self):
        """ Monta el layout del formulario. """

        # Opciones del usuario
        ## Datos de usuario
        self.layout_gr_usuario.addWidget(self.form_usuario)

        ## Monta el proyecto y acuario
        self.layout_proyecto.addWidget(self.label_proyecto)
        self.layout_proyecto.addWidget(self.combo_proyecto)

        self.layout_acuario.addWidget(self.label_acuario)
        self.layout_acuario.addWidget(self.combo_acuario)

        self.layout_gr_proyecto.addLayout(self.layout_proyecto)
        self.layout_gr_proyecto.addLayout(self.layout_acuario)

        ## Monta el usuario
        self.layout_usuario.addWidget(self.usuario_group_box)
        self.layout_usuario.addWidget(self.proyectro_group_box)
        self.tab_usuario.setLayout(self.layout_usuario)

        # Unidades
        ## Unidades dimensionales
        self.layout_dim_urna.addWidget(self.label_dim_urna)
        self.layout_dim_urna.addWidget(self.combo_dim_urna)

        self.layout_grosor_cristal.addWidget(self.label_grosor_cristal)
        self.layout_grosor_cristal.addWidget(self.combo_grosor_cristal)

        self.layout_dim_filtro.addWidget(self.label_dim_filtro)
        self.layout_dim_filtro.addWidget(self.combo_dim_filtro)

        self.layout_dim_iluminacion.addWidget(self.label_dim_iluminacion)
        self.layout_dim_iluminacion.addWidget(self.combo_dim_iluminacion)

        self.layout_dim_talla.addWidget(self.label_dim_talla)
        self.layout_dim_talla.addWidget(self.combo_dim_talla)

        self.layout_gr_domensiones.addLayout(self.layout_dim_urna)
        self.layout_gr_domensiones.addLayout(self.layout_grosor_cristal)
        self.layout_gr_domensiones.addLayout(self.layout_dim_filtro)
        self.layout_gr_domensiones.addLayout(self.layout_dim_iluminacion)
        self.layout_gr_domensiones.addLayout(self.layout_dim_talla)

        ## Unidades de potencia
        self.layout_potencia_filtro.addWidget(self.label_potencia_filtro)
        self.layout_potencia_filtro.addWidget(self.combo_potencia_filtro)

        self.layout_potencia_calentador.addWidget(
            self.label_potencia_calentador)
        self.layout_potencia_calentador.addWidget(
            self.combo_potencia_calentador)

        self.layout_potencia_luminaria.addWidget(self.label_potencia_luminaria)
        self.layout_potencia_luminaria.addWidget(self.combo_potencia_luminaria)

        self.layout_gr_potencia.addLayout(self.layout_potencia_filtro)
        self.layout_gr_potencia.addLayout(self.layout_potencia_calentador)
        self.layout_gr_potencia.addLayout(self.layout_potencia_luminaria)

        self.potencia_group_box.setLayout(self.layout_potencia_filtro)
        self.potencia_group_box.setLayout(self.layout_potencia_calentador)

        # Montamos las unidades
        self.layout_unidades.addWidget(self.dimensiones_group_box, 0, 0)
        self.layout_unidades.addWidget(self.potencia_group_box, 0, 1)

        # Se monta el formulario
        self.tab_widget.addTab(self.tab_usuario, "USUARIO: INIGOI")
        self.tab_widget.addTab(self.tab_unidades, "UNIDADES")
        self.layout_form.addWidget(self.tab_widget)
        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ConfiguracionForm()
    ventana.setMinimumWidth(600)
    ventana.setMinimumHeight(400)
    ventana.show()

    sys.exit(app.exec())
