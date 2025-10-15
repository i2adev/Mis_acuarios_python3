"""
Autor: Inigo Iturriagaetxebarria
Fecha: 29/09/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de tipo de filtro.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Services.Result.result import Result
from material_urna_controller import MaterialUrnaController
from material_urna_dao import MaterialUrnaDAO
from material_urna_dialog import MaterialUrnaDialog
from material_urna_entity import MaterialUrnaEntity


class MaterialUrnaDialogController(MaterialUrnaController):
    """ Controlador del cuadro de diálogo tipo de filtro. """

    def __init__(self, view: MaterialUrnaDialog, dao: MaterialUrnaDAO,
                 mod: MaterialUrnaEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de material de urna
        :param dao: DAO de material de urna
        :param mod: Modelo del material de urna
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
        self._material_urna_result = MaterialUrnaEntity(
            id = res.value,
            num = None,
            material = self._view.frame.edit_material.text(),
            descripcion = self._view.frame.text_descripcion.toPlainText()
                          if self._view.frame.text_descripcion.toPlainText()
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
            material_urna = self._get_material_urna()
            return Result.success(material_urna)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")