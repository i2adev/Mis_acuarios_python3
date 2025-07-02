"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/07/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad SUBCATEGORÍA
    DE ACUARIO.
"""

# Importaciones
from PyQt6.QtCore import qSetMessagePattern, Qt, QEvent
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QTextEdit, QPlainTextEdit, QMessageBox, \
    QTableView, QHeaderView, QComboBox, QCompleter

from Controllers.base_controller import BaseController
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.paginator import Paginator
from Model.DAO.subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.Entities.subcategoria_acuario_entity import SubcategoriaAcuarioEntity
from Services.Result.result import Result
from Services.Validators.categoria_acuario_validator import \
    CategoriaAcuarioValidator
from Services.Validators.subcategoria_acuario_validator import \
    SubcategoriaAcuarioValidator
from Views.subcategoria_Acuario_dialog import SubcategoriaAcuarioDialog
from Views.tipo_filtro_view import TipoFiltroView
from Views.table_menu_contextual import TableMenuContextual
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.TableModel.tipo_filtro_table_model import TipoFiltroTableModel
from Services.Validators.tipo_filtro_validator import TipoFiltroValidator

class SubcategoriaAcuarioDialogController(BaseController):
    """ Controlador del diálogo categoría de acuario. """

    def __init__(self):
        """ Constructor base """

        # Inicializamos la vista, la entidad y el dao
        self.__view = SubcategoriaAcuarioDialog(
            "INSERTAR SUBCATEGORÍA DE ACUARIO"
        )
        self.__mod = SubcategoriaAcuarioEntity()
        self.__dao = SubcategoriaAcuarioDAO()

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(self.__view)

        # Llenar combos
        self.fill_combos()

        # Inicializamos los eventos
        self.init_handlers()

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self.__view.exec():
            # Obtenemos la categoría de acuario
            categoria_acuario = self.get_subcategoria_Acuario()
            return Result.success(categoria_acuario)
        else:
            return Result.failure("NO SE HA PODIDO OBTENER LA ENTIDAD.")

    def init_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        # Inicializa los widgets de introducción de texto
        for widget in self.__view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)

        # Inizializa los botones
        self.__view.button_accept.clicked.connect(self.dialog_accept)
        self.__view.button_cancel.clicked.connect(self.dialog_cancel)

    def entity_configuration(self) -> SubcategoriaAcuarioEntity:
        """ Configura la entidad. """

        ent = SubcategoriaAcuarioEntity()

        if self.__view.frame.edit_id.text():
            ent.id = int(self.__view.frame.edit_id.text())
        else:
            ent.id = None

        ent.id_categoria = (self.__view.frame.combo_categoria_acuario
                            .currentData())
        ent.subcategoria = self.__view.frame.edit_subcategoria_acuario.text()
        ent.observaciones = self.__view.frame.text_observaciones.toPlainText()

        return ent

    def insert(self):
        """ Inserta un registro en la base de datos. """

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self.__dao.insert(ent)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        return Result.success(res.value)

    def dialog_accept(self):
        """ Se acepta el diálogo. """

        # Valida la vista
        res = self.validate_view()

        if not res.is_success:
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                res.error_msg
            )
            return

        # Insertamos el registro
        res = self.insert()

        if not res.is_success:
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                res.error_msg
            )

        # Configuramos la entidad
        self.subcategoria_acuario_result = SubcategoriaAcuarioEntity(
            id = res.value,
            num = None,
            id_cat= self.__view.frame.combo_categoria_acuario.currentData(),
            subcategoria = self.__view.frame.edit_subcategoria_acuario.text(),
            observaciones = self.__view.frame.text_observaciones.toPlainText()
                          if self.__view.frame.text_observaciones.toPlainText()
                          else None
        )

        # Aceptamos el diálogo
        self.__view.accept()

    def get_subcategoria_Acuario(self):
        """ Devuelve la categoría de filtro resultante. """

        return self.subcategoria_acuario_result

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self.__view.reject()

    def validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida la categoría de acuario
        res = SubcategoriaAcuarioValidator.ValidateCategoriaAcuario(
            self.__view.frame.combo_categoria_acuario
        )

        if not res.is_success:
            self.__view.frame.combo_categoria_acuario.setFocus()
            return res

        # Valida la subcategoría de acuario
        res = SubcategoriaAcuarioValidator.ValidateSubcategoriaAcuario(
            self.__view.frame.edit_subcategoria_acuario
        )

        if not res.is_success:
            self.__view.frame.edit_subcategoria_acuario.setFocus()
            return res

        # En caso de no haber errores
        return Result.success(1)

    def fill_combos(self):
        """ Llena los combos del formulario"""

        self.fill_combo_tipo()

    def fill_combo_tipo(self):
        """ Llena el combo de tipos de acuario. """

        # Vaciamos el combo
        self.__view.frame.combo_categoria_acuario.clear()

        # Obtenemos los datos
        dao = CategoriaAcuarioDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE FILTRO'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self.__view.frame.combo_categoria_acuario.addItem(ent.categoria, ent.id)

        # Establecemos el autocompletado
        self.set_autocomplete(self.__view.frame.combo_categoria_acuario)

        # Deseleccionamos el valor
        self.__view.frame.combo_categoria_acuario.setCurrentIndex(-1)

    def set_autocomplete(self, combo: QComboBox):
        """
        Configura el autocompletado del combo.

        :param combo: El QCOmboBox al que se le aplica el autocomplete.
        """

        completer = QCompleter()
        completer.setModel(combo.model())
        completer.setCompletionMode(
            QCompleter.CompletionMode.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        combo.setCompleter(completer)
