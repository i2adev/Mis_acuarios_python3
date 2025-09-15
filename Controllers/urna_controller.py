"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      11/08/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad ACUARIO.
"""

from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtWidgets import (QWidget, QMessageBox, QTableView, QCompleter,
                             QComboBox)

from Controllers.base_controller import BaseController
from Controllers.marca_comercial_controller import \
    MarcaComercialDialogController
from Controllers.material_urna_controller import MaterialUrnaDialogController
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Model.DAO.material_urna_dao import MaterialUrnaDAO
from Model.DAO.paginator import Paginator
from Model.DAO.urna_dao import UrnaDAO
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.Entities.material_urna_entity import MaterialUrnaEntity
from Model.Entities.urna_entity import UrnaEntity
from Model.TableModel.urna_table_model import UrnaTableModel
from Services.Result.result import Result
from Services.Validators.urna_validator import UrnaValidator
from Views.Dialogs.marca_comercial_dialog import MarcaComercialDialog
from Views.Dialogs.material_urna_dialog import MaterialUrnaDialog
from Views.Dialogs.urna_dialog import UrnaDialog
from Views.Masters.urna_view import UrnaView
from Views.table_menu_contextual import TableMenuContextual


class UrnaDialogController(BaseController):
    """ Controlador del diálogo de acuario. """

    def __init__(self, view: UrnaDialog, dao: UrnaDAO,
                 mod: UrnaEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista tipo Acuario
        :param dao: DAO de la entidad UrnaDAO
        :param mod: Modelo de la entidad UrnaEntity
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
            # Obtenemos la subcategoría de acuario
            acuario = self.get_urna()
            return Result.success(acuario)
        else:
            return Result.failure("NO SE HA PODIDO OBTENER LA ENTIDAD.")

    def init_basic_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        self.init_imput_handlers()

        if isinstance(self._view, UrnaDialog):
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
            if isinstance(widget, QComboBox):
                widget.installEventFilter(self)

        # Botones
        self._view.frame.button_insert_marca.clicked.connect(
            self.open_marca_comercial_dialog
        )

        self._view.frame.button_insert_material.clicked.connect(
            self.open_material_urna_dialog
        )

    def entity_configuration(self) -> UrnaEntity:
        """ Configura la entidad. """

        ent = UrnaEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.id_marca = self._view.frame.combo_marca.currentData()
        ent.modelo = self._view.frame.edit_modelo.text()
        ent.anchura = self._view.frame.edit_ancho.text()
        ent.profundidad = self._view.frame.edit_profundo.text()
        ent.altura = self._view.frame.edit_alto.text()
        ent.grosor_cristal = self._view.frame.edit_grosor.text()
        ent.volumen_tanque = self._view.frame.edit_volumen.text()
        ent.id_material = (self._view.frame.combo_material.currentData())
        ent.descripcion = self._view.frame.text_descripcion.toPlainText()

        return ent

    def insert(self) -> Result(int):
        """ Inserta un registro en la base de datos. """

        # Validamos el formulario
        val = self.validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res_urna = self._dao.insert(ent)
        if not res_urna.is_success:
            return res_urna

        # Insertamos las fotografías
        res_foto = self._view.frame_imagen.insert_foto(res_urna.value)

        if not res_foto.is_success:
            return Result.failure(res_foto.error_msg)

        # Limpiamos el formulario
        self._clean_view(self._view.frame.combo_marca)
        self._view.frame_imagen.lista_fotos.clear()

        return Result.success(res_urna.value)

    def validate_view(self):
        """ Valida el formulario. """

        # Valida la marca
        res = UrnaValidator.validate_marca(
            self._view.frame.combo_marca
        )

        if not res.is_success:
            self._view.frame.combo_marca.setFocus()
            return res

        # Valida el modelo de la urna
        res = UrnaValidator.validate_modelo_urna(
            self._view.frame.edit_modelo
        )

        if not res.is_success:
            self._view.frame.edit_modelo.setFocus()
            return res

        # Valida la anchura de la urna
        res = UrnaValidator.validate_anchura(
            self._view.frame.edit_ancho
        )

        if not res.is_success:
            self._view.frame.edit_ancho.setFocus()
            return res

        # Valida la profundidad de la urna
        res = UrnaValidator.validate_profundidad(
            self._view.frame.edit_profundo
        )

        if not res.is_success:
            self._view.frame.edit_profundo.setFocus()
            return res

        # Valida la altura de la urna
        res = UrnaValidator.validate_altura(
            self._view.frame.edit_alto
        )

        if not res.is_success:
            self._view.frame.edit_alto.setFocus()
            return res

        # Válida el grosor del cristal
        res = UrnaValidator.validate_grosor(
            self._view.frame.edit_grosor
        )

        if not res.is_success:
            self._view.frame.edit_grosor.setFocus()
            return res

        # Válida el volumen del tanque
        res = UrnaValidator.validate_volumen(
            self._view.frame.edit_volumen
        )

        if not res.is_success:
            self._view.frame.edit_volumen.setFocus()
            return res

        # Válida el volumen del tanque
        res = UrnaValidator.validate_volumen(
            self._view.frame.edit_volumen
        )

        if not res.is_success:
            self._view.frame.edit_volumen.setFocus()
            return res

        # Valida el material de la urna
        res = UrnaValidator.validate_material(
            self._view.frame.combo_material
        )

        if not res.is_success:
            self._view.frame.combo_material.setFocus()
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
        self.urna_result = UrnaEntity(
            id = res.value,
            num = None,
            id_marca = self._view.frame.combo_marca.currentData(),
            modelo = self._view.frame.edit_modelo.text(),
            anchura = self._view.frame.edit_ancho.text(),
            profundidad = self._view.frame.edit_profundo.text(),
            altura = self._view.frame.edit_alto.text(),
            grosor_cristal = self._view.frame.edit_grosor.tect(),
            volumen_tanque = self._view.frame.edit_volumen.text(),
            id_material = self._view.frame.combo_material.currentData(),
            descripcion = self._view.frame.text_descripcion.toPlainText()
                          if self._view.frame.text_descripcion.toPlainText()
                          else None
        )

        # Aceptamos el diálogo
        self._view.accept()

    def get_urna(self):
        """ Devuelve la categoría de filtro resultante. """

        return self.urna_result

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

    def fill_combos(self):
        """ Llena los combos del formulario"""

        self.fill_combo_marca()
        self.fill_combo_material()

    def fill_combo_marca(self):
        """ Llena el combo de tipos de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_marca.clear()

        # Obtenemos los datos
        dao = MarcaComercialDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'MARCAS COMERCIALES'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_marca.addItem(ent.nombre_marca, ent.id)

        # Establecemos el autocompletado
        self.set_autocomplete(self._view.frame.combo_marca)

        # Deseleccionamos el valor
        self._view.frame.combo_marca.setCurrentIndex(-1)

    def fill_combo_material(self):
        """ Llena el combo del material de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_material.clear()

        # Obtenemos los datos
        dao = MaterialUrnaDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'MATERIALES DE URNA'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_material.addItem(ent.material, ent.id)

        # Establecemos el autocompletado
        self.set_autocomplete(self._view.frame.combo_material)

        # Deseleccionamos el valor
        self._view.frame.combo_material.setCurrentIndex(-1)

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

    def open_marca_comercial_dialog(self):
        """ Abrimos el diálogo de marca comercial. """

        # Configuramos el CONTROLADOR
        view = MarcaComercialDialog("INSERTAR MARCA COMERCIAL")
        dao = MarcaComercialDAO()
        mod = MarcaComercialEntity()

        ctrl = MarcaComercialDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_marca

        self.fill_combo_marca()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def open_material_urna_dialog(self):
        """ Abrimos el diálogo de categoria de acuario. """

        view = MaterialUrnaDialog(
            "INSERTAR MATERIAL DE URNA"
        )
        mod = MaterialUrnaEntity()
        dao = MaterialUrnaDAO()

        ctrl = MaterialUrnaDialogController(view, dao, mod)
        res = ctrl.show_modal()

        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_material

        self.fill_combo_material()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

class UrnaController(UrnaDialogController):
    """ Controlador del formulario maestro de subcategoría de acuario. """

    def __init__(self, view: UrnaView, dao: MaterialUrnaDAO,
                 mod: UrnaEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista urna
        :param dao: DAO de la entidad urna
        :param mod: Modelo de la entidad urna
        """

        # Constructor base
        super().__init__(view, dao, mod)

        # Inicializamos el paginador
        self._pag = Paginator("VISTA_URNAS", 5)
        self._pag.initialize_paginator()
        self._view.label_status.setText(f"Sin filtrar. {self._pag.records} "
                                        "registros.")

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
            self._view.frame.combo_marca
        ))
        self._view.button_next.clicked.connect(self._next_page)
        self._view.button_prev.clicked.connect(self._previous_page)
        self._view.button_first.clicked.connect(self._first_page)
        self._view.button_last.clicked.connect(self._last_page)
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

        # Actualiza el registro
        res_data = self.update_data()

        if not res_data.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res_data.error_msg
            )
            return

        # Insertamos las fotografías
        res_foto = self._view.frame_imagen.insert_foto(res_data.value)
        
        if not res_foto.is_success:
            return Result.failure(res_foto.error_msg)

        # Configuramos el paginador
        self._pag.initialize_paginator()

        # Establecemos la página actual
        self._view.combo_select_page.setCurrentIndex(-1)

        # Seleccionamos el último registro utilizado
        self.configure_table_after_crud(res_data.value)

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
                       data: list[UrnaEntity]):
        """ Carga los datos en la tabla. """

        tv_model = UrnaTableModel(data)
        table.setModel(tv_model)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()

    def spell_check(self):
        """ No aplicable. """
        pass

    def update_data(self) -> Result:
        """ Actualiza el registro en la base de datos. """
        # Valida el formulario
        val = self.validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self.entity_configuration()

        # Actualiza el registro
        res = self._dao.update(ent)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view(self._view.frame.combo_marca)

        # Configuramos la tabla
        self.load_tableview()
        self.configure_table_after_crud(res.value)

        return Result.success(ent.id)

    def load_record(self) -> None:
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self.load_data()

        # Carga las imágenes
        self._view.frame_imagen.load_images(res_id.value)

    def load_data(self) -> Result(int):
        """ Carga los datos. """

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
        id_ent = modelo.index(fila, 0).data()
        marca = modelo.index(fila,
                             2).data()  # La columna 1 es el nº correlativo.
        modelo_urna = modelo.index(fila, 3).data()
        ancho = modelo.index(fila, 4).data()
        profundo = modelo.index(fila, 5).data()
        alto = modelo.index(fila, 6).data()
        grosor = modelo.index(fila, 7).data()
        volumen = modelo.index(fila, 8).data()
        material = modelo.index(fila, 9).data()
        descripcion = modelo.index(fila, 10).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ent) if id_ent is not None else ""
        )
        self._view.frame.combo_marca.setCurrentIndex(
            self._view.frame.combo_marca.findText(marca)
        )
        self._view.frame.edit_modelo.setText(
            str(modelo_urna) if modelo_urna is not None else ""
        )
        self._view.frame.edit_ancho.setText(
            str(ancho) if ancho is not None else ""
        )
        self._view.frame.edit_profundo.setText(
            str(profundo) if profundo is not None else ""
        )
        self._view.frame.edit_alto.setText(
            str(alto) if alto is not None else ""
        )
        self._view.frame.edit_grosor.setText(
            str(grosor) if grosor is not None else ""
        )
        self._view.frame.edit_volumen.setText(
            str(volumen) if volumen is not None else ""
        )
        self._view.frame.combo_material.setCurrentIndex(
            self._view.frame.combo_material.findText(material)
        )
        self._view.frame.text_descripcion.setPlainText(
            str(descripcion) if descripcion is not None else ""
        )

        return Result.success(id_ent)

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
        self._clean_view(self._view.frame.combo_marca)

        # Configuramos la tabla
        self.load_tableview()

        return Result.success(id_)

