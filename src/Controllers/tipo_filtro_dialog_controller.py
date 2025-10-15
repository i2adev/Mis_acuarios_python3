"""
Autor: Inigo Iturriagaetxebarria
Fecha: 29/09/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de tipo de filtro.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox, QCompleter

from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Services.Result.result import Result
from Views.Dialogs.tipo_filtro_dialog import TipoFiltroDialog
from tipo_filtro_controller import TipoFiltroController


class TipoFiltroDialogoController(TipoFiltroController):
    """ Controlador del cuadro de diálogo tipo de filtro. """

    def __init__(self, view: TipoFiltroDialog, dao: TipoFiltroDAO,
                 mod: TipoFiltroEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de tipo de filtro
        :param dao: DAO del tipo de filtro
        :param mod: Modelo del tipo de filtro
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

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
        self._tipo_filtro_result = TipoFiltroEntity(
            id = res.value,
            num = None,
            tipo_filtro = self._view.frame.edit_tipo_filtro.text(),
            observaciones = self._view.frame.text_observaciones.toPlainText()
                          if self._view.frame.text_observaciones.toPlainText()
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
            tipo_filyto = self._get_tipo_filtro()
            return Result.success(tipo_filyto)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")