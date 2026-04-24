"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      07/04/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de PERIODO Este
    módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from ModuloMaestro.Model.Entities.periodo_entity import PeriodoEntity


class PeriodoTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de requerimientos de
    periodo.
    """

    def __init__(self, data: list[PeriodoEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "PERIODO"]

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
            return entidad.periodo

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
                <h2>Identificador de periodo</h2>
                Este campo muestra el <b>ID</b> del periodo.
                """,
                1: """
                <h2>Número correlativo del periodo</h2>
                Este campo muestra el <b>número correlativo</b> del 
                periodo.
                """,
                2: """
                <h2>Periodo</h2>
                Este campo muestra el <b>periodo</b>.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
