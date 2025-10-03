from PyQt6.QtWidgets import QWidget, QMessageBox

from categoria_incidencia_controller import CategoriaIncidenciaController
from categoria_incidencia_dao import CategoriaIncidenciaDAO
from categoria_incidencia_dialog import CategoriaIncidenciaDialog
from categoria_incidencia_entity import CategoriaIncidenciaEntity
from result import Result


class CategoriaIncidenciaDialogController(CategoriaIncidenciaController):
    """ """
    def __init__(self, view: CategoriaIncidenciaDialog, dao: CategoriaIncidenciaDAO,
                 mod: CategoriaIncidenciaEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de categoria de incidencia
        :param dao: DAO de categoría de incidencia
        :param mod: Modelo de categoria de incidencia
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
        self._categoria_incidencia_result = CategoriaIncidenciaEntity(
            id = res.value,
            num = None,
            categoria_incidencia = self._view.frame
                                            .edit_categoria_incidencia.text(),
            observaciones = self._view.frame.text_descripcion.toPlainText()
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
            tipo_filtro = self._get_categoria_incidencia()
            return Result.success(tipo_filtro)
        else:
            return Result.failure("EL USUARIO CANCELÓ EL DIÁLOGO.")