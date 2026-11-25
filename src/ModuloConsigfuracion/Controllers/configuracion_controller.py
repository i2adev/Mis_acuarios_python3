"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  11/11/2026
Comentarios:
    Controlador del módulo de configuración.
"""
import os
import sys

from PyQt6.QtCore import QProcess
from PyQt6.QtWidgets import QApplication, QFrame, QMessageBox

import globales
from CustomControls.boton_lateral import BotonLateral
from Main.Controllers.base_controller import BaseController
from ModuloConsigfuracion.Models.DAO.unidad_kh_dao import UnidadesKHDAO
from ModuloConsigfuracion.Models.DAO.unidades_caudal_dao import \
    UnidadesCaudalDAO
from ModuloConsigfuracion.Models.DAO.unidades_concentracion_dao import \
    UnidadesConcentracionDAO
from ModuloConsigfuracion.Models.DAO.unidades_conductividad_dao import \
    UnidadesConductividadDAO
from ModuloConsigfuracion.Models.DAO.unidades_densidad_dao import \
    UnidadesDensidadDAO
from ModuloConsigfuracion.Models.DAO.unidades_distancia_dao import \
    UnidadesDistanciaDAO
from ModuloConsigfuracion.Models.DAO.configuracion_dao import ConfiguracionDAO
from ModuloConsigfuracion.Models.DAO.unidades_energia_dao import \
    UnidadesEnergiaDAO
from ModuloConsigfuracion.Models.DAO.unidades_gh_dao import UnidadesGHDAO
from ModuloConsigfuracion.Models.DAO.unidades_iluminacion_dao import \
    UnidadesIluminacionDAO
from ModuloConsigfuracion.Models.DAO.unidades_masa_dao import UnidadesMasaDAO
from ModuloConsigfuracion.Models.DAO.unidades_potencia_dao import \
    UnidadesPotenciaDAO
from ModuloConsigfuracion.Models.DAO.unidades_presion_dao import \
    UnidadesPresionDAO
from ModuloConsigfuracion.Models.DAO.unidades_salinidad_dao import \
    UnidadesSalinidadDAO
from ModuloConsigfuracion.Models.DAO.unidades_temperatura_dao import \
    UnidadesTemperaturaDAO
from ModuloConsigfuracion.Models.DAO.unidades_volumen_dao import \
    UnidadesVolumenDAO
from ModuloConsigfuracion.Models.Entities.configuracion_entity import \
    ConfiguracionEntity
from ModuloConsigfuracion.Views.Masters.modulo_configuracion_view import \
    ModuloConfiguracionView
from ModuloMaestro.Model.DAO.acuario_dao import AcuarioDAO
from ModuloMaestro.Model.DAO.proyecto_dao import ProyectoDAO


class ConfiguracionController(BaseController):
    """ Controlador de la vista configuración. """

    def __init__(self, view: ModuloConfiguracionView,
                 dao: ConfiguracionDAO,
                 entity: ConfiguracionEntity):
        # Llama al constructor base
        super().__init__(view, dao, entity)

        # Inicializa las variables
        self._combos_config = (
            self._view.frame_cuenta.combo_proyecto,
            self._view.frame_cuenta.combo_acuario,
            self._view.frame_unidades.combo_dimensiones,
            self._view.frame_unidades.combo_volumen,
            self._view.frame_unidades.combo_masa,
            self._view.frame_unidades.combo_temp,
            self._view.frame_unidades.combo_potencia,
            self._view.frame_unidades.combo_energia,
            self._view.frame_unidades.combo_caudal,
            self._view.frame_unidades.combo_presion,
            self._view.frame_unidades.combo_iluminacion,
            self._view.frame_unidades.combo_concentracion,
            self._view.frame_unidades.combo_kh,
            self._view.frame_unidades.combo_gh,
            self._view.frame_unidades.combo_cond,
            self._view.frame_unidades.combo_sal,
            self._view.frame_unidades.combo_densidad,
        )

        # Selecciona el primer frame
        self.select_secction(self._view.section_list[0][0].objectName())

        # Llenar los combos asincronamente
        self.load_combos_async()

        # Inicializa los handlers
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los eventos de la vista. """

        # Botones de las secciones
        self._view.button_cuenta.boton.clicked.connect(
            lambda: self.section_click())
        self._view.button_unidades.boton.clicked.connect(
            lambda: self.section_click())

        # Botones del pie de formulario
        self._view.button_cerrar.clicked.connect(
            self.cerrar_formulario
        )

        # Eventos de los combos
        ## Cuenta
        self._view.frame_cuenta.combo_proyecto.currentIndexChanged.connect(
            self.on_proyecto_changed)
        self._view.frame_cuenta.combo_proyecto.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="cuenta",
                key="proyecto_por_defecto")
        )
        self._view.frame_cuenta.combo_acuario.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="cuenta",
                key="acuario_por_defecto")
        )
        ## Unidades
        self._view.frame_unidades.combo_dimensiones.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="dimension")
        )
        self._view.frame_unidades.combo_volumen.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="volumen")
        )
        (self._view.frame_unidades.combo_temp.currentIndexChanged
        .connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="temperatura")
        ))
        self._view.frame_unidades.combo_masa.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="masa")
        )
        self._view.frame_unidades.combo_potencia.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="potencia")
        )
        self._view.frame_unidades.combo_energia.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="energia")
        )
        self._view.frame_unidades.combo_caudal.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="caudal")
        )
        self._view.frame_unidades.combo_presion.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="presion")
        )
        (self._view.frame_unidades.combo_iluminacion.currentIndexChanged
        .connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="iluminacion")
        ))
        (self._view.frame_unidades.combo_concentracion.currentIndexChanged
        .connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="concentracion")
        ))
        self._view.frame_unidades.combo_kh.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="dureza_carbonatos")
        )
        self._view.frame_unidades.combo_gh.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="dureza_general")
        )
        self._view.frame_unidades.combo_cond.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="conductividad")
        )
        self._view.frame_unidades.combo_sal.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="salinidad")
        )
        self._view.frame_unidades.combo_densidad.currentIndexChanged.connect(
            lambda index: self.change_config_value(
                section="unidades",
                key="densidad")
        )

    def cerrar_formulario(self):
        """ Cierra el formulario. """

        # Detecta los cambios realizados en la configuracxión
        if globales.CONFIG_MANAGER.has_changes():
            res = QMessageBox.question(
                self._view,
                self._view.window_title,
                (
                    "SE HAN REALIZADO CAMBIOS EN LA CONFIGURACIÓN.\n"
                    "¿DESEA GUARDAR LOS CAMBIOS?"
                ),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.Yes
            )

            if res == QMessageBox.StandardButton.Yes:
                self.save_config()

        self._view.close()

    def save_config(self, to_exit: bool = False):
        """
        Guarda la configuración en el archivo JSON.
        :param to_exit: Boleano que indica si se sale de la aplicación.
        """

        # Guarda el archivo
        if not globales.CONFIG_MANAGER.save():
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                "ERROR EN EL GUARDADO DE LA CONFIGURACIÓN"
            )
            return

        if to_exit:
            QApplication.quit()
        else:
            res = QMessageBox.question(
                self._view,
                self._view.window_title,
                ("PARA QUE LOS CAMBIOS SEAN EFECTIVOS, DEBE REINICIAR LA "
                 "APLICACIÓN.\n¿DESEA REINICIAR LA APLICACIÓN?"),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.Yes,
            )

            if res == QMessageBox.StandardButton.Yes:
                self.reiniciar_programa()

    def change_config_value(self, section, key):
        combo = self.sender()
        value = combo.currentData()

        if not value:
            return

        globales.CONFIG_MANAGER.set_value(
            section=section,
            key=key,
            value=value
        )

    def on_proyecto_changed(self, index: int):
        """ Se ejecuta cuando se cambia el valor del proyecto por defecto. """

        if index == -1:
            return

        combo = self._view.frame_cuenta.combo_acuario

        self._load_combo(
            combo=combo,
            worker_fn=lambda: AcuarioDAO().get_list_combo_by_project(
                int(globales.CONFIG_MANAGER.get_value(
                    "cuenta",
                    "proyecto_por_defecto")
                )
            ),
            data=globales.CONFIG_MANAGER.get_value(
                "cuenta",
                "acuario_por_defecto"
            )
        )

    def section_click(self):
        """
        Cuando se pulsa en una de las secciones a traves del menú lateral.
        """

        button = self.sender()
        lateral_button = button.parentWidget()

        control_name = lateral_button.objectName()

        self.select_secction(control_name)

    def select_secction(self, control_name: str):
        """
        Selecciona la sección de la configuración.
        :param control_name: Nombre del botón de sección.
        """

        # Desactiva las secciones
        for i in range(self._view.layout_controls.count()):
            widget = self._view.layout_controls.itemAt(i).widget()

            if isinstance(widget, QFrame):
                widget.hide()

        # Activa el botón que se ha pulsado
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

    def load_combos_async(self):
        """ Carga todos los combos de forma asíncrona. """

        for combo in self._combos_config:
            match combo.objectName():
                case "combo_dimensiones":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesDistanciaDAO().get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "dimension"
                        )
                    )
                case "combo_volumen":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesVolumenDAO().get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "volumen"
                        )
                    )
                case "combo_masa":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesMasaDAO().get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "masa"
                        )
                    )
                case "combo_temp":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesTemperaturaDAO().get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "temperatura"
                        )
                    )
                case "combo_potencia":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesPotenciaDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "potencia"
                        )
                    )
                case "combo_energia":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesEnergiaDAO(

                        ).get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "energia"
                        )
                    )
                case "combo_caudal":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesCaudalDAO(

                        ).get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "caudal"
                        )
                    )
                case "combo_presion":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesPresionDAO(

                        ).get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "presion"
                        )
                    )
                case "combo_iluminacion":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesIluminacionDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "iluminacion"
                        )
                    )
                case "combo_concentracion":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesConcentracionDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "concentracion"
                        )
                    )
                case "combo_kh":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesKHDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "dureza_carbonatos"
                        )
                    )
                case "combo_gh":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesGHDAO().get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "dureza_general"
                        )
                    )
                case "combo_cond":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesConductividadDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "conductividad"
                        )
                    )
                case "combo_sal":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesSalinidadDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "salinidad"
                        )
                    )
                case "combo_densidad":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: UnidadesDensidadDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "unidades",
                            "densidad"
                        )
                    )
                case "combo_proyecto":
                    self._load_combo(
                        combo=combo,
                        worker_fn=lambda: ProyectoDAO()
                        .get_list_combo(),
                        data=globales.CONFIG_MANAGER.get_value(
                            "cuenta",
                            "proyecto_por_defecto"
                        )
                    )

    def reiniciar_programa(self):
        """ Reinicia la aplicación con otra instancia de la aplicación. """

        # Inicia una nueva instancia con el mismo ejecutable y argumentos
        QProcess.startDetached(sys.executable,
                               [os.path.abspath(sys.argv[0])] + sys.argv[1:])
        QApplication.quit()

    def show(self):
        """ Abre la vista """

        self._view.show()
        self._center_window()
