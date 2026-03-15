"""
Autor: Inigo Iturriagaetxebarria
Fecha: 15/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de nivel de nado.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.nivel_nado_controller import NivelNadoController
from Model.DAO.niveles_nado_dao import NivelNadoDAO
from Model.Entities.nivel_nado_entity import NivelNadoEntity
from Services.Result.result import Result
from Views.Dialogs.nivel_nado_dialog import NivelNadoDialog
from Views.Masters.nivel_nado_view import NivelNadoView


class NivelNadoDialogController(NivelNadoController):
    """ Controlador del cuadro de diálogo nivel de nado """

    def __init__(self,
                 view: NivelNadoDialog | NivelNadoView,
                 dao: NivelNadoDAO,
                 mod: NivelNadoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de nivel de nado.
        :param dao: DAO de nivel de nado.
        :param mod: Modelo de nivel de nado.
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
        self._comportamiento_result = NivelNadoEntity(
            id=res.value,
            num=None,
            nivel_nado=self._view.frame.edit_nivel.value(),
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
            # Obtenemos la entidad
            nivel_nado = self._get_nivel()
            return Result.success(nivel_nado)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
