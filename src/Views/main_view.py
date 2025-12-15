"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      22/06/2025
Comentarios:
    Módulo que contiene el formulario principal.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QFont, QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                             QPushButton, QSizeGrip, QSizePolicy, QSpacerItem,
                             QVBoxLayout, QWidget)


class MainView(QWidget):
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
        self.set_tab_order()
        self.init_basic_handlers()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

    def init_basic_handlers(self):
        """ Inicializamos los eventos de la ventana """

        # mover ventana
        self.frame_title_bar.mouseMoveEvent = self.mover_ventana

        # Botones de la barra de título
        self.button_tb_close.clicked.connect(lambda: self.close())
        self.button_tb_maximize.clicked.connect(self.control_bt_maximizar)
        self.button_tb_restore.clicked.connect(self.control_bt_normal)
        self.button_tb_minimize.clicked.connect(self.control_bt_minimizar)

    def build_layout(self):
        """ Construye el layout de la ventana """

        # Establece las dimensiones minimas de la vista
        self.setMinimumWidth(1500)
        self.setMinimumHeight(900)

        # Ocultar barra de título
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Configuramos el menú lateral
        self.menu_layout.addWidget(self.button_menu_insert)
        self.menu_layout.addWidget(self.button_menu_maestro)
        self.menu_layout.addLayout(self.maestro_layout)
        self.menu_layout.addLayout(self.maestro_layout)
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

        # Layout de menú maestro
        self.maestro_layout.addWidget(self.button_maestro_acuario)
        self.maestro_layout.addWidget(self.button_maestro_tipo_acuario)
        self.maestro_layout.addWidget(self.button_maestro_categoria_acuario)
        self.maestro_layout.addWidget(self.button_maestro_subcategoria_acuario)
        self.maestro_layout.addWidget(self.button_maestro_subcat_incidencia)
        self.maestro_layout.addWidget(self.button_maestro_cat_producto)
        self.maestro_layout.addWidget(self.button_maestro_comercio)
        self.maestro_layout.addWidget(self.button_maestro_equipamiento)
        self.maestro_layout.addWidget(self.button_maestro_cat_equipamiento)
        self.maestro_layout.addWidget(self.button_maestro_facturas)
        self.maestro_layout.addWidget(self.button_maestro_filtro)
        self.maestro_layout.addWidget(self.button_maestro_tipo_filtro)
        self.maestro_layout.addWidget(self.button_maestro_incidencia)
        self.maestro_layout.addWidget(self.button_maestro_cat_incidencia)
        self.maestro_layout.addWidget(self.button_maestro_subcat_incidencia)
        self.maestro_layout.addWidget(self.button_maestro_marca)
        self.maestro_layout.addWidget(self.button_maestro_proyecto)
        self.maestro_layout.addWidget(self.button_maestro_estado_proyecto)
        self.maestro_layout.addWidget(self.button_maestro_urna)
        self.maestro_layout.addWidget(self.button_maestro_material)

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

        # Controles del área de menú
        self.button_menu_insert = QPushButton("INSERT")
        self.button_menu_insert.setObjectName("button_menu_insert")
        self.button_menu_insert.setFlat(True)
        self.button_menu_insert.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_menu_maestro = QPushButton("MAESTRO")
        self.button_menu_maestro.setObjectName("button_menu_maestro")
        self.button_menu_maestro.setFlat(True)

        ## Botones del layout maestro
        self.button_maestro_acuario = QPushButton("ACUARIOS")
        self.button_maestro_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_cat_incidencia = QPushButton(
            " > CATEGORÍAS DE INCIDENCIA"
        )
        self.button_maestro_cat_incidencia.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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
            " > SUBCATEGORÍAS DE INCIDENCIA"
        )
        self.button_maestro_subcat_incidencia.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_cat_producto = QPushButton(
            "CATEGORÍAS DE PRODUCTO"
        )
        self.button_maestro_cat_producto.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_cat_producto.setObjectName(
            "button_maestro_cat_producto"
        )
        self.button_maestro_cat_producto.setFlat(True)
        self.button_maestro_cat_producto.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_comercio = QPushButton(
            "COMERCIOS"
        )
        self.button_maestro_comercio.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_facturas = QPushButton(
            "FACTURAS"
        )
        self.button_maestro_facturas.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_facturas.setObjectName(
            "button_maestro_facturas"
        )
        self.button_maestro_facturas.setFlat(True)
        self.button_maestro_facturas.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_filtro = QPushButton(
            "FILTROS"
        )
        self.button_maestro_filtro.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_incidencia = QPushButton(
            "INCIDENCIAS"
        )
        self.button_maestro_incidencia.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
                font-family: 'Roboto'; 
                font-size: 14px;
            }
            """
        )
        self.button_maestro_incidencia.setObjectName(
            "button_maestro_incidencia"
        )
        self.button_maestro_incidencia.setFlat(True)
        self.button_maestro_incidencia.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_maestro_marca = QPushButton(
            "MARCAS COMERCIALES"
        )
        self.button_maestro_marca.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_material = QPushButton(
            " > MATERIALES DE URNAS"
        )
        self.button_maestro_material.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_proyecto = QPushButton(
            "PROYECTOS"
        )
        self.button_maestro_proyecto.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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
            " > ESTADOS PROYECTOS"
        )
        self.button_maestro_estado_proyecto.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_tipo_acuario = QPushButton(
            " > TIPOS DE ACUARIO"
        )
        self.button_maestro_tipo_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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
            " > CATEGORÍAS DE ACUARIO"
        )
        self.button_maestro_categoria_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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
            " > SUBCATEGORÍAS DE ACUARIO"
        )
        self.button_maestro_subcategoria_acuario.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_tipo_filtro = QPushButton(" > TIPOS DE FILTRO")
        self.button_maestro_tipo_filtro.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_urna = QPushButton("URNAS")
        self.button_maestro_urna.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_maestro_equipamiento = QPushButton("EQUIPAMIENTOS")
        self.button_maestro_equipamiento.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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
            " > CAT. EQUIPAMIENTOS"
        )
        self.button_maestro_cat_equipamiento.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                text-align: left;
                margin-bottom: 0;
                margin-left: 20;
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

        self.button_menu_maestro.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

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
        icon.addPixmap(QPixmap(":/Images/close.png"), QIcon.Mode.Normal,
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
        icon2.addPixmap(QPixmap(":/Images/maximize.png"), QIcon.Mode.Normal,
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
        icon3.addPixmap(QPixmap(":/Images/restore.png"), QIcon.Mode.Normal,
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
        icon4.addPixmap(QPixmap(":/Images/minimize.png"), QIcon.Mode.Normal,
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


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainView("M I S    1A C U A R I O S")

    # Cargar el archivo .qss
    with open("../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
