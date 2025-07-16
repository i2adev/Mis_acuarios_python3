"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad TIPO DE
    ACUARIO.
"""
from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableView, QHeaderView, \
    QCompleter, QComboBox

from Controllers.base_controller import BaseController
from Controllers.categoria_acuario_controller import CategoriaAcuarioDialogController
from Controllers.subcategoria_acuario_controller import \
    SubcategoriaAcuarioDialogController
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.paginator import Paginator
from Model.DAO.subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.TableModel.tipo_acuario_table_model import TipoAcuarioTableModel
from Services.Result.result import Result
from Services.Validators.tipo_acuario_validator import TipoAcuarioValidator
from Views.categoria_acuario_dialog import CategoriaAcuarioDialog
from Views.table_menu_contextual import TableMenuContextual
from Views.tipo_acuario_view import TipoAcuarioView

class TipoAcuarioController(BaseController):
    """ Controlador de la entidad tipo de acuario. """

    def __init__(self, view: TipoAcuarioView):
        """ Constructor base """

        # Inicializamos la vista, la entidad y el dao
        self._mod = TipoAcuarioEntity()
        self._dao = TipoAcuarioDAO()

        # Inicializamos el paginador
        self._pag = Paginator("VISTA_TIPOS_ACUARIO", 5)
        self._pag.initialize_paginator()

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view)

        # Llenamos la tabla
        self.load_tableview()
        self.configure_table_foot()

        # Llenar combos
        self.fill_combos()

        # Inicializamos los eventos
        self.init_handlers()

    def load_tableview(self):
        """ Gestiona los datos para llenar la tabl. """

        self.fill_tableview(self._view.data_table, self._pag.current_data)
        self._configure_table(self._view.data_table)

    def show(self):
        """ Abre la vista """

        self._view.show()

    def init_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        # Inicializa los widgets de introducción de texto
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)

        # self._view.text_observaciones.textChanged.connect(lambda:
        #                                                    self.spell_check)

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

        self._view.frame.button_insert_tipo_acuario.clicked.connect(
            self.open_categoria_acuario_dialog
        )
        self._view.frame.button_insert_subtipo_acuario.clicked.connect(
            self.open_subcategoria_acuario_dialog
        )

        # Inicializamos los combos
        self._view.combo_select_page.currentIndexChanged.connect(
            self.combo_page_indexchanged
        )

        self._view.frame.combo_categoria_acuario.currentIndexChanged.connect(
            self.combo_categoria_indexchanged
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
                "ANTES DE CARGAR UN REGISTRO, DEBES DE "
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

        # Comprobamos si al añadir un registro se ha aumentado el número
        # de páginas totales
        if pagina_actual > self._pag.total_pages:

            total = self._view.combo_select_page.count()
            index = self._view.combo_select_page.currentIndex()

            # Verifica si es el último ítem
            if index == total - 1 and total > 1:
                self._view.combo_select_page.removeItem(index)
                # Selecciona el nuevo último (el anterior al que se eliminó)
                self._view.combo_select_page.setCurrentIndex(
                    self._view.combo_select_page.count() - 1
                )
            elif index == total - 1 and total == 1:
                # Sí es el único ítem, eliminarlo y limpiar la selección
                self._view.combo_select_page.removeItem(index)
                self._view.combo_select_page.setCurrentIndex(-1)

        # Establecemos la página actual
        if pagina_actual > self._pag.total_pages:
            self._view.combo_select_page.setCurrentIndex(
                self._pag.total_pages - 1
            )
            pagina_actual -= 1
            self._view.label_total_pages.setText( str(pagina_actual))
            self._view.label_total_pages.setText( str(pagina_actual))


        self._view.combo_select_page.setCurrentIndex(-1)
        self._view.combo_select_page.setCurrentIndex(pagina_actual - 1)


    def action_cargar(self, event):
        """ Carga un registro desde el menú contextual. """

        self.load()

    def button_delete_click(self, event):
        """ Controla el clic en el botón eliminar. """

        # Sí tenemos un registro cargado
        if not self._view.frame.edit_id.text():
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                "DEBES SELECCIIONAR UN REGISTRO DE LA TABLA ANTES DE "
                "ELIMINARLO."
            )
            return

        # Obtener el ID desde el cuadro de texto id_parent
        id_tipo = int(self._view.frame.edit_id.text())
        pagina_actual = self._view.combo_select_page.currentData()

        # Insertar el registro
        res = self.delete(id_tipo)

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )

        # Configurar paginador
        self._pag.initialize_paginator()

        # Comprobamos si al añadir un registro se ha aumentado el número
        # de páginas totales
        if pagina_actual > self._pag.total_pages:

            total = self._view.combo_select_page.count()
            index = self._view.combo_select_page.currentIndex()

            # Verifica si es el último ítem
            if index == total - 1 and total > 1:
                self._view.combo_select_page.removeItem(index)
                # Selecciona el nuevo último (el anterior al que se eliminó)
                self._view.combo_select_page.setCurrentIndex(
                    self._view.combo_select_page.count() - 1
                )
            elif index == total - 1 and total == 1:
                # Sí es el único ítem, eliminarlo y limpiar la selección
                self._view.combo_select_page.removeItem(index)
                self._view.combo_select_page.setCurrentIndex(-1)

        # Establecemos la página actual
        if pagina_actual > self._pag.total_pages:
            self._view.combo_select_page.setCurrentIndex(
                self._pag.total_pages - 1
            )
            pagina_actual -= 1
            self._view.label_total_pages.setText( str(pagina_actual))

        self._view.combo_select_page.setCurrentIndex(-1)
        self._view.combo_select_page.setCurrentIndex(pagina_actual - 1)

    def button_load_click(self, event):
        """ Controla el clic del boton de cargar. """

        self.load()

    def button_update_click(self, event):
        """ Controla el clic del botón actualizar. """

        pagina_actual = self._view.combo_select_page.currentData()

        # Valida el formulario
        res = self.view_validator()

        if not res.is_success:
            QMessageBox.information(self._view, "ERROR", res.error_msg)
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

        # Establecemos la página actual
        self._view.combo_select_page.setCurrentIndex(-1)
        self._view.combo_select_page.setCurrentIndex(pagina_actual - 1)

        self._select_row_by_id(self._view.data_table, res.value)

    def view_validator(self):
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

        return res

    def button_insert_click(self, event):
        """ Controla el clic del botón insertar. """

        # Valida el formulario
        res = self.view_validator()

        if not res.is_success:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                res.error_msg)
            return


        # Insertamos el registro
        res = self.insert()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Configura el paginador
        self._pag.initialize_paginator()

        # Comprobamos si al añadir un registro se ha aumentado el número
        # de páginas totales
        if self._pag.total_pages > self._view.combo_select_page.count():
            self._view.combo_select_page.addItem(
                str(self._pag.total_pages),
                self._pag.total_pages
            )
            self._view.label_total_pages.setText(
                str(self._view.combo_select_page.count())
            )

        # Establecemos la página final
        self._view.combo_select_page.setCurrentIndex(-1)
        self._view.combo_select_page.setCurrentIndex(
            self._view.combo_select_page.count() - 1
        )

        self._select_row_by_id(self._view.data_table, res.value)

    def fill_tableview(self, table: QTableView, data: list[TipoAcuarioEntity]):
        """ Carga los datos en la tabla. """

        tv_model = TipoAcuarioTableModel(data)
        table.setModel(tv_model)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()

    def _configure_table(self, table: QTableView):
        """ Configura l atabla de datos. """

        # Selecciona un afila entera
        table.setSelectionBehavior(
            QTableView.SelectionBehavior.SelectRows)

        # Solo se puede seleccionar uan fila
        table.setSelectionMode(
            QTableView.SelectionMode.SingleSelection)

        # Color de las filas alternadas
        table.setAlternatingRowColors(True)

        # Oculta las líneas de la tabla
        table.setShowGrid(False)

        # Elimina el tabulador
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # Ocultar la columna ID (columna 0)
        table.setColumnHidden(0, True)

        # Hacer que la columna de observaciones (columna 4) use el espacio
        # restante
        header = table.horizontalHeader()
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        # Mostrar puntos suspensivos si el texto no cabe
        table.setTextElideMode(Qt.TextElideMode.ElideRight)

    def spell_check(self):
        """ No aplicable. """
        pass

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
        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self._dao.insert(ent)
        if not res.is_success:
            return Result.failure( res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        return Result.success(res.value)

    def update(self) -> Result:
        """ Actualiza el registro en la base de datos. """

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self._dao.update(ent)
        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()
        self._select_row_by_id(self._view.data_table, res.value)

        return Result.success(ent.id)

    def load(self) -> Result:
        """ Carga el registro en el formulario. """

        # limpiamos el formulario
        self._clean_view()

        # Carga el modelo de la fila seleccionada
        selection_model = self._view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            return Result.failure(
                "ANTES DE CARGAR UN REGISTRO, DEBES DE "
                "SELECCIONAR UN REGISTRO EN LA TABLA."
            )

        # Configuramos la fila
        index = selection_model.currentIndex()
        fila = index.row()
        modelo = self._view.data_table.model()

        # Lee los datos del modelo
        id_tipo = modelo.index(fila, 0).data()
        categoria_acuario = modelo.index(fila, 2).data()
        subcategoria_acuario = modelo.index(fila, 3).data()
        observaciones = modelo.index(fila, 4).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_tipo) if id_tipo is not None else ""
        )

        if categoria_acuario:
            indexCat = self._view.frame.combo_categoria_acuario.findText(
                categoria_acuario
            )
            self._view.frame.combo_categoria_acuario.setCurrentIndex(indexCat)

        if subcategoria_acuario:
            indexSub = self._view.frame.combo_subcategoria_acuario.findText(
                subcategoria_acuario
            )
            self._view.frame.combo_subcategoria_acuario.setCurrentIndex(indexSub)

        self._view.frame.text_observaciones.setPlainText(
            str(observaciones) if observaciones is not None else ""
        )

        return Result.success(id_tipo)

    def delete(self, id: int) -> Result:
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
        res = self._dao.delete(id)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()

        return Result.success(id)

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

    def fill_combos(self):
        """ Llena los combos del formulario"""

        self.fill_combo_categoria()
        # self.fill_combo_subcategoria()

    def fill_combo_subcategoria(self, id_Cat: int):
        """ Llena el combo de subcategoría de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_subcategoria_acuario.clear()

        # Obtenemos los datos
        dao = SubcategoriaAcuarioDAO()
        lista = dao.get_list_combo_by_categoria(id_Cat)
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

    def fill_combo_categoria(self):
        """ Llena el combo de categoría de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_categoria_acuario.clear()

        # Obtenemos los datos
        dao = CategoriaAcuarioDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'CATEGORÍAS DE ACUARIO'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_categoria_acuario.addItem(ent.categoria, ent.id)

        # Establecemos el autocompletado
        self.set_autocomplete(self._view.frame.combo_categoria_acuario)

        # Deseleccionamos el valor
        self._view.frame.combo_categoria_acuario.setCurrentIndex(-1)

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

        ix_cat = self._view.frame.combo_categoria_acuario.currentIndex()

        ctrl = SubcategoriaAcuarioDialogController(ix_cat)

        # idx = self._view.frame.combo_categoria_acuario.currentIndex()
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
        ctrl = CategoriaAcuarioDialogController(view)
        res = ctrl.show_modal()

        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_categoria_acuario

        self.fill_combo_categoria()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def combo_categoria_indexchanged(self):
        """ Se ejecuta cuando el índice del combo cambia. """

        # Condiciones de salida
        if self._view.frame.combo_categoria_acuario.currentIndex() == -1:
            return

        # Obtenemos el dato a cargar
        data = self._view.frame.combo_categoria_acuario.currentData()

        # Cargamos el combo subcategoría
        self.fill_combo_subcategoria(data)