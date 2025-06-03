"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad TIPO DE
    FILTRO.
"""

# Importaciones
from PyQt6.QtWidgets import QWidget

from Controllers.base_controller import BaseController
from Views.tipo_filtro_view import TipoFiltroView
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO

class TipoFiltroController(BaseController):
    """ Controlador de la entidad tipo de filtro. """
    def __init__(self):
        """ Constructor base """
        super().__init__()

        # Inicializamos la vista, la entidad y el dao
        self.view = TipoFiltroView("TIPOS DE FILTRO")
        self.mod = TipoFiltroEntity()
        self.dao = TipoFiltroDAO()

        # Inicializamos los eventos
        self.Init_handlers()

    def show(self):
        """ Abre la vista """
        self.view.show()

    def get_tipo_filtro_list(self):
        """ Obtiene el listado de tipos de filtro. """
        pass

    def Init_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        # Inicializa los widgets de introducción de texto
        for widget in self.view.findChildren(QWidget):
            if isinstance(widget, self.text_widgets):
                widget.installEventFilter(self)

