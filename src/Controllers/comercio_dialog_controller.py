"""
Autor: Inigo Iturriagaetxebarria
Fecha: 19/12/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de comercio.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.comercio_conttroller import ComercioController
from Model.DAO.comercio_dao import ComercioDAO
from Model.Entities.comercio_entity import ComercioEntity
from Services.Result.result import Result
from Views.Dialogs.comercio_dialog import ComercioDialog


class ComercioDialogController(ComercioController):
    """ Controlador del cuadro de diálogo de comercio """

    def __init__(self, view: ComercioDialog, dao: ComercioDAO,
                 mod: ComercioEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción del comercio
        :param dao: DAO del comercio
        :param mod: Modelo del comercio
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
        self._tipo_filtro_result = ComercioEntity(
            id=res.value,
            num=None,
            nombre_comercio=self._view.frame.edit_comercio.text(),
            direccion=self._view.frame.edit_direccion.text(),
            cod_postal=self._view.frame.edit_cod_postal.text(),
            poblacion=self._view.frame.edit_poblacion.text(),
            provincia=self._view.frame.edit_provincia.text(),
            id_pais=int(self._view.frame.combo_pais.currentData()),
            observaciones=self._view.frame.text_observaciones.toPlainText()
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
            comercio = self._get_comercio()
            return Result.success(comercio)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
