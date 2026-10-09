"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      13/05/2026
Comentarios:
    Módulo que contiene la clase controladora del módulo proyecto.
"""

import globales
from Main.Controllers.base_controller import BaseController
from ModuloProyecto.Models.DAO.tarjeta_acuario_dao import TarjetaAcuarioDAO
from ModuloProyecto.Models.DAO.tarjeta_proyecto_dao import TarjetaProyectoDAO
from ModuloProyecto.Models.Entities.tarjeta_acuaerio_entity import \
    TarjetaAcuarioEntity
from ModuloProyecto.Models.Entities.tarjeta_proyecto_entity import \
    TarjetaProyectoEntity
from ModuloProyecto.Views.Forms.tarjeta_acuario_form import TarjetaAcuarioFrame
from ModuloProyecto.Views.Forms.tarjeta_proyecto_form import \
    TarjetaProyectoFrame
from ModuloProyecto.modulo_proyecto_view import ModuloProyectoView


class ModuloProyectoController(BaseController):
    """
    Clase controladora que maneja los eventos del formulario del modulo 
    maestro.
    """

    def __init__(self):
        """ Constructor de clase. """

        # Inicializa la vista, la entidad y los DAOs
        self._view = ModuloProyectoView("MÓDULO PROYECTO")

        self._daoTarjetaProyecto = TarjetaProyectoDAO()
        proyectos = (self._daoTarjetaProyecto.get_proyectos_by_user(10001)
                     .value)
        self.proyecto_frames = (self.crear_tarjetas_proyecto(proyectos))

        self._daoTarjetaAcuario = TarjetaAcuarioDAO()
        acuarios = (self._daoTarjetaAcuario.get_acuarios_by_project(10001)
                    .value)
        self.acuario_frames = self.crear_tarjetas_acuario(acuarios)

        # Llama al constructor base
        super().__init__(self._view, None, None)

        # Añadimos las tarjetas al formulario
        self.add_tarjetas_formulario(self.acuario_frames)
        self.add_tarjetas_proyecto(self.proyecto_frames)

        # Inicializa los eventos
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los handlers. """

        # Botones de la barra de menú
        self._view.button_menu_cerrar.clicked.connect(
            lambda: self._view.close()
        )

    def crear_tarjetas_acuario(self, acuarios:
    list[TarjetaAcuarioEntity]) -> list[TarjetaAcuarioFrame]:
        """
        Crea una lista de tarjetas de acuario para que se pueda mostrar en
        el formulario.
        :param acuarios: lista de las entidades  tarjetas de acuario.
        :return: lista de tarjetas de acuario widgets.
        """

        tarjetas = []
        for acuario in acuarios:
            tarjetas.append(TarjetaAcuarioFrame(acuario))

        return tarjetas

    def crear_tarjetas_proyecto(self, proyectos:
    list[TarjetaProyectoEntity]) -> list[TarjetaProyectoFrame]:
        """
        Crea una lista de tarjetas de proyecto para que se pueda mostrar en
        el formulario.
        :param proyectos: lista de las entidades  tarjetas de proyecto.
        :return: lista de tarjetas de proyecto widgets.
        """

        tarjetas = []
        for proyecto in proyectos:
            tarjetas.append(TarjetaProyectoFrame(proyecto))

        return tarjetas

    def add_tarjetas_formulario(self, tarjetas: list[TarjetaAcuarioEntity]):
        """
        Añade las tarjetas al formulario.
        :param tarjetas: Lista de tarjetas de acuario.
        :return: None
        """

        for tarjeta in tarjetas:
            self._view.layout_acuario.addWidget(tarjeta)

    def add_tarjetas_proyecto(self, tarjetas: list[TarjetaProyectoEntity]):
        """
        Añade las tarjetas al formulario.
        :param tarjetas: Lista de tarjetas de proyecto.
        :return: None
        """

        for tarjeta in tarjetas:
            self._view.layout_proyecto.addWidget(tarjeta)

    def select_current_project(self, id_project: int) -> None:
        """
        Selecciona la tarjeta del proyecto.
        :param id_project: Id del proyecto a seleccionar.
        :return: None
        """

        for proyecto in self.proyecto_frames:
            if proyecto.id == id_project:
                proyecto.label_selected.setVisible(True)
                break

    def select_current_acuarium(self, id_acuarium: int) -> None:
        """
        Selecciona la tarjeta del acuario.
        :param id_acuarium: Id del acuario a seleccionar.
        :return: None
        """

        for acuario in self.acuario_frames:
            if acuario.id == id_acuarium:
                acuario.label_selected.setVisible(True)
                break

    def show(self, id_project: int | None = None,
             id_acuarium: int | None = None):
        """ Abre la vista """

        if id_project:
            self.select_current_project(id_project)
        else:
            self.proyecto_frames[0].label_selected.setVisible(True)

        if id_acuarium:
            self.select_current_acuarium(id_acuarium)
        else:
            self.acuario_frames[0].label_selected.setVisible(True)

        self._view.show()
