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
from Services.Validators.tipo_filtro_validator import TipoFiltroValidator
from Views.Dialogs.tipo_filtro_dialog import TipoFiltroDialog
from base_controller import BaseController
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

        # Controles de entrada de texto
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)

        # Botones
        self._view.button_accept.clicked.connect(self.dialog_accept)
        self._view.button_cancel.clicked.connect(self.dialog_cancel)

    # def entity_configuration(self) -> TipoFiltroEntity:
    #     """ Configura la entidad. """
    #
    #     ent = TipoFiltroEntity()
    #
    #     if self._view.frame.edit_id.text():
    #         ent.id = int(self._view.frame.edit_id.text())
    #     else:
    #         ent.id = None
    #
    #     ent.tipo_filtro = self._view.frame.edit_tipo_filtro.text()
    #     ent.observaciones = self._view.frame.text_observaciones.toPlainText()
    #
    #     return ent

    # def insert(self) -> Result:
    #     """ Inserta un registro en la base de datos. """
    #
    #     # Validamos el formulario
    #     val = self.validate_view()
    #
    #     if not val.is_success:
    #         return val
    #
    #     # Configura la entidad
    #     ent = self.entity_configuration()
    #
    #     # Inserta el registro
    #     res = self._dao.insert(ent)
    #     if not res.is_success:
    #         return res
    #
    #     # Limpiamos el formulario
    #     self._clean_view(self._view.frame.edit_tipo_filtro)
    #
    #     return Result.success(res.value)

    # def validate_view(self):
    #     """ Valida el formulario. """
    #
    #     # Valida el tipo de filtro
    #     res = TipoFiltroValidator.validate_tipo_filtro(
    #         self._view.frame.edit_tipo_filtro
    #     )
    #
    #     if not res.is_success:
    #         self._view.frame.edit_tipo_filtro.setFocus()
    #         return res
    #
    #     return Result.success(1)

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

    # def get_tipo_filtro(self):
    #     """ Devuelve la categoría de filtro resultante. """
    #
    #     return self._tipo_filtro_result

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

    # def set_autocomplete(self, combo: QComboBox):
    #     """
    #     Configura el autocompletado del combo.
    #     :param combo: El QCOmboBox al que se le aplica el autocomplete.
    #     """
    #
    #     completer = QCompleter()
    #     completer.setModel(combo.model())
    #     completer.setCompletionMode(
    #         QCompleter.CompletionMode.PopupCompletion)
    #     completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
    #     combo.setCompleter(completer)

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            # Obtenemos la subcategoría de acuario
            tipo_filtro = self.get_tipo_filtro()
            return Result.success(tipo_filtro)
        else:
            return Result.failure("EL USUARIO CANCELÓ EL DIÁLOGO.")