"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  04/03/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de
    FORMATOS DE CONSUMIBLE. Este módulo se encarga de dar formato a los
    datos de la tabla.
"""

# Importaciones
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

from Model.Entities.formato_consumible_entity import FormatoConsumibleEntity


class FormatoConsumibleTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de los estados de
    proyecto.
    """

    def __init__(self, data: list[FormatoConsumibleEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "FORMATO CONSUMIBLE", "OBSERVACIONES"]

    def rowCount(self, parent=QModelIndex()):
        """ Devuelve el número de filas de la lista de tipos de filtro. """

        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        """ Devuelve el número de columnas que tiene la lista. """

        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """
        Devuelve el dato de una de las celdas.
        :param index: Índice de la columna
        :param role: Rol de la _______
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
            return entidad.formato
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
                <h2>Identificador de la categoría de consumible</h2>
                Este campo muestra el <b>ID</b> del formato de consumible.
                """,
                1: """
                <h2>Número correlativo del formato de consumible</h2>
                Este campo muestra el <b>número correlativo</b> del 
                formato de consumible.
                """,
                2: """
                <h2>Formato de consumible</h2>
                Este campo muestra el <b>formato</b> en el que viene el 
                consumible.
                """,
                3: """
                <h2>Descripción</h2>
                Este campo muestra la descripción del <b>formato de 
                consumible</b>.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
