"""
Autor: Inigo Iturriagaetxebarria
Fecha: 29/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de la posición de la
    planta en el acuario.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox

from ModuloMaestro.Controllers.requerimiento_co2_controller import RequerimientoCO2Controller
from ModuloMaestro.Model.DAO.requerimiento_co2_dao import RequerimientoCO2DAO
from ModuloMaestro.Model.Entities.requerimiento_co2_entity import \
    RequerimientoCO2Entity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.requerimiento_co2_dialog import RequerimientoCO2Dialog
from ModuloMaestro.Views.Masters.requerimiento_co2_view import RequerimientoCO2View


class RequerimientoCO2DialogController(RequerimientoCO2Controller):
    """ Controlador del cuadro de diálogo posición de planta en el acuario. """

    def __init__(self,
                 view: RequerimientoCO2Dialog | RequerimientoCO2View,
                 dao: RequerimientoCO2DAO,
                 mod: RequerimientoCO2Entity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción del requerimiento de CO2.
        :param dao: DAO de comportamiento de la posición del requerimiento de CO2.
        :param mod: Modelo de comportamiento de la posición del requerimiento de CO2.
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
        self._requerimiento_result = RequerimientoCO2Entity(
            id=res.value,
            num=None,
            requerimiento=self._view.frame.edit_requerimiento.value(),
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
            requerimiento = self._get_requerimiento()
            return Result.success(requerimiento)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
