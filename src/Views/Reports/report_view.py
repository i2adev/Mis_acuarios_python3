# """
# Autor:      Inigo Iturriagaetxebarria
# Fecha:      13/01/2026
# Comentarios:
#     Módulo que contiene la vista para mostrar los reportes sin parámetros.
# """
#
# import sys
#
# from PyQt6.QtCore import Qt, QRect
# from PyQt6.QtGui import QIcon, QPixmap, QCursor
# from PyQt6.QtPdf import QPdfDocument
# from PyQt6.QtPdfWidgets import QPdfView
# from PyQt6.QtWidgets import (QApplication, QGroupBox, QWidget, QLabel,
#                              QPushButton,
#                              QHBoxLayout, QVBoxLayout, QSpacerItem,
#                              QSizePolicy, QFrame)
#
#
# class ReportView(QWidget):
#     """ Formulario principal de los reportes. """
#
#     def __init__(self, w_title: str):
#         """ Constructor de clase """
#
#         super().__init__()
#
#         # Variables de redimensionamiento y movimiento de la ventana
#         self.setMouseTracking(True)
#         self._resize_margin = 6
#         self._resizing = False
#         self._resize_direction = None
#         self._start_pos = None
#         self._start_geom = None
#
#         # Configura el formulario
#         self.window_title = w_title
#         self.create_widgets()
#         self.build_layout()
#
#         self.init_basic_handlers()
#
#     def init_basic_handlers(self):
#         """ Inicializamos los eventos de la ventana """
#
#         # mover ventana
#         self.frame_title_bar.mouseMoveEvent = self.mover_ventana
#
#         # Botones de la barra de título
#         self.button_tb_close.clicked.connect(lambda: self.close())
#         self.button_tb_maximize.clicked.connect(self.control_bt_maximizar)
#         self.button_tb_restore.clicked.connect(self.control_bt_normal)
#         self.button_tb_minimize.clicked.connect(self.control_bt_minimizar)
#
#         # Botones
#         self.button_close.clicked.connect(lambda: self.close())
#
#     def create_widgets(self):
#         """ Crea los elementos del formulario"""
#         self.layout_main = QVBoxLayout()  # Layout principal
#
#         self.frame_main = QFrame()
#         self.frame_main.setMouseTracking(True)
#         self.frame_main.setObjectName("frame_main")
#         self.frame_main.setSizePolicy(QSizePolicy.Policy.Expanding,
#                                       QSizePolicy.Policy.Expanding)
#         self.frame_main.setLayout(self.layout_main)  # layout_main ya existe
#         self.frame_main.setStyleSheet("""
#             #frame_main {
#                 border: 1px solid #4a4a4a;
#                 border-radius: 0px;
#                 background-color: transparent;
#             }
#         """)
#
#         # Barra de título
#         self.layout_title_bar = QHBoxLayout()  # Layout barra título
#         self.layout_title_bar.setContentsMargins(0, 0, 0, 0)
#
#         # Layout de controles
#         self.layout_controls = QHBoxLayout()
#         self.layout_controls.setContentsMargins(5, 5, 5, 5)
#         self.layout_controls.setSpacing(5)
#
#         # Grupo de listados
#         # self.layout_lists = QVBoxLayout()
#         # self.group_lists = QGroupBox("LISTADOS")
#         # self.group_lists.setLayout(self.layout_lists)
#         self.pdf = QPdfDocument(self)
#         self.pdf_viewr = QPdfView(self)
#
#         # Layout de pie
#         self.layout_footer = QHBoxLayout()
#
#         # Controles de la barra de título
#         ## Frame de la barra de título
#         self.frame_title_bar = QFrame()
#         self.frame_title_bar.setLayout(self.layout_title_bar)
#         self.frame_title_bar.setStyleSheet(
#             """
#                 QFrame {
#                     background-color: transparent;
#                     border: 0px solid transparent;
#                 }
#             """
#         )
#         self.frame_title_bar.setContentsMargins(0, 0, 0, 10)
#
#         ## Botón de cerrar
#         icon = QIcon()
#         icon.addPixmap(QPixmap(":/Images/close.png"), QIcon.Mode.Normal,
#                        QIcon.State.On)
#         self.button_tb_close = QPushButton()
#         self.button_tb_close.setIcon(icon)
#         self.button_tb_close.setObjectName("button_bt_close")
#         self.button_tb_close.setFlat(True)
#         self.button_tb_close.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor)
#         )
#
#         ## Botón de maximizar
#         icon2 = QIcon()
#         icon2.addPixmap(QPixmap(":/Images/maximize.png"), QIcon.Mode.Normal,
#                         QIcon.State.On)
#         self.button_tb_maximize = QPushButton()
#         self.button_tb_maximize.setIcon(icon2)
#         self.button_tb_maximize.setObjectName("button_bt_maximize")
#         self.button_tb_maximize.setFlat(True)
#         self.button_tb_maximize.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor)
#         )
#         self.button_tb_maximize.hide()
#
#         ## Pripiedades del botón restaurar
#         icon3 = QIcon()
#         icon3.addPixmap(QPixmap(":/Images/restore.png"), QIcon.Mode.Normal,
#                         QIcon.State.On)
#         self.button_tb_restore = QPushButton()
#         self.button_tb_restore.setIcon(icon3)
#         self.button_tb_restore.setObjectName("button_bt_restore")
#         self.button_tb_restore.setFlat(True)
#         self.button_tb_restore.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor)
#         )
#         self.button_tb_restore.hide()
#
#         ## Propiedades del botón minimizar
#         icon4 = QIcon()
#         icon4.addPixmap(QPixmap(":/Images/minimize.png"), QIcon.Mode.Normal,
#                         QIcon.State.On)
#         self.button_tb_minimize = QPushButton()
#         self.button_tb_minimize.setIcon(icon4)
#         self.button_tb_minimize.setObjectName("button_tb_minimize")
#         self.button_tb_minimize.setFlat(True)
#         self.button_tb_minimize.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor)
#         )
#         self.button_tb_minimize.hide()
#
#         ## Título de la ventana
#         self.label_window_title = QLabel(self.window_title)
#
#         ## Icono de la ventana
#         self.label_icon = QLabel()
#         icon5 = QPixmap(":/Images/Window_icon.png")
#         self.label_icon.setPixmap(icon5)
#
#         ## Botón Cerrar
#         self.button_close = QPushButton()
#         self.button_close.setText("C&ERRAR")
#         self.button_close.setFlat(True)
#         self.button_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#
#         # Controles de los listados
#         ## Botones
#         self.buton_report_listado_proyectos = QPushButton(
#             "LISTADO DE PROYECTOS")
#         self.buton_report_listado_proyectos.setFlat(True)
#         self.buton_report_listado_proyectos.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor))
#
#         self.buton_report_listado_acuarios = QPushButton(
#             "LISTADO DE ACUARIOS")
#         self.buton_report_listado_acuarios.setFlat(True)
#         self.buton_report_listado_acuarios.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor))
#
#         self.buton_report_listado_urnas = QPushButton(
#             "LISTADO DE URNAS")
#         self.buton_report_listado_urnas.setFlat(True)
#         self.buton_report_listado_urnas.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor))
#
#         ## Botón Cerrar
#         self.button_close = QPushButton()
#         self.button_close.setText("C&ERRAR")
#         self.button_close.setFlat(True)
#         self.button_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#
#         self.layout_lists.addWidget(self.buton_report_listado_proyectos)
#         self.layout_lists.addWidget(self.buton_report_listado_acuarios)
#         self.layout_lists.addWidget(self.buton_report_listado_urnas)
#
#     def build_layout(self):
#         """ Construye el layout de la ventana """
#
#         # Ocultar barra de título
#         self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
#
#         # Configuramos la barra del título
#         self.layout_title_bar.addWidget(self.label_icon)
#         self.layout_title_bar.addWidget(self.label_window_title)
#         self.layout_title_bar.addSpacerItem(
#             QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
#                         QSizePolicy.Policy.Minimum)
#         )
#         self.layout_title_bar.addWidget(self.button_tb_minimize)
#         self.layout_title_bar.addWidget(self.button_tb_restore)
#         self.layout_title_bar.addWidget(self.button_tb_maximize)
#         self.layout_title_bar.addWidget(self.button_tb_close)
#
#         # Configuramos los controles del formulario
#         self.layout_controls.addWidget(self.group_lists)
#
#         # Configulamos el layout del pie de formulario
#         self.layout_footer.addSpacerItem(
#             QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
#                         QSizePolicy.Policy.Minimum)
#         )
#         self.layout_footer.addWidget(self.button_close)
#
#         # Cargamos los layout en la ventana
#         self.layout_main.addWidget(self.frame_title_bar)
#         self.layout_main.addLayout(self.layout_controls)
#         self.layout_main.addLayout(self.layout_footer)
#
#         layout_root = QVBoxLayout(self)
#         layout_root.setContentsMargins(0, 0, 0, 0)
#         layout_root.setSpacing(0)
#         layout_root.addWidget(self.frame_main)
#
#     """
#     El comportamiento básico de la barra de titulo que hemos creado
#     """
#
#     def control_bt_minimizar(self):
#         """ Minimiza la ventana """
#         self.showMinimized()
#
#     def control_bt_maximizar(self):
#         """ Maximiza la ventana """
#         self.showMaximized()
#         self.button_tb_maximize.hide()
#         self.button_tb_restore.show()
#
#     def control_bt_normal(self):
#         """ Establece el tamaño normal de la ventana """
#         self.showNormal()
#         self.button_tb_restore.hide()
#         self.button_tb_maximize.show()
#
#     """
#     El comportamiento básico de la barra de titulo que hemos creado
#     """
#
#     def control_bt_minimizar(self):
#         """ Minimiza la ventana """
#         self.showMinimized()
#
#     def control_bt_maximizar(self):
#         """ Maximiza la ventana """
#         self.showMaximized()
#         self.button_tb_maximize.hide()
#         self.button_tb_restore.show()
#
#     def control_bt_normal(self):
#         """ Establece el tamaño normal de la ventana """
#         self.showNormal()
#         self.button_tb_restore.hide()
#         self.button_tb_maximize.show()
#
#     def mover_ventana(self, event):
#         try:
#             if not self.isMaximized():
#                 if event.buttons() == Qt.MouseButton.LeftButton:
#                     self.move(self.pos() + event.globalPosition().toPoint()
#                               - self.drag_position)
#                     self.drag_position = event.globalPosition().toPoint()
#                     event.accept()
#
#             if self.drag_position.y() <= 20:
#                 self.showMaximized()
#         except Exception as e:
#             print(f"Error en mover_ventana: {e}")
#
#     """
#     El comportamiento del redimensionado de la ventana
#     """
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.MouseButton.LeftButton:
#             self._resize_direction = self._detect_resize_region(event.pos())
#             if self._resize_direction:
#                 self._resizing = True
#                 self._start_pos = event.globalPosition().toPoint()
#                 self._start_geom = self.geometry()
#             else:
#                 self._dragging = True
#                 self.drag_position = event.globalPosition().toPoint()
#
#     def mouseMoveEvent(self, event):
#         if self._resizing and self._resize_direction:
#             self._perform_resize(event.globalPosition().toPoint())
#         else:
#             direction = self._detect_resize_region(event.pos())
#             self._update_cursor(direction)
#
#     def mouseReleaseEvent(self, event):
#         self._resizing = False
#         self._resize_direction = None
#
#     def leaveEvent(self, event):
#         self.unsetCursor()
#
#     def _detect_resize_region(self, pos):
#         rect = self.rect()
#         x, y, w, h = pos.x(), pos.y(), rect.width(), rect.height()
#         margin = self._resize_margin
#
#         vertical = None
#         horizontal = None
#         if y < margin:
#             vertical = 'top'
#         elif y > h - margin:
#             vertical = 'bottom'
#         if x < margin:
#             horizontal = 'left'
#         elif x > w - margin:
#             horizontal = 'right'
#
#         if vertical and horizontal:
#             return f"{vertical}-{horizontal}"
#         elif vertical:
#             return vertical
#         elif horizontal:
#             return horizontal
#         else:
#             return None
#
#     def _update_cursor(self, direction):
#         cursors = {
#             'left': Qt.CursorShape.SizeHorCursor,
#             'right': Qt.CursorShape.SizeHorCursor,
#             'top': Qt.CursorShape.SizeVerCursor,
#             'bottom': Qt.CursorShape.SizeVerCursor,
#             'top-left': Qt.CursorShape.SizeFDiagCursor,
#             'bottom-right': Qt.CursorShape.SizeFDiagCursor,
#             'top-right': Qt.CursorShape.SizeBDiagCursor,
#             'bottom-left': Qt.CursorShape.SizeBDiagCursor,
#         }
#         self.setCursor(cursors.get(direction, Qt.CursorShape.ArrowCursor))
#
#     def _perform_resize(self, current_pos):
#         dx = current_pos.x() - self._start_pos.x()
#         dy = current_pos.y() - self._start_pos.y()
#         geom = self._start_geom
#         new_rect = QRect(geom)
#
#         if 'left' in self._resize_direction:
#             new_rect.setLeft(geom.left() + dx)
#         if 'right' in self._resize_direction:
#             new_rect.setRight(geom.right() + dx)
#         if 'top' in self._resize_direction:
#             new_rect.setTop(geom.top() + dy)
#         if 'bottom' in self._resize_direction:
#             new_rect.setBottom(geom.bottom() + dy)
#
#         min_width, min_height = self.minimumWidth(), self.minimumHeight()
#         if new_rect.width() < min_width:
#             new_rect.setWidth(min_width)
#         if new_rect.height() < min_height:
#             new_rect.setHeight(min_height)
#
#         self.setGeometry(new_rect)
#
#
# # Entrada a la aplicación
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     ventana = ReportView("REPORTES")
#
#     # Cargar el archivo .qss
#     with open("../Resources/Styles/main_style.qss", "r",
#               encoding="utf-8-sig") as f:
#         estilo = f.read()
#         app.setStyleSheet(estilo)
#
#     ventana.show()
#     sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QToolBar, QWidget
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtPdf import QPdfDocument
from PyQt6.QtPdfWidgets import QPdfView
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog


