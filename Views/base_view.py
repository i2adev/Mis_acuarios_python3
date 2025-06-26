"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/06/2025
Commentarios:
    Módulo que contiene la clase base de los formularios
"""

# Importaciones
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout,
                             QSpacerItem, QComboBox, QSizePolicy, QFrame,
                             QTableView, QSizeGrip, QAbstractItemView)
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtCore import Qt

import Resources.image_rc

class BaseView(QWidget):
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

        # # Consfiguramos el layout de inserción de datos
        # # Primera línea
        # # ID
        # self.layout_id.addWidget(self.label_id)
        # self.layout_id.addWidget(self.edit_id)
        #
        # # TIPO DE FILTRO
        # self.layout_tipo_filtro.addWidget(self.label_tipo_filtro)
        # self.layout_tipo_filtro.addWidget(self.edit_tipo_filtro)
        #
        # # Segunda línea
        # # OBSERVACIONES
        # self.layout_observaciones.addWidget(self.label_observaciones)
        # self.layout_observaciones.addWidget(self.text_observaciones)

        # Datatable y crud
        self.layout_table.addWidget(self.data_table)

        self.layout_crud.addWidget(self.button_insert)
        self.layout_crud.addWidget(self.button_update)
        self.layout_crud.addWidget(self.button_load)
        self.layout_crud.addWidget(self.button_delete)
        self.layout_crud.addWidget(self.button_clean)
        self.layout_crud.addWidget(self.button_search)
        self.layout_crud.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding)
        )

        self.layout_data.addWidget(self.frame_table)
        self.layout_data.addLayout(self.layout_crud)

        # # Montamos los layouts
        # # Layput inserción de datos
        # self.layout_first_line.addLayout(self.layout_id)
        # self.layout_first_line.addLayout(self.layout_tipo_filtro)
        # self.layout_second_line.addLayout(self.layout_observaciones)

        # self.layout_form_data.addLayout(self.layout_first_line)
        # self.layout_form_data.addLayout(self.layout_second_line)

        # Configuramos el layout de navegación
        self.layout_navigation.addWidget(self.button_first)
        self.layout_navigation.addWidget(self.button_prev)
        self.layout_navigation.addWidget(self.label_page)
        self.layout_navigation.addWidget(self.combo_select_page)
        self.layout_navigation.addWidget(self.label_de)
        self.layout_navigation.addWidget(self.label_total_pages)
        self.layout_navigation.addWidget(self.button_next)
        self.layout_navigation.addWidget(self.button_last)
        self.layout_navigation.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum)
        )

        # Configulamos el layout del pie de formulario
        # self.layout_footer.addItem(self.spacer_foot)
        self.layout_footer.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum)
        )
        self.layout_footer.addWidget(self.button_accept)
        self.layout_footer.addWidget(self.button_cancel)
        self.layout_footer.addWidget(self.button_close)

        # Cargamos los layout en la ventana
        self.layout_main.addWidget(self.frame_title_bar)
        self.layout_main.addLayout(self.layout_form_data)
        self.layout_main.addLayout(self.layout_data)
        self.layout_main.addLayout(self.layout_navigation)
        self.layout_main.addLayout(self.layout_footer)
        self.setLayout(self.layout_main)

    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout() # Layout principal
        self.layout_title_bar = QHBoxLayout() # Layout barra título
        self.layout_title_bar.setContentsMargins(0, 0, 0, 0)
        self.layout_table = QHBoxLayout() # Contiene la tabla
        self.layout_data = QHBoxLayout() # Layout de datatable y crud
        self.frame_table = QFrame() # Frame que contiene el datatable
        self.frame_table.setLayout(self.layout_table)
        # self.frame_table.setMinimumHeight(210)
        self.layout_crud = QVBoxLayout()  # Layout donde se colocan los botones 
                                          # del CRUD
        self.layout_form_data = QVBoxLayout() # Layout del frame que contiene
                                              # los datos del formulario
        #self.frame_form_data = QFrame() # Frame de la inserción de datos
        # self.frame_form_data.setSizePolicy(QSizePolicy.Policy.Expanding,
        #                               QSizePolicy.Policy.Fixed)
        # self.frame_form_data.setLayout(self.layout_form_data)
        
        # self.layout_first_line = QHBoxLayout() # Primera línea del formulario
        # self.layout_second_line = QHBoxLayout() # Segunda línea del formulario
        # self.layout_id = QVBoxLayout() # El campo ID
        # self.layout_tipo_filtro = QVBoxLayout() # El campo TIPO DE FILTRO
        # self.layout_observaciones = QVBoxLayout() # El campo OBSERVACIONES
        
        self.layout_navigation = QHBoxLayout()  # Layout de navegación de
                                                # páginas
        self.layout_footer = QHBoxLayout() # Layout pie de formulario

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

        # # Controles de inserción de datos
        # ## Primera línea
        # ### Label ID
        # self.label_id = QLabel("ID")
        # self.label_id.setMinimumWidth(50)
        # self.label_id.setMaximumWidth(50)
        #
        # ### Texbox ID
        # self.edit_id = QLineEdit()
        # self.edit_id.setObjectName("edit_id")
        # self.edit_id.setMinimumWidth(50)
        # self.edit_id.setMaximumWidth(50)
        # self.edit_id.setEnabled(False)

        # ### Label TIPO DE FILTRO
        # self.label_tipo_filtro = QLabel("TIPO DE FILTRO")
        #
        # ### Textbox TIPO DE FILTRO
        # self.edit_tipo_filtro = QLineEdit()
        # self.edit_tipo_filtro.setObjectName("edit_tipo_filtro")

        # ## Segunda línea
        # ### Label OBSERVACIONES
        # self.label_observaciones = QLabel("OBSERVACIONES")
        #
        # ### Text OBSERVACIONES
        # self.text_observaciones = QTextEdit()
        # self.text_observaciones.setObjectName("text_observaciones")
        # self.text_observaciones.setMinimumHeight(80)
        # self.text_observaciones.setMaximumHeight(80)

        ## Controles de tabla y CRUD
        ### Tabla
        self.data_table = QTableView()
        self.data_table.setMinimumWidth(600)
        self.data_table.verticalHeader().setVisible(False)
        self.data_table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.data_table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection)
        self.data_table.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu)

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
        # self.spacer_crud = QSpacerItem(40,10)

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
        self.label_page.setMinimumWidth(60)
        self.label_page.setMaximumWidth(60)

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
        self.label_total_pages.setMinimumWidth(30)
        self.label_total_pages.setMaximumWidth(30)

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

    ventana = BaseView("TIPOS DE FILTRO")

    # Cargar el archivo .qss
    with open("../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())