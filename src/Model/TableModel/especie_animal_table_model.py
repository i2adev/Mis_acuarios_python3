"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/03/2026
Comentarios:
    Módulo que contiene el modelo de visualización de la tabla de ESPECIE 
    ANIMAL. Este módulo se encarga de dar formato a los datos de la tabla.
"""
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

from Model.Entities.especie_animal_entity import EspecieAnimalEntity


class EspecieAnimalTableModel(QAbstractTableModel):
    """
    Clase que controla la visualización de la lista de especies animales.
    """

    def __init__(self, data: list[EspecieAnimalEntity]):
        """ Constructor de la clase. """

        super().__init__()
        self.data = data
        self._headers = ["ID", "#", "REINO", "FILO", "CLASE", "ORDEN",
                         "FAMILIA", "GÉNERO", "ESPECIE", "NOMBRE CIENTÍFICO",
                         "NOMBRE COMÚN", "HIBRIDA", "NOMBRE HIBRIDA",
                         "GRUPO TAXONÓMICO", "PH", "KH", "GH", "TEMPERATURA",
                         "ORIGEN", "TAMAÑO", "COMPORTAMIENTO", "DIETA",
                         "NIVEL NADO", "DESCRIPCIÓN"]

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
            return entidad.filo
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
            return entidad.es_hibrida
        elif columna == 12:
            return entidad.nombre_especie_hirida
        elif columna == 13:
            return entidad.id_grupo_taxonomicvo
        elif columna == 14:
            return entidad.ph_min
        elif columna == 15:
            return entidad.kh_min
        elif columna == 16:
            return entidad.gh_min
        elif columna == 17:
            return entidad.temp_min
        elif columna == 18:
            return entidad.origen
        elif columna == 19:
            return entidad.tamano_cm
        elif columna == 20:
            return entidad.id_comportamiento
        elif columna == 21:
            return entidad.id_dieta
        elif columna == 22:
            return entidad.id_nivel_nado
        elif columna == 23:
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
                <h2>Identificador de la especie animal</h2>
                Este campo muestra el <b>ID</b> de la especie animal.
                """,
                1: """
                <h2>Número correlativo de la especie animal</h2>
                Este campo muestra el <b>número correlativo</b> de la 
                especie animal.
                """,
                2: """
                <h1>Reino</h1>
                Taxonomía: Reino al que pertenece la especie.""",
                3: """            
                <h1>Filo</h1>
                Taxonomía: Filo al que pertenece la especie.
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
                <h1>Especie híbrida</h1>
                En esta columna se especifica sí la especie es el resultado de la 
                cria artificial.
                """,
                12: """
                <h1>Nombre de la especie híbrida</h1>
                En esta columna se muestra el nombre que se le ha dado a la 
                especie híbrida.
                """,
                13: """
                <h1>Grupo taxonómico</h1>
                En esta columna se muestra el <b>grupo taxonómico</b> al que 
                pertenece la especie.
                """,
                14: """
                <h1>PH</h1>
                En esta columna se muestra el rango de PH que tolera la especie.
                """,
                15: """
                <h1>KH</h1>
                En esta columna se muestra el rango de KH que tolera la especie.
                """,
                16: """
                <h1>GH</h1>
                En esta columna se muestra el rango de GH que tolera la especie.
                """,
                17: """
                <h1>Temperatura</h1>
                En esta columna se muestra el rango de temperatura que tolera la 
                especie.
                """,
                18: """
                <h1>Origen</h1>
                En esta columna se muestra el origen donde se encuentra la 
                especie en la naturaleza.
                """,
                19: """
                <h1>Tamaño</h1>
                En esta columna se muestra el <b>tamaño máximo</b> que que 
                alcanza la especie cuando llega a edad adulta.
                """,
                20: """
                <h1>Comportamiento</h1>
                En esta columna se muestra el <b>comportamiento</b> que exhibe la 
                especie en el acuario.
                """,
                21: """
                <h1>Dieta</h1>
                En esta columna se muestra la <b>dieta</b> con la que se 
                alimenta la especie.
                """,
                22: """
                <h1>Nivel de nado</h1>
                En esta columna se muestra el <b>nivel</b> por el que se mueve la 
                espècie en el acuario.
                """,
                23: """
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
