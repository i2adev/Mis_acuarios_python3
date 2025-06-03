"""
Controlador de la entidad tipo de filtro
"""

# Importaciones
from PyQt6.QtWidgets import QWidget

from Controllers.base_controller import BaseController
from Views.tipo_filtro_view import TipoFiltroView

class TipoFiltroController(BaseController):
    """ Controlador de la entidad tipo de filtro """
    def __init__(self):
        """ Constructor base """
        super().__init__() # Llamamos al constructor base
        self.view = TipoFiltroView("TIPOS DE FILTRO") # Inicializamos la
                                                        # vista
        self.Init_handlers()

    def show(self):
        """ Abre la vista """
        self.view.show()

    def get_tipo_filtro_list(self):
        """ Obtiene el listado de tipos de filtro """
        pass

    def Init_handlers(self):
        """
        Instala este filtro de eventos a todos los widgets de texto de un
        formulario.
        """
        for widget in self.view.findChildren(QWidget):
            if isinstance(widget, self.text_widgets):
                widget.installEventFilter(self)

