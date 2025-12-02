"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  06/10/2025
Comentarios:
    Controlador del formulario maestro del acuario.
"""

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QMessageBox, QTableView, QWidget, QComboBox

import globals
from Controllers.acuario_controller import AcuarioController
from CustomControls.nullable_date_edit import NullableDateEdit
from Model.DAO.acuario_dao import AcuarioDAO
from Model.DAO.paginator import Paginator
from Model.Entities.acuario_entity import AcuarioEntity
from Model.TableModel.acuario_table_model import AcuarioTableModel
from Views.Masters.acuario_view import AcuarioView
from Views.table_menu_contextual import TableMenuContextual


class AcuarioMasterController(AcuarioController):
    """ Controlador del formulario maestro de acuario. """

    def __init__(self, view: AcuarioView,
                 dao: AcuarioDAO,
                 mod: AcuarioEntity):
        """
        Constructor base
        :param view: Formulario maestro de acuario
        :param dao: DAO de acuario
        :param mod: Modelo de acuario
        """

        # Constructor base
        super().__init__(view, dao, mod)

        # Rellena los combos
        self._fill_combos()

        # Inicializamos el paginador
        self._pag = Paginator("VISTA_ACUARIOS", 5)
        self._pag.initialize_paginator()
        self._configure_status_bar(self._pag)

        # Llenamos la tabla
        self._load_tableview()
        self._configure_table_foot()

        # Ocultamos los layouts
        self._hide_layout(self._view.frame.layout_id)
        self._hide_layout(self._view.frame.layout_color)
        # self._hide_layout(self._view.frame.layout_motivo_desmontaje)

        # Inhabilitamos el layout del motivo de desmontaje
        self._view.frame.edit_motivo_desmontaje.setEnabled(False)

        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """
        Inicializa los eventos de los widgets del formulario maestro.
        """

        # Textos y combos
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)
            if isinstance(widget, QComboBox):
                widget.installEventFilter(self)
            if isinstance(widget, NullableDateEdit):
                widget.edit_date.installEventFilter(self)

        # Inicializa los botones
        self._view.frame.button_insert_urna.clicked.connect(
            self._open_urna_dialog
        )
        self._view.frame.button_insert_tipo_acuario.clicked.connect(
            self._open_tipo_acuario_dialog
        )
        self._view.frame.button_color.clicked.connect(self._choose_color)
        self._view.button_insert.clicked.connect(self.button_insert_click)
        self._view.button_update.clicked.connect(self.button_update_click)
        self._view.button_load.clicked.connect(self.button_load_click)
        self._view.button_delete.clicked.connect(self.delete_click)
        self._view.button_clean.clicked.connect(lambda: self._clean_view(
            self._view.frame.edit_nombre_acuario
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
            self._configure_status_bar(self._pag)

            # Cargamos la tabla
            self._fill_tableview(self._view.data_table, self._pag._total_data)
            self._configure_table(self._view.data_table)
            self._clean_view(self._view.frame.combo_proyecto)
            self._view.label_total_pages.setText(str(self._pag.total_pages))

            # Configuramos la tabla
            self._load_tableview()

            # Configuramos el pie de tabla
            self._configure_table_foot()

            # Configura la barra de estado
            self._configure_status_bar(self._pag)

    def button_search_clicked(self):
        """ Busca los registros que contengan el patrón. """

        # Variables
        pattern = self._view.edit_patron.text()
        user = globals.CURRENT_USER.id
        total_records = self._pag.records

        # Condiciones de salida
        if not pattern:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "ANTES DE PROCEDER CON LA BÚSQUEDA "
                "DEBES INSERTAR UN PATRÓN."
            )
            return

        print(f"SEARCH: {pattern}, {user}")

        # Obtiene los datos
        # ----------------------------------------------------------------------
        # SE BÚSCA EN BASE A USUARIO
        # ----------------------------------------------------------------------
        self._pag.get_filtered_list_by_id(pattern, user)

        # Cargamos la tabla
        self._fill_tableview(self._view.data_table, self._pag._total_data)
        self._configure_table(self._view.data_table)
        self._clean_view(self._view.frame.combo_proyecto)

        self._view.button_filter.setIcon(QIcon(":/Images/filtered.png"))

        self._pag.status = "FILTERED"
        self._view.label_total_pages.setText(str(self._pag.total_pages))
        self._load_tableview()
        self._configure_table_foot()
        self._configure_status_bar(self._pag, total_records, pattern)
        self._configure_table_foot()

    def combo_page_indexchanged(self):
        """
        Se ejecuta cuando el índice del combo de selección de página.
        """

        page = self._view.combo_select_page.currentData()

        # Condiciones de salida
        if page is None:
            return

        # Configuración de salida
        self._pag.current_page = page
        self._pag.current_data = self._pag.get_paged_list(
            self._pag.current_page)
        self._load_tableview()

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
        action_eliminar.triggered.connect(self.delete_click)

        # Armamos el menú
        menu.addAction(action_cargar)
        menu.addAction(action_eliminar)

        menu.exec(self._view.data_table.viewport().mapToGlobal(position))

    def action_cargar(self, event):
        """ Carga un registro desde el menú contextual. """

        self._load_record()

    def delete_click(self):
        """ Controla el clic en el botón eliminar. """

        # Obtenemos el origen del evento
        sender = self.sender()
        res_id = self._get_row_id(sender)
        if not res_id.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res_id.error_msg
            )
            return

        current_page = self._view.combo_select_page.currentData()
        paginator_pages = self._pag.total_pages

        # Insertar el registro
        res = self._delete(res_id.value)

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Limpiamos el formulario
        self._clean_view(self._view.frame.combo_proyecto)

        # Configurar paginator
        self._pag.initialize_paginator()

        # Configuramos la tabla tras la inserción
        self._load_tableview()

        # Configura el pie de tabla
        self.configure_table_foot("DELETE", paginator_pages,
                                  current_page)
        # Configura la barra de estado
        self._configure_status_bar(self._pag)

    def button_load_click(self, event):
        """ Controla el clic del botón de cargar. """

        self._load_record()

    def button_insert_click(self, event):
        """ Controla el clic del botón insertar. """

        # Insertamos el registro
        res = self._insert()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Limpiamos el formulario
        self._clean_view(self._view.frame.combo_proyecto)

        # Obtenemos los datos de paginación actuales
        paginator_pages = self._pag.total_pages

        # Configura el paginador
        self._pag.initialize_paginator()

        # Configuramos la tabla tras la inserción
        self._load_tableview()

        # Configura el pie de tabla
        self.configure_table_crud(res.value)
        self.configure_table_foot("INSERT", paginator_pages)

        # Configura la barra de estado
        self._configure_status_bar(self._pag)

    def button_update_click(self, event):
        """ Controla el clic del botón actualizar. """

        current_page = self._view.combo_select_page.currentData()

        # Actualiza el registro
        res = self._update()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Limpiamos el formulario
        self._clean_view(self._view.frame.combo_proyecto)

        # Configuramos el paginador
        self._pag.initialize_paginator()

        # Configuramos la tabla tras la inserción
        self._load_tableview()

        # Configura la tabla y el pie
        self.configure_table_crud(res.value)
        self.configure_table_foot("UPDATE", None,
                                  current_page)

    def configure_table_crud(self, ide: int):
        """
        Configura la tabla tras una operación de crud, seleccionando el último
        registro insertado, actualizado.
        """

        # Seleccionamos la página en la que se encuentra el registro
        self._view.combo_select_page.setCurrentIndex(-1)
        num_reg = next(x.num for x in self._pag.total_data if x.id == ide)
        num_pag = self._pag.get_page_number_by_num(num_reg)
        self._view.combo_select_page.setCurrentIndex(num_pag - 1)

        # Selecciona la última fila
        self._select_row_by_id(self._view.data_table, ide)

    def configure_table_foot(self, operation: str, before_pages: int,
                             current_page: int = 1):
        """ Configura el pie de la tabla. """

        if operation == "INSERT":
            # Comprobamos si al añadir un registro se ha aumentado el número
            # de páginas totales
            if self._pag.total_pages > before_pages:
                self._view.combo_select_page.addItem(
                    str(self._pag.total_pages),
                    self._pag.total_pages
                )
                self._view.label_total_pages.setText(str(self._pag.total_pages))

        elif operation == "DELETE":
            # Comprobamos si al eliminar un registro se la disminuido el número
            # de páginas totales
            if self._pag.total_pages < before_pages:
                page_index = self._pag.total_pages  # ïndice del item a eliminar
                self._view.combo_select_page.removeItem(page_index)
                if current_page > self._pag.total_pages:
                    current_page -= 1
                if current_page <= 0:
                    current_page = 1

                self._view.label_total_pages.setText(str(self._pag.total_pages))

                self._view.combo_select_page.setCurrentIndex(-1)
                self._view.combo_select_page.setCurrentIndex(current_page - 1)

            if self._pag.total_pages == before_pages:
                self._view.combo_select_page.setCurrentIndex(-1)
                self._view.combo_select_page.setCurrentIndex(current_page - 1)

        elif operation == "UPDATE":
            pass
        else:
            pass

    def _load_tableview(self):
        """ Gestiona los datos para llenar la tabla. """

        self._fill_tableview(self._view.data_table, self._pag.current_data)
        self._configure_table(self._view.data_table,
                              [0, 3, 9, 10, 12, 13, 15, ]
                              )

    def _fill_tableview(self, table: QTableView,
                        data: list[AcuarioEntity]):
        """ Carga los datos en la tabla. """

        tv_model = AcuarioTableModel(data)
        table.setModel(tv_model)
        table.resizeColumnsToContents()

    def show(self):
        """ Abre la vista """

        self._view.show()
        self._center_window()
