"""
Formulario de tipo de filtro
"""

# Importaciones
import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout,
                             QSpacerItem, QComboBox, QSizePolicy)
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtCore import Qt

import Resources.image_rc

# TODO: Hacer esta vista como base de las otras vistas
#       1.  Gestionar los eventos del formulario, tales como, mover el formulario, los botones de la barra de titulo,...

class BaseView(QWidget):
    """ Formulario de tipo de filtro """

    def __init__(self, w_title: str):
        """ Constructor de clase """
        super().__init__()
        self.window_title = w_title
        self.create_widgets()
        self.build_layout()
        self.set_properties()

    def build_layout(self):
        """ Construye el layout de la ventana """

        # Establece las dimensiones y la posición de la ventana
        # self.setGeometry(300, 200, 850, 600)

        # Ocultar barra de título
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Definimos los layouts
        layout_main = QVBoxLayout() # Layout principal
        layout_title_bar = QHBoxLayout() # Layout barra titulo
        layout_title_bar.setContentsMargins(0, 0, 0, 20) # Aumenta el espacio inferior a 20pix
        layout_data = QVBoxLayout() # Layout de la inserción de datos
        layout_data_table = QHBoxLayout() # Layout de datatable y crud
        layout_navigation = QHBoxLayout() # Layout de la navegación entre páginas
        layout_foot = QHBoxLayout() # Layout pie de formulario

        # Configuramos la barra del titulo
        layout_title_bar.addWidget(self.label_icon)
        layout_title_bar.addWidget(self.label_window_title)
        layout_title_bar.addItem(self.spacer_tb)
        layout_title_bar.addWidget(self.button_tb_minimize)
        layout_title_bar.addWidget(self.button_tb_restore)
        layout_title_bar.addWidget(self.button_tb_maximize)
        layout_title_bar.addWidget(self.button_tb_close)


        # Configuramos el layout de navegación
        layout_navigation.addWidget(self.button_first)
        layout_navigation.addWidget(self.label_page)
        layout_navigation.addWidget(self.button_prev)
        layout_navigation.addWidget(self.combo_select_page)
        layout_navigation.addWidget(self.label_de)
        layout_navigation.addWidget(self.label_total_pages)
        layout_navigation.addWidget(self.button_next)
        layout_navigation.addWidget(self.button_last)
        layout_navigation.addItem(self.spacer_navigation)

        # Configulamos el layout del pie de formulario
        layout_foot.addItem(self.spacer_foot)
        layout_foot.addWidget(self.button_accept)
        layout_foot.addWidget(self.button_cancel)
        layout_foot.addWidget(self.button_close)

        # Cargamos los layout en la ventana
        layout_main.addLayout(layout_title_bar)
        layout_main.addLayout(layout_data)
        layout_main.addLayout(layout_data_table)
        layout_main.addLayout(layout_navigation)
        layout_main.addLayout(layout_foot)
        self.setLayout(layout_main)

    def set_properties(self):
        """ Configura las propiedades de los widgets """

        # Controles de la barra de titulo
        # Propiedades del botón cerrar
        icon = QIcon()
        icon.addPixmap(QPixmap(":/Images/close.png"), QIcon.Mode.Normal, QIcon.State.On)
        self.button_tb_close.setIcon(icon)
        self.button_tb_close.setFlat(True)
        self.button_tb_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del botón maximizar
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/Images/maximize.png"), QIcon.Mode.Normal, QIcon.State.On)
        self.button_tb_maximize.setIcon(icon2)
        self.button_tb_maximize.setFlat(True)
        self.button_tb_maximize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Pripiedades del botón restaurar
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/Images/restore.png"), QIcon.Mode.Normal, QIcon.State.On)
        self.button_tb_restore.setIcon(icon3)
        self.button_tb_restore.setFlat(True)
        self.button_tb_restore.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del botón minimizar
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/Images/minimize.png"), QIcon.Mode.Normal, QIcon.State.On)
        self.button_tb_minimize.setIcon(icon4)
        self.button_tb_minimize.setFlat(True)
        self.button_tb_minimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del título de la ventana
        # self.label_window_title.setText(title)

        # Propiedades del icono de la ventana
        icon5 = QPixmap(":/Images/Window_icon.png")
        self.label_icon.setPixmap(icon5)

        # Controles del pie de formulario
        # Propiedades del botón aceptar
        self.button_accept.setText("&ACEPTAR")
        self.button_accept.setFlat(True)
        self.button_accept.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del botón cancelar
        self.button_cancel.setText("&CANCELAR")
        self.button_cancel.setFlat(True)
        self.button_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del botón cerrar
        self.button_close.setText("C&ERRAR")
        self.button_close.setFlat(True)
        self.button_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Controles de la barra de navegación
        # Pripiedades del botón página inicial
        self.button_first.setText("<<")
        self.button_first.setMinimumWidth(30)
        self.button_first.setMaximumWidth(30)
        self.button_first.setFlat(True)
        self.button_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del botón página previa
        self.button_prev.setText("<")
        self.button_prev.setMinimumWidth(30)
        self.button_prev.setMaximumWidth(30)
        self.button_prev.setFlat(True)
        self.button_prev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del botón siguiente página
        self.button_next.setText(">")
        self.button_next.setMinimumWidth(30)
        self.button_next.setMaximumWidth(30)
        self.button_next.setFlat(True)
        self.button_next.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades del botón última página
        self.button_last.setText(">>")
        self.button_last.setMinimumWidth(30)
        self.button_last.setMaximumWidth(30)
        self.button_last.setFlat(True)
        self.button_last.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Propiedades de etiqueta página
        self.label_page.setText("PÁGINA")
        self.label_page.setMinimumWidth(50)
        self.label_page.setMaximumWidth(50)

        # Propiedades del combobox de selección de página
        self.combo_select_page.setMaximumWidth(50)
        self.combo_select_page.setMaximumWidth(50)

        # Propiedades de la eqtiqueta DE
        self.label_de.setText("DE")
        self.label_de.setMinimumWidth(30)
        self.label_de.setMaximumWidth(30)

        # Propiedades de la etiqueta páginas totales
        self.label_total_pages.setMinimumWidth(40)
        self.label_total_pages.setMaximumWidth(40)

    def create_widgets(self):
        """ Crea los elementos del formulario"""

        # Controles de la barra de titulo
        self.button_tb_close = QPushButton()
        self.button_tb_maximize = QPushButton()
        self.button_tb_restore = QPushButton()
        self.button_tb_minimize = QPushButton()

        self.spacer_tb = QSpacerItem(400, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.label_window_title = QLabel(self.window_title)
        self.label_icon = QLabel()

        # Controles de navegación
        self.button_last = QPushButton()
        self.button_next = QPushButton()
        self.button_prev = QPushButton()
        self.button_first = QPushButton()

        # Controles del pie de formulario
        self.button_accept = QPushButton()
        self.button_cancel = QPushButton()
        self.button_close = QPushButton()
        self.spacer_foot = QSpacerItem(400, 10)

        self.label_page = QLabel()
        self.combo_select_page = QComboBox()
        self.label_de = QLabel()
        self.label_total_pages = QLabel()

        self.spacer_navigation = QSpacerItem(400, 10)

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Tipo_filtro_view("TIPOS DE FILTRO")

    # Cargar el archivo .qss
    with open("../Resources/Styles/main_style.qss", "r", encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())