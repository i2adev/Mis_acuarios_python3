"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Commentarios:
    Módulo que contiene la vista de la que derivan los dialogos.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtWidgets import QDialog, QSizeGrip, QVBoxLayout, QFrame, \
    QSizePolicy, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QApplication


class BaseDialog(QDialog):
    """ Formulario de tipo de filtro """

    def __init__(self, w_title: str):
        """ Constructor de clase """

        super().__init__()

        # SizeGrip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Configura el formulario
        self.window_title = w_title
        self.create_widgets()
        self.build_layout()
        # self.set_tab_order()
        self.init_basic_handlers()

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

        # Establece las dimensiones y la posición de la ventana
        # self.setGeometry(300, 200, 850, 600)

        # Ocultar barra de título
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Configuramos la barra del título
        self.layout_title_bar.addWidget(self.label_icon)
        self.layout_title_bar.addWidget(self.label_window_title)
        self.layout_title_bar.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Minimum)
        )
        self.layout_title_bar.addWidget(self.button_tb_minimize)
        self.layout_title_bar.addWidget(self.button_tb_restore)
        self.layout_title_bar.addWidget(self.button_tb_maximize)
        self.layout_title_bar.addWidget(self.button_tb_close)

        # Configulamos el layout del pie de formulario
        self.layout_footer.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Minimum)
        )
        self.layout_footer.addWidget(self.button_accept)
        self.layout_footer.addWidget(self.button_cancel)
        # self.layout_footer.addWidget(self.button_close)

        # Cargamos los layout en la ventana
        self.layout_main.addWidget(self.frame_title_bar)
        self.layout_main.addLayout(self.layout_form_data)
        # self.layout_main.addLayout(self.layout_data)
        # self.layout_main.addLayout(self.layout_navigation)
        self.layout_main.addLayout(self.layout_footer)

        layout_root = QVBoxLayout(self)
        layout_root.setContentsMargins(0, 0, 0, 0)
        layout_root.setSpacing(0)
        layout_root.addWidget(self.frame_main)

    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout()  # Layout principal

        self.frame_main = QFrame()
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

        self.layout_title_bar = QHBoxLayout()  # Layout barra título
        self.layout_title_bar.setContentsMargins(0, 0, 0, 0)
        self.layout_form_data = QHBoxLayout()  # Layout que contiene el frame con
                                               # el formulario de datos
        self.layout_footer = QHBoxLayout()  # Layout pie de formulario

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
        self.button_tb_maximize.hide()

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
        self.button_tb_minimize.hide()

        self.label_window_title = QLabel(self.window_title)

        ## Icono de la ventana
        self.label_icon = QLabel()
        icon5 = QPixmap(":/Images/Window_icon.png")
        self.label_icon.setPixmap(icon5)

        ## Botón Aceptar
        self.button_accept = QPushButton("&ACEPTAR")
        self.button_accept.setFlat(True)
        self.button_accept.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ## Botón Cancelar
        self.button_cancel = QPushButton("&&CANCELAR")
        self.button_cancel.setFlat(True)
        self.button_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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
        try:
            if not self.isMaximized():
                if event.buttons() == Qt.MouseButton.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint()
                              - self.drag_position)
                    self.drag_position = event.globalPosition().toPoint()
                    event.accept()

            if self.drag_position.y() <= 20:
                self.showMaximized()
        except Exception as e:
            print(f"Error en mover_ventana: {e}")


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = BaseDialog("BASE DIALOG")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())