"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contien la vista de la entidad TIPO DE FILTRO.
"""

# Importaciones
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout,
                             QSpacerItem, QComboBox, QSizePolicy, QFrame,
                             QTableView, QSizeGrip)
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtCore import Qt

import Resources.image_rc

class TipoFiltroView(QWidget):
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
        self.set_tab_order()
        self.init_basic_handlers()

        # Establece el foco inicial
        self.edit_tipo_filtro.setFocus()


    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las politicas de focus
        self.edit_tipo_filtro.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.text_observaciones.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.edit_tipo_filtro, self.text_observaciones)

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

        # Definimos los layouts
        # layout_main = QVBoxLayout() # Layout principal
        # self.layout_title_bar = QHBoxLayout() # Layout barra título
        # self.layout_title_bar.setContentsMargins(0, 0, 0, 0)

        layout_form_data = QVBoxLayout()
        frame_form_data = QFrame() # Frame de la inserción de datos
        frame_form_data.setSizePolicy(QSizePolicy.Policy.Expanding,
                                      QSizePolicy.Policy.Fixed)
        frame_form_data.setLayout(layout_form_data)

        layout_first_line = QHBoxLayout() # Primera linea del formulario
        layout_second_line = QHBoxLayout() # Segunda línea del formularfio
        layout_id = QVBoxLayout() # El campo ID
        layout_tipo_filtro = QVBoxLayout() # El campo TIPO DE FILTRO
        layout_observaciones = QVBoxLayout() # El campo OBSERVACIONES

        layout_table = QHBoxLayout() # Contiene la tabla
        layout_data = QHBoxLayout() # Layout de datatable y crud
        frame_table = QFrame() # Frame que contiene el datatable
        frame_table.setLayout(layout_table)
        # Layout donde se colocan los botones del crud
        layout_crud = QVBoxLayout()
        # Layout de la navegación entre páginas
        layout_navigation = QHBoxLayout()
        layout_footer = QHBoxLayout() # Layout pie de formulario

        # Configuramos la barra del titulo
        self.layout_title_bar.addWidget(self.label_icon)
        self.layout_title_bar.addWidget(self.label_window_title)
        self.layout_title_bar.addItem(self.spacer_tb)
        self.layout_title_bar.addWidget(self.button_tb_minimize)
        self.layout_title_bar.addWidget(self.button_tb_restore)
        self.layout_title_bar.addWidget(self.button_tb_maximize)
        self.layout_title_bar.addWidget(self.button_tb_close)

        # Consfiguramos el layout de inserción de datos
        # Primera línea
        # ID
        layout_id.addWidget(self.label_id)
        layout_id.addWidget(self.edit_id)

        # TIPO DE FILTRO
        layout_tipo_filtro.addWidget(self.label_tipo_filtro)
        layout_tipo_filtro.addWidget(self.edit_tipo_filtro)

        # Segunda línea
        # OBSERVACIONES
        layout_observaciones.addWidget(self.label_observaciones)
        layout_observaciones.addWidget(self.text_observaciones)

        # Datatable y crud
        layout_table.addWidget(self.data_table)

        layout_crud.addWidget(self.button_insert)
        layout_crud.addWidget(self.button_update)
        layout_crud.addWidget(self.button_load)
        layout_crud.addWidget(self.button_delete)
        layout_crud.addWidget(self.button_clean)
        layout_crud.addWidget(self.button_search)

        layout_data.addWidget(frame_table)
        layout_data.addLayout(layout_crud)

        # Montamos los layouts
        # Layput inserción de datos
        layout_first_line.addLayout(layout_id)
        layout_first_line.addLayout(layout_tipo_filtro)
        layout_second_line.addLayout(layout_observaciones)

        layout_form_data.addLayout(layout_first_line)
        layout_form_data.addLayout(layout_second_line)

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
        layout_footer.addItem(self.spacer_foot)
        layout_footer.addWidget(self.button_accept)
        layout_footer.addWidget(self.button_cancel)
        layout_footer.addWidget(self.button_close)

        # Cargamos los layout en la ventana
        self.layout_main.addWidget(self.frame_title_bar)
        self.layout_main.addWidget(frame_form_data)
        self.layout_main.addLayout(layout_data)
        self.layout_main.addLayout(layout_navigation)
        self.layout_main.addLayout(layout_footer)
        self.setLayout(self.layout_main)

    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout() # Layout principal
        self.layout_title_bar = QHBoxLayout() # Layout barra título
        self.layout_title_bar.setContentsMargins(0, 0, 0, 0)

        # Controles de la barra de titulo
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

        ### Espaciador
        self.spacer_tb = QSpacerItem(400, 10, QSizePolicy.Policy.Expanding,
                                     QSizePolicy.Policy.Minimum)

        self.label_window_title = QLabel(self.window_title)

        ## Icono de la ventana
        self.label_icon = QLabel()
        icon5 = QPixmap(":/Images/Window_icon.png")
        self.label_icon.setPixmap(icon5)

        # Controles de inserción de datos
        ## Primera linea
        ### Label ID
        self.label_id = QLabel("ID")
        self.label_id.setMinimumWidth(50)
        self.label_id.setMaximumWidth(50)

        ### Texbox ID
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setMinimumWidth(50)
        self.edit_id.setMaximumWidth(50)
        self.edit_id.setEnabled(False)

        ### Label TIPO DE FILTRO
        self.label_tipo_filtro = QLabel("TIPO DE FILTRO")

        ### Textbox TIPO DE FILTRO
        self.edit_tipo_filtro = QLineEdit()
        self.edit_tipo_filtro.setObjectName("edit_tipo_filtro")

        ## Segunda línea
        ### Label OBSERVACIONES
        self.label_observaciones = QLabel("OBSERVACIONES")

        ### Text OBSERVACIONES
        self.text_observaciones = QTextEdit()
        self.text_observaciones.setObjectName("text_observaciones")
        self.text_observaciones.setMinimumHeight(80)
        self.text_observaciones.setMaximumHeight(80)

        ## Controles de tabla y CRUD
        ### Tabla
        self.data_table = QTableView()

        ### Botón INSERT
        self.button_insert = QPushButton()
        self.button_insert.setText("&INSERTAR")

        ### Botón UPDATE
        self.button_update = QPushButton()
        self.button_update.setText("AC&TUALIZAR")

        ### Botón DELETE
        self.button_delete = QPushButton()
        self.button_delete.setText("&ELIMINAR")

        ### Botón LOAD
        self.button_load = QPushButton()
        self.button_load.setText("CAR&GAR")

        ### Botón CLEAN
        self.button_clean = QPushButton()
        self.button_clean.setText("LIM&PIAR")

        ### Botón SEARCH
        self.button_search = QPushButton()
        self.button_search.setText("&BUSCAR")

        ### Espaciador
        self.spacer_crud = QSpacerItem(40,10)

        ## Controles de navegación
        ### Botón última página
        self.button_last = QPushButton()
        self.button_last.setText(">>")
        self.button_last.setMinimumWidth(30)
        self.button_last.setMaximumWidth(30)
        self.button_last.setFlat(True)
        self.button_last.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ### Botón siguiente página
        self.button_next = QPushButton()
        self.button_next.setText(">")
        self.button_next.setMinimumWidth(30)
        self.button_next.setMaximumWidth(30)
        self.button_next.setFlat(True)
        self.button_next.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ### Botón página previa
        self.button_prev = QPushButton()
        self.button_prev.setText("<")
        self.button_prev.setMinimumWidth(30)
        self.button_prev.setMaximumWidth(30)
        self.button_prev.setFlat(True)
        self.button_prev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ### Botón página inicial
        self.button_first = QPushButton()
        self.button_first.setText("<<")
        self.button_first.setMinimumWidth(30)
        self.button_first.setMaximumWidth(30)
        self.button_first.setFlat(True)
        self.button_first.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ### Etiqueta página
        self.label_page = QLabel()
        self.label_page.setText("PÁGINA")
        self.label_page.setMinimumWidth(50)
        self.label_page.setMaximumWidth(50)

        ### Combo selector de página
        self.combo_select_page = QComboBox()
        self.combo_select_page.setMinimumWidth(50)
        self.combo_select_page.setMaximumWidth(50)

        ### Label DE
        self.label_de = QLabel()
        self.label_de.setText("DE")
        self.label_de.setMinimumWidth(30)
        self.label_de.setMaximumWidth(30)

        ### Label TOTAL PAGES
        self.label_total_pages = QLabel()
        self.label_total_pages.setMinimumWidth(40)
        self.label_total_pages.setMaximumWidth(40)

        ### Espaciador
        self.spacer_navigation = QSpacerItem(400, 10)

        # Controles del pie de formulario
        ## Botón aceptar
        self.button_accept = QPushButton()
        self.button_accept.setText("&ACEPTAR")
        self.button_accept.setFlat(True)
        self.button_accept.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ## Botón cancelar
        self.button_cancel = QPushButton()
        self.button_cancel.setText("&CANCELAR")
        self.button_cancel.setFlat(True)
        self.button_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ## Botón Cerrar
        self.button_close = QPushButton()
        self.button_close.setText("C&ERRAR")
        self.button_close.setFlat(True)
        self.button_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ## Espaciador
        self.spacer_foot = QSpacerItem(400, 10)

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

    ventana = TipoFiltroView("TIPOS DE FILTRO")

    # Cargar el archivo .qss
    with open("../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())