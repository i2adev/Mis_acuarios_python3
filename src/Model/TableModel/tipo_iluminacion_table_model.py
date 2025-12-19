"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/12/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de TIPOS DE
    ILUMINACIÓN. Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

from Model.Entities.tipo_iluminacion_entity import TipoIluminacionEntity


class TipoIluminacionTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de tipos de
    iluminación.
    """

    def __init__(self, data: list[TipoIluminacionEntity]):
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
            return entidad.tipo_iluminacion
        elif columna == 3:
            return entidad.descripcion

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
                <h2>Identificador del tipo de iluminación</h2>
                Este campo muestra el <b>ID</b> del tipo de iluminación.
                """,
                1: """
                <h2>Número correlativo del tipo de iluminación</h2>
                Este campo muestra el <b>número correlativo</b> del tipo de 
                iluminación.
                """,
                2: """
                <h2>Tipo de iluminación</h2>
                Este campo muestra el <b>tipo de iluminación</b>.
                """,
                3: """
                <h2>Descripción</h2>
                Este campo muestra la <b>descripción</b> del tipo de 
                iluminación.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
