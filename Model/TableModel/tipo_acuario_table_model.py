"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene el modelo de visualización de la tabla de TIPOS DE
    ACUARIO. Este módulo se encarga de dar formato a los datos de la tabla.
"""
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity


class TipoAcuarioTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de tipos de acuario.
    """

    def __init__(self, data: list[TipoAcuarioEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "TIPO", "SUBTIPO", "OBSERVACIONES"]

    def rowCount(self, parent=QModelIndex()):
        """ Devuelve el número de filas de la lista de tipos de filtro. """

        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        """ Devuelve el número de columnas que tiene la lista. """

        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """
        Devuelve el dato de una de las celdas.
        Parametros:
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
            return entidad.tipo_acuario
        elif columna == 3:
            return entidad.subtipo_acuario
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