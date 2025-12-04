"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/11/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de FILTRO. 
    Este módulo se encarga de dar formato a los datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.filtro_entity import FiltroEntity


class FiltroTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de acuarios.
    """

    def __init__(self, data: list[FiltroEntity]):
        super().__init__()
        self.data = data

        self._headers = ([
            "ID", "#", "MARCA", "MODELO", "TIPO FILTRO", "TERMO.",
            "NUMERO SERIE", "VOLUMEN ACUARIO", "CAUDAL", "ALTURA BOMBEO",
            "CONSUMO FILTRO", "CONSUMO CALENTADOR", "VOL. FILTRANTE.",
            "DIMENSIONES (cm)", "F.COMPRA", "F. BAJA.", "DISP.", "MOTIVO BAJA",
            "DESCRIPCIÓN"
        ])

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """
        Devuelve el dato de una de las celdas.
        Parámetros:
        :param index: Índice de la column
        :param role: Rol de la _______
        """
        
        if not index.isValid():
            return None

        entidad = self.data[index.row()]
        column = index.column()

        # --- CENTRADO ---
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if column in (1, 5, 8, 9, 10, 11, 12):
                return Qt.AlignmentFlag.AlignCenter

        # --- CHECKBOX TERMOFILTRO ---
        if column == 5:
            if role == Qt.ItemDataRole.CheckStateRole:
                return Qt.CheckState.Checked if entidad.es_thermo == 1 else Qt.CheckState.Unchecked
            if role == Qt.ItemDataRole.DisplayRole:
                return ""  # MUY IMPORTANTE: evita mostrar 0/1
            return None

        # --- CHECKBOX DISPONIBLE ---
        if column == 16:
            if role == Qt.ItemDataRole.CheckStateRole:
                disponible = entidad.fecha_baja in (None, "")
                return Qt.CheckState.Checked if disponible else Qt.CheckState.Unchecked
            return None

        # --- SOLO DISPLAY PARA EL RESTO ---
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if column == 0:  # ID del filtro
            return entidad.id
        elif column == 1:  # Número correlativo de filtro
            return entidad.num
        elif column == 2:  # Marca de filtro
            return entidad.id_marca
        elif column == 3:  # Modelo de filtro
            return entidad.modelo
        elif column == 4:  # Tipo de filtro
            return entidad.id_tipo
        elif column == 6:  # Número de serie
            return entidad.num_serie
        elif column == 7:  # Volumen mínimo del acuario recomendado
            return entidad.vol_min_acuario
        elif column == 8:  # Volumen máximo del acuario recomendado
            return entidad.caudal
        elif column == 9:  # Altura máxima de bombeo
            return entidad.altura_bombeo
        elif column == 10:  # Consumo del filtro
            return entidad.consumo
        elif column == 11:  # Consumo del calentador
            return entidad.consumo_calentador
        elif column == 12:  # Volumen de material filtrante
            return entidad.vol_filtrante
        elif column == 13:  # Dimensiones del acuario
            return entidad.ancho
        elif column == 14:  # Fecha de compra del filtro
            return entidad.fecha_compra
        elif column == 15:  # Fecha de baja del filtro
            return entidad.fecha_baja
        elif column == 16:  # Filtro disponible?
            return entidad.fecha_baja
        elif column == 17:  # Motivo de la baja del filtro
            return entidad.motivo_baja
        elif column == 18:  # Descripción del filtro
            return entidad.descripcion
        else:
            return None

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):

        # Tooltip para cada column
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: "Identificador del filtro",
                1: "Número correlativo del filtro",
                2: "Marca del filtro",
                3: "Modelo del filtro",
                4: "Tipo de filtro",
                5: "Especifica si se trata de un termofiltro",
                6: "Número de serie",
                7: "Volumen de acuario recomendado por el fabricante ("
                   "desde/hasta)",
                8: "Caudal que es capaz de mover la bomba (litros/hora)",
                9: "Altura a la que es capaz de levantar el agua la bomba",
                10: "Consumo eléctrico del filtro (w)",
                11: "Consumo eléctrico del calentador del filtro (w)",
                12: "Volumen de material filtrante que puede albergar el "
                    "filtro (litros)",
                13: "Dimensiones del filtro (ancho x fondo x alto) (cm)",
                14: "Fecha de compra dle filtro",
                15: "Fecha de baja del filtro",
                16: "¿Está disponible el filtro?",
                17: "Motivo de baja del filtro",
                18: "Descripción general"
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

        # Número de fila
        return str(section + 1)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags

        if index.column() == 5 or index.column() == 16:
            return (
                    Qt.ItemFlag.ItemIsEnabled |
                    Qt.ItemFlag.ItemIsUserCheckable |
                    Qt.ItemFlag.ItemIsSelectable
            )

        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
