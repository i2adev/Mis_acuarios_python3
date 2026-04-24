"""
Autor: Inigo Iturriagaetxebarria
Fecha: 12/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de comportamiento de fauna.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from ModuloMaestro.Controllers.comportamiento_fauna_controller import \
    ComportamientoFaunaController
from ModuloMaestro.Model.DAO.comportamiento_fauna_dao import \
    ComportamientoFaunaDAO
from ModuloMaestro.Model.Entities.comprtamiento_fauna_entity import \
    ComportamientoFaunaEntity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.comportamiento_fauna_dialog import \
    ComportamientoFaunaDialog
from ModuloMaestro.Views.Masters.comportamiento_fauna_view import \
    ComportamientoFaunaView


class ComportamientoFaunaDialogController(ComportamientoFaunaController):
    """ Controlador del cuadro de diálogo comprtamiento de fauna. """

    def __init__(self,
                 view: ComportamientoFaunaDialog | ComportamientoFaunaView,
                 dao: ComportamientoFaunaDAO,
                 mod: ComportamientoFaunaEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de comportamiento de fauna.
        :param dao: DAO de comportamiento de fauna.
        :param mod: Modelo de comportamiento de fauna.
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
        self._comportamiento_result = ComportamientoFaunaEntity(
            id=res.value,
            num=None,
            comportamiento=self._view.frame.edit_comportamiento.value(),
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
            categoria_acuario = self._get_comportamiento()
            return Result.success(categoria_acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
