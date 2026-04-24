"""
Autor: Inigo Iturriagaetxebarria
Fecha: 04/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de categoría de consumible.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from ModuloMaestro.Controllers.categoria_consumible_controller import \
    CategoriaConsumibleController
from ModuloMaestro.Model.DAO.categoria_consumible_dao import \
    CategoriaConsumibleDAO
from ModuloMaestro.Model.Entities.categoria_consumible_entity import \
    CategoriaConsumibleEntity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.categoria_consumible_dialog import \
    CategoriaConsumibleDialog


class CategoriaConsumibleDialogController(CategoriaConsumibleController):
    """ Controlador del cuadro de diálogo categoría de consumible. """

    def __init__(self, view: CategoriaConsumibleDialog,
                 dao: CategoriaConsumibleDAO,
                 mod: CategoriaConsumibleEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de estado de proyecto
        :param dao: DAO de la categoría de consumible
        :param mod: Modelo de la categoría de consumible
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
        self._categoria_consumible_result = CategoriaConsumibleEntity(
            id=res.value,
            num=None,
            categoria=self._view.frame.edit_categoria_consumible.value(),
            observaciones=self._view.frame.text_observaciones.toPlainText()
            if self._view.frame.text_observaciones.toPlainText()
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
            categoria_consumible = self._get_categoria_consumible()
            return Result.success(categoria_consumible)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
