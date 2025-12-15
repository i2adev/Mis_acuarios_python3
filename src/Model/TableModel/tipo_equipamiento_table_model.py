"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/15/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de CATEGORÍA DE
    EQUIPAMIENTO. Este módulo se encarga de dar formato a los datos de la 
    tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt

from Model.Entities.categoria_equipamiento_entity import \
    CategoriaEquipamientoEntity


class TipoEquipamientoTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de categorías de
    equipamiento.
    """

    def __init__(self, data: list[CategoriaEquipamientoEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "CATEGORÍA", "DESCRIPCIÓN"]

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
            return entidad.categoria_equipamiento
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
                <h2>Identificador de la categoría de equipamiento</h2>
                Este campo muestra el <b>ID</b> de la categoría de 
                equipamiento.
                """,
                1: """
                <h2>Número correlativo de la categoría de equipamiento</h2>
                Este campo muestra el <b>número correlativo</b> de la 
                categoría de equipamiento.
                """,
                2: """
                <h2>Categoría de equipamiento</h2>
                Este campo muestra la <b>categoría</b> a la que pertenece 
                el equipamiento.
                """,
                3: """
                <h2>Descripción</h2>
                Este campo muestra la <b>descripción </b> de la categoría a 
                la que pertenece el equipo.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
