﻿"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  02/06/2025
Commentarios:
    Módulo que contiene el modelo de visualización de la tabla de ESTADOS DE 
    PROYECTO. Este módulo se encarga de dar formato a los datos de la tabla.
"""

# Importaciones
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

from Model.Entities.estado_proyecto_entity import EstadoProyectoEntity


class EstadoProyectoTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de los estados de 
    proyecto.
    """

    def __init__(self, data: list[EstadoProyectoEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "ESTADO PROYECTO", "OBSERVACIONES"]

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
            return entidad.estado
        elif columna == 3:
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

