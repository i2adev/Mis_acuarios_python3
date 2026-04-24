"""
Autor: Inigo Iturriagaetxebarria
Fecha: 07/04/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de periodo.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox

from ModuloMaestro.Controllers.periodo_controller import PeriodoController
from ModuloMaestro.Model.DAO.periodo_dao import PeriodoDAO
from ModuloMaestro.Model.Entities.periodo_entity import PeriodoEntity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.periodo_dialog import PeriodoDialog
from ModuloMaestro.Views.Masters.periodo_view import PeriodoView


class PeriodoDialogController(PeriodoController):
    """ Controlador del cuadro de diálogo posición de planta en el acuario. """

    def __init__(self,
                 view: PeriodoDialog | PeriodoView,
                 dao: PeriodoDAO,
                 mod: PeriodoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de periodo.
        :param dao: DAO de periodo.
        :param mod: Modelo de periodo.
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
        self._requerimiento_result = PeriodoEntity(
            id=res.value,
            num=None,
            periodo=self._view.frame.edit_periodo.value(),
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
            periodo = self._get_periodo()
            return Result.success(periodo)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
