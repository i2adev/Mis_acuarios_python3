"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      20/07/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad TIPO DE ACUARIO.
"""


# Importaciones
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QWidget, QMessageBox, QTableView, QHeaderView,
                             QCompleter, QComboBox)

from Controllers.base_controller import BaseController
from Controllers.categoria_acuario_controller import \
    CategoriaAcuarioDialogController
from Controllers.subcategoria_acuario_controller import \
    SubcategoriaAcuarioDialogController
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.paginator import Paginator
from Model.DAO.subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.TableModel.tipo_acuario_table_model import TipoAcuarioTableModel
from Services.Result.result import Result
from Services.Validators.tipo_acuario_validator import TipoAcuarioValidator
from Views.categoria_acuario_dialog import CategoriaAcuarioDialog
from Views.subcategoria_Acuario_dialog import SubcategoriaAcuarioDialog
from Views.table_menu_contextual import TableMenuContextual
from Views.tipo_acuario_dialog import TipoAcuarioDialog
from Views.tipo_acuario_view import TipoAcuarioView


class TipoAcuarioDialogController(BaseController):
    """ Controlador del diálogo subcategoría de acuario. """

    def __init__(self, view: TipoAcuarioDialog, dao: SubcategoriaAcuarioDAO,
                 mod: TipoAcuarioEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista tipo CategoríaAcuario
        :param dao: DAO de la entidad SubcategoriaAcuarioDAO
        :param mod: Modelo de la entidad TipoAcuarioEntity
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Llenamo los combos
        self.fill_combos()

        # Inicializamos los eventos
        self.init_basic_handlers()

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            self._view.frame.combo_categoria_acuario.setCurrentIndex(self.ix_ta)

            # Obtenemos la subcategoría de acuario
            tipo_acuario = self.get_tipo_acuario()
            return Result.success(tipo_acuario)
        else:
            return Result.failure("NO SE HA PODIDO OBTENER LA ENTIDAD.")

    def init_basic_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """
        self.init_imput_handlers()

        if isinstance(self._view, TipoAcuarioDialog):
            self.init_dialog_handlers()

    def init_dialog_handlers(self):
        """ Inicializa los controles del cuadro de diálogo. """

        # Botones
        self._view.button_accept.clicked.connect(self.dialog_accept)
        self._view.button_cancel.clicked.connect(self.dialog_cancel)

    def init_imput_handlers(self):
        """ Inicializa los controles de entrada. """

        # Controles de entrada de texto
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)

        # Comboboxes
        self._view.frame.combo_categoria_acuario.currentIndexChanged.connect(
            self.combo_categoria_indexchanged
        )

        # Botones
        self._view.frame.button_insert_tipo_acuario.clicked.connect(
            self.open_categoria_acuario_dialog
        )
        self._view.frame.button_insert_subtipo_acuario.clicked.connect(
            self.open_subcategoria_acuario_dialog
        )

    def entity_configuration(self) -> TipoAcuarioEntity:
        """ Configura la entidad. """

        ent = TipoAcuarioEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.id_categoria_acuario = self._view.frame.combo_categoria_acuario.currentData()
        ent.id_subcategoria_acuario = (self._view.frame
                                       .combo_subcategoria_acuario.currentData())
        ent.observaciones = self._view.frame.text_observaciones.toPlainText()

        return ent

    def insert(self) -> Result:
        """ Inserta un registro en la base de datos. """

        # Validamos el formulario
        val = self.validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self._dao.insert(ent)
        if not res.is_success:
            return res

        # Limpiamos el formulario
        self._clean_view()

        return Result.success(res.value)

    def validate_view(self):
        """ Valida el formulario. """

        # Valida el tipo de acuario
        res = TipoAcuarioValidator.validate_categoria_acuario(
            self._view.frame.combo_categoria_acuario
        )

        if not res.is_success:
            self._view.frame.combo_categoria_acuario.setFocus()
            return res

        # Valida el subtipo de acuario
        res = TipoAcuarioValidator.ValidateSubcategoriaAcuario(
            self._view.frame.combo_subcategoria_acuario
        )

        if not res.is_success:
            self._view.frame.combo_subcategoria_acuario.setFocus()
            return res

        return Result.success(1)

    def dialog_accept(self):
        """ Se acepta el diálogo. """

        # Insertamos el registro
        res = self.insert()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Configuramos la entidad
        self.tipo_acuario_result = TipoAcuarioEntity(
            id = res.value,
            num = None,
            id_ta_acuario = self._view.frame.combo_categoria_acuario.currentData(),
            id_subcat_acuario = self._view.frame
                    .combo_subcategoria_acuario.currentData(),
            observaciones = self._view.frame.text_observaciones.toPlainText()
                          if self._view.frame.text_observaciones.toPlainText()
                          else None
        )

        # Aceptamos el diálogo
        self._view.accept()

    def get_tipo_acuario(self):
        """ Devuelve la categoría de filtro resultante. """

        return self.tipo_acuario_result

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

    def fill_combos(self):
        """ Llena los combos del formulario"""

        self.fill_combo_categoria()

    def fill_combo_categoria(self):
        """ Llena el combo de tipos de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_categoria_acuario.clear()

        # Obtenemos los datos
        dao = CategoriaAcuarioDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE FILTRO'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_categoria_acuario.addItem(ent.categoria,
                                                              ent.id)

        # Establecemos el autocompletado
        self.set_autocomplete(self._view.frame.combo_categoria_acuario)

        # Deseleccionamos el valor
        self._view.frame.combo_categoria_acuario.setCurrentIndex(-1)

    def fill_combo_subcategoria(self, id_ta: int):
        """ Llena el combo de subcategoría de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_subcategoria_acuario.clear()

        # Condiciones de salida
        if id_ta == -1:
            return

        # Obtenemos los datos
        dao = SubcategoriaAcuarioDAO()
        lista = dao.get_list_combo_by_categoria(id_ta)
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'SUBCATEGORÍAS DE ACUARIO'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_subcategoria_acuario.addItem(ent.subcategoria, ent.id)

        # Establecemos el autocompletado
        self.set_autocomplete(self._view.frame.combo_categoria_acuario)

        # Deseleccionamos el valor
        self._view.frame.combo_subcategoria_acuario.setCurrentIndex(-1)



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

    def combo_categoria_indexchanged(self):
        """ Se ejecuta cuando el índice del combo cambia. """

        # Cuando en el combo categoría se limpia, se limpia a su vez el combo de
        # subcategoría
        if self._view.frame.combo_categoria_acuario.currentIndex() == -1:
            self._view.frame.combo_subcategoria_acuario.clear()
            return

        # Obtenemos el dato a cargar
        data = self._view.frame.combo_categoria_acuario.currentData()

        # Cargamos el combo subcategoría
        self.fill_combo_subcategoria(data)

    def open_subcategoria_acuario_dialog(self):
        """ Abrimos el diálogo de subcategoria de acuario. """

        # Condiciones de salida
        data = self._view.frame.combo_categoria_acuario.currentData()
        if not data:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                """
                NO HAY NINGUNA CATEGORÍA SELECCIONADA.
                SELECCIONE PRIMERO UNA CATEGFORÍA.
                """
            )
            return

        # Configuramos el CONTROLADOR
        ix_cat = self._view.frame.combo_categoria_acuario.currentIndex()
        view = SubcategoriaAcuarioDialog("INSERTAR SUBCATEGORÍA")
        dao = SubcategoriaAcuarioDAO()
        mod = TipoAcuarioEntity()

        ctrl = SubcategoriaAcuarioDialogController(view, dao, mod, ix_cat)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_subcategoria_acuario

        self.fill_combo_subcategoria(data)
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def open_categoria_acuario_dialog(self):
        """ Abrimos el diálogo de categoria de acuario. """

        view = CategoriaAcuarioDialog(
            "INSERTAR CATEGORÍA DE ACUARIO"
        )
        mod = CategoriaAcuarioEntity()
        dao = CategoriaAcuarioDAO()

        ctrl = CategoriaAcuarioDialogController(view, dao, mod)
        res = ctrl.show_modal()

        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_categoria_acuario

        self.fill_combo_categoria()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

