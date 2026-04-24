"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/04/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de ESPECIE
    VEGETAL. Este módulo se encarga de dar formato a los datos de la tabla.
"""
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from ModuloMaestro.Model.Entities.especie_vegetal_entity import \
    EspecieVegetalEntity


class EspecieVegetalTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de especies animales.
    """

    def __init__(self, data: list[EspecieVegetalEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "REINO", "REINO", "CLASE", "ORDEN",
                         "FAMILIA", "GÉNERO", "ESPECIE", "NOMBRE CIENT.",
                         "NOMBRE COMÚN", "PH", "KH", "GH", "TEMP.",
                         "ORIGEN", "POSICIÓN", "ILUMINACIÓN", "CO2",
                         "CRECIMIENTO", "DIFICULTAD", "DESCRIPCIÓN"]

    def rowCount(self, parent=QModelIndex()):
        """ Devuelve el número de filas de la lista de tipos de filtro. """

        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        """ Devuelve el número de columnas que tiene la lista. """

        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """
        Devuelve el dato de una de las celdas.
        Parámetros:
        :param index: Índice de la columna
        :param role: Rol de la _______
        """

        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        entidad = self.data[index.row()]
        columna = index.column()

        if columna == 0:
            return entidad.id  # el ID de fila
        elif columna == 1:
            return entidad.num  # Número de la fila
        elif columna == 2:
            return entidad.reino
        elif columna == 3:
            return entidad.division
        elif columna == 4:
            return entidad.clase
        elif columna == 5:
            return entidad.orden
        elif columna == 6:
            return entidad.familia
        elif columna == 7:
            return entidad.genero
        elif columna == 8:
            return entidad.especie
        elif columna == 9:
            return entidad.nombre_cientifico
        elif columna == 10:
            return entidad.nombre_comun
        elif columna == 11:
            return entidad.ph_min
        elif columna == 12:
            return entidad.kh_min
        elif columna == 13:
            return entidad.gh_min
        elif columna == 14:
            return entidad.temp_min
        elif columna == 15:
            return entidad.origen
        elif columna == 16:
            return entidad.id_posicion_acuario
        elif columna == 17:
            return entidad.id_req_iluminacion
        elif columna == 18:
            return entidad.id_req_co2
        elif columna == 19:
            return entidad.id_tasa_crecimiento
        elif columna == 20:
            return entidad.id_dificultad
        elif columna == 21:
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
                <h2>Identificador de la especie vegetal</h2>
                Este campo muestra el <b>ID</b> de la especie vegetal.
                """,
                1: """
                <h2>Número correlativo de la especie vegetal</h2>
                Este campo muestra el <b>número correlativo</b> de la 
                especie vegetal.
                """,
                2: """
                <h1>Reino</h1>
                Taxonomía: Reino al que pertenece la especie.""",
                3: """            
                <h1>División</h1>
                Taxonomía: División al que pertenece la especie.
                """,
                4: """
                <h1>Clase</h1>
                Taxonomía: Clase al que pertenece la especie.
                """,
                5: """
                <h1>Clase</h1>
                Taxonomía: Clase al que pertenece la especie.
                """,
                6: """
                <h1>Familia</h1>
                Taxonomía: Familia al que pertenece la especie.
                """,
                7: """
                <h1>Género</h1>
                Taxonomía: Género al que pertenece la especie.
                """,
                8: """
                <h1>Especie</h1>
                Taxonomía: Especie al que pertenece el animal.
                """,
                9: """
                <h1>Nombre científico</h1>
                En esta columna se muestra el <b>nombre científico</b> de la 
                especie.
                """,
                10: """
                <h1>Nombre común</h1>
                En esta columna se muestra el <b>nombre común</b> con el que se 
                conoce la especie.
                """,
                11: """
                <h1>PH</h1>
                En esta columna se muestra el rango de PH que tolera la especie.
                """,
                12: """
                <h1>KH</h1>
                En esta columna se muestra el rango de KH que tolera la especie.
                """,
                13: """
                <h1>GH</h1>
                En esta columna se muestra el rango de GH que tolera la especie.
                """,
                14: """
                <h1>Temperatura</h1>
                En esta columna se muestra el rango de temperatura que tolera la 
                especie.
                """,
                15: """
                <h1>Origen</h1>
                En esta columna se muestra el origen donde se encuentra la 
                especie en la naturaleza.
                """,
                16: """
                <h1>Posición</h1>
                En esta columna se muestra la <b>posición en el acuario</b> 
                en la que se pone la planta.
                """,
                17: """
                <h1>Requerimiento de iluminación</h1>
                En esta columna se muestra el <b>requerimiento de 
                iluminación</b> que tiene la planta.
                """,
                18: """
                <h1>Requerimiento de CO<sub>2</sub></h1>
                En esta columna se muestra el <b>requerimiento de 
                CO<sub>2</sub></b> que tiene la planta.
                """,
                19: """
                <h1>Crecimiento</h1>
                En esta columna se muestra la <b>tasa de crecimiento</b> de 
                la planta.
                """,
                20: """
                <h1>Dificultad</h1>
                En esta columna se muestra la <b>Dificultad de 
                mantenimiento</b> que tiene la planta.
                """,
                21: """
                <h2>Descripción</h2><br>
                En esta columna se muestra una breve descripción de la especie.
                """,
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        else:
            return str(section + 1)
