"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      17/09/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de
    CONTROLADORES DE TEMPERATURA. Este módulo se encarga de dar formato 
    a los datos de la tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from ModuloMaestro.Model.Entities.control_temperatura_entity import \
    ControladorTemperaturaEntity


class ControladorTemperaturaTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de controladores de 
    temperatura..
    """

    def __init__(self, data: list[ControladorTemperaturaEntity]):
        super().__init__()
        self.data = data

        self._headers = ([
            "ID", "#", "TIPO CONTROL", "MARCA", "MODELO", "NUM. SERIE",
            "T. MIN.", "T. MAX.", "CONSUMO", "ALTA", "BAJA",
            "MOTIVO BAJA", "DESCRIPCIÓN"
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

        # --- SOLO DISPLAY PARA EL RESTO ---
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if column == 0:  # ID del controlador de temperatura
            return entidad.id
        elif column == 1:  # Número correlativo de controlador de temperatura
            return entidad.num
        elif column == 2:  # Categoría del controlador de temperatura
            return entidad.id_tipo_control_temperatura
        elif column == 3:  # Marca del controlador de temperatura.
            return entidad.id_marca
        elif column == 4:  # Modelo del controlador de temperatura
            return entidad.modelo
        elif column == 5:  # Número de serie
            return entidad.numero_serie
        elif column == 6:  # Temperatura mínima
            return entidad.temperatura_minima
        elif column == 7:  # Temperatura máxima
            return entidad.temperatura_maxima
        elif column == 8:  # Consumo
            return entidad.consumo
        elif column == 9:  # Fecha de alta del controlador de temperatura
            return entidad.fecha_alta
        elif column == 10:  # Fecha de baja del controlador de temperatura
            return entidad.fecha_baja
        elif column == 11:  # Motivo de la baja del controlador de temperatura
            return entidad.motivo_baja
        elif column == 12:  # Descripción del controlador de temperatura
            return entidad.descripcion
        else:
            return None

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):

        # Tooltip para cada column
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador del controlador de temperatura</h2>
                Este campo muestra el <b>ID</b> del controlador de temperatura.
                """,
                1: """
                <h2>Número correlativo del controlador de temperatura</h2>
                Este campo muestra el <b>número correlativo</b> del controlador de temperatura.
                """,
                2: """
                <h2>Categoria del controlador de temperatura</h2>
                Este campo muestra la <b>Categoria</b> a la que pertenece el 
                controlador de temperatura.
                """,
                3: """
                <h2>Marca del controlador de temperatura</h2>
                Este campo muestra la <b>marca</b> del controlador de temperatura
                """,
                4: """
                <h2>Modelo del controlador de temperatura</h2>
                Este campo muestra el <b>modelo del controlador de temperatura</b>.
                """,
                5: """
                <h2>Número de serie</h2>
                Este campo muestra el <b>numero de serie</b> del controlador de temperatura.
                """,
                6: """
                <h2>Temperatura mínima</h2>
                Esta campo muestra la temperatura minima del controlador de 
                temperatura.
                """,
                7: """
                <h2>Temperatura máxima</h2>
                Esta campo muestra la temperatura máxima del controlador de 
                temperatura.
                """,
                8: """
                <h2>Consumo</h2>
                Esta campo muestra el consumo que tiene el controlador de 
                temperatura.
                """,
                9: """
                <h2>Fecha de alta</h2>
                Este campo muestra la fecha en la que se ha dado de alta el 
                controlador de temperatura. 
                """,
                10: """
                <h2>Fecha de baja</h2>
                Este campo muestra la fecha en la que se ha dado de baja al 
                controlador de temperatura.
                """,
                11: """
                <h2>Motivo de baja</h2>
                Este campo muestra el motivo de la baja del controlador de temperatura.
                """,
                12: """
                <h2>Descripción</h2>
                Este campo muestra la descripción general del controlador de temperatura.
                """
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

        # Número de fila
        return str(section + 1)
