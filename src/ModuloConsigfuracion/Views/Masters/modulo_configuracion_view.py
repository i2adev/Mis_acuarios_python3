"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/11/2026
Comentarios:
    Módulo que contiene el formulario del módulo configuración.
"""

import sys
from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QFont, QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                             QPushButton, QSizeGrip, QSizePolicy, QSpacerItem,
                             QVBoxLayout, QWidget)

import globales
from CustomControls.boton_lateral import BotonLateral
from ModuloConsigfuracion.Views.Forms.cuenta_form import CuentaForm
from ModuloConsigfuracion.Views.Forms.unidades_form import UnidadesForm


class ModuloConfiguracionView(QWidget):
    """ Formulario del módulo de proyecto """

    def __init__(self, w_title: str):
        """ Constructor de clase """

        super().__init__()

        # Dimensiones del cuadro del formulario
        self.setFixedSize(800, 800)

        # Inicializamos las variables
        self.section_list = list()
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

        # Ocultar barra de título
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Configura el menú lateral
        self.menu_layout.addWidget(self.button_cuenta)
        self.menu_layout.addWidget(self.button_unidades)
        self.menu_layout.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Minimum,
                        QSizePolicy.Policy.Expanding)
        )

        # Configura el layout de los controles
        self.layout_controls.addWidget(self.frame_cuenta)
        self.layout_controls.addWidget(self.frame_unidades)
        self.layout_controls.addLayout(self.layout_pie)

        # Configuramos la barra del título
        self.layout_title_bar.addWidget(self.label_icon)
        self.layout_title_bar.addWidget(self.label_window_title)
        self.layout_title_bar.addItem(self.spacer_tb)
        self.layout_title_bar.addWidget(self.button_tb_minimize)
        self.layout_title_bar.addWidget(self.button_tb_restore)
        self.layout_title_bar.addWidget(self.button_tb_maximize)
        self.layout_title_bar.addWidget(self.button_tb_close)

        # Configura el pie del formulario
        self.layout_pie.addWidget(self.button_accept)
        self.layout_pie.addWidget(self.button_cancel)

        # Cargamos los layout en la ventana
        self.layout_central.addWidget(self.frame_menu)
        self.layout_central.addLayout(self.layout_controls)

        self.layout_root = QVBoxLayout(self)
        self.layout_root.setContentsMargins(0, 0, 0, 0)
        self.layout_root.setSpacing(0)
        self.layout_root.addWidget(self.frame_main)

        self.layout_main.addWidget(self.frame_title_bar)
        self.layout_main.addLayout(self.layout_central)
        self.setLayout(self.layout_root)

    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout(self)  # Layout principal

        self.layout_pie = QHBoxLayout()
        self.layout_pie.setAlignment(Qt.AlignmentFlag.AlignRight)

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

        self.frame_cuenta = CuentaForm()
        self.frame_unidades = UnidadesForm()

        self.layout_central = QHBoxLayout()  # Layout central donde se coloca
        # la barra de título y los controles.
        self.menu_layout = QVBoxLayout()  # Layout donde se alberga el menú
        # lateral
        self.menu_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
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
        self.frame_menu.setLayout(self.menu_layout)

        self.layout_title_bar = QHBoxLayout()  # Layout barra título
        self.layout_title_bar.setContentsMargins(0, 0, 0, 0)

        self.layout_controls = QVBoxLayout()  # Layout donde se colocan los
        # controles
        self.layout_controls.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Cuenta
        self.button_cuenta = BotonLateral(
            control_name="buttton_cuenta",
            label="CUENTA",
            image_rte=str(globales.PATH_IMAGES / "usuario.png")
        )
        self.section_list.append([self.button_cuenta, self.frame_cuenta])

        # Unidades
        self.button_unidades = BotonLateral(
            control_name="buttton_unidades",
            label="UNIDADES",
            image_rte=str(globales.PATH_IMAGES / "unidad-medida.png")
        )
        self.section_list.append([self.button_unidades, self.frame_unidades])

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

        ## Botón Aceptar
        self.button_accept = QPushButton("&ACEPTAR")
        self.button_accept.setFlat(True)
        self.button_accept.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))

        ## Botón Cancelar
        self.button_cancel = QPushButton("&&CANCELAR")
        self.button_cancel.setFlat(True)
        self.button_cancel.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))

        ## Icono de la ventana
        self.label_icon = QLabel()
        icon5 = QPixmap(str(Path(globales.PATH_IMAGES) / "Window_icon.png"))
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

    ventana = ModuloConfiguracionView("MODULO CONFIGURACIÓN")

    # Cargar el archivo .qss
    with open("../../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
