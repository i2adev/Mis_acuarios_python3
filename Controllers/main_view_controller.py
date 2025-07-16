"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la vista principal.
"""

from Controllers.base_controller import BaseController
from Controllers.categoria_acuario_controller import CategoriaAcuarioController
from Controllers.tipo_acuario_controller import TipoAcuarioController
from Controllers.tipo_filtro_controller import TipoFiltroController
from Views.categoria_acuario_view import CategoriaAcuarioView
from Views.main_view import MainView
from Views.tipo_acuario_view import TipoAcuarioView


class MainViewController(BaseController):
    """
    Clase controladora que maneja los eventos de la vista principal.
    """

    def __init__(self):
        """ Construtctor de clase. """

        # Inicializamos la vista, la entitdad y el DAO
        self.__view = MainView("MIS ACIUARIOS")
        # TODO: Crear e inicializar el DAO que gestiona el dashboard.

        # Llamamos al constructor base
        super().__init__(self.__view)

        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los handlers. """
        # Inicializamos los botones
        self.__view.button_maestro_tipo_giltro.clicked.connect(
            self.tipo_filtro_clicked
        )
        self.__view.button_maestro_tipo_acuario.clicked.connect(
            self.tipo_acuario_clicked
        )
        self.__view.button_maestro_categoria_acuario.clicked.connect(
            self.categoria_acuario_clicked
        )


    def tipo_filtro_clicked(self, event):
        """
        Cuando se presiona en el maestro de tipo de filtro.
        Acción: Abre el formulario de tipo de filtro
        """
        ctrl = TipoFiltroController()
        ctrl.show()

    def tipo_acuario_clicked(self, event):
        """
        Cuando se presiona en el maestro de tipo de acuario.
        Acción: Abre el formulario de tipo de acuario
        """
        view = TipoAcuarioView(
            "MAESTRO DE TIPOS DE ACUARIO"
        )
        ctrl = TipoAcuarioController(view)
        ctrl.show()

    def categoria_acuario_clicked(self, event):
        """
        Cuando se presiona en el maestro de tipo categoría de acuariode filtro.
        Acción: Abre el formulario de categoría de acuario.
        """
        view = CategoriaAcuarioView(
            "MAESTRO DE CATEGORÍAS DE ACUARIO"
        )
        ctrl = CategoriaAcuarioController(view)
        ctrl.show()

    def show(self):
        """ Abre la vista """
        self.__view.show()
        #self._view.showMaximized()
