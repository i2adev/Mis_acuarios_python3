"""
Autor: Inigo Iturriagaetxebarria
Fecha: 16/09/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de tipo de control de 
    iluminación.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from ModuloMaestro.Controllers.tipo_control_iluminacion_controller import \
    TipoControlTemperaturaController
from ModuloMaestro.Model.DAO.tipo_control_temperatura_dao import \
    TipoControlTemperaturaDAO
from ModuloMaestro.Model.Entities.tipo_control_temperatura_entity import \
    TipoControlTemperaturaEntity
from ModuloMaestro.Views.Dialogs.tipo_control_temperatura_dialog import \
    TipoControlTemperaturaDialog
from Services.Result.result import Result


class TipoControlTemperaturaDialogController(TipoControlTemperaturaController):
    """ Controlador del cuadro de diálogo tipo de filtro. """

    def __init__(self, view: TipoControlTemperaturaDialog,
                 dao: TipoControlTemperaturaDAO,
                 mod: TipoControlTemperaturaEntity):
        """
        Constructor base
        :param view: TipoControlTemperaturaDialog
        :param dao: TipoControlTemperaturaDAO
        :param mod: TipoControlTemperaturaEntity
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Oculta el layout del ID
        self._hide_layout(self._view.frame.layout_id)

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
        self._tipo_control_temperatura_result = TipoControlTemperaturaEntity(
            id=res.value,
            num=None,
            tipo_control_temperatura=self._view.frame
            .edit_tipo_control_temperatura
            .text(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
        )

        # Aceptamos el diálogo
        self._view.accept()

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            # Obtenemos la subcategoría de acuario
            tipo_control_temperatura = self._get_tipo_control_temperatura()
            return Result.success(tipo_control_temperatura)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
