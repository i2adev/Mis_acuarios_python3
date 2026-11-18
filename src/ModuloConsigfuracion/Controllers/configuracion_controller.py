"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  11/11/2026
Comentarios:
    Controlador del módulo de configuración.
"""
from PyQt6.QtWidgets import QFrame, QWidget

from CustomControls.boton_lateral import BotonLateral
from Main.Controllers.base_controller import BaseController
from ModuloConsigfuracion.Models.DAO.configuracion_dao import ConfiguracionDAO
from ModuloConsigfuracion.Models.Entities.configuracion_entity import \
    ConfiguracionEntity
from ModuloConsigfuracion.Views.Masters.modulo_configuracion_view import \
    ModuloConfiguracionView


class ConfiguracionController(BaseController):
    """ Controlador de la vista configuración. """

    def __init__(self, view: ModuloConfiguracionView,
                 dao: ConfiguracionDAO,
                 entity: ConfiguracionEntity):
        # Llama al constructor base
        super().__init__(view, dao, entity)

        # Selecciona el primer frame
        self.select_secction(self._view.section_list[0][0].objectName())

        # Inicializa los handlers
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los eventos de la vista. """

        # Botones de la barra de menú
        self._view.button_menu_cerrar.clicked.connect(
            lambda: self._view.close()
        )

        self._view.button_cuenta.boton.clicked.connect(
            lambda: self.section_click())
        self._view.button_unidades.boton.clicked.connect(
            lambda: self.section_click())

    def section_click(self):
        """
        Cuando se pulsa en una de las secciones a traves del menú
        lateral.
        """

        button = self.sender()
        lateral_button = button.parentWidget()

        control_name = lateral_button.objectName()

        self.select_secction(control_name)

    def select_secction(self, control_name: str):
        """ Selecciona la sección de la configuración. """

        # Desactiva las secciones
        for i in range(self._view.layout_controls.count()):
            widget = self._view.layout_controls.itemAt(i).widget()

            if isinstance(widget, QFrame):
                widget.hide()

        for i in range(self._view.menu_layout.count()):
            widget = self._view.menu_layout.itemAt(i).widget()

            if isinstance(widget, BotonLateral):
                widget.set_inactive()

        # Señala el botón con el nombre 'control_name'
        for button, frame in filter(
                lambda section: section[0].objectName() in [control_name],
                self._view.section_list
        ):
            button.set_active()
            frame.show()

    def show(self):
        """ Abre la vista """

        self._view.show()
        self._center_window()
