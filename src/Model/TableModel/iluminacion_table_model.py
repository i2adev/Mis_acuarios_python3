"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/02/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de
    ILUMINACIONESX. Este módulo se encarga de dar formato a los datos de la
    tabla.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.iluminacion_entity import IluminacionEntity


class IluminacionTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de acuarios.
    """

    def __init__(self, data: list[IluminacionEntity]):
        super().__init__()
        self.data = data

        # Encabezados de columna de la tabla
        self._headers = ([
            "ID", "#", "MARCA", "MODELO", "NÚM. SERIE", "TIPO",
            "POTENCIA", "F.L", "TEMP.", "VIDA UTIL",
            "LONGITUD", "ANCHURA", "CONTROL", "I.R", "E.C",
            "F. ALTA", "F. BAJA", "MOTIVO BAJA", "DESCRIPCIÓN"
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

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if col == 0:
            return entidad.id
        elif col == 1:
            return entidad.num
        elif col == 2:
            return entidad.id_marca
        elif col == 3:
            return entidad.modelo
        elif col == 4:
            return entidad.num_serie
        elif col == 5:
            return entidad.id_tipo_iluminacion
        elif col == 6:
            return entidad.potencia
        elif col == 7:
            return entidad.flujo_luminico
        elif col == 8:
            return entidad.temperatura
        elif col == 9:
            return entidad.vida_util
        elif col == 10:
            return entidad.longitud
        elif col == 11:
            return entidad.anchura
        elif col == 12:
            return entidad.id_control_iluminacion
        elif col == 13:
            return entidad.intensidad_regulable
        elif col == 14:
            return entidad.espectro_completo
        elif col == 15:
            return entidad.fecha_alta
        elif col == 16:
            return entidad.fecha_baja
        elif col == 17:
            return entidad.motivo_baja
        elif col == 18:
            return entidad.descripcion

        return None

    def headerData(self, section, orientation,
                   role=Qt.ItemDataRole.DisplayRole):

        # Tooltip para cada columna
        if role == Qt.ItemDataRole.ToolTipRole:
            tooltips = {
                0: """
                <h2>Identificador de la luminaria</h2>
                Este campo muestra el ID de la luminaria.
                """,
                1: """
                <h2>Número correlativo de la luminaria</h2>
                Este campo muestra el número correlativo de la luminaria.
                """,
                2: """
                <h2>Marca de la luminaria</h2>
                Este campo muestra la marca de la luminaria.
                """,
                3: """
                <h2>Modelo de la luminaria</h2>
                Este campo muestra el modelo de la luminaria.
                """,
                4: """
                <h2>Número de serie</h2>
                Este campo muestra el <b>número de serie</b> de la luminaria
                """,
                5: """
                <h2>Tipo de iluminación</h2>
                Este campo muestra el <b>tipo de iluminación</b> de la 
                luminaria
                """,
                6: """
                <h2>Potencia</h2>
                Este campo muestra la <b>potencia lumínica en vatios (w)</b> 
                de la luminaria.
                """,
                7: """
                <h2>Flujo lumínico</h2>
                Este campo muestra el <b>flujo lumínico en lúmenes/litro 
                (lm/l)</b> de la luminaria.
                """,
                8: """
                <h2>Temperatura de color</h2>
                Este campo muestra la <b>temperatura de color en grados 
                kelvin (K)</b> de la luminaria.
                """,
                9: """
                <h2>Vida util</h2>
                Este campo muestra la <b>vida util en horas</b> de la 
                luminaria.
                """,
                10: """
                <h2>Longitud</h2>
                Este campo muestra la <b>longitud en cm</b> de la luminaria.
                """,
                11: """
                <h2>Anchura</h2>
                Este campo muestra la <b>anchura en cm</b> de la luminaria.
                """,
                12: """
                <h2>Control de iluminación</h2>
                Este campo muestra el <b>tipo de control</b> de la luminaria.
                """,
                13: """
                <h2>Intensidad regulable</h2>
                Este campo especifica si la luminaria cuenta con la 
                capacidad de regular la intensidad de la iluminación.
                """,
                14: """
                <h2>Espectro completo</h2>
                Este campo muestra si la luminaria emite la luz en un 
                espectro completo.
                """,
                15: """
                <h2>Fecha de alta</h2>
                En este campo se muestra la fecha de alta de la luminaria
                """,
                16: """
                <h2>Fecha de baja</h2>
                En este campo se muestra la fecha de baja de la luminaria
                """,
                17: """
                <h2>Motivo de la baja</h2>
                En este campo se muestra el motivo de la baja de la 
                luminaria en caso de que haya sido dado de baja.
                luminaria en caso de que haya sido dado de baja.
                """,
                18: """
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
