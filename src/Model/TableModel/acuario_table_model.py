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
        super().__init__()
        self.data = data

        # Añadimos la columna CICL. después de "F. F. CICLADO"
        self._headers = ([
            "ID", "#", "PROYECTO", "COLOR", "NOMBRE", "URNA",
            "TIPO", "VOLUMEN", "F. MONTAJE", "F. I. CICLADO",
            "F. F. CICLADO", "CICL.", "UBICACIÓN", "F.DESMONTAJE",
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

        # === Columna del CHECKBOX (CICL. = col 11) ===
        if col == 11:
            if role == Qt.ItemDataRole.CheckStateRole:
                ciclado = entidad.fecha_fin_ciclado not in (None, "")
                return Qt.CheckState.Checked if ciclado else Qt.CheckState.Unchecked
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
        elif col == 14:
            return entidad.motivo_desmontaje
        elif col == 15:
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

        # Resto columnas → seleccionables
        return (Qt.ItemFlag.ItemIsEnabled |
                Qt.ItemFlag.ItemIsSelectable)

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):

        # Tooltip para cada columna
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: "Identificador del acuario",
                1: "Identificador del proyecto",
                2: "Número interno",
                3: "Código de color",
                4: "Nombre del acuario",
                5: "Identificador de la urna",
                6: "Tipo de acuario",
                7: "Volumen neto del acuario",
                8: "Fecha de montaje",
                9: "Inicio de ciclado",
                10: "Fin de ciclado",
                11: "Ciclado completado",
                12: "Ubicación del acuario",
                13: "Fecha de desmontaje",
                14: "Motivo del desmontaje",
                15: "Descripción general"
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

        # Número de fila
        return str(section + 1)

# def brakdown_volumes(self, volumes: str) -> str:
#     """
#     Desmonta la celda del volumen y devuelve el volumen neto
#     :param volumes: Cadena que representa las dimensiones del acuario
#     """
#     if not volumes:
#         return ""
#
#     lista = volumes.split("/")
#     volumen_neto = lista[1]
#
#     return volumen_neto
