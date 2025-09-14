"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      01/07/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad CATEGORÍA DE
    ACUARIO.
"""

# Importaciones
from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (QWidget, QMessageBox, QTableView)

from Controllers.base_controller import BaseController
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.paginator import Paginator
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.TableModel.categoria_acuario_table_model import \
    CategoriaAcuarioTableModel
from Services.Result.result import Result
from Services.Validators.categoria_acuario_validator import \
    CategoriaAcuarioValidator
from Views.Masters.categoria_acuario_view import CategoriaAcuarioView
from Views.Dialogs.categoria_acuario_dialog import CategoriaAcuarioDialog
from Views.table_menu_contextual import TableMenuContextual

class CategoriaAcuarioDialogController(BaseController):
    """ Controlador del diálogo categoría de acuario. """

    def __init__(self, view: QWidget, dao: CategoriaAcuarioDAO,
                 mod: CategoriaAcuarioEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista tipo CategoríaAcuario
        :param dao: DAO de la entidad CategoriaaCUARIOeNTITY
        :param mod: Modelo de la entidad CategoriaAcuarioEntity
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Inicializamos los eventos
        self.init_basic_handlers()

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            # Obtenemos la categoría de acuario
            categoria_acuario = self.get_categoria_Acuario()
            return Result.success(categoria_acuario)
        else:
            return Result.failure("NO SE HA PODIDO OBTENER LA ENTIDAD.")

    def init_basic_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """
        self.init_imput_handlers()

        if isinstance(self._view, CategoriaAcuarioDialog):
            self.init_dialog_handlers()

    def init_dialog_handlers(self):
        """ Inicializa los controles del cuadro de diálogo. """

        # Botones
        self._view.button_accept.clicked.connect(self.dialog_accept)
        self._view.button_cancel.clicked.connect(self.dialog_cancel)

    def init_imput_handlers(self):
        """ Inicializa los controles de entrada. """

        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)

    def entity_configuration(self) -> CategoriaAcuarioEntity:
        """ Configura la entidad. """

        ent = CategoriaAcuarioEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.categoria = self._view.frame.edit_categoria_acuario.text()
        ent.observaciones = self._view.frame.text_observaciones.toPlainText()

        return ent

    def insert(self) -> Result(int):
        """ Inserta un registro en la base de datos. """

        # Validamos el formulario
        val = self.validate_view()

        if not val.is_success:
            self._view.frame.edit_categoria_acuario.setFocus()
            return val

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self._dao.insert(ent)
        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return res

        # Limpiamos el formulario
        self._clean_view(self._view.frame.edit_categoria_acuario)

        return Result.success(res.value)

    def validate_view(self):
        """ Valida el formulario. """
        val = CategoriaAcuarioValidator.validate_categoria_acuario(
            self._view.frame.edit_categoria_acuario
        )

        return val

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
        self.categoria_acuario_result = CategoriaAcuarioEntity(
            id = res.value,
            num = None,
            categoria = self._view.frame.edit_categoria_acuario.text(),
            observaciones = self._view.frame.text_descripcion.toPlainText()
                          if self._view.frame.text_observaciones.toPlainText()
                          else None
        )

        # Aceptamos el diálogo
        self._view.accept()

    def get_categoria_Acuario(self):
        """ Devuelve la categoría de filtro resultante. """

        return self.categoria_acuario_result

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

