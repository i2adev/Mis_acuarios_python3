"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/05/2025
Comentarios:
    Módulo que contiene el formulario del modulo maestro.
"""

import sys
from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QFont, QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                             QPushButton, QSizeGrip, QSizePolicy, QSpacerItem,
                             QVBoxLayout, QWidget)

import globales


class ModuloMaestroView(QWidget):
    """ Formulario de tipo de filtro """

    def __init__(self, w_title: str):
        """ Constructor de clase """

        super().__init__()
        # self.setMinimumSize(800, 600)

        self.fuente_menu = QFont("Roboto", 14, QFont.Weight.Bold)

        # SizeGrip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Configura el formulario
        self.window_title = w_title
        self.label_window_title = w_title
        self.create_widgets()
        self.build_layout()
        self.hide_panels()
        self.set_tab_order()
        self.init_handlers()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

    def init_handlers(self):
        """ Inicializamos los eventos de la ventana """

        # mover ventana
        self.frame_title_bar.mouseMoveEvent = self.mover_ventana

        # Botones de la barra de título
        self.button_tb_close.clicked.connect(lambda: self.close())
        self.button_tb_maximize.clicked.connect(self.control_bt_maximizar)
        self.button_tb_restore.clicked.connect(self.control_bt_normal)
        self.button_tb_minimize.clicked.connect(self.control_bt_minimizar)

        # Botones de la barra de menú
        self.button_menu_acuario.clicked.connect(
            lambda: self.show_panel(self.acuario)
            if self.acuario.isHidden()
            else self.hide_panel(self.acuario)
        )

        self.button_menu_comercio.clicked.connect(
            lambda: self.show_panel(self.comercio)
            if self.comercio.isHidden()
            else self.hide_panel(self.comercio)
        )

        self.button_menu_consumible.clicked.connect(
            lambda: self.show_panel(self.consumible)
            if self.consumible.isHidden()
            else self.hide_panel(self.consumible)
        )

        self.button_menu_equipamiento.clicked.connect(
            lambda: self.show_panel(self.equipamiento)
            if self.equipamiento.isHidden()
            else self.hide_panel(self.equipamiento)
        )

        self.button_menu_fauna.clicked.connect(
            lambda: self.show_panel(self.fauna)
            if self.fauna.isHidden()
            else self.hide_panel(self.fauna)
        )

        self.button_menu_filtro.clicked.connect(
            lambda: self.show_panel(self.filtro)
            if self.filtro.isHidden()
            else self.hide_panel(self.filtro)
        )

        self.button_menu_flora.clicked.connect(
            lambda: self.show_panel(self.flora)
            if self.flora.isHidden()
            else self.hide_panel(self.flora)
        )

        self.button_menu_iluminacion.clicked.connect(
            lambda: self.show_panel(self.iluminacion)
            if self.iluminacion.isHidden()
            else self.hide_panel(self.iluminacion)
        )

        self.button_menu_incidencia.clicked.connect(
            lambda: self.show_panel(self.incidencia)
            if self.incidencia.isHidden()
            else self.hide_panel(self.incidencia)
        )

        self.button_menu_marca.clicked.connect(
            lambda: self.show_panel(self.marca)
            if self.marca.isHidden()
            else self.hide_panel(self.marca)
        )

        self.button_menu_proyecto.clicked.connect(
            lambda: self.show_panel(self.proyecto)
            if self.proyecto.isHidden()
            else self.hide_panel(self.proyecto)
        )

        self.button_menu_urna.clicked.connect(
            lambda: self.show_panel(self.urna)
            if self.urna.isHidden()
            else self.hide_panel(self.urna)
        )

        self.button_menu_otros.clicked.connect(
            lambda: self.show_panel(self.otro)
            if self.otro.isHidden()
            else self.hide_panel(self.otro)
        )

    def build_layout(self):
        """ Construye el layout de la ventana """

        # Establece las dimensiones minimas de la vista
        self.setMinimumWidth(1500)
        self.setMinimumHeight(900)

        # Ocultar barra de título
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Configuramos el menú lateral
        self.menu_layout.addWidget(self.button_menu_acuario)
        self.menu_layout.addWidget(self.acuario)
        self.menu_layout.addWidget(self.button_menu_comercio)
        self.menu_layout.addWidget(self.comercio)
        self.menu_layout.addWidget(self.button_menu_consumible)
        self.menu_layout.addWidget(self.consumible)
        self.menu_layout.addWidget(self.button_menu_equipamiento)
        self.menu_layout.addWidget(self.equipamiento)
        self.menu_layout.addWidget(self.button_menu_fauna)
        self.menu_layout.addWidget(self.fauna)
        self.menu_layout.addWidget(self.button_menu_filtro)
        self.menu_layout.addWidget(self.filtro)
        self.menu_layout.addWidget(self.button_menu_flora)
        self.menu_layout.addWidget(self.flora)
        self.menu_layout.addWidget(self.button_menu_iluminacion)
        self.menu_layout.addWidget(self.iluminacion)
        self.menu_layout.addWidget(self.button_menu_incidencia)
        self.menu_layout.addWidget(self.incidencia)
        self.menu_layout.addWidget(self.button_menu_marca)
        self.menu_layout.addWidget(self.marca)
        self.menu_layout.addWidget(self.button_menu_proyecto)
        self.menu_layout.addWidget(self.proyecto)
        self.menu_layout.addWidget(self.button_menu_urna)
        self.menu_layout.addWidget(self.urna)
        self.menu_layout.addWidget(self.button_menu_otros)
        self.menu_layout.addWidget(self.otro)

        self.menu_layout.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Minimum,
                        QSizePolicy.Policy.Expanding)
        )

        # Configuramos la barra del título
        self.layout_title_bar.addWidget(self.label_icon)
        self.layout_title_bar.addWidget(self.label_window_title)
        self.layout_title_bar.addItem(self.spacer_tb)
        self.layout_title_bar.addWidget(self.button_tb_minimize)
        self.layout_title_bar.addWidget(self.button_tb_restore)
        self.layout_title_bar.addWidget(self.button_tb_maximize)
        self.layout_title_bar.addWidget(self.button_tb_close)

        # Cargamos los layout en la ventana
        self.layout_central.addWidget(self.frame_menu)
        self.layout_central.addLayout(self.layout_dashboard)

        self.layout_main.addWidget(self.frame_title_bar)
        self.layout_main.addLayout(self.layout_central)
        self.setLayout(self.layout_main)

    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout(self)  # Layout principal
        self.layout_central = QVBoxLayout()  # Layout central donde se coloca
        # la barra de título y el dashboard
        self.menu_layout = QVBoxLayout()  # Layout donde se alberga el menú
        # lateral
        self.maestro_layout = QVBoxLayout()
        self.frame_menu = QFrame()
        self.frame_menu.setStyleSheet(
            """
            QFrame {
                background-color: transparent;
                border: 0px solid transparent;
            }

            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 18px; 
                font-weight: bold;
            }
            """
        )

        self.frame_menu.setObjectName("frame_menu")
        self.frame_menu.setFixedWidth(250)
        self.frame_menu.setLayout(self.menu_layout)

        self.layout_title_bar = QHBoxLayout()  # Layout barra título
        self.layout_title_bar.setContentsMargins(0, 0, 0, 0)

        self.layout_dashboard = QHBoxLayout()  # Layout del dashboard

        # ACUARIO
        self.button_menu_acuario = QPushButton("ACUARIO")
        self.button_menu_acuario.setIcon(
            QIcon(str(globales.PATH_IMAGES / "acuario.png"))
        )
        self.button_menu_acuario.setIconSize(QSize(32, 32))
        self.button_menu_acuario.setObjectName("button_menu_acuario")
        self.button_menu_acuario.setFlat(True)
        self.button_menu_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.acuario = QWidget()
        self.layout_acuario = QVBoxLayout(self.acuario)
        self.layout_acuario.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_acuario = QPushButton("ACUARIOS")
        self.button_maestro_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_acuario.setObjectName(
            "button_maestro_acuario"
        )
        self.button_maestro_acuario.setFlat(True)
        self.button_maestro_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_tipo_acuario = QPushButton(
            "TIPOS DE ACUARIO"
        )
        self.button_maestro_tipo_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_tipo_acuario.setObjectName(
            "button_maestro_tipo_acuario"
        )
        self.button_maestro_tipo_acuario.setFlat(True)
        self.button_maestro_tipo_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_categoria_acuario = QPushButton(
            "CATEGORÍAS DE ACUARIO"
        )
        self.button_maestro_categoria_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_categoria_acuario.setObjectName(
            "button_maestro_categoria_acuario"
        )
        self.button_maestro_categoria_acuario.setFlat(True)
        self.button_maestro_categoria_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_subcategoria_acuario = QPushButton(
            "SUBCATEGORÍAS DE ACUARIO"
        )
        self.button_maestro_subcategoria_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_subcategoria_acuario.setObjectName(
            "button_maestro_subcategoria_acuario"
        )
        self.button_maestro_subcategoria_acuario.setFlat(True)
        self.button_maestro_subcategoria_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_acuario.addWidget(self.button_maestro_acuario)
        self.layout_acuario.addWidget(self.button_maestro_tipo_acuario)
        self.layout_acuario.addWidget(self.button_maestro_categoria_acuario)
        self.layout_acuario.addWidget(self.button_maestro_subcategoria_acuario)

        # COMERCIO
        self.button_menu_comercio = QPushButton(
            "COMERCIO"
        )
        self.button_menu_comercio.setIcon(
            QIcon(str(globales.PATH_IMAGES / "comercio.png"))
        )
        self.button_menu_comercio.setIconSize(QSize(32, 32))
        self.button_menu_comercio.setObjectName(
            "button_menu_comercio"
        )
        self.button_menu_comercio.setFlat(True)
        self.button_menu_comercio.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.comercio = QWidget()
        self.layout_comercio = QVBoxLayout(self.comercio)
        self.layout_comercio.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_comercio = QPushButton(
            "COMERCIOS"
        )
        self.button_maestro_comercio.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_comercio.setObjectName(
            "button_maestro_comercio"
        )
        self.button_maestro_comercio.setFlat(True)
        self.button_maestro_comercio.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_comercio.addWidget(self.button_maestro_comercio)

        # CONSUMIBLE
        self.button_menu_consumible = QPushButton(
            "CONSUMIBLE"
        )
        self.button_menu_consumible.setIcon(
            QIcon(str(globales.PATH_IMAGES / "consumible.png"))
        )
        self.button_menu_consumible.setIconSize(QSize(32, 32))
        self.button_menu_consumible.setObjectName(
            "button_menu_consumible"
        )
        self.button_menu_consumible.setFlat(True)
        self.button_menu_consumible.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.consumible = QWidget()
        self.layout_consumible = QVBoxLayout(self.consumible)
        self.layout_consumible.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_consumible = QPushButton(
            "CONSUMIBLES"
        )
        self.button_maestro_consumible.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_consumible.setObjectName(
            "button_maestro_consumible"
        )
        self.button_maestro_consumible.setFlat(True)
        self.button_maestro_consumible.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_cat_consumible = QPushButton(
            "CAT. CONSUMIBLES"
        )
        self.button_maestro_cat_consumible.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_cat_consumible.setObjectName(
            "button_maestro_cat_consumible"
        )
        self.button_maestro_cat_consumible.setFlat(True)
        self.button_maestro_cat_consumible.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_formato_consumible = QPushButton(
            "FORMATOS CONSUMIBLE"
        )
        self.button_maestro_formato_consumible.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_formato_consumible.setObjectName(
            "button_maestro_formato_consumible"
        )
        self.button_maestro_formato_consumible.setFlat(True)
        self.button_maestro_formato_consumible.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_unidad_contenido = QPushButton(
            "UNIDAD DE CONTENIDO"
        )
        self.button_maestro_unidad_contenido.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_unidad_contenido.setObjectName(
            "button_maestro_unidad_contenido"
        )
        self.button_maestro_unidad_contenido.setFlat(True)
        self.button_maestro_unidad_contenido.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_consumible.addWidget(self.button_maestro_consumible)
        self.layout_consumible.addWidget(self.button_maestro_cat_consumible)
        self.layout_consumible.addWidget(
            self.button_maestro_formato_consumible)
        self.layout_consumible.addWidget(self.button_maestro_unidad_contenido)

        # EQUIPAMIENTO
        self.button_menu_equipamiento = QPushButton("EQUIPAMIENTO")
        self.button_menu_equipamiento.setIcon(
            QIcon(str(globales.PATH_IMAGES / "equipamiento.png"))
        )
        self.button_menu_equipamiento.setIconSize(QSize(32, 32))
        self.button_menu_equipamiento.setObjectName(
            "button_menu_equipamiento"
        )
        self.button_menu_equipamiento.setFlat(True)
        self.button_menu_equipamiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.equipamiento = QWidget()
        self.layout_equipamiento = QVBoxLayout(self.equipamiento)
        self.layout_equipamiento.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_equipamiento = QPushButton("EQUIPAMIENTOS")
        self.button_maestro_equipamiento.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_equipamiento.setObjectName(
            "button_maestro_equipamiento"
        )
        self.button_maestro_equipamiento.setFlat(True)
        self.button_maestro_equipamiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_cat_equipamiento = QPushButton(
            "CAT. EQUIPAMIENTOS"
        )
        self.button_maestro_cat_equipamiento.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_cat_equipamiento.setObjectName(
            "button_maestro_equipamiento"
        )
        self.button_maestro_cat_equipamiento.setFlat(True)
        self.button_maestro_cat_equipamiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.button_maestro_cat_equipamiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_equipamiento.addWidget(self.button_maestro_equipamiento)
        self.layout_equipamiento.addWidget(
            self.button_maestro_cat_equipamiento)

        # FAUNA
        self.button_menu_fauna = QPushButton(
            "FAUNA"
        )
        self.button_menu_fauna.setIcon(
            QIcon(str(globales.PATH_IMAGES / "fauna.png"))
        )
        self.button_menu_fauna.setIconSize(QSize(32, 32))
        self.button_menu_fauna.setObjectName(
            "button_maestro_fauna"
        )
        self.button_menu_fauna.setFlat(True)
        self.button_menu_fauna.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.fauna = QWidget()
        self.layout_fauna = QVBoxLayout(self.fauna)
        self.layout_fauna.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_especies_animales = QPushButton(
            "ESPECIES ANIMALES"
        )
        self.button_maestro_especies_animales.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_especies_animales.setObjectName(
            "button_maestro_especies_animales"
        )
        self.button_maestro_especies_animales.setFlat(True)
        self.button_maestro_especies_animales.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_comportamiento = QPushButton(
            "COMPORTAMIENTO"
        )
        self.button_maestro_comportamiento.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_comportamiento.setObjectName(
            "button_maestro_comportamiento"
        )
        self.button_maestro_comportamiento.setFlat(True)
        self.button_maestro_comportamiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_nivel_nado = QPushButton(
            "NIVEL DE NADO"
        )
        self.button_maestro_nivel_nado.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_nivel_nado.setObjectName(
            "button_maestro_nivel_nado"
        )
        self.button_maestro_nivel_nado.setFlat(True)
        self.button_maestro_nivel_nado.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.button_maestro_grupo_taxonomico = QPushButton(
            "GRUPO TAXONÓMICO"
        )
        self.button_maestro_grupo_taxonomico.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_grupo_taxonomico.setObjectName(
            "button_maestro_grupo_taxonomico"
        )
        self.button_maestro_grupo_taxonomico.setFlat(True)
        self.button_maestro_grupo_taxonomico.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_dieta = QPushButton(
            "DIETA"
        )
        self.button_maestro_dieta.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_dieta.setObjectName(
            "button_maestro_dieta"
        )
        self.button_maestro_dieta.setFlat(True)
        self.button_maestro_dieta.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_sexo = QPushButton(
            "SEXO"
        )
        self.button_maestro_sexo.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_sexo.setObjectName(
            "button_maestro_sexo"
        )
        self.button_maestro_sexo.setFlat(True)
        self.button_maestro_sexo.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_fauna.addWidget(self.button_maestro_especies_animales)
        self.layout_fauna.addWidget(self.button_maestro_comportamiento)
        self.layout_fauna.addWidget(self.button_maestro_dieta)
        self.layout_fauna.addWidget(self.button_maestro_nivel_nado)
        self.layout_fauna.addWidget(self.button_maestro_grupo_taxonomico)
        self.layout_fauna.addWidget(self.button_maestro_sexo)

        # FILTROS
        self.button_menu_filtro = QPushButton(
            "FILTRO"
        )
        self.button_menu_filtro.setIcon(
            QIcon(str(globales.PATH_IMAGES / "filtro.png"))
        )
        self.button_menu_filtro.setIconSize(QSize(32, 32))
        self.button_menu_filtro.setObjectName(
            "button_menu_filtro"
        )
        self.button_menu_filtro.setFlat(True)
        self.button_menu_filtro.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.filtro = QWidget()
        self.layout_filtro = QVBoxLayout(self.filtro)
        self.layout_filtro.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_filtro = QPushButton(
            "FILTROS"
        )
        self.button_maestro_filtro.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_filtro.setObjectName(
            "button_maestro_filtro"
        )
        self.button_maestro_filtro.setFlat(True)
        self.button_maestro_filtro.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_tipo_filtro = QPushButton("TIPOS DE FILTRO")
        self.button_maestro_tipo_filtro.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_tipo_filtro.setObjectName(
            "button_maestro_tipo_filtro"
        )
        self.button_maestro_tipo_filtro.setFlat(True)
        self.button_maestro_tipo_filtro.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_filtro.addWidget(self.button_maestro_filtro)
        self.layout_filtro.addWidget(self.button_maestro_tipo_filtro)

        # FLORA
        self.button_menu_flora = QPushButton(
            "FLORA"
        )
        self.button_menu_flora.setIcon(
            QIcon(str(globales.PATH_IMAGES / "flora.png"))
        )
        self.button_menu_flora.setIconSize(QSize(32, 32))
        self.button_menu_flora.setObjectName(
            "button_menu_flora"
        )
        self.button_menu_flora.setFlat(True)
        self.button_menu_flora.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.flora = QWidget()
        self.layout_flora = QVBoxLayout(self.flora)
        self.layout_flora.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_dificultad_planta = QPushButton(
            "DIFICULTAD DE LAS PLANTAS"
        )
        self.button_maestro_dificultad_planta.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_dificultad_planta.setObjectName(
            "button_maestro_dificultad_planta"
        )
        self.button_maestro_dificultad_planta.setFlat(True)
        self.button_maestro_dificultad_planta.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.button_maestro_especie_vegetal = QPushButton(
            "ESPECIE VEGETAL"
        )
        self.button_maestro_especie_vegetal.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_especie_vegetal.setObjectName(
            "button_maestro_especie_vegetal"
        )
        self.button_maestro_especie_vegetal.setFlat(True)
        self.button_maestro_especie_vegetal.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_tasa_crecimiento = QPushButton(
            "TASAS DE CRECIMIENTO"
        )
        self.button_maestro_tasa_crecimiento.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_tasa_crecimiento.setObjectName(
            "button_maestro_tasa_crecimiento"
        )
        self.button_maestro_tasa_crecimiento.setFlat(True)
        self.button_maestro_tasa_crecimiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_posición_planta = QPushButton(
            "POSICIÓN EN EL ACUARIO"
        )
        self.button_maestro_posición_planta.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_posición_planta.setObjectName(
            "button_maestro_posición_planta"
        )
        self.button_maestro_posición_planta.setFlat(True)
        self.button_maestro_posición_planta.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_requerimiento_co2 = QPushButton(
            "REQUERIMIENTOS DE CO2"
        )
        self.button_maestro_requerimiento_co2.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_requerimiento_co2.setObjectName(
            "button_maestro_requerimiento_co2"
        )
        self.button_maestro_requerimiento_co2.setFlat(True)
        self.button_maestro_requerimiento_co2.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_requerimiento_iluminacion = QPushButton(
            "REQUERIMIENTOS DE ILUMINACIÓN"
        )
        self.button_maestro_requerimiento_iluminacion.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_requerimiento_iluminacion.setObjectName(
            "button_maestro_requerimiento_iluminacion"
        )
        self.button_maestro_requerimiento_iluminacion.setFlat(True)
        self.button_maestro_requerimiento_iluminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_flora.addWidget(self.button_maestro_especie_vegetal)
        self.layout_flora.addWidget(self.button_maestro_dificultad_planta)
        self.layout_flora.addWidget(self.button_maestro_posición_planta)
        self.layout_flora.addWidget(self.button_maestro_requerimiento_co2)
        self.layout_flora.addWidget(
            self.button_maestro_requerimiento_iluminacion)
        self.layout_flora.addWidget(self.button_maestro_tasa_crecimiento)

        # ILUMINACIÓN
        self.button_menu_iluminacion = QPushButton(
            "ILUMINACIÓN"
        )
        self.button_menu_iluminacion.setIcon(
            QIcon(str(globales.PATH_IMAGES / "iluminacion.png"))
        )
        self.button_menu_iluminacion.setIconSize(QSize(32, 32))
        self.button_menu_iluminacion.setObjectName(
            "button_menu_iluminacion"
        )
        self.button_menu_iluminacion.setFlat(True)
        self.button_menu_iluminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.iluminacion = QWidget()
        self.layout_iluminacion = QVBoxLayout(self.iluminacion)
        self.layout_iluminacion.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_iluminacion = QPushButton(
            "LUMINARIAS"
        )
        self.button_maestro_iluminacion.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_iluminacion.setObjectName(
            "button_maestro_iluminacion"
        )
        self.button_maestro_iluminacion.setFlat(True)
        self.button_maestro_iluminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_control_iluminacion = QPushButton(
            "CONTROLES DE ILUMINACIÓN"
        )
        self.button_maestro_control_iluminacion.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_control_iluminacion.setObjectName(
            "button_maestro_control_iluminacion"
        )
        self.button_maestro_control_iluminacion.setFlat(True)
        self.button_maestro_control_iluminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_tipo_iluminacion = QPushButton(
            "TIPOS DE ILUMINACIÓN"
        )
        self.button_maestro_tipo_iluminacion.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_tipo_iluminacion.setObjectName(
            "button_maestro_tipo_iluminacion"
        )
        self.button_maestro_tipo_iluminacion.setFlat(True)
        self.button_maestro_tipo_iluminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_iluminacion.addWidget(self.button_maestro_iluminacion)
        self.layout_iluminacion.addWidget(self.button_maestro_tipo_iluminacion)
        self.layout_iluminacion.addWidget(
            self.button_maestro_control_iluminacion)

        # INCIDENCIAS
        self.button_menu_incidencia = QPushButton(
            "INCIDENCIA"
        )
        self.button_menu_incidencia.setIcon(
            QIcon(str(globales.PATH_IMAGES / "incidencia.png"))
        )
        self.button_menu_incidencia.setIconSize(QSize(32, 32))
        self.button_menu_incidencia.setObjectName(
            "button_menu_incidencia"
        )
        self.button_menu_incidencia.setFlat(True)
        self.button_menu_incidencia.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.incidencia = QWidget()
        self.layout_incidencia = QVBoxLayout(self.incidencia)
        self.layout_incidencia.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_cat_incidencia = QPushButton(
            "CATEGORÍAS DE INCIDENCIA"
        )
        self.button_maestro_cat_incidencia.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_cat_incidencia.setObjectName(
            "button_maestro_cat_incidencia"
        )
        self.button_maestro_cat_incidencia.setFlat(True)
        self.button_maestro_cat_incidencia.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_subcat_incidencia = QPushButton(
            "SUBCATEGORÍAS DE INCIDENCIA"
        )
        self.button_maestro_subcat_incidencia.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_subcat_incidencia.setObjectName(
            "button_maestro_subcat_incidencia"
        )
        self.button_maestro_subcat_incidencia.setFlat(True)
        self.button_maestro_subcat_incidencia.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_incidencia.addWidget(self.button_maestro_cat_incidencia)
        self.layout_incidencia.addWidget(self.button_maestro_subcat_incidencia)

        # MARCAS COMERCIALES
        self.button_menu_marca = QPushButton(
            "MARCA COMERCIAL"
        )
        self.button_menu_marca.setIcon(
            QIcon(str(globales.PATH_IMAGES / "marca-comercial.png"))
        )
        self.button_menu_marca.setIconSize(QSize(32, 32))
        self.button_menu_marca.setObjectName(
            "button_menu_marca"
        )
        self.button_menu_marca.setFlat(True)
        self.button_menu_marca.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.marca = QWidget()
        self.layout_marca = QVBoxLayout(self.marca)
        self.layout_marca.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_marca = QPushButton(
            "MARCAS COMERCIALES"
        )
        self.button_maestro_marca.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;                
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_marca.setObjectName(
            "button_maestro_marca"
        )
        self.button_maestro_marca.setFlat(True)
        self.button_maestro_marca.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_marca.addWidget(self.button_maestro_marca)

        # PROYECTO
        self.button_menu_proyecto = QPushButton(
            "PROYECTO"
        )
        self.button_menu_proyecto.setIcon(
            QIcon(str(globales.PATH_IMAGES / "proyecto.png"))
        )
        self.button_menu_proyecto.setIconSize(QSize(32, 32))
        self.button_menu_proyecto.setObjectName(
            "button_menu_proyecto"
        )
        self.button_menu_proyecto.setFlat(True)
        self.button_menu_proyecto.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.proyecto = QWidget()
        self.layout_proyecto = QVBoxLayout(self.proyecto)
        self.layout_proyecto.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_proyecto = QPushButton(
            "PROYECTOS"
        )
        self.button_maestro_proyecto.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_proyecto.setObjectName(
            "button_maestro_proyecto"
        )
        self.button_maestro_proyecto.setFlat(True)
        self.button_maestro_proyecto.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_estado_proyecto = QPushButton(
            "ESTADOS PROYECTOS"
        )
        self.button_maestro_estado_proyecto.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;                
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_estado_proyecto.setObjectName(
            "button_maestro_estado_proyecto"
        )
        self.button_maestro_estado_proyecto.setFlat(True)
        self.button_maestro_estado_proyecto.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_proyecto.addWidget(self.button_maestro_proyecto)
        self.layout_proyecto.addWidget(self.button_maestro_estado_proyecto)

        # URNA
        self.button_menu_urna = QPushButton("URNA")
        self.button_menu_urna.setIcon(
            QIcon(str(globales.PATH_IMAGES / "urna.png"))
        )
        self.button_menu_urna.setIconSize(QSize(32, 32))
        self.button_menu_urna.setObjectName(
            "button_menu_urna"
        )
        self.button_menu_urna.setFlat(True)
        self.button_menu_urna.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.urna = QWidget()
        self.layout_urna = QVBoxLayout(self.urna)
        self.layout_urna.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_urna = QPushButton("URNAS")
        self.button_maestro_urna.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_urna.setObjectName(
            "button_maestro_urna"
        )
        self.button_maestro_urna.setFlat(True)
        self.button_maestro_urna.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_material = QPushButton(
            "MATERIALES DE URNAS"
        )
        self.button_maestro_material.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_material.setObjectName(
            "button_maestro_material"
        )
        self.button_maestro_material.setFlat(True)
        self.button_maestro_material.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_urna.addWidget(self.button_maestro_urna)
        self.layout_urna.addWidget(self.button_maestro_material)

        # OTROS
        self.button_menu_otros = QPushButton("OTROS")
        self.button_menu_otros.setIcon(
            QIcon(str(globales.PATH_IMAGES / "otros.png"))
        )
        self.button_menu_otros.setIconSize(QSize(32, 32))
        self.button_menu_otros.setObjectName(
            "button_menu_otros"
        )
        self.button_menu_otros.setFlat(True)
        self.button_menu_otros.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.otro = QWidget()
        self.layout_otros = QVBoxLayout(self.otro)
        self.layout_otros.setContentsMargins(35, 0, 0, 0)

        self.button_maestro_periodos = QPushButton(
            "PERIODOS"
        )
        self.button_maestro_periodos.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_periodos.setObjectName(
            "button_maestro_periodos"
        )
        self.button_maestro_periodos.setFlat(True)
        self.button_maestro_periodos.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.layout_otros.addWidget(self.button_maestro_periodos)

        # Controles de la barra de título
        ## Frame de la barra de título
        self.frame_title_bar = QFrame()
        self.frame_title_bar.setLayout(self.layout_title_bar)
        self.frame_title_bar.setStyleSheet(
            """
                QFrame {
                    background-color: transparent;
                    border: 0px solid transparent;
                }
            """
        )
        self.frame_title_bar.setContentsMargins(0, 0, 0, 10)

        ## Botón de cerrar
        icon = QIcon()
        icon.addPixmap(
            QPixmap(str(Path(globales.PATH_IMAGES) / "close.png")),
            QIcon.Mode.Normal,
            QIcon.State.On)
        self.button_tb_close = QPushButton()
        self.button_tb_close.setIcon(icon)
        self.button_tb_close.setObjectName("button_bt_close")
        self.button_tb_close.setFlat(True)
        self.button_tb_close.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Botón de maximizar
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(str(Path(globales.PATH_IMAGES) / "maximize.png")),
            QIcon.Mode.Normal,
            QIcon.State.On)
        self.button_tb_maximize = QPushButton()
        self.button_tb_maximize.setIcon(icon2)
        self.button_tb_maximize.setObjectName("button_bt_maximize")
        self.button_tb_maximize.setFlat(True)
        self.button_tb_maximize.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Pripiedades del botón restaurar
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(str(Path(globales.PATH_IMAGES) / "restore.png")),
            QIcon.Mode.Normal,
            QIcon.State.On)
        self.button_tb_restore = QPushButton()
        self.button_tb_restore.setIcon(icon3)
        self.button_tb_restore.setObjectName("button_bt_restore")
        self.button_tb_restore.setFlat(True)
        self.button_tb_restore.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.button_tb_restore.hide()

        ## Propiedades del botón minimizar
        icon4 = QIcon()
        icon4.addPixmap(
            QPixmap(str(Path(globales.PATH_IMAGES) / "minimize.png")),
            QIcon.Mode.Normal,
            QIcon.State.On)
        self.button_tb_minimize = QPushButton()
        self.button_tb_minimize.setIcon(icon4)
        self.button_tb_minimize.setObjectName("button_tb_minimize")
        self.button_tb_minimize.setFlat(True)
        self.button_tb_minimize.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ### Espaciador
        self.spacer_tb = QSpacerItem(400, 10, QSizePolicy.Policy.Expanding,
                                     QSizePolicy.Policy.Minimum)

        self.label_window_title = QLabel(self.window_title)

        ## Icono de la ventana
        self.label_icon = QLabel()
        icon5 = QPixmap(":/Images/Window_icon.png")
        self.label_icon.setPixmap(icon5)

    """
    El comportamiento básico de la barra de titulo que hemos creado
    """

    def control_bt_minimizar(self):
        """ Minimiza la ventana """
        self.showMinimized()

    def control_bt_maximizar(self):
        """ Maximiza la ventana """
        self.showMaximized()
        self.button_tb_maximize.hide()
        self.button_tb_restore.show()

    def control_bt_normal(self):
        """ Establece el tamaño normal de la ventana """
        self.showNormal()
        self.button_tb_restore.hide()
        self.button_tb_maximize.show()

    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom()
                       - self.gripSize)

    ## mover ventana
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint()

    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint()
                          - self.drag_position)
                self.drag_position = event.globalPosition().toPoint()
                event.accept()

        if self.drag_position.y() <= 20:
            self.showMaximized()

    def hide_panels(self):
        """ Oculta todos los paneles. """

        if not self.acuario.isHidden():
            self.acuario.hide()
        if not self.comercio.isHidden():
            self.comercio.hide()
        if not self.consumible.isHidden():
            self.consumible.hide()
        if not self.equipamiento.isHidden():
            self.equipamiento.hide()
        if not self.fauna.isHidden():
            self.fauna.hide()
        if not self.filtro.isHidden():
            self.filtro.hide()
        if not self.flora.isHidden():
            self.flora.hide()
        if not self.marca.isHidden():
            self.marca.hide()
        if not self.iluminacion.isHidden():
            self.iluminacion.hide()
        if not self.incidencia.isHidden():
            self.incidencia.hide()
        if not self.proyecto.isHidden():
            self.proyecto.hide()
        if not self.urna.isHidden():
            self.urna.hide()
        if not self.otro.isHidden():
            self.otro.hide()

    def show_panel(self, panel: QWidget):
        """
        Muestra un panel.
        :param panel: Panel a mostrar.
        """

        self.hide_panels()
        panel.show()

    def hide_panel(self, panel: QWidget):
        """
        Oculta un panel.
        :param panel: Panel a ocultar.
        """

        panel.hide()


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ModuloMaestroView("MODULO MAESTRO")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
