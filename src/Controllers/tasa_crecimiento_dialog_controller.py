"""
Autor: Inigo Iturriagaetxebarria
Fecha: 11/04/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de la tasa de crecimiento.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox

from Controllers.tasa_crecimiento_controller import TasaCrecimientoController
from Model.DAO.tasa_crecimiento_dao import TasaCrecimientoDAO
from Model.Entities.tasa_crecimiento_entity import TasaCrecimientoEntity
from Services.Result.result import Result
from Views.Dialogs.tasa_crecimiento_dialog import TasaCrecimientoDialog
from Views.Masters.tasa_crecimiento_view import TasaCrecimientoView


class TasaCrecimientoDialogController(TasaCrecimientoController):
    """ Controlador del cuadro de diálogo posición de la tasa de crecimiento """

    def __init__(self,
                 view: TasaCrecimientoDialog | TasaCrecimientoView,
                 dao: TasaCrecimientoDAO,
                 mod: TasaCrecimientoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de la tasa de crecimiento.
        :param dao: DAO de comportamiento de la tasa de crecimiento.
        :param mod: Modelo de comportamiento de la tasa de crecimiento.
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
        self._crecimiento_result = TasaCrecimientoEntity(
            id=res.value,
            num=None,
            tasa_crecimiento=self._view.frame.edit_tasa_crecimiento.value(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
            if self._view.frame.text_descripcion.toPlainText()
            else None
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
            crecimiento = self._get_crecimiento()
            return Result.success(crecimiento)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
