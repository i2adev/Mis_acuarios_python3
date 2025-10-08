"""
Autor: Inigo Iturriagaetxebarria
Fecha: 03/10/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de marca comercial.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from result import Result
from subcategoria_Acuario_dialog import SubcategoriaAcuarioDialog
from subcategoria_acuario_controller import SubcategoriaAcuarioController
from subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from subcategoria_acuario_entity import SubcategoriaAcuarioEntity


class SubcategoriaAcuarioDialogController(SubcategoriaAcuarioController):
    """ Controlador del cuadro de diálogo marca comercial. """

    def __init__(self, view: SubcategoriaAcuarioDialog, dao: SubcategoriaAcuarioDAO,
                 mod: SubcategoriaAcuarioEntity, id_sa: int = None):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de subcategoría de acuario
        :param dao: DAO de la subcategoría de acuario
        :param mod: Modelo de la subcategoría de acuario
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llenamo los combos
        self._fill_combos()
        self._view.frame.combo_categoria_acuario.setCurrentIndex(id_sa)

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
        self._view.frame.button_insert_categoria_acuario.clicked.connect(
            self._open_categoria_acuario_dialog
        )

        # Comboboxes
        # self._view.frame.combo_categoria_acuario.currentIndexChanged.connect(
        #     self._combo_categoria_indexchanged
        # )

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
        self._subcategoria_acuario_result = SubcategoriaAcuarioEntity(
            id = res.value,
            num = None,
            id_cat = self._view.frame.combo_categoria_acuario.currentData(),
            subcategoria = self._view.frame.edit_subcategoria_acuario.text(),
            observaciones = self._view.frame.text_observaciones.toPlainText()
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
            subcategoria_acuario = self._get_subcategoria_acuario()
            return Result.success(subcategoria_acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")