"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/06/2025
Comentarios:
    Módulo que contiene la clase controladora de la vista principal.
"""
import sys

from PyQt6.QtWidgets import QMessageBox

import globales

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Controllers.main_reports_controller import \
    MainReportsController
from ModuloMaestro.Views.main_reports_view import MainReportsView
from Main.main_view import MainView
from ModuloMaestro.modulo_maestro_controller import ModuloMaestroController


class MainViewController(BaseController):
    """
    Clase controladora que maneja los eventos de la vista principal.
    """

    def __init__(self):
        """ Constructor de clase. """

        # Inicializamos la vista, la entidad y el DAO
        self._view = MainView("ACUARIOS DE "
                              f"{globales.CURRENT_USER.nombre.upper()} "
                              f"{globales.CURRENT_USER.apellido1.upper()}")
        # TODO: Crear e inicializar el DAO que gestiona el dashboard.

        # Llamamos al constructor base
        super().__init__(self._view, None, None)

        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los handlers. """

        # Botones principales de menú
        self._view.button_modulo_maestro.clicked.connect(
            self.modulo_maestro_click
        )
        self._view.button_modulo_acuario.clicked.connect(
            lambda: self.en_construccion("ACUARIO")
        )
        self._view.button_modulo_mantenimiento.clicked.connect(
            lambda: self.en_construccion("MANTENIMIENTO")
        )
        self._view.button_modulo_compras.clicked.connect(
            lambda: self.en_construccion("COMPRAS")
        )
        self._view.button_modulo_inventario.clicked.connect(
            lambda: self.en_construccion("INVENTARIO")
        )
        self._view.button_modulo_reportes.clicked.connect(
            lambda: self.en_construccion("REPORTES")
        )
        self._view.button_modulo_configuracion.clicked.connect(
            lambda: self.en_construccion("CONFIGURACIÓN")
        )
        self._view.button_salir_aplicacion.clicked.connect(
            lambda: sys.exit(0)
        )

    def reportes_click(self):
        """ Cuando se pulsa el control de reportes. """
        view = MainReportsView("REPORTES")
        ctrl = MainReportsController(view)

        ctrl.show()

    def modulo_maestro_click(self):
        """ Abre el módulo maestro. """

        ctrl = ModuloMaestroController()
        ctrl.show()

    def en_construccion(self, modulo: str):
        """
        Muestra un mensaje indicando que el módulo está en construcción.
        :param modulo: Nombre del módulo.
        """

        QMessageBox.information(self._view, "EN CONSTRUCION",
                                f"EL 'MÓDULO {modulo}' ESTÁ EN CONSTRUCCIÓN")

    def show(self):
        """ Abre la vista """
        self._view.show()
        self._view.showMaximized()
        self._view.button_tb_maximize.hide()
        self._view.button_tb_restore.show()
