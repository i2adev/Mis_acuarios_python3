"""
Autor: Inigo Iturriagaetxebarria
Fecha: 15/12/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de categoría de 
    equipamiento..
"""

from PyQt6.QtWidgets import QComboBox, QMessageBox, QWidget

from Controllers.categoria_equipamiento_controller import \
    CategoriaEquipamientoController
from Model.DAO.categoria_equipamiento_dao import CategoriaEquipamientoDAO
from Model.Entities.categoria_equipamiento_entity import \
    CategoriaEquipamientoEntity
from Services.Result.result import Result
from Views.Dialogs.cattegoria_equipamiento_dialog import \
    CategoriaEquipamientoDialog


class CategoriaEquipamientoDialogController(CategoriaEquipamientoController):
    """ Controlador del cuadro de diálogo de categoría de equipamiento. """

    def __init__(self, view: CategoriaEquipamientoDialog,
                 dao: CategoriaEquipamientoDAO,
                 mod: CategoriaEquipamientoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de categoría de equipamiento
        :param dao: DAO de categoría de equipamiento
        :param mod: Modelo de categoría de equipamiento
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
        self._cat_equipamiento_result = CategoriaEquipamientoEntity(
            id=res.value,
            num=None,
            categoria=self._view.frame.edit_categoria_equipamiento.text(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
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
            cat_equipamiento = self._get_cat_equipamiento()
            return Result.success(cat_equipamiento)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
