"""
Autor: Inigo Iturriagaetxebarria
Fecha: 03/10/2025
Commentarios:
    Controlador del cuadro de diálogo de inserción de marca comercial.
"""

from PyQt6.QtWidgets import QWidget, QMessageBox, QComboBox

from Services.Result.result import Result
from marca_comercial_controller import MarcaComercialController
from marca_comercial_dao import MarcaComercialDAO
from marca_comercial_dialog import MarcaComercialDialog
from marca_comercial_entity import MarcaComercialEntity
from pais_dao import PaisDAO


class MarcaComercialDialogController(MarcaComercialController):
    """ Controlador del cuadro de diálogo marca comercial. """

    def __init__(self, view: MarcaComercialDialog, dao: MarcaComercialDAO,
                 mod: MarcaComercialEntity):
        """
        Constructor base
        :param view: Cuadro de diálogo de inserción de marca comercial
        :param dao: DAO de la marca comercial
        :param mod: Modelo de la marca comercial
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llenamo los combos
        self._fill_combos()

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
        self._marca_comercial_result = MarcaComercialEntity(
            id = res.value,
            num = None,
            nombre_marca = self._view.frame.edit_marca.text(),
            direccion = self._view.frame.edit_direccion.text(),
            cod_postal = self._view.frame.edit_cod_postal.text(),
            poblacion = self._view.frame.edit_poblacion.text(),
            provincia = self._view.frame.edit_provincia.text,
            id_pais = self._view.frame.combo_pais.currentData(),
            observaciones = self._view.frame.text_observaciones.toPlainText()
                          if self._view.frame.text_observaciones.toPlainText()
                          else ""
        )

        # Aceptamos el diálogo
        self._view.accept()

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()
        
    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_pais()

    def _fill_combo_pais(self):
        """ Llena el combo de paises. """

        # Vaciamos el combo
        self._view.frame.combo_pais.clear()

        # Obtenemos los datos
        dao = PaisDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'PAISES'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_pais.addItem(ent.pais, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_pais)

        # Deseleccionamos el valor
        self._view.frame.combo_pais.setCurrentIndex(-1)
        
    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            # Obtenemos la subcategoría de acuario
            marca_comercial = self._get_marca_comercial()
            return Result.success(marca_comercial)
        else:
            return Result.failure("EL USUARIO CANCELO LA INSERCIÓN")