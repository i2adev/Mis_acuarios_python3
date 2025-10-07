"""
Autor: Inigo Iturriagaetxebarria
Fecha: 03/10/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de marca comercial.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from result import Result
from tipo_acuario_controller import TipoAcuarioController
from tipo_acuario_dao import TipoAcuarioDAO
from tipo_acuario_dialog import TipoAcuarioDialog
from tipo_acuario_entity import TipoAcuarioEntity


class TipoAcuarioDialogController(TipoAcuarioController):
    """ Controlador del cuadro de diálogo tipo de acuario. """

    def __init__(self, view: TipoAcuarioDialog, dao: TipoAcuarioDAO,
                 mod: TipoAcuarioEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de tipo de acuario
        :param dao: DAO del tipo de acuario
        :param mod: Modelo del tipo de acuario
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llenamo los combos
        self._fill_combos()

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
        self._view.frame.button_insert_tipo_acuario.clicked.connect(
            self._open_categoria_acuario_dialog
        )
        self._view.frame.button_insert_subtipo_acuario.clicked.connect(
            self._open_subcategoria_acuario_dialog
        )

        # Combos
        self._view.frame.button_insert_categoria_acuario.clicked.connect(
            self._open_categoria_acuario_dialog
        )

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
        self._tipo_acuario_result = TipoAcuarioEntity(
            id = res.value,
            num = None,
            id_cat_acuario = self._view.frame.combo_categoria_acuario.currentData(),
            id_subcat_acuario = self._view.frame
                    .combo_subcategoria_acuario.currentData(),
            observaciones = self._view.frame.text_descripcion.toPlainText()
                          if self._view.frame.text_descripcion.toPlainText()
                          else ""
        )

        # Aceptamos el diálogo
        self._view.accept()

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

    def show_modal(self) -> Result:
        """ Abre la ventava modal. """

        if self._view.exec():
            # Obtenemos la subcategoría de acuario
            tipo_acuario = self._get_tipo_acuario()
            return Result.success(tipo_acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")