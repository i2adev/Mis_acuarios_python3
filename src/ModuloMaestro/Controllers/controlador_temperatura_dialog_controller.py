"""
Autor: Inigo Iturriagaetxebarria
Fecha: 18/09/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de controlador de 
    temperatura.
"""
from CustomControls.nullable_date_edit import NullableDateEdit
from PyQt6.QtWidgets import QComboBox, QMessageBox, QWidget

from ModuloMaestro.Controllers.controlador_temperatura_controller import \
    ControladorTemperaturaController
from ModuloMaestro.Model.DAO.controlador_temperatura_dao import \
    ControladorTemperaturaDAO
from ModuloMaestro.Model.Entities.control_temperatura_entity import \
    ControladorTemperaturaEntity
from ModuloMaestro.Views.Dialogs.controlador_temperatura_dialog import \
    ControladorTemperaturaDialog
from Services.Result.result import Result


class ControladorTemperaturaDialogController(ControladorTemperaturaController):
    """ Controlador del cuadro de diálogo categoría de controlador de temperatura. """

    def __init__(self, view: ControladorTemperaturaDialog,
                 dao: ControladorTemperaturaDAO,
                 mod: ControladorTemperaturaEntity):
        """
        Constructor base.
        :param view: Cuadro de diálogo de inserción de acuario
        :param dao: DAO de categoría de controlador de temperatura
        :param mod: Modelo de categoría de controlador de temperatura
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llena los combos
        self._fill_combos_async()

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
        self._view.frame.fecha_baja.edit_date.textChanged.connect(
            self._on_text_changed
        )

        # Botones
        self._view.frame.button_insert_tipo_controlador.clicked.connect(
            self._open_tipo_control_temperatura_dialog()
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
        self._equipamiento_result = ControladorTemperaturaEntity(
            id=res.value,
            num=None,
            id_tipo_control_temperatura=int(
                self._view.frame.combo_tipo_controlador.currentData()),
            id_marca=int(self._view.frame.combo_marca.currentData()),
            modelo=self._view.frame.edit_modelo.text(),
            numero_serie=self._view.frame.numero_serie.text(),
            fecha_alta=int(
                self._view.frame.fecha_alta.dateTime().toSecsSinceEpoch()),
            fecha_baja=int(
                self._view.frame.fecha_baja.dateTime().toSecsSinceEpoch()),
            motivo_baja=self._view.frame.edit_motivo_baja.text(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
            if self._view.frame.text_descripcion.toPlainText() else None
        )

        # Aceptamos el diálogo
        self._view.accept()

    def dialog_cancel(self):
        """ Cancela el diálogo. """

        self._view.reject()

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            controlador = self._get_controlador()
            return Result.success(controlador)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
