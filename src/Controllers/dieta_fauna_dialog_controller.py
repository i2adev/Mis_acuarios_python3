"""
Autor: Inigo Iturriagaetxebarria
Fecha: 13/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de dieta de fauna.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.dieta_fauna_controller import DietaFaunaController
from Model.DAO.dieta_fauna_dao import DietaFaunaDAO
from Model.Entities.dieta_fauna_entity import DietaFaunaEntity
from Services.Result.result import Result
from Views.Dialogs.dieta_fauna_dialog import DietaFaunaDialog
from Views.Masters.dieta_fauna_view import DietaFaunaView


class DietaFaunaDialogController(DietaFaunaController):
    """ Controlador del cuadro de diálogo dieta de fauna. """

    def __init__(self,
                 view: DietaFaunaDialog | DietaFaunaView,
                 dao: DietaFaunaDAO,
                 mod: DietaFaunaEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de dieta de fauna.
        :param dao: DAO de dieta de fauna.
        :param mod: Modelo de dieta de fauna.
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
        self._dieta_fauna = DietaFaunaEntity(
            id=res.value,
            num=None,
            dieta=self._view.frame.edit_dieta.value(),
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
            dieta_fauna = self._get_dieta()
            return Result.success(dieta_fauna)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
