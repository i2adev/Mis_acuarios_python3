"""
Autor: Inigo Iturriagaetxebarria
Fecha: 06/10/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de subcategoria de
    incidencia.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.subcategoria_incidencia_controller import \
    SubcategoriaIncidenciaController
from Model.DAO.subcategoria_incidencia_dao import SubcategoriaIncidenciaDAO
from Model.Entities.subcategoria_incidencia_entity import \
    SubcategoriaIncidenciaEntity
from Services.Result.result import Result
from Views.Dialogs.subcategoria_incidencia_dialog import \
    SubcategoriaIncidenciaDialog


class SubcategoriaIncidenciaDialogController(SubcategoriaIncidenciaController):
    """ Controlador del cuadro de diálogo marca comercial. """

    def __init__(self, view: SubcategoriaIncidenciaDialog,
                 dao: SubcategoriaIncidenciaDAO,
                 mod: SubcategoriaIncidenciaEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de subcategoría de
        incidencia
        :param dao: DAO de la subcategoría de incidencia
        :param mod: Modelo de la subcategoría de incidencia
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
        self._view.frame.button_insert_categoria_incidencia.clicked \
            .connect(self.open_categoria_incidencia_dialog)

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
        self._subcategoria_incidencia_result = SubcategoriaIncidenciaEntity(
            id=res.value,
            num=None,
            id_categoria=self._view.frame.combo_categoria_incidencia.currentData(),
            subcategoria=self._view.frame.edit_subcategoria_incidencia.text(),
            observaciones=self._view.frame.text_descripcion.toPlainText()
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
            subcategoria_acuario = self._get_marca_comercial()
            return Result.success(subcategoria_acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
