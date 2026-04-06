"""
Autor: Inigo Iturriagaetxebarria
Fecha: 06/04/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción del sexo del animal.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox

from Controllers.sexo_animal_controller import SexoAnimalController
from Model.DAO.sexo_animal_dao import SexoAnimalDAO
from Model.Entities.sexo_animal_entity import SexoAnimalEntity
from Services.Result.result import Result
from Views.Dialogs.sexo_animal_dialog import SexoAnimalDialog
from Views.Masters.sexo_animal_view import SexoAnimalView


class SexoAnimalDialogController(SexoAnimalController):
    """ Controlador del cuadro de diálogo posición de planta en el acuario. """

    def __init__(self,
                 view: SexoAnimalDialog | SexoAnimalView,
                 dao: SexoAnimalDAO,
                 mod: SexoAnimalEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo del sexo del animal.
        :param dao: DAO de comportamiento del sexo del animal.
        :param mod: Modelo de comportamiento del sexo del animal.
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
        self._requerimiento_result = SexoAnimalEntity(
            id=res.value,
            num=None,
            sexo=self._view.frame.edit_sexo.value(),
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
            sexo = self._get_sexo()
            return Result.success(sexo)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