class PdfViewer(QDialog):
    def __init__(self, pdf_path: str):
        super().__init__()

        self.setWindowTitle("Visor de documentos PDF")
        self.resize(900, 700)

        # Documento PDF
        self.pdf = QPdfDocument(self)
        self.pdf.load(pdf_path)

        # Visor
        self.view = QPdfView(self)
        self.view.setDocument(self.pdf)

        # Layout principal
        layout = QVBoxLayout(self)

        # Barra de herramientas
        toolbar = QToolBar("PDF", self)

        # Acciones
        act_prev = QAction("◀", self)
        act_next = QAction("▶", self)
        act_zoom_in = QAction("＋", self)
        act_zoom_out = QAction("－", self)
        act_fit_width = QAction("Ajustar ancho", self)
        act_fit_page = QAction("Ajustar página", self)
        act_print = QAction(self)
        act_print.setIcon(QIcon("../../Resources/Images/impresora.png"))

        # Conexiones
        act_prev.triggered.connect(self._prev_page)
        act_next.triggered.connect(self._next_page)

        act_zoom_in.triggered.connect(
            lambda: self.view.setZoomFactor(self.view.zoomFactor() * 1.2))
        act_zoom_out.triggered.connect(
            lambda: self.view.setZoomFactor(self.view.zoomFactor() / 1.2))
        act_fit_width.triggered.connect(
            lambda: self.view.setZoomMode(QPdfView.ZoomMode.FitToWidth))
        act_fit_page.triggered.connect(
            lambda: self.view.setZoomMode(QPdfView.ZoomMode.FitInView))
        act_print.triggered.connect(self._print_pdf)

        toolbar.addActions([
            act_prev, act_next,
            act_zoom_in, act_zoom_out,
            act_fit_width, act_fit_page,
            act_print
        ])

        layout.addWidget(toolbar)
        layout.addWidget(self.view)

    # --------------------------
    # Funciones
    # --------------------------

    def _prev_page(self):
        navigator = self.view.pageNavigator()
        current = navigator.currentPage()

        if current > 0:
            navigator.jump(current - 1)

    def _next_page(self):
        navigator = self.view.pageNavigator()
        current = navigator.currentPage()

        if current < self.pdf.pageCount() - 1:
            navigator.jump(current + 1)

    def _print_pdf(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec():
            self.pdf.render(printer)


# --------------------------
# EJECUCIÓN DIRECTA
# --------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)

    viewer = PdfViewer("urnas.pdf")  # Cambia aquí el nombre del PDF
    viewer.exec()

    sys.exit()
