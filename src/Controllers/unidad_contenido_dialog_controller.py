"""
Autor: Inigo Iturriagaetxebarria
Fecha: 05/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de unidades de contenido.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.unidad_contenido_controller import UnidadContenidoController
from Model.DAO.unidad_contenido_dao import UnidadContenidoDAO
from Model.Entities.unidades_contenido_entity import UnidadContenidoEntity
from Services.Result.result import Result
from Views.Dialogs.unidad_contenido_dialog import UnidadContenidoDialog


class UnidadContenidoDialogController(UnidadContenidoController):
    """ Controlador del cuadro de diálogo unidad contenido. """

    def __init__(self, view: UnidadContenidoDialog,
                 dao: UnidadContenidoDAO,
                 mod: UnidadContenidoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de unidad de contenido
        :param dao: DAO de unidad de contenido
        :param mod: Modelo de unidad de contenido
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
        self._formato_consumible_result = UnidadContenidoEntity(
            id=res.value,
            num=None,
            unidad=self._view.frame.edit_unidad_consumible.text(),
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
            unidad_contenido = self._get_unidad_contenido()
            return Result.success(unidad_contenido)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
