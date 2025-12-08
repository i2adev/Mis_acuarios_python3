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
        Depencdiendo de la orientación de la tabla, Obtiene el encabezado
        de la columna o número de fila.
        """
        # Tooltip para cada column
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador de la subcategoría de acuario</h2>
                Este campo muestra el <b>ID</b> de la subcategoría de acuario.
                """,
                1: """
                <h2>Número correlativo de la subcategoría de acuario</h2>
                Este campo muestra el <b>número correlativo</b> de la 
                subcategoría de acuario.
                """,
                2: """
                <h2>Categoría de acuario</h2>
                Este campo muestra la <b>categoría de acuario</b>.
                """,
                3: """
                <h2>Subcategoría de acuario</h2>
                Este campo muestra la <b>subcategoría de acuario</b>.
                """,
                4: """
                <h2>Observaciones</h2>
                Este campo muestra las <b>observaciones</b> de la 
                subcategoría de acuario.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
