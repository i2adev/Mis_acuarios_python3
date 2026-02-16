"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/06/2025
Comentarios:
    Módulo que contiene la clase controladora de la vista principal.
"""
import globals
from Controllers.acuario_master_controller import AcuarioMasterController
from Controllers.base_controller import BaseController
from Controllers.categoria_acuario_master_controller import \
    CategoriaAcuarioMasterController
from Controllers.categoria_equipamiento_master_dialog import \
    CategoriaEquipamientoMasterController
from Controllers.categoria_incidencia_master_controller import \
    CategoriaIncidenciaMasterController
from Controllers.comercio_master_controller import ComercioMasterController
from Controllers.control_iluminacion_master_controller import \
    ControlIluminacionMasterController
from Controllers.equipamiento_master_controller import \
    EquipamientoMasterController
from Controllers.estado_proyecto_master_controller import \
    EstadoProyectoMasterController
from Controllers.filtro_master_controller import FiltroMasterController
from Controllers.iluminacion_master_controller import \
    IluminacionMasterController
from Controllers.main_reports_controller import MainReportsController
from Controllers.marca_comercial_master_controller import \
    MarcaComercialMasterController
from Controllers.material_urna_master_controler import \
    MaterialUrnaMasterController
from Controllers.proyecto_master_controller import ProyectoMasterController
from Controllers.subcategoria_acuario_master_controller import \
    SubcategoriaAcuarioMasterController
from Controllers.subcategoria_incidencia_master_controller import \
    SubcategoriaIncidenciaMasterController
from Controllers.tipo_acuario_master_controller import \
    TipoAcuarioMasterController
from Controllers.tipo_filtro_master_controller import \
    TipoFiltroMasterController
from Controllers.tipo_iluminacion_controller import TipoIluminacionController
from Controllers.tipo_iluminacion_master_controller import \
    TipoIluminacionMasterController
from Controllers.urna_master_controller import UrnaMasterController
from Model.DAO.acuario_dao import AcuarioDAO
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.categoria_equipamiento_dao import CategoriaEquipamientoDAO
from Model.DAO.categoria_incidencia_dao import CategoriaIncidenciaDAO
from Model.DAO.comercio_dao import ComercioDAO
from Model.DAO.control_iluminacion_dao import ControlIluminacionDAO
from Model.DAO.equipamiento_dao import EquipamientoDAO
from Model.DAO.estado_proyecto_dao import EstadoProyectoDAO
from Model.DAO.filtro_dao import FiltroDAO
from Model.DAO.iluminacion_dao import IluminacionDAO
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Model.DAO.material_urna_dao import MaterialUrnaDAO
from Model.DAO.proyecto_dao import ProyectoDAO
from Model.DAO.subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from Model.DAO.subcategoria_incidencia_dao import SubcategoriaIncidenciaDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.DAO.tipo_iluminacion_dao import TipoIluminacionDAO
from Model.DAO.urna_dao import UrnaDAO
from Model.Entities.acuario_entity import AcuarioEntity
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.Entities.categoria_equipamiento_entity import \
    CategoriaEquipamientoEntity
from Model.Entities.categoria_incidencia_entity import \
    CategoriaIncidenciaEntity
from Model.Entities.comercio_entity import ComercioEntity
from Model.Entities.control_iluminacion_entity import ControlIluminacionEntity
from Model.Entities.equipamiento_entity import EquipamientoEntity
from Model.Entities.estado_proyecto_entity import EstadoProyectoEntity
from Model.Entities.filtro_entity import FiltroEntity
from Model.Entities.iluminacion_entity import IluminacionEntity
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.Entities.material_urna_entity import MaterialUrnaEntity
from Model.Entities.proyecto_entity import ProyectoEntity
from Model.Entities.subcategoria_acuario_entity import \
    SubcategoriaAcuarioEntity
from Model.Entities.subcategoria_incidencia_entity import \
    SubcategoriaIncidenciaEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Model.Entities.tipo_iluminacion_entity import TipoIluminacionEntity
from Model.Entities.urna_entity import UrnaEntity
from Views.Masters.acuario_view import AcuarioView
from Views.Masters.categoria_acuario_view import CategoriaAcuarioView
from Views.Masters.categoria_equipamiento_view import CategoriaEquipamientoView
from Views.Masters.categoria_incidencia_view import CategoriaIncidenciaView
from Views.Masters.comercio_view import ComercioView
from Views.Masters.control_iluminacion_view import ControlIluminacionView
from Views.Masters.equipamiento_view import EquipamientoView
from Views.Masters.estado_proyecto_view import EstadoProyectoView
from Views.Masters.filtro_view import FiltroView
from Views.Masters.iluminacion_view import IluminacionView
from Views.Masters.marca_comercial_view import MarcaComercialView
from Views.Masters.material_urna_view import MaterialUrnaView
from Views.Masters.proyecto_view import ProyectoView
from Views.Masters.subcategoria_acuario_view import SubcategoriaAcuarioView
from Views.Masters.subcategoria_incidencia_view import \
    SubcategoriaIncidenciaView
from Views.Masters.tipo_acuario_view import TipoAcuarioView
from Views.Masters.tipo_filtro_view import TipoFiltroView
from Views.Masters.tipo_iluminacion_view import TipoIluminacionView
from Views.Masters.urna_view import UrnaView
from Views.main_reports_view import MainReportsView
from Views.main_view import MainView


class MainViewController(BaseController):
    """
    Clase controladora que maneja los eventos de la vista principal.
    """

    def __init__(self):
        """ Constructor de clase. """

        # Inicializamos la vista, la entidad y el DAO
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
        # Inicializamos los botónes

        self._view.button_maestro_filtro.clicked.connect(
            self.filtro_clicked
        )

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

        self._view.button_maestro_proyecto.clicked.connect(
            self.proyecto_clicked
        )

        self._view.button_maestro_estado_proyecto.clicked.connect(
            self.estado_proyecto_clicked
        )

        self._view.button_maestro_acuario.clicked.connect(
            self.acuario_clicked
        )

        self._view.button_maestro_cat_equipamiento.clicked.connect(
            self.cat_equipamientto_clicked
        )

        self._view.button_maestro_equipamiento.clicked.connect(
            self.equipamiento_clicked
        )

        self._view.button_maestro_comercio.clicked.connect(
            self.comercio_clicked
        )

        self._view.button_maestro_tipo_iluminacion.clicked.connect(
            self.tipo_iluminacion_clicked
        )

        self._view.button_maestro_control_iluminacion.clicked.connect(
            self.control_iluminacion_clicked
        )

        self._view.button_menu_reportes.clicked.connect(
            self.reportes_click
        )
        self._view.button_maestro_iluminacion.clicked.connect(
            self.iluminacion_click
        )

    def reportes_click(self):
        """ Cuando se pulsa el control de reportes. """
        view = MainReportsView("REPORTES")
        ctrl = MainReportsController(view)

        ctrl.show()

    def iluminacion_click(self):
        """ Cuando se pulsa el botón de iluminaciones. """

        view = IluminacionView("MAESTRO DE ILUMINACIÓN")
        dao = IluminacionDAO()
        mod = IluminacionEntity()

        ctrl = IluminacionMasterController(view, dao, mod)
        ctrl.show()

    def control_iluminacion_clicked(self):
        """ Cuando se pulsa el control de iluminación. """

        view = ControlIluminacionView("MAESTRO DE CONTROLES DE ILUMINACIÓN")
        dao = ControlIluminacionDAO()
        mod = ControlIluminacionEntity()

        ctrl = ControlIluminacionMasterController(view, dao, mod)
        ctrl.show()

    def tipo_iluminacion_clicked(self):
        """ Cuando se pulsa el tipo de iluminacion. """

        view = TipoIluminacionView("MAESTRO DE TIPOS DE ILUMINACIÓN")
        dao = TipoIluminacionDAO()
        mod = TipoIluminacionEntity()

        ctrl = TipoIluminacionMasterController(view, dao, mod)
        ctrl.show()

    def comercio_clicked(self):
        """ Cuando se presiona en el botón comercio. """

        view = ComercioView("MAESTRO DE COMERCIOS")
        dao = ComercioDAO()
        mod = ComercioEntity()

        ctrl = ComercioMasterController(view, dao, mod)
        ctrl.show()

    def equipamiento_clicked(self):
        """ Cuando se presiona en el equipamiento. """

        view = EquipamientoView("MAESTRO DE EQUIPAMIENTOS")
        dao = EquipamientoDAO()
        mod = EquipamientoEntity()

        ctrl = EquipamientoMasterController(view, dao, mod)
        ctrl.show()

    def filtro_clicked(self):
        """
        Cuando se presiona en el filtro.
        Acción: Abre el formulario de filtro.
        """

        view = FiltroView("MAESTRO DE FILTROS")
        dao = FiltroDAO()
        mod = FiltroEntity()

        ctrl = FiltroMasterController(view, dao, mod)
        ctrl.show()

    def acuario_clicked(self):
        """
        Cuando se presiona en el acuario.
        Acción: Abre el formulario de acuario.
        """

        view = AcuarioView("MAESTRO DE ACUARIOS")
        dao = AcuarioDAO()
        mod = AcuarioEntity()

        ctrl = AcuarioMasterController(view, dao, mod)
        ctrl.show()

    def proyecto_clicked(self):
        """
        Cuando se presiona en el proyecto.
        Acción: Abre el formulario de proyecto.
        """

        view = ProyectoView("MAESTRO DE PROYECTOS")
        dao = ProyectoDAO()
        mod = ProyectoEntity()

        ctrl = ProyectoMasterController(view, dao, mod)
        ctrl.show()

    def estado_proyecto_clicked(self):
        """
        Cuando se presiona en el estado de proyecto.
        Acción: Abre el formulario de estado de proyecto.
        """

        view = EstadoProyectoView("MAESTRO DE ESTADOS DE PROYECTO")
        dao = EstadoProyectoDAO()
        mod = EstadoProyectoEntity()

        ctrl = EstadoProyectoMasterController(view, dao, mod)
        ctrl.show()

    def material_urna_clicked(self):
        """
        Cuando se presiona en el maestro de material.
        Acción: Abre el formulario de material de urna
        """

        view = MaterialUrnaView("MAESTRO DE MATERIALES DE URNA")
        dao = MaterialUrnaDAO()
        mod = MaterialUrnaEntity()

        ctrl = MaterialUrnaMasterController(view, dao, mod)
        ctrl.show()

    def urna_clicked(self):
        """
        Cuando se presiona en el maestro de urna.
        Acción: Abre el formulario de urna
        """
        view = UrnaView("MAESTRO DE URNA")
        dao = UrnaDAO()
        mod = UrnaEntity()

        ctrl = UrnaMasterController(view, dao, mod)
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

        ctrl = TipoAcuarioMasterController(view, dao, mod)
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

        ctrl = SubcategoriaAcuarioMasterController(view, dao, mod)
        ctrl.show()

    def categoria_incidencia_clicked(self):
        """
        Cuando se presiona en el maestro de categoría de incidencia.
        Acción: Abre el formulario de subcategoría de acuario.
        """

        view = CategoriaIncidenciaView("MAESTRO DE CATEGORÍAS DE INCIDENCIAS")
        dao = CategoriaIncidenciaDAO()
        mod = CategoriaIncidenciaEntity()

        ctrl = CategoriaIncidenciaMasterController(view, dao, mod)
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

        ctrl = SubcategoriaIncidenciaMasterController(view, dao, mod)
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

        ctrl = MarcaComercialMasterController(view, dao, mod)
        ctrl.show()

    def cat_equipamientto_clicked(self):
        """
        Cuando se presiona en el maestro de categorías de equipamiento.
        Acción: Abre el formulario de categorías de equipamiento.
        """

        view = CategoriaEquipamientoView(
            "MAESTRO DE CATEGORÍAS DE EQUIPAMIENTO"
        )
        dao = CategoriaEquipamientoDAO()
        mod = CategoriaEquipamientoEntity()

        ctrl = CategoriaEquipamientoMasterController(view, dao, mod)
        ctrl.show()

    def show(self):
        """ Abre la vista """
        self._view.show()
        # self._view.showMaximized()