class CategoriaAcuarioController(CategoriaAcuarioDialogController):
    """ Controlador del formulario maestro de categoría de acuario. """

    def __init__(self, view: CategoriaAcuarioView, dao: CategoriaAcuarioDAO,
                 mod: CategoriaAcuarioEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista tipo CategoríaAcuario
        :param dao: DAO de la entidad CategoriaaCUARIOeNTITY
        :param mod: Modelo de la entidad CategoriaAcuarioEntity
        """

        # Constructor base
        super().__init__(view, dao, mod)

        # Inicializamos el paginador
        self._pag = Paginator("VISTA_CATEGORIAS_ACUARIO", 5)
        self._pag.initialize_paginator()

        # Llenamos la tabla
        self.load_tableview()
        self._configure_table_foot()

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
        self._view.button_clean.clicked.connect(lambda: self._clean_view(
            self._view.frame.edit_categoria_acuario
        ))
        self._view.button_next.clicked.connect(self._next_page)
        self._view.button_prev.clicked.connect(self._previous_page)
        self._view.button_first.clicked.connect(self._first_page)
        self._view.button_last.clicked.connect(self._last_page)
        self._view.button_close.clicked.connect(
            lambda: self._view.close()
        )
        self._view.button_search.clicked.connect(
            self.button_search_clicked
        )
        self._view.button_filter.clicked.connect(
            self.button_filter_clicked
        )

        # Inicializamos los combos
        self._view.combo_select_page.currentIndexChanged.connect(
            self.combo_page_indexchanged
        )

        # Eventos de la tabla
        self._view.data_table.customContextMenuRequested.connect(
            self.show_context_menu
        )

    def button_filter_clicked(self):
        """ Conmuta entre los modos filtrado y no filtrado. """

        if self._pag.status == "FILTERED":
            self._pag.status = "UNFILTERED"
            self._pag.initialize_paginator()
            self._view.button_filter.setIcon(
                QIcon(":/Images/filter.png")
            )
            self._view.label_status.setText(
                f"Sin filtrar. {self._pag.records} registros"
            )

            # Cargamos la tabla
            self.fill_tableview(self._view.data_table, self._pag._total_data)
            self._configure_table(self._view.data_table)
            self._clean_view(self._view.frame.edit_categoria_acuario)
            self._view.label_total_pages.setText(str(self._pag.total_pages))

    def button_search_clicked(self):
        """ Busca los registros que contengan el patrón. """

        # Variables
        patron = self._view.edit_patron.text()
        total_records = self._pag.records

        # Condiciones de salida
        if not patron:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "ANTES DE PROCEDER CON LA BÚSQUEDA "
                "DEBES INSERTAR UN PATRÓN."
            )
            return

        # Obtoenemos los datos
        self._pag.get_filtered_list(patron)

        # Cargamos la tabla
        self.fill_tableview(self._view.data_table, self._pag._total_data)
        self._configure_table(self._view.data_table)
        self._clean_view(self._view.frame.edit_categoria_acuario)

        self._view.button_filter.setIcon(QIcon(":/Images/filtered.png"))

        self._pag.status = "FILTERED"
        self._view.label_status.setText(
            f"Filtrados {len(self._pag._total_data)} de {total_records} con "
            f"el patrón '{patron.upper()}'."
        )
        self._view.label_total_pages.setText(str(self._pag.total_pages))

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

        self.load()


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

        tv_model = CategoriaAcuarioTableModel(data)
        table.setModel(tv_model)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()

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
        self._clean_view(self._view.frame.edit_categoria_acuario)

        # Configuramos la tabla
        self.load_tableview()
        self.configure_table_after_crud(res.value)

        return Result.success(ent.id)

    def load(self) -> Result:
        """ Carga el registro en el formulario. """

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
        id_cat = modelo.index(fila, 0).data()
        categoria = modelo.index(fila, 2).data()  # La columna 1 es el
                                                    # númer correlativo.
        observaciones = modelo.index(fila, 3).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_cat) if id_cat is not None else ""
        )
        self._view.frame.edit_categoria_acuario.setText(
            str(categoria) if categoria is not None else ""
        )
        self._view.frame.text_observaciones.setPlainText(
            str(observaciones) if observaciones is not None else ""
        )

        return Result.success(id_cat)

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
        self._clean_view(self._view.frame.edit_categoria_acuario)

        # Configuramos la tabla
        self.load_tableview()

        return Result.success(id)