class TipoAcuarioController(TipoAcuarioDialogController):
    """ Controlador del formulario maestro de subcategoría de acuario. """

    def __init__(self, view: TipoAcuarioView, dao: TipoAcuarioDAO,
                 mod: TipoAcuarioEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista tipo acuario
        :param dao: DAO de la entidad tipo de acuario
        :param mod: Modelo de la entidad tipo de acuario
        """

        # Constructor base
        super().__init__(view, dao, mod)

        # Inicializamos el paginador
        self._pag = Paginator("VISTA_TIPOS_ACUARIO", 5)
        self._pag.initialize_paginator()

        # Llenamos la tabla
        self.load_tableview()
        self.configure_table_foot()

        # Inicializamos los eventos
        self.init_master_handlers()

    def load_tableview(self):
        """ Gestiona los datos para llenar la tabla. """

        self.fill_tableview(self._view.data_table, self._pag.current_data)
        self._configure_table(self._view.data_table)

    def show(self):
        """ Abre la vista """

        self._view.show()

    def init_master_handlers(self):
        """
        Inicializa los eventos de los widgets del formulario maestro.
        """

        # Inizializa los botones
        self._view.button_insert.clicked.connect(self.button_insert_click)
        self._view.button_update.clicked.connect(self.button_update_click)
        self._view.button_load.clicked.connect(self.button_load_click)
        self._view.button_delete.clicked.connect(self.button_delete_click)
        self._view.button_clean.clicked.connect(lambda: self._clean_view())
        self._view.button_next.clicked.connect(self.next_page)
        self._view.button_prev.clicked.connect(self.previous_page)
        self._view.button_first.clicked.connect(self.first_page)
        self._view.button_last.clicked.connect(self.last_page)
        self._view.button_close.clicked.connect(
            lambda: self._view.close()
        )
        # Inicializamos los combos
        self._view.combo_select_page.currentIndexChanged.connect(
            self.combo_page_indexchanged
        )
        # Eventos de la tabla
        self._view.data_table.customContextMenuRequested.connect(
            self.show_context_menu
        )

    def combo_page_indexchanged(self, event: QEvent):
        """
        Se ejecuta cuando el índice del combo de selección de página.
        """

        page = self._view.combo_select_page.currentData()

        # Condiciones de salida
        if page is None:
            return

        # Configuración de salida
        self._pag.current_page = page
        self._pag.current_data = self._pag.get_paged_list(self._pag.current_page)
        self.load_tableview()

    def show_context_menu(self, position):
        """ Muestra el menú contextual de la tabla. """

        # Obtiene el indice de la fila
        index = self._view.data_table.indexAt(position)

        # Si el índice no es valido
        if not index.isValid():
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                "DEBES PULSAR SOBRE UN REGISTRO DE LA TABLA."
            )
            return

        # Muestra el menú
        menu = TableMenuContextual(self._view.data_table)

        # Creamos el menú
        action_cargar = QAction("CARGAR REGISTRO", self)
        action_cargar.triggered.connect(self.action_cargar)
        action_eliminar = QAction("ELIMINAR REGISTRO", self)
        action_eliminar.triggered.connect(self.action_eliminar)

        # Armamos el menú
        menu.addAction(action_cargar)
        menu.addAction(action_eliminar)

        menu.exec(self._view.data_table.viewport().mapToGlobal(position))

    def action_eliminar(self, event):
        """ Elimina el registro desde el menú contextual"""

        # Carga el modelo de la fila seleccionada
        selection_model = self._view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                "ANTES DE ELIMINAR UN REGISTRO, DEBES "
                "SELECCIONAR UN REGISTRO EN LA TABLA."
            )
            return

        # Configuramos la fila
        index = selection_model.currentIndex()
        fila = index.row()
        modelo = self._view.data_table.model()

        # Lee los datos del modelo
        id_tipo = modelo.index(fila, 0).data()
        pagina_actual = self._view.combo_select_page.currentData()
        paginator_pages = self._pag.total_pages

        # Elimina el registro
        res = self.delete(id_tipo)

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Configurar paginador
        self._pag.initialize_paginator()

        # Configuramos el pie de tabla
        if paginator_pages > self._pag.total_pages:
            # Eliminamos la última página del combo de paginación
            self._view.combo_select_page.removeItem(self._pag.total_pages)
            self._view.label_total_pages.setText(str(self._pag.total_pages))

        # Establecemos la página actual
        if pagina_actual > self._pag.total_pages:
            self._view.combo_select_page.setCurrentIndex(
                self._pag.total_pages - 1
            )
            pagina_actual -= 1
        else:
            self._view.combo_select_page.setCurrentIndex(pagina_actual - 1)

        self._view.combo_select_page.setCurrentIndex(-1)
        self._view.combo_select_page.setCurrentIndex(pagina_actual - 1)

    def action_cargar(self, event):
        """ Carga un registro desde el menú contextual. """

        self.load_record()

    def button_delete_click(self, event):
        """ Controla el clic en el botón eliminar. """

        # Sí tenemos un registro cargado
        if not self._view.frame.edit_id.text():
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                "DEBES SELECCIONAR UN REGISTRO DE LA "
                "TABLA ANTES DE ELIMINARLO."
            )
            return

        # Obtener el ID desde el cuadro de texto id_parent
        id_row = int(self._view.frame.edit_id.text())
        pagina_actual = self._view.combo_select_page.currentData()
        paginator_pages = self._pag.total_pages

        # Insertar el registro
        res = self.delete(id_row)

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Configurar paginator
        self._pag.initialize_paginator()

        # Configuramos el pie de tabla
        if paginator_pages > self._pag.total_pages:
            # Eliminamos la última página del combo de paginación
            self._view.combo_select_page.removeItem(self._pag.total_pages)
            self._view.label_total_pages.setText(str(self._pag.total_pages))

        # Establecemos la página actual
        if pagina_actual > self._pag.total_pages:
            self._view.combo_select_page.setCurrentIndex(
                self._pag.total_pages - 1
            )
            pagina_actual -= 1
        else:
            self._view.combo_select_page.setCurrentIndex(pagina_actual - 1)

        self._view.combo_select_page.setCurrentIndex(-1)
        self._view.combo_select_page.setCurrentIndex(pagina_actual - 1)

    def button_load_click(self, event):
        """ Controla el clic del boton de cargar. """

        self.load_record()

    def button_update_click(self, event):
        """ Controla el clic del botón actualizar. """

        # Valida el formulario
        val = self.validate_view()

        if not val.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                val.error_msg
            )
            self._view.frame.edit_categoria_acuario.setFocus()
            return


        # Actualiza el registro
        res = self.update()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )

        # Configuramos el paginador
        self._pag.initialize_paginator()

        # # Establecemos la página actual
        self._view.combo_select_page.setCurrentIndex(-1)

        # Seleccionamos el último registro utilizado
        self.configure_table_after_crud(res.value)

    def configure_table_after_crud(self, id_: int):
        """
        Configura la tabla tras una operación de crud, seleccionando el último
        registro insertado, actualizado.
        """

        # Seleccionamos la página en la que se encuentra el registro
        num_reg = next(x.num for x in self._pag.total_data if x.id == id_)
        num_pag =  self._pag.get_page_number_by_num(num_reg)
        self._view.combo_select_page.setCurrentIndex(num_pag - 1)

        # Selecciona la última fila
        self._select_row_by_id(self._view.data_table, id_)

    def button_insert_click(self, event):
        """ Controla el clic del botón insertar. """

        # Insertamos el registro
        res = self.insert()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Obtenemos los datos de paginación actuales
        pagitator_pages = self._pag.total_pages

        # Configura el paginador
        self._pag.initialize_paginator()

        # Comprobamos si al añadir un registro se ha aumentado el número
        # de páginas totales
        if self._pag.total_pages > pagitator_pages:
            self._view.combo_select_page.addItem(
                str(self._pag.total_pages),
                self._pag.total_pages
            )
            self._view.label_total_pages.setText(
                str(self._pag.total_pages)
            )

        self.configure_table_after_crud(res.value)

    def fill_tableview(self, table: QTableView,
                       data: list[CategoriaAcuarioEntity]):
        """ Carga los datos en la tabla. """

        tv_model = TipoAcuarioTableModel(data)
        table.setModel(tv_model)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()

    # def _configure_table(self, table: QTableView):
    #     """ Configura l atabla de datos. """
    #
    #     # Selecciona un afila entera
    #     table.setSelectionBehavior(
    #         QTableView.SelectionBehavior.SelectRows)
    #
    #     # Solo se puede seleccionar uan fila
    #     table.setSelectionMode(
    #         QTableView.SelectionMode.SingleSelection)
    #
    #     # Color de las filas alternadas
    #     table.setAlternatingRowColors(True)
    #
    #     # Oculta las líneas de la tabla
    #     table.setShowGrid(False)
    #
    #     # Elimina el tabulador
    #     table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    #
    #     # Ocultar la columna ID (columna 0)
    #     table.setColumnHidden(0, True)
    #
    #     # Hacer que la columna de observaciones (columna 3) use el espacio
    #     # restante
    #     header = table.horizontalHeader()
    #     header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
    #
    #     # Mostrar puntos suspensivos si el texto no cabe
    #     table.setTextElideMode(Qt.TextElideMode.ElideRight)

    def spell_check(self):
        """ No aplicable. """
        pass

    def update(self) -> Result:
        """ Actualiza el registro en la base de datos. """
        # Valida el formulario
        val = self.validate_view()

        if not val.is_success:
            self._view.frame.edit_categoria_acuario.setFocus()
            return val

        # Configura la entidad
        ent = self.entity_configuration()

        # Actualiza el registro
        res = self._dao.update(ent)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()
        self.configure_table_after_crud(res.value)

        return Result.success(ent.id)

    def load_record(self) -> Result:
        """ Carga el registro en el formulario. """

        # Carga el modelo de la fila seleccionada
        selection_model = self._view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            return Result.failure(
                "ANTES DE CARGAR UN REGISTRO, DEBES "
                "SELECCIONAR UN REGISTRO EN LA TABLA."
            )

        # Configuramos la fila
        index = selection_model.currentIndex()
        fila = index.row()
        modelo = self._view.data_table.model()

        # Lee los datos del modelo
        id_ta = modelo.index(fila, 0).data()
        categoria = modelo.index(fila, 2).data()  # La columna 1 es el
                                                    # númer correlativo.
        subcategoria = modelo.index(fila, 3).data()
        observaciones = modelo.index(fila, 4).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ta) if id_ta is not None else ""
        )

        self._view.frame.combo_categoria_acuario.setCurrentIndex(
            self._view.frame.combo_categoria_acuario.findText(categoria)
        )

        self._view.frame.combo_subcategoria_acuario.setCurrentIndex(
            self._view.frame.combo_subcategoria_acuario.findText(subcategoria)
        )

        self._view.frame.text_observaciones.setPlainText(
            str(observaciones) if observaciones is not None else ""
        )

        return Result.success(id_ta)

    def delete(self, id_: int) -> Result:
        """ Elimina un registro de la base de datos.

            Parámetros:
            ID: Id del registro a eliminar.
        """

        # Solicitamos doble confirmación
        res = QMessageBox.question(
            self._view,
            self._view.window_title,
            "¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        res = QMessageBox.question(
            self._view,
            self._view.window_title,
            "R E P I T O\n¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        # Elimina el registro
        res = self._dao.delete(id_)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()

        return Result.success(id_)

    def configure_table_foot(self):
        """ Configura el pie de la tabla. """

        self._view.label_total_pages.setText(str(self._pag.total_pages))
        self.fill_combo_page()

    def next_page(self, event: QEvent) -> None:
        """ Pasa a la siguiente página de la tabla. """

        page_to = self._view.combo_select_page.currentData() + 1

        if page_to > self._pag.total_pages:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "SE HA LLEGADO A LA ÚLTIMA PÁGINA"
            )
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def previous_page(self, event: QEvent) -> None:
        """ Pasa a la anterior página de la tabla. """

        page_to = self._view.combo_select_page.currentData() - 1

        if page_to < 1:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "SE HA LLEGADO A LA PRIMERA PÁGINA"
            )
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def first_page(self, event: QEvent) -> None:
        """ Pasa a la primera página de la tabla. """

        page_to = 1

        if self._pag.current_page == 1:
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def last_page(self, event: QEvent) -> None:
        """ Pasa a la primera página de la tabla. """

        page_to = self._pag.total_pages

        if self._pag.current_page == self._pag.total_pages:
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def fill_combo_page(self):
        """ Rellena el combo de selección de página. """

        self._view.combo_select_page.clear()
        for i in range(1, self._pag.total_pages + 1):
            self._view.combo_select_page.addItem(str(i), i)

