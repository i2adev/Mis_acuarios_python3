"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de TIPOS DE
    FILTRO. Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

from Model.Entities.tipo_filtro_entity import TipoFiltroEntity


class TipoFiltroTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de tipos de
    filtro.
    """

    def __init__(self, data: list[TipoFiltroEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "TIPO", "OBSERVACIONES"]

    def rowCount(self, parent=QModelIndex()):
        """ Devuelve el número de filas de la lista de tipos de filtro. """

        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        """ Devuelve el número de columnas que tiene la lista. """

        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """
        Devuelve el dato de una de las celdas.
        Parámetros:
        - INDEX: Índice de la columna
        - ROLE: Rol de la _______
        """

        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        entidad = self.data[index.row()]
        columna = index.column()

        if columna == 0:
            return entidad.id  # el número de fila visible
        elif columna == 1:
            return entidad.num
        elif columna == 2:
            return entidad.tipo_filtro
        elif columna == 3:
            return entidad.observaciones

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):
        """
        Depencdiendo de la orientación de la tabla, Obtiene el encabezado
        de la columna o número de fila.
        """
        # Tooltip para cada column
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador del tipo de filtro</h2>
                Este campo muestra el <b>ID</b> del tipo de filtro.
                """,
                1: """
                <h2>Número correlativo del tipo de filtro</h2>
                Este campo muestra el <b>número correlativo</b> del tipo de 
                filtro.
                """,
                2: """
                <h2>Tipo de filtro</h2>
                Este campo muestra la <b>tipo de filtro</b>.
                """,
                3: """
                <h2>Observaciones</h2>
                Este campo muestra las <b>observaciones</b> del tipo de 
                filtro.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
