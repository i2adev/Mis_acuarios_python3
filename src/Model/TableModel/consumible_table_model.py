"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/07/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de CATEGORÍAS DE
    ACUARIO. Este módulo se encarga de dar formato a los datos de la tabla.
"""
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.consumible_entity import ConsumibleEntity


class ConsumibleTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de consumibles.
    """

    def __init__(self, data: list[ConsumibleEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "MARCA", "PRODUCTO", "CATEGORÍA",
                         "FORMATO", "CONTENIDO", "UNIDAD", "DESCRIPCIÓN"]

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
        :param index: Índice de la columna
        :param role: Rol de la _______
        """

        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        entidad = self.data[index.row()]
        columna = index.column()

        if columna == 0:
            return entidad.id  # el ID de fila
        elif columna == 1:
            return entidad.num  # Número de la fila
        elif columna == 2:
            return entidad.id_marca  # Id de la marca
        elif columna == 3:
            return entidad.producto
        elif columna == 4:
            return entidad.id_categoria
        elif columna == 5:
            return entidad.id_formato
        elif columna == 6:
            return entidad.contenido
        elif columna == 7:
            return entidad.id_unidad
        elif columna == 8:
            return entidad.descripcion
        else:
            return None

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
                <h2>Identificador del consumible</h2>
                Este campo muestra el <b>ID</b> del consumible.
                """,
                1: """
                <h2>Número correlativo del consumible</h2>
                Este campo muestra el <b>número correlativo</b> del consumible.
.
                """,
                2: """
                <h2>Marca</h2>
                Este campo muestra la <b>marca</b> del consumible.
                """,
                3: """
                <h2>Producto</h2>
                Este campo muestra el <b>nombre comercial</b> del consumible.
                """,
                4: """
                <h2>Categoría</h2>
                Este campo muestra la <b>categoróa</b> del consumible.
                """,
                5: """
                <h2>Formato</h2>
                Este campo muestra el <b>formato</b> con el cual se presenta 
                el consumible.
                """,
                6: """
                <h2>Contenido</h2>
                Este campo muestra el <b>contenido</b> del consumible.
                """,
                7: """
                <h2>Unidad</h2>
                Este campo muestra la <b>unidad</b> del contenido del 
                consumible.
                """,
                8: """
                <h2>Descripción</h2>
                Este campo muestra la <b>unidad</b> del consumible.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
