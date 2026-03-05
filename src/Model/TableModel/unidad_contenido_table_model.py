"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  05/03/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de
    UNIDADES DE CONTENIDO. Este módulo se encarga de dar formato a los
    datos de la tabla.
"""

# Importaciones
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

from Model.Entities.unidades_contenido_entity import UnidadContenidoEntity


class UnidadContenidoTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de las unidades de
    contenido.
    """

    def __init__(self, data: list[UnidadContenidoEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "UNIDAD", "DESCRIPCIÓN"]

    def rowCount(self, parent=QModelIndex()):
        """
        Devuelve el número de filas de la lista de las unidades de
        contenido.
        """

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
            return entidad.unidad
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
                <h2>Identificador de la unidad de contenido.</h2>
                Este campo muestra el <b>ID</b> de la unidad de contenido.
                """,
                1: """
                <h2>Número correlativo de la unidad de contenido</h2>
                Este campo muestra el <b>número correlativo</b> de la 
                unidad de contenido.
                """,
                2: """
                <h2>Unidad de contenido</h2>
                Este campo muestra la <b>unidad</b> en la que se mide el 
                contenido del consumible.
                """,
                3: """
                <h2>Descripción</h2>
                Este campo muestra la descripción de la <b>unidad de 
                contenido</b>.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
