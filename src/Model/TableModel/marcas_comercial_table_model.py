"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/07/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de MARCAS 
    COMERCIALES. Este módulo se encarga de dar formato a los datos de la tabla.
"""
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.marca_comercial_entity import MarcaComercialEntity


class MarcaComercialTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de tipos de acuario.
    """

    def __init__(self, data: list[MarcaComercialEntity]):
        """
        Constructor de la clase.

        :param data: Lista de marcas comerciales
        """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "MARCA", "DIRECCIÓN", "CÓDIGO POSTAL",
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

        :param index: Índice de la columna
        :param role: Rol del item
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
            return entidad.nombre_marca
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
                <h2>Identificador de la marca comercial</h2>
                Este campo muestra el <b>ID</b> de la marca comercial.
                """,
                1: """
                <h2>Número correlativo de la marca comercial</h2>
                Este campo muestra el <b>número correlativo</b> de la 
                marca comercial.
                """,
                2: """
                <h2>Marca comercial</h2>
                Este campo muestra la <b>marca comercial</b>.
                """,
                3: """
                <h2>Dirección</h2>
                Este campo muestra la <b>dirección</b> de la sede social de 
                la marca comercial.
                """,
                4: """
                <h2>Código postal</h2>
                Este campo muestra el <b>código postal</b> de la población 
                de donde se encuentra la sede social de la marca comercial.
                """,
                5: """
                <h2>Población</h2>
                Este campo muestra la <b>población</b> donde se encuentra la 
                sede social de la marca comercial.
                """,
                6: """
                <h2>Provincia</h2>
                Este campo muestra la <b>provincia</b> donde se encuentra la 
                sede social de la marca comercial.
                """,
                7: """
                <h2>País</h2>
                Este campo muestra el <b>páis</b> donde se encuentra la sede 
                social de la marca comercial.
                """,
                8: """
                <h2>Observaciones</h2>
                Este campo muestra las <b>observaciones</b> de la marca 
                comercial.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
