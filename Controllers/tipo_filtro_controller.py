"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad TIPO DE
    FILTRO.
"""

# Importaciones
from PyQt6.QtWidgets import QWidget, QTextEdit, QPlainTextEdit, QMessageBox

from Controllers.base_controller import BaseController
from Views.tipo_filtro_view import TipoFiltroView
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO

class TipoFiltroController(BaseController):
    """ Controlador de la entidad tipo de filtro. """
    def __init__(self):
        """ Constructor base """
        # inicializamos la vista y pasamos al constructor padre
        view = TipoFiltroView("TIPOS DE FILTRO")
        super().__init__(view)

        # Inicializamos la vista, la entidad y el dao
        self.__mod = TipoFiltroEntity()
        self.__dao = TipoFiltroDAO()

        # Inicializamos los eventos
        self.Init_handlers()

    def show(self):
        """ Abre la vista """
        self._view.show()

    def get_tipo_filtro_list(self):
        """ Obtiene el listado de tipos de filtro. """
        pass

    def Init_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        # Inicializa los widgets de introducción de texto
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)
