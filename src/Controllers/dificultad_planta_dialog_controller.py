"""
Autor: Inigo Iturriagaetxebarria
Fecha: 12/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de comportamiento de fauna.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.dificultad_planta_controller import DificultadPlantaController
from Model.DAO.dificultad_plantas_dao import DificultadPlantaDAO
from Model.Entities.dificultad_planta_entity import DificultadPlantaEntity
from Services.Result.result import Result
from Views.Dialogs.dificultad_planta_dialog import DificultadPlantaDialog
from Views.Masters.dificultad_planta_view import DificultadPlantaView


class DificultadPlantaDialogController(DificultadPlantaController):
    """
    Controlador del cuadro de diálogo dificultad de mantenimiento de la
    planta.
    """

    def __init__(self,
                 view: DificultadPlantaDialog | DificultadPlantaView,
                 dao: DificultadPlantaDAO,
                 mod: DificultadPlantaEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de dificultad de planta.
        :param dao: DAO de dificultad de planta.
        :param mod: Modelo de dificultad de planta.
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
        self._comportamiento_result = DificultadPlantaEntity(
            id=res.value,
            num=None,
            nivel=self._view.frame.edit_nivel.value(),
            dificultad=self._view.frame.edit_dificultad.value(),
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
            dificultad_planta = self._get_dificultad()
            return Result.success(dificultad_planta)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
