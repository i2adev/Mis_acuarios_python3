"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la vista principal.
"""

from Controllers.base_controller import BaseController
from Controllers.categoria_acuario_controller import CategoriaAcuarioController
from Controllers.subcategoria_acuario_controller import \
    SubcategoriaAcuarioController
from Controllers.tipo_acuario_controller import TipoAcuarioController
from Controllers.tipo_filtro_controller import TipoFiltroController
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.Entities.subcategoria_acuario_entity import SubcategoriaAcuarioEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Views.categoria_acuario_view import CategoriaAcuarioView
from Views.main_view import MainView
from Views.subcategoria_acuario_view import SubcategoriaAcuarioView
from Views.tipo_acuario_view import TipoAcuarioView


class MainViewController(BaseController):
    """
    Clase controladora que maneja los eventos de la vista principal.
    """

    def __init__(self):
        """ Construtctor de clase. """

        # Inicializamos la vista, la entitdad y el DAO
        self._view = MainView("MIS ACIUARIOS")
        # TODO: Crear e inicializar el DAO que gestiona el dashboard.

        # Llamamos al constructor base
        super().__init__(self._view, None, None)

        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los handlers. """
        # Inicializamos los botones
        self._view.button_maestro_tipo_giltro.clicked.connect(
            self.tipo_filtro_clicked
        )
        self._view.button_maestro_tipo_acuario.clicked.connect(
            self.tipo_acuario_clicked
        )
        self._view.button_maestro_categoria_acuario.clicked.connect(
            self.categoria_acuario_clicked
        )

        self._view.button_maestro_subcategoria_acuario.clicked.connect(
            self.subcategoria_Acuario_clicked
        )


    def tipo_filtro_clicked(self, event):
        """
        Cuando se presiona en el maestro de tipo de filtro.
        Acción: Abre el formulario de tipo de filtro
        """

        dao = TipoFiltroDAO()
        mod = TipoFiltroEntity()

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
        dao = TipoAcuarioDAO()
        mod = TipoAcuarioEntity()

        ctrl = TipoAcuarioController(view, dao, mod)
        ctrl.show()

    def categoria_acuario_clicked(self, event):
        """
        Cuando se presiona en el maestro de tipo categoría de acuariode filtro.
        Acción: Abre el formulario de categoría de acuario.
        """

        view = CategoriaAcuarioView(
            "MAESTRO DE CATEGORÍAS DE ACUARIO"
        )
        dao = CategoriaAcuarioDAO()
        mod = CategoriaAcuarioEntity()

        ctrl = CategoriaAcuarioController(view, dao, mod)
        ctrl.show()

    def subcategoria_Acuario_clicked(self):
        """
        Cuando se presiona en el maestro de subcategoría de acuario de filtro.
        Acción: Abre el formulario de subcategoría de acuario.
        """

        view = SubcategoriaAcuarioView(
            "MAESTRO DE SUBCATEGORÍAS DE ACUARIO"
        )
        dao = SubcategoriaAcuarioDAO()
        mod = SubcategoriaAcuarioEntity()

        ctrl = SubcategoriaAcuarioController(view, dao, mod)
        ctrl.show()

    def show(self):
        """ Abre la vista """
        self._view.show()
        #self._view.showMaximized()


