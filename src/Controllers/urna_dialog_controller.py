"""
Autor: Inigo Iturriagaetxebarria
Fecha: 08/10/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de urna.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.urna_controller import UrnaController
from Model.DAO.urna_dao import UrnaDAO
from Model.Entities.urna_entity import UrnaEntity
from Services.Result.result import Result
from Views.Dialogs.urna_dialog import UrnaDialog


class UrnaDialogController(UrnaController):
    """ Controlador del cuadro de diálogo marca comercial. """

    def __init__(self, view: UrnaDialog, dao: UrnaDAO,
                 mod: UrnaEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de urna
        :param dao: DAO de la urna
        :param mod: Modelo de la urna
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llena los combos
        self._fill_combos()

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
        self._view.frame.button_insert_marca.clicked.connect(
            self._open_marca_comercial_dialog
        )
        self._view.frame.button_insert_material.clicked.connect(
            self._open_material_urna_dialog
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
        self._urna_result = UrnaEntity(
            id=res.value,
            num=None,
            id_marca=self._view.frame.combo_marca.currentData(),
            modelo=self._view.frame.edit_modelo.text(),
            anchura=self._view.frame.edit_ancho.text(),
            profundidad=self._view.frame.edit_profundo.text(),
            altura=self._view.frame.edit_alto.text(),
            grosor_cristal=self._view.frame.edit_grosor.text(),
            volumen_tanque=self._view.frame.edit_volumen.text(),
            id_material=self._view.frame.combo_material.currentData(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
            if self._view.frame.text_descripcion.toPlainText()
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
            subcategoria_acuario = self._get_urna()
            return Result.success(subcategoria_acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
