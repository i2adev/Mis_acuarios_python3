"""
Autor: Inigo Iturriagaetxebarria
Fecha: 19/12/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de tipo de iluminación.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.tipo_iluminacion_controller import TipoIluminacionController
from Model.DAO.tipo_iluminacion_dao import TipoIluminacionDAO
from Model.Entities.tipo_iluminacion_entity import TipoIluminacionEntity
from Services.Result.result import Result
from Views.Dialogs.tipo_iluminacion_dialog import TipoIluminacionDialog


class TipoIluminacionDialogController(TipoIluminacionController):
    """ Controlador del cuadro de diálogo tipo de filtro. """

    def __init__(self, view: TipoIluminacionDialog, dao: TipoIluminacionDAO,
                 mod: TipoIluminacionEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de tipo de filtro
        :param dao: DAO del tipo de iluminación
        :param mod: Modelo del tipo de iluminación
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
        self._tipo_filtro_result = TipoIluminacionEntity(
            id=res.value,
            num=None,
            tipo_iluminacion=self._view.frame.edit_tipo_iluminacion.text(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
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
