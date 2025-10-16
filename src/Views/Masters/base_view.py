"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene la vista base de la que derivan los formularios.
"""


import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout,
                             QSpacerItem, QComboBox, QSizePolicy, QFrame,
                             QTableView, QAbstractItemView)
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtCore import Qt, QRect

import Resources.image_rc

class BaseView(QWidget):
    """ Formulario maestro base """

    def __init__(self, w_title: str):
        """ Constructor de clase """

        super().__init__()

        # Variables de redimensionamiento y movimiento de la ventana
        self.setMouseTracking(True)
        self._resize_margin = 6
        self._resizing = False
        self._resize_direction = None
        self._start_pos = None
        self._start_geom = None

        # Configura el formulario
        self.window_title = w_title
        self.create_widgets()
        self.build_layout()

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

        # Datatable y crud
        self.layout_crud.addWidget(self.button_insert)
        self.layout_crud.addWidget(self.button_update)
        self.layout_crud.addWidget(self.button_load)
        self.layout_crud.addWidget(self.button_delete)
        self.layout_crud.addWidget(self.button_clean)
        # self.layout_crud.addWidget(self.button_search)
        self.layout_crud.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding)
        )

        self.layout_table.addWidget(self.data_table)
        self.layout_data.addWidget(self.frame_table)
        self.layout_data.addLayout(self.layout_crud)

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
        self.layout_footer.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum)
        )
        self.layout_footer.addWidget(self.button_close)

        # Configuramos el layout de la barra de estado
        self.layout_status_bar.addWidget(self.button_filter)
        self.layout_status_bar.addWidget(self.label_status)
        self.layout_status_bar.addSpacing(50)
        self.layout_status_bar.addWidget(self.edit_patron)
        self.layout_status_bar.addWidget(self.button_search)

        # Cargamos los layout en la ventana
        self.layout_main.addWidget(self.frame_title_bar)
        self.layout_main.addLayout(self.layout_form_data)
        self.layout_main.addLayout(self.layout_data)
        self.layout_main.addLayout(self.layout_navigation)
        self.layout_main.addLayout(self.layout_footer)
        self.layout_main.addLayout(self.layout_status_bar)

        layout_root = QVBoxLayout(self)
        layout_root.setContentsMargins(0, 0, 0, 0)
        layout_root.setSpacing(0)
        layout_root.addWidget(self.frame_main)

    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout() # Layout principal

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

        self.layout_title_bar = QHBoxLayout() # Layout barra título
        self.layout_title_bar.setContentsMargins(0, 0, 0, 0)
        self.layout_table = QHBoxLayout() # Layout del frame_table que contiene
                                          # la tabla
        self.layout_data = QHBoxLayout() # Layout de datatable y crud
        self.frame_table = QFrame() # Frame que contiene el datatable
        self.frame_table.setLayout(self.layout_table)
        self.frame_table.setMinimumHeight(210)
        self.layout_crud = QVBoxLayout()  # Layout donde se colocan los botones 
                                          # del CRUD
        self.layout_form_data = QHBoxLayout() # Layout que contiene el frame con
                                              # el formulario de datos
        self.layout_navigation = QHBoxLayout()  # Layout de navegación de
                                                # páginas
        self.layout_status_bar = QHBoxLayout()  # Barra de estado inferior
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
        self.button_insert.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ### Botón UPDATE
        self.button_update = QPushButton()
        self.button_update.setText("AC&TUALIZAR")
        self.button_update.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ### Botón DELETE
        self.button_delete = QPushButton()
        self.button_delete.setText("&ELIMINAR")
        self.button_delete.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ### Botón LOAD
        self.button_load = QPushButton()
        self.button_load.setText("CAR&GAR")
        self.button_load.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        ### Botón CLEAN
        self.button_clean = QPushButton()
        self.button_clean.setText("LIM&PIAR")
        self.button_clean.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

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
        self.combo_select_page.setObjectName("combo_select_page")
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

        ## Barra de estado
        ### Boton de filtro
        icon_filter = QIcon()
        icon_filter.addPixmap(QPixmap(":/Images/filter.png"), QIcon.Mode.Normal,
                       QIcon.State.On)
        self.button_filter = QPushButton()
        self.button_filter.setObjectName("button_filter")
        self.button_filter.setIcon(icon_filter)
        self.button_filter.setFixedSize(25,25)
        self.button_filter.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button_filter.setStyleSheet(
            """
            border: none;
            background-color: transparent;
            """
        )

        ### Label de estado
        self.label_status = QLabel("Sin filtrar")
        self.label_status.setObjectName("label_status")
        self.label_status.setStyleSheet(
            """
                background-color: transparent;
                color: white;
                font-family: "Roboto";
                font-size: 12pt;
                font-weight: normal;
            """
        )

        ### Patrón de busqueda
        self.edit_patron = QLineEdit()
        self.edit_patron.setObjectName("edit_patron")
        self.edit_patron.setFixedWidth(300)

        ### Botón de buscar
        icon_search = QIcon()
        icon_search.addPixmap(QPixmap(":/Images/search.png"), QIcon.Mode.Normal,
                       QIcon.State.On)
        self.button_search = QPushButton()
        self.button_search.setObjectName("button_search")
        self.button_search.setIcon(icon_search)
        self.button_search.setFixedSize(25, 25)
        self.button_search.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button_search.setStyleSheet(
            """
            border: none;
            background-color: transparent;
            """
        )

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

    """
    El comportamiento del redimensionado de la ventana
    """
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._resize_direction = self._detect_resize_region(event.pos())
            if self._resize_direction:
                self._resizing = True
                self._start_pos = event.globalPosition().toPoint()
                self._start_geom = self.geometry()
            else:
                self._dragging = True
                self.drag_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self._resizing and self._resize_direction:
            self._perform_resize(event.globalPosition().toPoint())
        else:
            direction = self._detect_resize_region(event.pos())
            self._update_cursor(direction)

    def mouseReleaseEvent(self, event):
        self._resizing = False
        self._resize_direction = None

    def leaveEvent(self, event):
        self.unsetCursor()

    def _detect_resize_region(self, pos):
        rect = self.rect()
        x, y, w, h = pos.x(), pos.y(), rect.width(), rect.height()
        margin = self._resize_margin

        vertical = None
        horizontal = None
        if y < margin:
            vertical = 'top'
        elif y > h - margin:
            vertical = 'bottom'
        if x < margin:
            horizontal = 'left'
        elif x > w - margin:
            horizontal = 'right'

        if vertical and horizontal:
            return f"{vertical}-{horizontal}"
        elif vertical:
            return vertical
        elif horizontal:
            return horizontal
        else:
            return None

    def _update_cursor(self, direction):
        cursors = {
            'left': Qt.CursorShape.SizeHorCursor,
            'right': Qt.CursorShape.SizeHorCursor,
            'top': Qt.CursorShape.SizeVerCursor,
            'bottom': Qt.CursorShape.SizeVerCursor,
            'top-left': Qt.CursorShape.SizeFDiagCursor,
            'bottom-right': Qt.CursorShape.SizeFDiagCursor,
            'top-right': Qt.CursorShape.SizeBDiagCursor,
            'bottom-left': Qt.CursorShape.SizeBDiagCursor,
        }
        self.setCursor(cursors.get(direction, Qt.CursorShape.ArrowCursor))

    def _perform_resize(self, current_pos):
        dx = current_pos.x() - self._start_pos.x()
        dy = current_pos.y() - self._start_pos.y()
        geom = self._start_geom
        new_rect = QRect(geom)

        if 'left' in self._resize_direction:
            new_rect.setLeft(geom.left() + dx)
        if 'right' in self._resize_direction:
            new_rect.setRight(geom.right() + dx)
        if 'top' in self._resize_direction:
            new_rect.setTop(geom.top() + dy)
        if 'bottom' in self._resize_direction:
            new_rect.setBottom(geom.bottom() + dy)

        min_width, min_height = self.minimumWidth(), self.minimumHeight()
        if new_rect.width() < min_width:
            new_rect.setWidth(min_width)
        if new_rect.height() < min_height:
            new_rect.setHeight(min_height)

        self.setGeometry(new_rect)

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = BaseView("BASE VIEW")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())