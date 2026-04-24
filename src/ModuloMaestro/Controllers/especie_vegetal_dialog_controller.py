"""
Autor: Inigo Iturriagaetxebarria
Fecha: 24/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de especie animal.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from ModuloMaestro.Controllers.especie_vegetal_controller import EspecieVegetalController
from ModuloMaestro.Model.DAO.especie_vegetal_dao import EspecieVegetalDAO
from ModuloMaestro.Model.Entities.especie_vegetal_entity import \
    EspecieVegetalEntity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.especie_vegetal_dialog import EspecieVegetalDialog


class EspecieVegetalDialogController(EspecieVegetalController):
    """ Controlador del cuadro de diálogo especie animal. """

    def __init__(self, view: EspecieVegetalDialog, dao: EspecieVegetalDAO,
                 mod: EspecieVegetalEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de especie vegetal.
        :param dao: DAO de especie vegetal.
        :param mod: Modelo de especie vegetal.
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llena los combos
        self._fill_combos()

        # Oculta los layouts
        self._hide_layout(self._view.frame.layout_id)

        # Deshabilitamos los controles
        self._setDisabledControl(self._view.frame.layout_n_cientifico, True)

        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los manejadores de eventos."""

        # Textos y combos
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)
            if isinstance(widget, QComboBox):
                widget.installEventFilter(self)

        # Botones
        self._view.frame.button_insert_posicion.clicked.connect(
            self._open_posicion_dialog
        )
        self._view.frame.button_insert_req_iuminacion.clicked.connect(
            self._open_req_iluminacion_dialog
        )
        self._view.frame.button_insert_req_co2.clicked.connect(
            self._open_req_co2_dialog
        )
        self._view.frame.button_insert_crecimiento.clicked.connect(
            self._open_tasa_crecimiento_dialog
        )
        self._view.frame.button_insert_dificultad.clicked.connect(
            self._open_dificultad_dialog
        )
        self._view.button_accept.clicked.connect(self.dialog_accept)
        self._view.button_cancel.clicked.connect(self.dialog_cancel)

    def dialog_accept(self):
        """ Se acepta el diálogo. """

        # Insertamos el registro
        res = self._insert()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Configuramos la entidad

        self._acuario_result = EspecieVegetalEntity(
            id=res.value,
            num=None,
            reino=self._view.frame.edit_reino.value(),
            division=self._view.frame.edit_division.value(),
            clase=self._view.frame.edit_clase.value(),
            orden=self._view.frame.edit_orden.value(),
            familia=self._view.frame.edit_familia.value(),
            genero=self._view.frame.edit_genero.value(),
            especie=self._view.frame.edit_especie.value(),
            nombre_cientifico=self._view.frame.edit_n_cientifico.value(),
            nombre_comun=self._view.frame.edit_n_comun.value(),
            ph_min=self._view.frame.edit_ph_min.value(),
            ph_max=self._view.frame.edit_ph_max.value(),
            kh_min=self._view.frame.edit_kh_min.value(),
            kh_max=self._view.frame.edit_kh_max.value(),
            gh_min=self._view.frame.edit_kh_min.value(),
            gh_max=self._view.frame.edit_gh_max.value(),
            temp_min=self._view.frame.edit_temp_min.value(),
            temp_max=self._view.frame.edit_temp_max.value(),
            origen=self._view.frame.edit_origen.value(),
            id_posicion_acuario=self._view.frame.combo_posicion.value(),
            id_req_iluminacion=self._view.frame.combo_req_iluminacion.value(),
            id_req_co2=self._view.frame.combo_req_co2.value(),
            id_tasa_crecimiento=self._view.frame.combo_crecimiento.value(),
            id_dificultad=self._view.frame.combo_dificultad.value(),
            descripcion=self._view.frame.text_descripcion.value() if
            self._view.frame.text_descripcion.value() else None
        )
        # Aceptamos el diálogo
        self._view.accept()

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            # Obtiene la subcategoría de acuario
            especie = self._get_especie()
            return Result.success(especie)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
