"""
Autor: Inigo Iturriagaetxebarria
Fecha: 29/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de la posición de la 
    planta en el acuario.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox

from ModuloMaestro.Controllers.posicion_planta_acuario_controller import \
    PosicionPlantaAcuarioController
from ModuloMaestro.Model.DAO.posicion_planta_acuario_dao import \
    PosicionPlantaAcuarioDAO
from ModuloMaestro.Model.Entities.posicion_planta_acuario_entity import \
    PosicionPlantaAcuarioEntity
from Services.Result.result import Result
from ModuloMaestro.Views.Dialogs.posicion_planta_acuario_dialog import \
    PosicionPlantaAcuarioDialog
from ModuloMaestro.Views.Masters.posicion_pnalta_acuario_view import \
    PosicionPlantaAcuarioView


class PosicionPlantaAcuarioDialogController(PosicionPlantaAcuarioController):
    """ Controlador del cuadro de diálogo posición de planta en el acuario. """

    def __init__(self,
                 view: PosicionPlantaAcuarioDialog | PosicionPlantaAcuarioView,
                 dao: PosicionPlantaAcuarioDAO,
                 mod: PosicionPlantaAcuarioEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de la posición de la planta en el acuario.
        :param dao: DAO de comportamiento de la posición de la planta en el acuario.
        :param mod: Modelo de comportamiento de la posición de la planta en el acuario.
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
        self._posicion_result = PosicionPlantaAcuarioEntity(
            id=res.value,
            num=None,
            posicion=self._view.frame.edit_posicion.value(),
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
            posicion = self._get_posicion()
            return Result.success(posicion)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
