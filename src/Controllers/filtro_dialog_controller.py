"""
Autor: Inigo Iturriagaetxebarria
Fecha: 02/12/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de filtro.
"""

from Controllers.filtro_controller import FiltroController
from CustomControls.nullable_date_edit import NullableDateEdit
from Model.DAO.filtro_dao import FiltroDAO
from Model.Entities.filtro_entity import FiltroEntity
from PyQt6.QtWidgets import QComboBox, QMessageBox, QWidget
from Services.Result.result import Result
from Views.Dialogs.filtro_dialog import FiltroDialog


class FiltroDialogController(FiltroController):
    """ Controlador del cuadro de diálogo filtro. """

    def __init__(self, view: FiltroDialog, dao: FiltroDAO,
                 mod: FiltroEntity):
        """
        Constructor base.
        :param view: Cuadro de diálogo de inserción de acuario
        :param dao: DAO de filtro
        :param mod: Modelo de filtro
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llena los combos
        self._fill_combos()

        # Oculta los layouts
        self._hide_layout(self._view.frame.layout_id)

        # Inhabilita el layout del motivo de baja
        self._setDisabledControl(self._view.frame.layout_motivo_baja, True)

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
            if isinstance(widget, NullableDateEdit):
                widget.edit_date.installEventFilter(self)

        # Textboxes
        self._view.frame.date_fin.edit_date.textChanged.connect(
            self._on_text_changed
        )

        # Botones
        self._view.frame.button_insert_tipo_filtro.clicked.connect(
            self._open_tipo_filtro_dialog()
        )
        self._view.frame.button_insert_marca.clicked.connect(
            self._open_marca_dialog()
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
        self._filtro_result = FiltroEntity(
            id=res.value,
            num=None,
            id_tipo=int(self._view.frame.combo_tipo_filtro.currentData()),
            id_marca=int(self._view.frame.combo_marca.currentData()),
            modelo=self._view.frame.edit_modelo.text(),
            es_thermo=self._view.frame.checkbox_thermo.isChecked(),
            vol_min_acuario=int(self._view.frame.edit_vol_min_acuario.text()),
            vol_max_acuario=int(self._view.frame.edit_vol_max_acuario.text()),
            caudal=int(self._view.frame.edit_caudal.text()),
            altura_bombeo=float(self._view.frame.edit_altura_bombeo.text()),
            consumo=int(self._view.frame.edit_consumo_filtro.text()),
            consumo_calentador=int(
                self._view.frame.edit_consumo_calentador.text()),
            vol_filtrante=float(self._view.frame.edit_vol_material.text()),
            ancho=int(self._view.frame.edit_ancho.text()),
            fondo=int(self._view.frame.edit_fondo.text()),
            alto=int(self._view.frame.edit_alto.text()),
            fecha_compra=int(
                self._view.frame.fecha_compra.dateTime().toSecsSinceEpoch()),
            fecha_baja=int(
                self._view.frame.fecha_baja.dateTime().toSecsSinceEpoch()),
            motivo_baja=self._view.frame.edit_motivo_baja.text(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
            if self._view.frame.text_descripcion.toPlainText() else None
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
            filtro = self._get_filtro()
            return Result.success(filtro)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
