"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      22/06/2025
Comentarios:
    Módulo que contiene el formulario principal.
"""

import sys
from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QFont, QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                             QPushButton, QSizeGrip, QSizePolicy, QSpacerItem,
                             QVBoxLayout, QWidget)

import globales


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
        self.menu_layout.addWidget(self.button_modulo_acuario)
        self.menu_layout.addWidget(self.button_modulo_mantenimiento)
        self.menu_layout.addWidget(self.button_modulo_compras)
        self.menu_layout.addWidget(self.button_modulo_inventario)
        self.menu_layout.addWidget(self.button_modulo_maestro)
        self.menu_layout.addWidget(self.button_modulo_reportes)
        self.menu_layout.addWidget(self.button_modulo_configuracion)
        self.menu_layout.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Minimum,
                        QSizePolicy.Policy.Expanding)
        )
        self.menu_layout.addWidget(self.button_salir_aplicacion)

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

        self.layout_root = QVBoxLayout(self)
        self.layout_root.setContentsMargins(0, 0, 0, 0)
        self.layout_root.setSpacing(0)
        self.layout_root.addWidget(self.frame_main)

        self.layout_main.addWidget(self.frame_title_bar)
        self.layout_main.addLayout(self.layout_central)
        self.setLayout(self.layout_main)

    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout(self)  # Layout principal

        self.frame_main = QFrame()
        self.frame_main.setMouseTracking(True)
        self.frame_main.setObjectName("frame_main")
        self.frame_main.setSizePolicy(QSizePolicy.Policy.Expanding,
                                      QSizePolicy.Policy.Expanding)
        self.frame_main.setLayout(self.layout_main)  # layout_main ya existe
        self.frame_main.setStyleSheet("""
            #frame_main {
                border: 1px solid #4a4a4a;
                border-radius: 0px;
                background-color: transparent;
            }
        """)

        self.layout_central = QVBoxLayout()  # Layout central donde se coloca
        # la barra de título y el dashboard
        self.menu_layout = QVBoxLayout()  # Layout donde se alberga el menú
        # lateral
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
        ## Cerrar aplicación
        self.button_salir_aplicacion = QPushButton("SALIR")
        self.button_salir_aplicacion.setIcon(
            QIcon(str(globales.PATH_IMAGES / "cerrar-aplicacion.png"))
        )
        self.button_salir_aplicacion.setIconSize(QSize(32, 32))
        self.button_salir_aplicacion.setObjectName("button_salir_aplicacion")
        self.button_salir_aplicacion.setFlat(True)
        self.button_salir_aplicacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Módulo Maestro
        self.button_modulo_maestro = QPushButton("MAESTRO")
        self.button_modulo_maestro.setIcon(
            QIcon(str(globales.PATH_IMAGES / "modulo-maestro.png"))
        )
        self.button_modulo_maestro.setIconSize(QSize(32, 32))
        self.button_modulo_maestro.setObjectName("button_modulo_maestro")
        self.button_modulo_maestro.setFlat(True)
        self.button_modulo_maestro.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Módulo acuario
        self.button_modulo_acuario = QPushButton("ACUARIO")
        self.button_modulo_acuario.setIcon(
            QIcon(str(globales.PATH_IMAGES / "acuario.png"))
        )
        self.button_modulo_acuario.setIconSize(QSize(32, 32))
        self.button_modulo_acuario.setObjectName("button_modulo_acuario")
        self.button_modulo_acuario.setFlat(True)
        self.button_modulo_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Módulo mantenimiento
        self.button_modulo_mantenimiento = QPushButton("MANTENIMIENTO")
        self.button_modulo_mantenimiento.setIcon(
            QIcon(str(globales.PATH_IMAGES / "modulo-mantenimiento.png"))
        )
        self.button_modulo_mantenimiento.setIconSize(QSize(32, 32))
        self.button_modulo_mantenimiento.setObjectName(
            "button_modulo_mantenimiento")
        self.button_modulo_mantenimiento.setFlat(True)
        self.button_modulo_mantenimiento.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Módulo compras
        self.button_modulo_compras = QPushButton("COMPRAS")
        self.button_modulo_compras.setIcon(
            QIcon(str(globales.PATH_IMAGES / "modulo-compras.png"))
        )
        self.button_modulo_compras.setIconSize(QSize(32, 32))
        self.button_modulo_compras.setObjectName(
            "button_modulo_compras")
        self.button_modulo_compras.setFlat(True)
        self.button_modulo_compras.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Módulo inventario
        self.button_modulo_inventario = QPushButton("INVENTARIO")
        self.button_modulo_inventario.setIcon(
            QIcon(str(globales.PATH_IMAGES / "modulo-inventario.png"))
        )
        self.button_modulo_inventario.setIconSize(QSize(32, 32))
        self.button_modulo_inventario.setObjectName(
            "button_modulo_inventario")
        self.button_modulo_inventario.setFlat(True)
        self.button_modulo_inventario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Módulo reportes
        self.button_modulo_reportes = QPushButton("REPORTES")
        self.button_modulo_reportes.setIcon(
            QIcon(str(globales.PATH_IMAGES / "modulo-reportes.png"))
        )
        self.button_modulo_reportes.setIconSize(QSize(32, 32))
        self.button_modulo_reportes.setObjectName(
            "button_modulo_reportes")
        self.button_modulo_reportes.setFlat(True)
        self.button_modulo_reportes.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Módulo configuración
        self.button_modulo_configuracion = QPushButton("CONFIGURACIÓN")
        self.button_modulo_configuracion.setIcon(
            QIcon(str(globales.PATH_IMAGES / "modulo-configuracion.png"))
        )
        self.button_modulo_configuracion.setIconSize(QSize(32, 32))
        self.button_modulo_configuracion.setObjectName(
            "button_modulo_configuracion")
        self.button_modulo_configuracion.setFlat(True)
        self.button_modulo_configuracion.setCursor(
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
