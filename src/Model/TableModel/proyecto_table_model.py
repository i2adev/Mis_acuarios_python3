"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      21/10/2025
Commentarios:
    Módulo que contiene el modelo de visualización de la tabla de PROYECTOS. 
    Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.proyecto_entity import ProyectoEntity


class ProyectoTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de proyectos.
    """

    def __init__(self, data: list[ProyectoEntity]):
        """
        Constructor de la clase.

        :param data: Lista de proyectos
        """

        super().__init__()
        self.data = data
        self._headers = ["ID", "ID_USUARIO", "#", "NOMBRE", "ESTADO",
                         "FECHA_INICIO", "FECHA_CIERRE", "MOTIVO_CIERRE",
                         "DESCRIPTION"]

    def rowCount(self, parent=QModelIndex()):
        """ Devuelve el número de filas de la lista de PROYECTOS. """

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
            return entidad.id
        elif columna == 1:
            return entidad.id_usuario
        elif columna == 2:
            return entidad.num
        elif columna == 3:
            return entidad.nombre
        elif columna == 4:
            return entidad.id_estado
        elif columna == 5:
            return entidad.fecha_inicio
        elif columna == 6:
            return entidad.fecha_fin
        elif columna == 7:
            return entidad.motivo_cierre
        elif columna == 8:
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

