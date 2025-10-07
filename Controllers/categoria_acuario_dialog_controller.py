"""
Autor: Inigo Iturriagaetxebarria
Fecha: 02/10/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de categoria de acuario.
"""
from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from categoria_acuario_controller import CategoriaAcuarioController, \
    CategoriaAcuarioDialog
from categoria_acuario_dao import CategoriaAcuarioDAO
from categoria_acuario_entity import CategoriaAcuarioEntity
from categoria_acuario_view import CategoriaAcuarioView
from result import Result


class CategoriaAcuarioDialogController(CategoriaAcuarioController):
    """ Controlador del cuadro de diálogo categoria de acuario. """

    def __init__(self, view: CategoriaAcuarioDialog | CategoriaAcuarioView, 
                 dao: CategoriaAcuarioDAO,
                 mod: CategoriaAcuarioEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de categoria de acuario.
        :param dao: DAO de la categoria de acuario.
        :param mod: Modelo de la categoria de acuario.
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
        self._categoria_acuario_result = CategoriaAcuarioEntity(
            id = res.value,
            num = None,
            categoria = self._view.frame.edit_categoria_acuario.text(),
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
            categoria_acuario = self._get_categoria_acuario()
            return Result.success(categoria_acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")