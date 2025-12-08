"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      21/10/2025
Comentarios:
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
                         "F. INICIO", "F. CIERRE", "MOTIVO CIERRE",
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
        Depencdiendo de la orientación de la tabla, Obtiene el encabezado
        de la columna o número de fila.
        """
        # Tooltip para cada column
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador del proyecto</h2>
                Este campo muestra el <b>ID</b> del proyecto.
                """,
                1: """
                <h2>Identificador del usuario</h2>
                Este campo muestra el <b>ID</b> del usuario.
                """,
                2: """
                <h2>Número correlativo del proyecto</h2>
                Este campo muestra el <b>número correlativo</b> del proyecto
                """,
                3: """
                <h2>Nombre del proyecto</h2>
                Este campo muestra el <b>nombre</b> que se le ha asignado al 
                proyecto.
                """,
                4: """
                <h2>Estado de proyecto</h2>
                Este campo muestra el <b>estado </b> en el que se encuentra 
                el proyecto.
                """,
                5: """
                <h2>Fecha de inicio del proyecto</h2>
                Este campo muestra la <b>fecha</b> en la que se da inicio al 
                proyecto.
                """,
                6: """
                <h2>Fecha de cierre del proyecto</h2>
                Este campo muestra la <b>fecha</b> en la que se 
                cierra/cancela al proyecto.
                """,
                7: """
                <h2>Motivo de cierre</h2>
                Este campo muestra el <b>motivo</b> por el que se 
                cierra/cancela al proyecto.
                """,
                8: """
                <h2>Descripción</h2>
                Este campo muestra la <b>descripción</b> del proyecto.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
