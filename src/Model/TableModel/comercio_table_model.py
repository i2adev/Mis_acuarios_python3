"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de COMERCIOS. 
    Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

from Model.Entities.comercio_entity import ComercioEntity


class ComercioTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de comercios.
    """

    def __init__(self, data: list[ComercioEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "COMERCIO", "DIRECCIÓN", "COD. POSTAL",
                         "POBLACIÓN", "PROVINCIA", "PAÍS", "OBSERVACIONES"]

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
            return entidad.nombre_comercio
        elif columna == 3:
            return entidad.direccion
        elif columna == 4:
            return entidad.cod_postal
        elif columna == 5:
            return entidad.poblacion
        elif columna == 6:
            return entidad.provincia
        elif columna == 7:
            return entidad.id_pais
        elif columna == 8:
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
                <h2>Identificador del comercio</h2>
                Este campo muestra el <b>ID</b> del comercio.
                """,
                1: """
                <h2>Número correlativo del comercio</h2>
                Este campo muestra el <b>número correlativo</b> del comercio.
                """,
                2: """
                <h2>Nombre del comercio</h2>
                Este campo muestra el <b>nombre del comercio</b>.
                """,
                3: """
                <h2>Dirección postal del comercio</h2>
                Este campo muestra la <b>dirección</b> en la que se 
                encuentra el comercio.
                """,
                4: """
                <h2>Código postal de la población</h2>
                Este campo muestra el <b>código postal</b> de la población 
                en la que se encuentra el comercio.
                """,
                5: """
                <h2>Población</h2>
                Este campo muestra la población en la que se encuentra el 
                comercio.
                """,
                6: """
                <h2>Provincia</h2>
                Este campo muestra la <b>provincia</b> en la que se 
                encuentra el comercio.
                """,
                7: """
                <h2>País</h2>
                Este campo muestra el <b>país</b> en la que se 
                encuentra el comercio.
                """,
                8: """
                <h2>Observaciones</h2>
                Este campo muestra las <b>observaciones</b> del comercio.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
