"""
Controlador de la entidad tipo de filtro
"""

# Importaciones
from PyQt6.QtWidgets import QWidget

from Controllers.base_controller import Base_controler
from Views.tipo_filtro_view import Tipo_filtro_view

class Tipo_filtro_controller(Base_controler):
    """ Controlador de la entidad tipo de filtro """
    def __init__(self):
        """ Constructor base """
        super().__init__() # Llamamos al constructor base
        self.view = Tipo_filtro_view("TIPOS DE FILTRO") # Inicializamos la
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

