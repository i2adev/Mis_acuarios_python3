"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Commentarios:
    Módulo que contiene el modelo de visualización de la tabla de ACUARIOS. 
    Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.acuario_entity import AcuarioEntity


class AcuarioTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de acuarios.
    """

    def __init__(self, data: list[AcuarioEntity]):
        """
        Constructor de la clase.

        :param data: Lista de acuarios
        """

        super().__init__()
        self.data = data
        self._headers = (["ID", "PROYECTO", "#", "COLOR", "NOMBRE", "URNA",
                          "TIPO", "VOLUMEN", "F. MONTAJE", "F. I. CICLADO",
                          "F. F. CICLADO", "UBICACIÓN", "F.DESMONTAJE",
                          "MOTIVO DESMONTAJE", "DESCRIPCIÓN"])

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

        self._headers = (["ID", "PROYECTO", "#", "COLOR", "NOMBRE", "URNA",
                          "TIPO", "VOLUMEN", "F. MONTAJE", "F. I. CICLADO",
                          "F. F. CICLADO", "UBICACIÓN", "F.DESMONTAJE",
                          "MOTIVO DESMONTAJE", "DESCRIPCIÓN"])

        if columna == 0:
            return entidad.id  # el número de fila visible
        elif columna == 1:
            return entidad.id_proyecto
        elif columna == 2:
            return entidad.num
        elif columna == 3:
            return entidad.cod_color
        elif columna == 4:
            return entidad.nombre
        elif columna == 5:
            return entidad.id_urna
        elif columna == 6:
            return entidad.id_tipo
        elif columna == 7:
            return entidad.volumen_neto
        elif columna == 8:
            return entidad.fecha_montaje
        elif columna == 9:
            return entidad.fecha_inicio_ciclado
        elif columna == 10:
            return entidad.fecha_inicio_ciclado
        elif columna == 11:
            return entidad.ubicacion_acuario
        elif columna == 12:
            return entidad.fecha_desmontaje
        elif columna == 13:
            return entidad.motivo_desmontaje
        elif columna == 14:
            return entidad.descripcion

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

    # @staticmethod
    # def brakdown_dimensions(self, dimensions: str) -> list[int]:
    #     """
    #     Separa la cadena de las dimensiones en enteros que representan la
    #     longitud, profundidad y altura del acuario.
    #
    #     :param dimensions: Cadena que representa las dimensiones del acuario
    #     """
    #
    #     lista = dimensions.split()
    #     lista = lista[0].split("x")
    #     ancho = int(lista[0])
    #     profundo = int(lista[1])
    #     alto = int(lista[2])
    #     dims = [ancho, profundo, alto]
    #
    #     return dims
