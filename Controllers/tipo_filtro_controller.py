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
from Views.tipo_filtro_view import TipoFiltroView
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.TableModel.tipo_filtro_table_model import TipoFiltroTableModel



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

    def fill_tableview(self, table: QTableView, data: list[TipoFiltroEntity]):
        """ Carga los datos en la tabla. """

        tv_model = TipoFiltroTableModel(data)
        table.setModel(tv_model)
        table.setColumnHidden(0, True)
        table.resizeColumnsToContents()