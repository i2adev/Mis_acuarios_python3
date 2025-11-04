"""
Autor: Inigo Iturriagaetxebarria
Fecha: 29/09/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de tipo de filtro.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.estado_proyecto_controller import EstadoProyectoController
from Model.DAO.estado_proyecto_dao import EstadoProyectoDAO
from Model.Entities.estado_proyecto_entity import EstadoProyectoEntity
from Services.Result.result import Result
from Views.Dialogs.estado_proyecto_dialog import EstadoProyectoDialog


class EstadoProyectoDialogController(EstadoProyectoController):
    """ Controlador del cuadro de diálogo tipo de filtro. """

    def __init__(self, view: EstadoProyectoDialog, dao: EstadoProyectoDAO,
                 mod: EstadoProyectoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de estado de proyecto
        :param dao: DAO del estado de proyecto
        :param mod: Modelo del estado de proyecto
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
        self._tipo_filtro_result = EstadoProyectoEntity(
            id=res.value,
            num=None,
            estado=self._view.frame.edit_estado_proyecto.text(),
            descripcion=self._view.frame.text_observaciones.toPlainText()
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
            estado_proyecto = self._get_estado_proyecto()
            return Result.success(estado_proyecto)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
