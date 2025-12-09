"""
Autor: Inigo Iturriagaetxebarria
Fecha: 08/10/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de urna.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

import globals
from Controllers.proyecto_controller import ProyectoController
from CustomControls.nullable_date_edit import NullableDateEdit
from Model.DAO.proyecto_dao import ProyectoDAO
from Model.Entities.proyecto_entity import ProyectoEntity
from Services.Result.result import Result
from Views.Dialogs.proyecto_dialog import ProyectoDialog


class ProyectoDialogController(ProyectoController):
    """ Controlador del cuadro de diálogo proyecto. """

    def __init__(self, view: ProyectoDialog, dao: ProyectoDAO,
                 mod: ProyectoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de proyecto
        :param dao: DAO de proyecto
        :param mod: Modelo de proyecto
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llena los combos
        self._fill_combos()

        # Ocultamos los controles del motivo de cierre
        self._hide_layout(self._view.frame.layout_motivo_cierre)
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
            if isinstance(widget, NullableDateEdit):
                widget.edit_date.installEventFilter(self)

        # Botones
        self._view.button_accept.clicked.connect(self.dialog_accept)
        self._view.button_cancel.clicked.connect(self.dialog_cancel)
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
        self._proyecto_result = ProyectoEntity(
            id=res.value,
            num=None,
            id_usuario=globals.CURRENT_USER.id_usuario,
            nombre=self._view.frame.edit_nombre_proyecto.text(),
            id_estado=self._view.frame.combo_estado_proyecto.currentData(),
            fecha_inicio=int(
                self._view.frame.date_inicio.dateTime().toSecsSinceEpoch()
            ),
            fecha_fin=int(
                self._view.frame.date_fin.dateTime().toSecsSinceEpoch()
            ),
            motivo_cierre=self._view.frame.edit_motivo_cierre_proyecto.text(),
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
            proyecto = self._get_proyecto()
            return Result.success(proyecto)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
