"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/03/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de 
    REQUERIMIENTOS DE ILUMINACIÓN. Este módulo se encarga de dar formato a los
    datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.requerimiento_iluminacion_entity import \
    RequerimientoIluminacionEntity


class RequerimientoIluminacionTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de requerimientos de 
    iluminación.
    """

    def __init__(self, data: list[RequerimientoIluminacionEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "REQUERIMIENTO", "DESCRIPCIÓN"]

    def rowCount(self, parent=QModelIndex()):
        """
        Devuelve el número de filas de la lista de requerimientos de CO2.
        """

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
            return entidad.requerimiento
        elif columna == 3:
            return entidad.descripcion

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):
        """
        Dependiendo de la orientación de la tabla, Obtiene el encabezado
        de la columna o número de fila.
        """

        # Tooltip para cada column
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador de requerimiento</h2>
                Este campo muestra el <b>ID</b> del requerimiento de 
                iluminación.
                """,
                1: """
                <h2>Número correlativo del requerimiento</h2>
                Este campo muestra el <b>número correlativo</b> de 
                requerimiento de iluminación.
                """,
                2: """
                <h2>Requerimiento</h2>
                Este campo muestra el <b>requerimiento de iluminación.
                """,
                3: """
                <h2>Descripción</h2>
                Este campo muestra la <b>descripción</b> del requerimiento 
                de iluminación.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
