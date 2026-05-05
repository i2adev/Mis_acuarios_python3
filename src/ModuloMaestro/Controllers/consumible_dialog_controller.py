"""
Autor: Inigo Iturriagaetxebarria
Fecha: 11/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de consumible.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from ModuloMaestro.Controllers.consumible_controller import \
    ConsumibleController
from ModuloMaestro.Model.DAO.consumible_dao import ConsumibleDAO
from ModuloMaestro.Model.Entities.consumible_entity import ConsumibleEntity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.consumible_dialogo import ConsumibleDialog


class ConsumibleDialogController(ConsumibleController):
    """ Controlador del cuadro de diálogo consumible. """

    def __init__(self, view: ConsumibleDialog, dao: ConsumibleDAO,
                 mod: ConsumibleEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de consumible
        :param dao: DAO de consumible
        :param mod: Modelo de consumible
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llena los combos
        self._fill_combos_async()

        # Oculta los layouts
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
        self._view.frame.button_insert_marca.clicked.connect(
            self._open_marca_dialog
        )
        self._view.frame.button_insert_categoria.clicked.connect(
            self._open_categoria_dialog
        )
        self._view.frame.button_insert_formato.clicked.connect(
            self._open_formato_dialog
        )
        self._view.frame.button_insert_unidad.clicked.connect(
            self._open_unidad_dialog
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
        self._consumible_result = ConsumibleEntity(
            num=None,
            id_marca=self._view.frame.combo_urna.value(),
            producto=self._view.frame.edit_producto.value(),
            id_categoria=self._view.frame.combo_categoria.value(),
            id_formato=self._view.frame.combo_formato.value(),
            contenido=self._view.frame.edit_contenido.value(),
            id_unidad=self._view.frame.combo_unidad.value(),
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
            # Obtiene la subcategoría de acuario
            consumible = self._get_consumible()
            return Result.success(consumible)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
