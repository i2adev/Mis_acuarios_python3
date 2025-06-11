"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad TIPO DE
    FILTRO.
"""

# Importaciones
from PyQt6.QtWidgets import QWidget, QTextEdit, QPlainTextEdit, QMessageBox, \
    QTableView

from Controllers.base_controller import BaseController
from Services.Result.result import Result
from Views.tipo_filtro_view import TipoFiltroView
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

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(self.__view)

        # Llenamos la tabla
        self.load_tableview()

        # Inicializamos los eventos
        self.init_handlers()

    def load_tableview(self):
        """ Gestiona los datos para llenar la tabl. """

        datos = self.__dao.get_list().value
        self.fill_tableview(self.__view.data_table, datos)


    def show(self):
        """ Abre la vista """

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

        self.__view.text_observaciones.textChanged.connect(lambda:
                                                           self.spell_check)

        # Inizializa los botones
        self.__view.button_insert.clicked.connect(self.button_insert_click)
        self.__view.button_update.clicked.connect(self.button_update_click)
        self.__view.button_load.clicked.connect(self.button_load_click)
        self.__view.button_delete.clicked.connect(self.button_delete_click)
        self.__view.button_clean.clicked.connect(lambda: self._clean_view())


    def button_delete_click(self, event):
        """ Controla el clic en el botón eliminar. """

        # Respuesta esperada
        res = None

        # Carga el modelo de la fila seleccionada
        selection_model = self.__view.data_table.selectionModel()

        # Chequeamos si hay un registro cargado o seleccionado
        if (not selection_model.hasSelection()
            and not self.__view.edit_id.text()):
            QMessageBox.information(self.__view, "ERROR",
                "DEBES CARGAR UN REGISTRO O TENER UNO SELECCIONADO EN LA "
                "TABLA.")
            return

        # Sí tenemos un registro cargado
        if self.__view.edit_id.text():
            id_tipo = int(self.__view.edit_id.text())
            res = self.__dao.delete(id_tipo)

            if not res.is_success:
                QMessageBox.information(self.__view, "ERROR", res.error_msg)
                return

        # Sí hay un registro seleccionado en la tabla
        # TODO: Implementar la eliminación de un registro de la tabla

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()
        # self._select_row_by_id(self.__view.data_table, res.value)



    def button_load_click(self, event):
        """ Controla el clic del boton de cargar. """

        # Carga el modelo de la fila seleccionada
        selection_model = self.__view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            QMessageBox.information(self.__view, "ERROR",
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


    def button_update_click(self, event):
        """ Controla el clic del botón actualizar. """

        # Valida el formulario
        res = TipoFiltroValidator.ValidateTipoFiltro(
            self.__view.edit_tipo_filtro
        )

        if not res.is_success:
            QMessageBox.information(self.__view, "ERROR", res.error_msg)
            return

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self.__dao.update(ent)
        if not res.is_success:
            QMessageBox.information(self.__view, "ERROR", res.error_msg)
            return

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()
        self._select_row_by_id(self.__view.data_table, res.value)

    def button_insert_click(self, event):
        """ Controla el clic del botón insertar. """

        # Valida el formulario
        res = TipoFiltroValidator.ValidateTipoFiltro(
            self.__view.edit_tipo_filtro
        )

        if not res.is_success:
            QMessageBox.information(self.__view, "ERROR", res.error_msg)
            return

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res = self.__dao.insert(ent)
        if not res.is_success:
            QMessageBox.information(self.__view, "ERROR", res.error_msg)
            return

        # Limpiamos el formulario
        self._clean_view()

        # Configuramos la tabla
        self.load_tableview()
        self._select_row_by_id(self.__view.data_table, res.value)


    def fill_tableview(self, table: QTableView, data: list[TipoFiltroEntity]):
        """ Carga los datos en la tabla. """

        tv_model = TipoFiltroTableModel(data)
        table.setModel(tv_model)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()

    def spell_check(self):
        QMessageBox.information(None, "...::OOOOPS::...", "Holaaaa...")

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