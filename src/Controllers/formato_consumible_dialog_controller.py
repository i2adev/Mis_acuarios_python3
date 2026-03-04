"""
Autor: Inigo Iturriagaetxebarria
Fecha: 04/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de formato de consumible.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.categoria_consumible_controller import \
    CategoriaConsumibleController
from Model.DAO.formato_consumible_dao import FormatoConsumibleDAO
from Model.Entities.formato_consumible_entity import FormatoConsumibleEntity
from Services.Result.result import Result
from Views.Dialogs.formato_consumible_dialog import FormatoConsumibleDialog


class FormatoConsumibleDialogController(CategoriaConsumibleController):
    """ Controlador del cuadro de diálogo formato de consumible. """

    def __init__(self, view: FormatoConsumibleDialog,
                 dao: FormatoConsumibleDAO,
                 mod: FormatoConsumibleEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de formato de consumible
        :param dao: DAO del formato de consumible
        :param mod: Modelo del formato de consumible
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
        self._formato_consumible_result = FormatoConsumibleEntity(
            id=res.value,
            num=None,
            formato=self._view.frame.edit_formato_consumible.text(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
            if self._view.frame.text_descripcion.toPlainText()
            else ""
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
            formato_consumible = self._get_categoria_consumible()
            return Result.success(formato_consumible)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
