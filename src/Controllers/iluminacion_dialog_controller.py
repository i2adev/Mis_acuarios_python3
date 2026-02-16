"""
Autor: Inigo Iturriagaetxebarria
Fecha: 08/10/2025
Comentarios:
    Controlador del cuadro de diálogo de inserción de urna.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.iluminacion_controller import IluminacionController
from Model.DAO.iluminacion_dao import IluminacionDAO
from Model.Entities.iluminacion_entity import IluminacionEntity
from Services.Result.result import Result
from Views.Dialogs.iluminacion_dialog import IluminacionDialog


class IluminacionDialogController(IluminacionController):
    """ Controlador del cuadro de diálogo marca comercial. """

    def __init__(self, view: IluminacionDialog, dao: IluminacionDAO,
                 mod: IluminacionEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de iluminación
        :param dao: DAO de la iluminación
        :param mod: Modelo de la iluminación
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
        self._view.frame.button_tipo_iluminacion.clicked.connect(
            self._open_tipo_iluminacion_dialog
        )
        self._view.frame.button_control_iluminacion.clicked.connect(
            self._open_control_iluminacion_dialog
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
        self._iluminacion_result = IluminacionEntity(
            id=res.value,
            num=None,
            id_tipo_iluminacion=self._view.frame.edit_modelo.text(),
            id_marca=int(self._view.frame.combo_marca.currentValue()),
            modelo=self._view.frame.edit_modelo.text(),
            num_serie=self._view.frame.edit_num_serie.text(),
            potencia=self._view.frame.edit_potencia.text(),
            flujo_luminico=self._view.frame.edit_flujo_luminoso.text(),
            temperatura=self._view.frame.edit_temperatura.text(),
            vida_util=self._view.frame.edit_vida_util.text(),
            longitud=self._view.frame.edit_longitud.text(),
            anchura=self._view.frame.edit_anchura.text(),
            id_control_iluminacion=int(
                self._view.frame.combo_tipo_control.currentData()),
            fecha_alta=int(
                self._view.frame.fecha_alta.dateTime().toSecsSinceEpoch()
            ),
            fecha_baja=int(
                self._view.frame.fecha_baja.dateTime().toSecsSinceEpoch()
            ),
            motivo_baja=self._view.frame.edit_motivo_baja.text(),
            espectro_completo=self._view.frame.check_espectro_completo.isChecked(),
            intensidad_regulable=self._view.frame.check_intensidad_regulable.isChecked(),
            descripcion=self._view.frame.text_descripcion.toPlainText()
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
            subcategoria_acuario = self._get_iluminacion()
            return Result.success(subcategoria_acuario)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
