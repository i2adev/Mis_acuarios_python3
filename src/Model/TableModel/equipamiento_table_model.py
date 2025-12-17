"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      17/12/2025
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de
    EQUIPAMIENTOS. Este módulo se encarga de dar formato a los datos de la
    tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.equipamiento_entity import EquipamientoEntity


class EquipamientoTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de equipamientos.
    """

    def __init__(self, data: list[EquipamientoEntity]):
        super().__init__()
        self.data = data

        self._headers = ([
            "ID", "#", "CATEGORÍA", "MARCA", "MODELO", "NUM. SERIE",
            "ALTTA", "BAJA", "MOTIVO DE LA BAJA", "DESCRIPCIÓN"
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

        # # --- CENTRADO ---
        # if role == Qt.ItemDataRole.TextAlignmentRole:
        #     if column in (1, 5, 8, 9, 10, 11, 12):
        #         return Qt.AlignmentFlag.AlignCenter

        # # --- CHECKBOX TERMOFILTRO ---
        # if column == 5:
        #     if role == Qt.ItemDataRole.CheckStateRole:
        #         return Qt.CheckState.Checked if entidad.es_thermo == 1 else Qt.CheckState.Unchecked
        #     if role == Qt.ItemDataRole.DisplayRole:
        #         return ""  # MUY IMPORTANTE: evita mostrar 0/1
        #     return None

        # # --- CHECKBOX DISPONIBLE ---
        # if column == 16:
        #     if role == Qt.ItemDataRole.CheckStateRole:
        #         disponible = entidad.fecha_baja in (None, "")
        #         return Qt.CheckState.Checked if disponible else Qt.CheckState.Unchecked
        #     return None

        # --- SOLO DISPLAY PARA EL RESTO ---
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if column == 0:  # ID del filtro
            return entidad.id
        elif column == 1:  # Número correlativo de filtro
            return entidad.num
        elif column == 2:  # Categoría del equipo
            return entidad.id_categoria
        elif column == 3:  # Marca del equipo.
            return entidad.id_marca
        elif column == 4:  # Modelo del equipo
            return entidad.modelo
        elif column == 5:  # Número de serie
            return entidad.numero_serie
        elif column == 6:  # Fecha de alta del equipo
            return entidad.fecha_alta
        elif column == 7:  # Fecha de baja del equipo
            return entidad.fecha_baja
        elif column == 8:  # Motivo de la baja del filtro
            return entidad.motivo_baja
        elif column == 9:  # Descripción del filtro
            return entidad.descripcion
        else:
            return None

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):

        # Tooltip para cada column
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador del equipo</h2>
                Este campo muestra el <b>ID</b> del equipo.
                """,
                1: """
                <h2>Número correlativo del equipo</h2>
                Este campo muestra el <b>número correlativo</b> del equipo.
                """,
                2: """
                <h2>Categoria del equipo</h2>
                Este campo muestra la <b>Categoria</b> a la que pertenece el 
                equipo.
                """,
                3: """
                <h2>Marca del equipo</h2>
                Este campo muestra la <b>marca</b> del equipo
                """,
                4: """
                <h2>Modelo del equipo</h2>
                Este campo muestra el <b>modelo del equipo</b>.
                """,
                5: """
                <h2>Número de serie</h2>
                Este campo muestra el <b>numero de serie</b> del equipo.
                """,
                6: """
                <h2>Fecha de alta</h2>
                Este campo muestra la fecha en la que se ha dado de alta el 
                equipo. 
                """,
                7: """
                <h2>Fecha de baja</h2>
                Este campo muestra la fecha en la que se ha dado de baja al 
                equipo.
                """,
                8: """
                <h2>Motivo de baja</h2>
                Este campo muestra el motivo de la baja del equipo.
                """,
                9: """
                <h2>Descripción</h2>
                Este campo muestra la descripción general del equipo.
                """
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

        # Número de fila
        return str(section + 1)

    # def flags(self, index):
    #     if not index.isValid():
    #         return Qt.ItemFlag.NoItemFlags
    #
    #     if index.column() == 5 or index.column() == 16:
    #         return (
    #                 Qt.ItemFlag.ItemIsEnabled |
    #                 Qt.ItemFlag.ItemIsUserCheckable |
    #                 Qt.ItemFlag.ItemIsSelectable
    #         )
    #
    #     return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
