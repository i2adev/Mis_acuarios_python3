"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/07/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de SUBCATEGORÍAS
    DE ACUARIO. Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.subcategoria_acuario_entity import SubcategoriaAcuarioEntity


class SubcategoriaAcuarioTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de subcategorías de acuario.
    """

    def __init__(self, data: list[SubcategoriaAcuarioEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "CATEGORÍA", "SUBCATEGORÍA",
                         "OBSERVACIONES"]

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
        :param index: Índice de la columna.
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
            return entidad.id_categoria  # Id de
        elif columna == 3:
            return entidad.subcategoria
        elif columna == 4:
            return entidad.observaciones

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):
        """
        Depencdiendo de la horientación de la tabla, Obtiene el encabezado
        de la columna o número de fila.
        """
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
