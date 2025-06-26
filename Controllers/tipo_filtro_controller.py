"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad TIPO DE
    FILTRO.
"""
# Importaciones
from PyQt6.QtCore import qSetMessagePattern, Qt, QEvent
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QTextEdit, QPlainTextEdit, QMessageBox, \
    QTableView, QHeaderView

from Controllers.base_controller import BaseController
from Model.DAO.paginator import Paginator
from Services.Result.result import Result
from Views.tipo_filtro_view import TipoFiltroView
from Views.table_menu_contextual import TableMenuContextual
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.TableModel.tipo_filtro_table_model import TipoFiltroTableModel
from Services.Validators.tipo_filtro_validator import TipoFiltroValidator

class TipoFiltroController(BaseController):
    """ Controlador de la entidad tipo de filtro. """

    def __init__(self):
        """ Constructor base """

        # Inicializamos la vista, la entidad y el dao
        self.__view = TipoFiltroView("TIPOS DE FILTRO")
        self.__mod = TipoFiltroEntity()
        self.__dao = TipoFiltroDAO()

        # Inicializamos el paginador
        self._pag = Paginator("VISTA_TIPOS_FILTRO", 5)
        self._pag.initialize_paginator()

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(self.__view)

        # Llenamos la tabla
        self.load_tableview()
        self.configure_table_foot()

        # Inicializamos los eventos
        self.init_handlers()

    def load_tableview(self):
        """ Gestiona los datos para llenar la tabl. """

        self.fill_tableview(self.__view.data_table, self._pag.current_data)
        self._configure_table(self.__view.data_table)

    def show(self):
        """ Abre la vista """
        self.__view.button_accept.hide()
        self.__view.button_cancel.hide()
        self.__view.show()

    def get_tipo_filtro_list(self):
        """ Obtiene el listado de tipos de filtro. """

        pass

    def init_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        # Inicializa los widgets de introducción de texto
        for widget in self.__view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)

        # self.__view.text_observaciones.textChanged.connect(lambda:
        #                                                    self.spell_check)

        # Inizializa los botones
        self.__view.button_insert.clicked.connect(self.button_insert_click)
        self.__view.button_update.clicked.connect(self.button_update_click)
        self.__view.button_load.clicked.connect(self.button_load_click)
        self.__view.button_delete.clicked.connect(self.button_delete_click)
        self.__view.button_clean.clicked.connect(lambda: self._clean_view())

        self.__view.button_next.clicked.connect(self.next_page)
        self.__view.button_prev.clicked.connect(self.previous_page)
        self.__view.button_first.clicked.connect(self.first_page)
        self.__view.button_last.clicked.connect(self.last_page)

        # Inicializamos los combos
        self.__view.combo_select_page.currentIndexChanged.connect(
            self.combo_page_indexchanged
        )

        # Eventos de la tabla
        self.__view.data_table.customContextMenuRequested.connect(
            self.show_context_menu
        )

    def combo_page_indexchanged(self, event: QEvent):
        """
        Se ejecuta cuando el índice del combo de selección de página.
        """

        page = self.__view.combo_select_page.currentData()

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
        index = self.__view.data_table.indexAt(position)

        # Si el índice no es valido
        if not index.isValid():
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                "DEBES PULSAR SOBRE UN REGISTRO DE LA TABLA."
            )
            return

        # Muestra el menú
        menu = TableMenuContextual(self.__view.data_table)

        # Creamos el menú
        action_cargar = QAction("CARGAR REGISTRO", self)
        action_cargar.triggered.connect(self.action_cargar)
        action_eliminar = QAction("ELIMINAR REGISTRO", self)
        action_eliminar.triggered.connect(self.action_eliminar)

        # Armamos el menú
        menu.addAction(action_cargar)
        menu.addAction(action_eliminar)

        menu.exec(self.__view.data_table.viewport().mapToGlobal(position))

    def action_eliminar(self, event):
        """ Elimina el registro desde el menú contextual"""

        id_tipo = None

        # Carga el modelo de la fila seleccionada
        selection_model = self.__view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                "ANTES DE CARGAR UN REGISTRO, DEBES DE "
                "SELECCIONAR UN REGISTRO EN LA TABLA."
            )
            return

        # Configuramos la fila
        index = selection_model.currentIndex()
        fila = index.row()
        modelo = self.__view.data_table.model()

        # Lee los datos del modelo
        id_tipo = modelo.index(fila, 0).data()
        pagina_actual = self.__view.combo_select_page.currentData()

        res = self.delete(id_tipo)

        if not res.is_success:
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                res.error_msg
            )
            return

        # Configurar paginador
        self._pag.initialize_paginator()

        # Comprobamos si al añadir un registro se ha aumentado el número
        # de páginas totales
        if pagina_actual > self._pag.total_pages:

            total = self.__view.combo_select_page.count()
            index = self.__view.combo_select_page.currentIndex()

            # Verifica si es el último ítem
            if index == total - 1 and total > 1:
                self.__view.combo_select_page.removeItem(index)
                # Selecciona el nuevo último (el anterior al que se eliminó)
                self.__view.combo_select_page.setCurrentIndex(
                    self.__view.combo_select_page.count() - 1
                )
            elif index == total - 1 and total == 1:
                # Sí es el único ítem, eliminarlo y limpiar la selección
                self.__view.combo_select_page.removeItem(index)
                self.__view.combo_select_page.setCurrentIndex(-1)

        # Establecemos la página actual
        if pagina_actual > self._pag.total_pages:
            self.__view.combo_select_page.setCurrentIndex(
                self._pag.total_pages - 1
            )

        if self._pag.total_pages == 1:
            self.__view.combo_select_page.addItem("2", 2)
            self.__view.combo_select_page.setCurrentIndex(1)
            self.__view.combo_select_page.setCurrentIndex(0)
            self.__view.combo_select_page.removeItem(1)
        else:
            self.__view.combo_select_page.setCurrentIndex(0)
            self.__view.combo_select_page.setCurrentIndex(pagina_actual - 1)


    def action_cargar(self, event):
        """ Carga un registro desde el menú contextual. """

        self.load()

    def button_delete_click(self, event):
        """ Controla el clic en el botón eliminar. """

        # Sí tenemos un registro cargado
        if not self.__view.edit_id.text():
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                "DEBES SELECCIIONAR UN REGISTRO DE LA TABLA ANTES DE "
                "ELIMINARLO."
            )
            return

        # Obtener el ID desde el cuadro de texto id_parent
        id_tipo = int(self.__view.edit_id.text())
        pagina_actual = self.__view.combo_select_page.currentData()

        # Insertar el registro
        res = self.delete(id_tipo)

        if not res.is_success:
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                res.error_msg
            )

        # Configurar paginador
        self._pag.initialize_paginator()

        # Comprobamos si al añadir un registro se ha aumentado el número
        # de páginas totales
        if pagina_actual > self._pag.total_pages:

            total = self.__view.combo_select_page.count()
            index = self.__view.combo_select_page.currentIndex()

            # Verifica si es el último ítem
            if index == total - 1 and total > 1:
                self.__view.combo_select_page.removeItem(index)
                # Selecciona el nuevo último (el anterior al que se eliminó)
                self.__view.combo_select_page.setCurrentIndex(
                    self.__view.combo_select_page.count() - 1
                )
            elif index == total - 1 and total == 1:
                # Sí es el único ítem, eliminarlo y limpiar la selección
                self.__view.combo_select_page.removeItem(index)
                self.__view.combo_select_page.setCurrentIndex(-1)

        # Establecemos la página actual
        if pagina_actual > self._pag.total_pages:
            self.__view.combo_select_page.setCurrentIndex(
                self._pag.total_pages - 1
            )

        if self._pag.total_pages == 1:
            self.__view.combo_select_page.addItem("2", 2)
            self.__view.combo_select_page.setCurrentIndex(1)
            self.__view.combo_select_page.setCurrentIndex(0)
            self.__view.combo_select_page.removeItem(1)
        else:
            self.__view.combo_select_page.setCurrentIndex(0)
            self.__view.combo_select_page.setCurrentIndex(pagina_actual - 1)

    def button_load_click(self, event):
        """ Controla el clic del boton de cargar. """

        self.load()


    def button_update_click(self, event):
        """ Controla el clic del botón actualizar. """

        pagina_actual = self.__view.combo_select_page.currentData()

        # Valida el formulario
        res = TipoFiltroValidator.ValidateTipoFiltro(
            self.__view.edit_tipo_filtro
        )

        if not res.is_success:
            QMessageBox.information(self.__view, "ERROR", res.error_msg)
            return

        # Actualiza el registro
        res = self.update()

        if not res.is_success:
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                res.error_msg
            )

        # Configuramos el paginador
        self._pag.initialize_paginator()

        # Establecemos la página actual
        if self._pag.total_pages == 1:
            self.__view.combo_select_page.addItem("2", 2)
            self.__view.combo_select_page.setCurrentIndex(1)
            self.__view.combo_select_page.setCurrentIndex(0)
            self.__view.combo_select_page.removeItem(1)
        else:
            self.__view.combo_select_page.setCurrentIndex(0)
            self.__view.combo_select_page.setCurrentIndex(pagina_actual - 1)


        self._select_row_by_id(self.__view.data_table, res.value)

    def button_insert_click(self, event):
        """ Controla el clic del botón insertar. """

        # Valida el formulario
        res = TipoFiltroValidator.ValidateTipoFiltro(
            self.__view.edit_tipo_filtro
        )

        if not res.is_success:
            QMessageBox.information(
                self.__view,
                self.__view.window_title,
                res.error_msg)
            return

        # Insertamos el registro
        res = self.insert()

        if not res.is_success:
            QMessageBox.warning(
                self.__view,
                self.__view.window_title,
                res.error_msg
            )
            return

        # Configura el paginador
        self._pag.initialize_paginator()

        # Comprobamos si al añadir un registro se ha aumentado el número
        # de páginas totales
        if self._pag.total_pages > self.__view.combo_select_page.count():
            self.__view.combo_select_page.addItem(
                str(self._pag.total_pages),
                self._pag.total_pages
            )
            self.__view.label_total_pages.setText(
                str(self.__view.combo_select_page.count())
            )

        # Establecemos la página final
        self.__view.combo_select_page.setCurrentIndex(-1)
        self.__view.combo_select_page.setCurrentIndex(
            self.__view.combo_select_page.count() - 1
        )

        self._select_row_by_id(self.__view.data_table, res.value)

    def fill_tableview(self, table: QTableView, data: list[TipoFiltroEntity]):
        """ Carga los datos en la tabla. """

        tv_model = TipoFiltroTableModel(data)
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

        # Hacer que la columna de observaciones (columna 3) use el espacio
        # restante
        header = table.horizontalHeader()
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        # Mostrar puntos suspensivos si el texto no cabe
        table.setTextElideMode(Qt.TextElideMode.ElideRight)

    def spell_check(self):
        """ No aplicable. """
        pass

    def entity_configuration(self) -> TipoFiltroEntity:
        """ Configura la entidad. """

        ent = TipoFiltroEntity()

        if self.__view.edit_id.text():
            ent.id = int(self.__view.edit_id.text())
        else:
            ent.id = None

        ent.tipo_filtro = self.__view.edit_tipo_filtro.text()
        ent.observaciones = self.__view.text_observaciones.toPlainText()

        return ent

    def insert(self) -> Result:
        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self.__dao.insert(ent)
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
        res = self.__dao.update(ent)
        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()
        self._select_row_by_id(self.__view.data_table, res.value)

        return Result.success(ent.id)

    def load(self) -> Result:
        """ Carga el registro en el formulario. """

        # Carga el modelo de la fila seleccionada
        selection_model = self.__view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            return Result.failure(
                "ANTES DE CARGAR UN REGISTRO, DEBES DE "
                "SELECCIONAR UN REGISTRO EN LA TABLA."
            )

        # Configuramos la fila
        index = selection_model.currentIndex()
        fila = index.row()
        modelo = self.__view.data_table.model()

        # Lee los datos del modelo
        id_tipo = modelo.index(fila, 0).data()
        tipo_filtro = modelo.index(fila, 2).data()  # La columna 1 es el
                                                    # númer correlativo.
        observaciones = modelo.index(fila, 3).data()

        # Cargamos los widgets
        self.__view.edit_id.setText(
            str(id_tipo) if id_tipo is not None else ""
        )
        self.__view.edit_tipo_filtro.setText(
            str(tipo_filtro) if tipo_filtro is not None else ""
        )
        self.__view.text_observaciones.setPlainText(
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
            self.__view,
            self.__view.window_title,
            "¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self.__view,
                self.__view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        res = QMessageBox.question(
            self.__view,
            self.__view.window_title,
            "R E P I T O\n¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self.__view,
                self.__view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        # Elimina el registro
        res = self.__dao.delete(id)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()

        return Result.success(id)

    def configure_table_foot(self):
        """ Configura el pie de la tabla. """

        self.__view.label_total_pages.setText(str(self._pag.total_pages))
        self.fill_combo_page()    

    def next_page(self, event: QEvent) -> None:
        """ Pasa a la siguiente página de la tabla. """

        page_to = self.__view.combo_select_page.currentData() + 1

        if page_to > self._pag.total_pages:
            QMessageBox.information(
                self.__view,
                self.__view.window_title,
                "SE HA LLEGADO A LA ÚLTIMA PÁGINA"
            )
            return

        self._pag.current_page = page_to
        self.__view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def previous_page(self, event: QEvent) -> None:
        """ Pasa a la anterior página de la tabla. """

        page_to = self.__view.combo_select_page.currentData() - 1

        if page_to < 1:
            QMessageBox.information(
                self.__view,
                self.__view.window_title,
                "SE HA LLEGADO A LA PRIMERA PÁGINA"
            )
            return

        self._pag.current_page = page_to
        self.__view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def first_page(self, event: QEvent) -> None:
        """ Pasa a la primera página de la tabla. """

        page_to = 1

        if self._pag.current_page == 1:
            return

        self._pag.current_page = page_to
        self.__view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def last_page(self, event: QEvent) -> None:
        """ Pasa a la primera página de la tabla. """

        page_to = self._pag.total_pages

        if self._pag.current_page == self._pag.total_pages:
            return

        self._pag.current_page = page_to
        self.__view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def fill_combo_page(self):
        """ Rellena el combo de selección de página. """

        self.__view.combo_select_page.clear()
        for i in range(1, self._pag.total_pages + 1):
            self.__view.combo_select_page.addItem(str(i), i)

