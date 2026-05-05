"""
Autor: Inigo Iturriagaetxebarria
Fecha: 24/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de especie animal.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from ModuloMaestro.Controllers.especie_animal_controller import \
    EspecieAnimalController
from ModuloMaestro.Model.DAO.especie_animal_dao import EspecieAnimalDAO
from ModuloMaestro.Model.Entities.especie_animal_entity import \
    EspecieAnimalEntity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.especie_animal_dialog import \
    EspecieAnimalDialog


class EspecieAnimalDialogController(EspecieAnimalController):
    """ Controlador del cuadro de diálogo especie animal. """

    def __init__(self, view: EspecieAnimalDialog, dao: EspecieAnimalDAO,
                 mod: EspecieAnimalEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de especie animal.
        :param dao: DAO de especie animal.
        :param mod: Modelo de especie animal.
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llena los combos
        self._fill_combos_async()

        # Oculta los layouts
        self._hide_layout(self._view.frame.layout_id)

        # Deshabilitamos los controles
        self._setDisabledControl(self._view.frame.layout_n_cientifico, True)
        self._setDisabledControl(self._view.frame.layout_n_e_hibrida, True)

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

        # Checboxes
        self._view.frame.check_hibrida.stateChanged.connect(
            self._check_state_changed
        )

        # Botones
        self._view.frame.button_insert_grupo_taxo.clicked.connect(
            self._open_grupo_taxo_dialog
        )
        self._view.frame.button_insert_comportamiento.clicked.connect(
            self._open_comportamiento_dialog
        )
        self._view.frame.button_insert_dieta.clicked.connect(
            self._open_dieta_dialog
        )
        self._view.frame.button_insert_nivel_nado.clicked.connect(
            self._open_nivel_nado_dialog
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

        self._acuario_result = EspecieAnimalEntity(
            id=res.value,
            num=None,
            reino=self._view.frame.edit_reino.value(),
            filo=self._view.frame.edit_filo.value(),
            clase=self._view.frame.edit_clase.value(),
            orden=self._view.frame.edit_orden.value(),
            familia=self._view.frame.edit_familia.value(),
            genero=self._view.frame.edit_genero.value(),
            especie=self._view.frame.edit_especie.value(),
            nombre_cientifico=self._view.frame.edit_n_cientifico.value(),
            nombre_comun=self._view.frame.edit_n_comun.value(),
            es_hibrida=True if self._view.frame.check_hibrida.isChecked()
            else False,
            nombre_especie_hibrida=self._view.frame.edit_n_e_hibrida.value(),
            id_grupo_taxonomico=self._view.frame.combo_grupo_taxo.value(),
            ph_min=self._view.frame.edit_ph_min.value(),
            ph_max=self._view.frame.edit_ph_max.value(),
            kh_min=self._view.frame.edit_kh_min.value(),
            kh_max=self._view.frame.edit_kh_max.value(),
            gh_min=self._view.frame.edit_kh_min.value(),
            gh_max=self._view.frame.edit_gh_max.value(),
            temp_min=self._view.frame.edit_temp_min.value(),
            temp_max=self._view.frame.edit_temp_max.value(),
            origen=self._view.frame.edit_origen.value(),
            tamano_cm=self._view.frame.edit_tamano.value(),
            id_comportamiento=self._view.frame.combo_comportamiento.value(),
            id_dieta=self._view.frame.combo_dieta.value(),
            id_nivel_nado=self._view.frame.combo_nivel_nado.value(),
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
