"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la vista principal.
"""

from Controllers.base_controller import BaseController
from Controllers.categoria_incidencia_controller_obs import \
    CategoriaIncidenciaControllerObs
from Controllers.marca_comercial_controller import MarcaComercialController
from Controllers.material_urna_controller import MaterialUrnaController
from Controllers.subcategoria_acuario_controller import \
    SubcategoriaAcuarioController
from Controllers.subcategoria_incidencia_controller import \
    SubcategoriaIncidenciaController
from Controllers.tipo_acuario_controller import TipoAcuarioController
from Controllers.urna_controller import UrnaController
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.categoria_incidencia_dao import CategoriaIncidenciaDAO
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Model.DAO.material_urna_dao import MaterialUrnaDAO
from Model.DAO.subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from Model.DAO.subcategoria_incidencia_dao import SubcategoriaIncidenciaDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.DAO.urna_dao import UrnaDAO
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.Entities.categoria_incidencia_entity import CategoriaIncidenciaEntity
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.Entities.material_urna_entity import MaterialUrnaEntity
from Model.Entities.subcategoria_acuario_entity import SubcategoriaAcuarioEntity
from Model.Entities.subcategoria_incidencia import SubcategoriaIncidenciaEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Model.Entities.urna_entity import UrnaEntity
from Views.Masters.categoria_acuario_view import CategoriaAcuarioView
from Views.Masters.categoria_incidencia_view import CategoriaIncidenciaView
from Views.Masters.material_urna_view import MaterialUrnaView
from Views.Masters.urna_view import UrnaView
from Views.main_view import MainView
from Views.Masters.marca_comercial_view import MarcaComercialView
from Views.Masters.subcategoria_acuario_view import SubcategoriaAcuarioView
from Views.Masters.subcategoria_incidencia_view import SubcategoriaIncidenciaView
from Views.Masters.tipo_acuario_view import TipoAcuarioView
from Views.Masters.tipo_filtro_view import TipoFiltroView
import globals
from categoria_acuario_master_controller import CategoriaAcuarioMasterController
from tipo_filtro_master_controller import TipoFiltroMasterController


class MainViewController(BaseController):
    """
    Clase controladora que maneja los eventos de la vista principal.
    """

    def __init__(self):
        """ Construtctor de clase. """

        # Inicializamos la vista, la entitdad y el DAO
        self._view = MainView("ACUARIOS DE "
                              f"{globals.CURRENT_USER.nombre.upper()} "
                              f"{globals.CURRENT_USER.apellido1.upper()}")
        # TODO: Crear e inicializar el DAO que gestiona el dashboard.

        # Llamamos al constructor base
        super().__init__(self._view, None, None)

        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los handlers. """
        # Inicializamos los botones
        self._view.button_maestro_tipo_filtro.clicked.connect(
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

        self._view.button_maestro_cat_incidencia.clicked.connect(
            self.categoria_incidencia_clicked
        )

        self._view.button_maestro_subcat_incidencia.clicked.connect(
            self.subcategoria_incidencia_clicked
        )

        self._view.button_maestro_marca.clicked.connect(
            self.marca_comercial_clicked
        )

        self._view.button_maestro_material.clicked.connect(
            self.material_urna_clicked
        )

        self._view.button_maestro_urna.clicked.connect(
            self.urna_clicked
        )

    def material_urna_clicked(self):
        """
        Cuando se presiona en el maestro de material.
        Acción: Abre el formulario de material de urna
        """

        view = MaterialUrnaView("MAESTRO DE MATERIALES DE URNA")
        dao = MaterialUrnaDAO()
        mod = MaterialUrnaEntity()

        ctrl = MaterialUrnaController(view, dao, mod)
        ctrl.show()

    def urna_clicked(self):
        """
        Cuando se presiona en el maestro de urna.
        Acción: Abre el formulario de urna
        """
        view = UrnaView("MAESTRO DE URNA")
        dao = UrnaDAO()
        mod = UrnaEntity()

        ctrl = UrnaController(view, dao, mod)
        ctrl.show()

    def tipo_filtro_clicked(self, event):
        """
        Cuando se presiona en el maestro de tipo de filtro.
        Acción: Abre el formulario de tipo de filtro
        """
        view = TipoFiltroView("MAESTRO DE TIPO DE FILTRO")
        dao = TipoFiltroDAO()
        mod = TipoFiltroEntity()

        ctrl = TipoFiltroMasterController(view, dao, mod)
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
        Cuando se presiona en el maestro de tipo categoría de acuario.
        Acción: Abre el formulario de categoría de acuario.
        """

        view = CategoriaAcuarioView(
            "MAESTRO DE CATEGORÍAS DE ACUARIO"
        )
        dao = CategoriaAcuarioDAO()
        mod = CategoriaAcuarioEntity()

        ctrl = CategoriaAcuarioMasterController(view, dao, mod)
        ctrl.show()

    def subcategoria_Acuario_clicked(self):
        """
        Cuando se presiona en el maestro de subcategoría de acuario.
        Acción: Abre el formulario de subcategoría de acuario.
        """

        view = SubcategoriaAcuarioView(
            "MAESTRO DE SUBCATEGORÍAS DE ACUARIO"
        )
        dao = SubcategoriaAcuarioDAO()
        mod = SubcategoriaAcuarioEntity()

        ctrl = SubcategoriaAcuarioController(view, dao, mod)
        ctrl.show()

    def categoria_incidencia_clicked(self):
        """
        Cuando se presiona en el maestro de categoría de incidencia.
        Acción: Abre el formulario de subcategoría de acuario.
        """

        view = CategoriaIncidenciaView("MAESTRO DE CATEGORÍAS DE INCIDENCIAS")
        dao = CategoriaIncidenciaDAO()
        mod = CategoriaIncidenciaEntity()

        ctrl = CategoriaIncidenciaControllerObs(view, dao, mod)
        ctrl.show()

    def subcategoria_incidencia_clicked(self):
        """
        Cuando se presiona en el maestro de subcategoría de incidencia.
        Acción: Abre el formulario de subcategoría de acuario.
        """

        view = SubcategoriaIncidenciaView(
            "MAESTRO DE SUBCATEGORÍAS DE INCIDENCIA"
        )
        dao = SubcategoriaIncidenciaDAO()
        mod = SubcategoriaIncidenciaEntity()

        ctrl = SubcategoriaIncidenciaController(view, dao, mod)
        ctrl.show()


    def marca_comercial_clicked(self):
        """
        Cuando se presiona en el maestro de marcas comerciales.
        Acción: Abre el formulario de marcas comerciales.
        """

        view = MarcaComercialView(
            "MAESTRO DE MARCAS COMERCIALES"
        )
        dao = MarcaComercialDAO()
        mod = MarcaComercialEntity()

        ctrl = MarcaComercialController(view, dao, mod)
        ctrl.show()

    def show(self):
        """ Abre la vista """
        self._view.show()
        #self._view.showMaximized()

