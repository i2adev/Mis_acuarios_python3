"""
Autor: Inigo Iturriagaetxebarria
Fecha: 08/10/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de urna.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.acuario_controller import AcuarioController
from CustomControls.nullable_date_edit import NullableDateEdit
from Model.DAO.acuario_dao import AcuarioDAO
from Model.Entities.acuario_entity import AcuarioEntity
from Services.Result.result import Result
from Views.Dialogs.acuario_dialog import AcuarioDialog


class AcuarioDialogController(AcuarioController):
    """ Controlador del cuadro de diálogo proyecto. """

    def __init__(self, view: AcuarioDialog, dao: AcuarioDAO,
                 mod: AcuarioEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de acuario
        :param dao: DAO de acuario
        :param mod: Modelo de acuario
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llenamo los combos
        self._fill_combos()

        # Ocultamos los layouts
        self._hide_layout(self._view.frame.layout_id)
        self._hide_layout(self._view.frame.layout_color)

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
        self._proyecto_result = AcuarioEntity(
            id=res.value,
            id_proyecto=self._view.frame.combo_proyecto.text(),
            num=None,
            cod_color=self._view.frame.edit_cod_color.text(),
            nombre=self._view.frame.edit_nombre_acuarfio.text(),
            id_urna=self._view.frame.combo_urna.currentData(),
            id_tipo=self._view.frame.combo_tipo_acuario.currentData(),
            volumen_neto=self._view.frame.edit_volumen_neto.text(),
            fecha_montaje=int(
                self._view.frame.fecha_montaje.dateTime().toSecsSinceEpoch()
            ),
            fecha_inicio_ciclado=int(
                self._view.frame.fecha_inicio_ciclado.dateTime().toSecsSinceEpoch()
            ),
            fecha_fin_ciclado=int(
                self._view.frame.fecha_fin_ciclado.dateTime().toSecsSinceEpoch()
            ),
            ubicacion_acuario=self._view.frame.edit_ubicacion_acuario.text(),
            fecha_desmontaje=int(
                self._view.frame.fecha_desmontaje.dateTime().toSecsSinceEpoch()
            ),
            motivo_desmontaje=self._view.frame.edit_motivo_desmontaje.text(),
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
            acuario = self._get_proyecto()
            return Result.success(acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
