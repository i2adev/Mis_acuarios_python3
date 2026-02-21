"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de ACUARIOS. 
    Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt6.QtGui import QColor

from Model.Entities.acuario_entity import AcuarioEntity


class AcuarioTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de acuarios.
    """

    def __init__(self, data: list[AcuarioEntity]):
        super().__init__()
        self.data = data

        # Encabezados de columna de la tabla
        self._headers = ([
            "ID", "#", "PROYECTO", "COLOR", "NOMBRE", "URNA",
            "TIPO", "VOLUMEN", "F. MONTAJE", "F. I. CICLADO",
            "F. F. CICLADO", "CICL.", "UBICACIÓN", "F.DESMONTAJE", "MONT.",
            "MOTIVO DESMONTAJE", "DESCRIPCIÓN"
        ])

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        entidad = self.data[index.row()]
        col = index.column()

        if col == 4:  # NOMBRE
            if role == Qt.ItemDataRole.DisplayRole:
                return entidad.nombre
            elif role == Qt.ItemDataRole.DecorationRole:
                return QColor(entidad.cod_color)
            return None

        # === Columna del CHECKBOX (CICL. = col 11) ===
        if col == 11:
            if role == Qt.ItemDataRole.CheckStateRole:
                ciclado = entidad.fecha_fin_ciclado not in (None, "")
                return Qt.CheckState.Checked if ciclado else Qt.CheckState.Unchecked
            return None

        # === Columna del CHECKBOX (MONT. = col 11) ===
        if col == 14:
            if role == Qt.ItemDataRole.CheckStateRole:
                mounted = entidad.fecha_desmontaje in (None, "")
                return Qt.CheckState.Checked if mounted else Qt.CheckState.Unchecked
            return None

        # === Resto de columnas (DisplayRole) ===
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if col == 0:
            return entidad.id
        elif col == 1:
            return entidad.num
        elif col == 2:
            return entidad.id_proyecto
        elif col == 3:
            return entidad.cod_color
        elif col == 4:
            return entidad.nombre
        elif col == 5:
            return entidad.id_urna
        elif col == 6:
            return entidad.id_tipo
        elif col == 7:
            return entidad.volumen_neto
        elif col == 8:
            return entidad.fecha_montaje
        elif col == 9:
            return entidad.fecha_inicio_ciclado
        elif col == 10:
            return entidad.fecha_fin_ciclado
        elif col == 12:
            return entidad.ubicacion_acuario
        elif col == 13:
            return entidad.fecha_desmontaje
        elif col == 15:
            return entidad.motivo_desmontaje
        elif col == 16:
            return entidad.descripcion

        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags

        col = index.column()

        # Checkbox → no editable pero sí seleccionable
        if col == 11:
            return (Qt.ItemFlag.ItemIsEnabled |
                    Qt.ItemFlag.ItemIsSelectable)

        if col == 14:
            return (Qt.ItemFlag.ItemIsEnabled |
                    Qt.ItemFlag.ItemIsSelectable)

        # Resto columnas → seleccionables
        return (Qt.ItemFlag.ItemIsEnabled |
                Qt.ItemFlag.ItemIsSelectable)

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):

        # Tooltip para cada columna
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador del acuario</h2>
                Este campo muestra el ID del acuario.
                """,
                1: """
                <h2>Identificador del proyecto</h2>
                Este campo muestra el ID del proyecto.
                """,
                2: """
                <h2>Número correlativo de acuario</h2>
                Este campo muestra el número correlativo de acuario.
                """,
                3: """
                <h2>Color del acuario</h2>
                Este campo muestra el color asignado al acuario.
                """,
                4: """
                <h2>Nombre del acuario</h2>
                Este campo muestra el nombre distintivo que se le ha 
                asignado al acuario.
                """,
                5: """
                <h2>Urna del acuario</h2>
                Este campo muestra la urna del acuario.
                """,
                6: """
                <h2>Tipo de acuario</h2>
                Este campo muestra el tipo de acuario.
                """,
                7: """
                <h2>Volumen del acuario</h2>
                Este campo muestra el volumen del acuario. La primera cifra 
                muestra el volumen bruto del acuario, y la segunda cifra, 
                separada por una barra, muestra el volumen neto.
                """,
                8: """
                <h2>Fecha de montaje</h2>
                Este campo muestra la fecha en la que se ha montado el 
                acuario.
                """,
                9: """
                <h2>Inicio de ciclado</h2>
                Este campo muestra la fecha en la que se ha llenado el 
                acuario y ha comenzado el proceso de ciclado del mismo.
                """,
                10: """
                <h2>Fin de ciclado</h2>
                Este campo muestra la fecha en la que se ha finalizado la 
                fase de ciclado.
                """,
                11: """
                <h2>Ciclado completado</h2>
                Este campo muestra si se ha completado el ciclado del 
                acuario. Si tiene palometa, ha finalizado el ciclado, 
                en caso contrario, no.
                """,
                12: """
                <h2>Ubicación del acuario</h2>
                Este campo muestra en que parte de la casa se ha 
                instalado el acuario.
                """,
                13: """
                <h2>Fecha de desmontaje</h2>
                Este campo muestra la fecha en la que se ha desmontado el 
                acuario.
                """,
                14: """
                <h2>¿Está montado el acuario?</h2>
                Este campo muestra si el acuario se encuentra en uso, 
                es decir que sigue montado.. Si tiene palometa, se encuentra 
                montado y en uso, en caso contrario, no.
                """,
                15: """
                <h2>Motivo del desmontaje</h2>
                Este campo muestra el motivo por el que se ha desmontado el 
                acuario.
                """,
                16: """
                <h2>Descripción</h2>
                Este camo muestra la descripción general del acuario.
                """
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

        # Número de fila
        return str(section + 1)
