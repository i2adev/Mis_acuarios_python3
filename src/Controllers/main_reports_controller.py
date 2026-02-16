"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  07/01/2026
Comentarios:
    Controlador del formulario maestro de reportes.
"""

from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QWidget, QComboBox

from Controllers.base_controller import BaseController
from Views.main_reports_view import MainReportsView


class MainReportsController(BaseController):
    """ Controlador del formulario maestro de reportes. """

    def __init__(self, view: MainReportsView):
        """
        Constructor base
        :param view: Formulario maestro de reportes
        """

        # Constructor base
        super().__init__(view, None, None)

        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """
        Inicializa los eventos de los widgets del formulario maestro.
        """

        # Textos y combos
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)
            if isinstance(widget, QComboBox):
                widget.installEventFilter(self)

        # Inicializa los botónes
        self._view.buton_report_listado_proyectos.clicked.connect(
            self.button_listado_proyectos_click
        )

        self._view.buton_report_listado_acuarios.clicked.connect(
            self.button_listado_acuarios_click
        )

        self._view.buton_report_listado_urnas.clicked.connect(
            self.button_listado_urnas_click
        )

    def button_listado_proyectos_click(self):
        """
        Cuando se pulsa el botón de listado de proyectos.
        Abre el reporte de listado de proyectos.
        """
        pass

    def button_listado_acuarios_click(self):
        """
        Cuando se pulsa el botón de listado de acuarios.
        Abre el reporte de listado de acuarios.
        """
        pass

    def button_listado_urnas_click(self):
        """
        Cuando se pulsa el botón de listado de urnas.
        Abre el reporte de listado de urnas.
        """
        pass

    def show(self):
        """ Abre la vista """

        self._view.show()
        self._center_window()
