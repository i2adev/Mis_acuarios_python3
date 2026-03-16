"""
Autor: Inigo Iturriagaetxebarria
Fecha: 16/03/2026
Comentarios:
    Controlador del cuadro de diálogo de inserción de grupo taxonómico.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Controllers.grupo_taxonomico_controller import GrupoTaxonomicoController
from Model.DAO.grupo_taxonomico_dao import GrupoTaxonomicoDAO
from Model.Entities.grupo_taxonomico_entity import GrupoTaxonomicoEntity
from Services.Result.result import Result
from Views.Dialogs.grupo_taxonomico_dialog import GrupoTaxonomicoDialog
from Views.Masters.grupo_taxonomico_view import GrupoTaxonomicoView


class GrupoTaxonomicoDialogController(GrupoTaxonomicoController):
    """ Controlador del cuadro de diálogo grupo taxonómico. """

    def __init__(self,
                 view: GrupoTaxonomicoDialog | GrupoTaxonomicoView,
                 dao: GrupoTaxonomicoDAO,
                 mod: GrupoTaxonomicoEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de grupo taxonómico.
        :param dao: DAO de grupo taxonómico.
        :param mod: Modelo de grupo taxonómico.
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
        self._grupo_result = GrupoTaxonomicoEntity(
            id=res.value,
            num=None,
            grupo_taxo=self._view.frame.edit_grupo.value(),
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
            grupo = self._get_grupo()
            return Result.success(grupo)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")
