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

    sql = """
    SELECT  F.ID_FILTRO AS ID,
          ROW_NUMBER() OVER(ORDER BY MC.MARCA, F.MODELO) AS NUM,
          MC.MARCA AS MARCA,
          F.MODELO AS MODELO,
          TF.TIPO_FILTRO AS TIPO_FILTRO,
          F.ES_THERMOFILTRO AS TERMOFILTRO,
          F.NUMERO_SERIE AS NUMERO_SERIE,
          F.VOLUMEN_MIN_ACUARIO || '/' || F.VOLUMEN_MAX_ACUARIO AS 
          VOLUMEN_ACUARIO,
          F.CAUDAL AS CAUDAL,
          F.ALTURA_BOMBEO AS ALTURA_BOMBEO,
          F.CONSUMO AS CONSUMO,
          F.CONSUMO_CALENTADOR AS CONSUMO_CALENTADOR,
          F.VOLUMEN_FILTRANTE AS VOLUMEN_FILTRANTE,
          F.ANCHO || 'x' || F.FONDO || 'x' || F.ALTO AS DIMENSIONES,
          F.FECHA_INSTALACION AS FECHA_INSTALACIÓN,
          F.FECHA_BAJA AS FECHA_BAJA,
          F.MOTIVO_BAJA AS MOTIVO_BAJA,
          F.DESCRIPCION AS DESCRIPCIÓN
    FROM  FILTROS F
    LEFT JOIN MARCAS_COMERCIALES MC ON F.ID_MARCA = MC.ID_MARCA
    LEFT JOIN TIPOS_FILTRO TF ON F.ID_TIPO = TF.ID_TIPO
    """

    def __init__(self, data: list[FiltroEntity]):
        super().__init__()
        self.data = data

        self._headers = ([
            "ID", "#", "MARCA", "MODELO", "TIPO FILTRO", "NUMERO SERIE",
            "VOLUMEN ACUARIO", "CAUDAL", "ALTURA BOMBEO", "CONSUMO FILTRO",
            "CONSUMO CALENTADOR", "VOL. FILTRANTE.", "DIMENSIONES (cm)",
            "F.COMPRA", "F. BAJA.", "MOTIVO BAJA", "DESCRIPCIÓN"
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

        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        entidad = self.data[index.row()]
        column = index.column()

        if column == 0:
            return entidad.id  # el ID de fila
        elif column == 1:
            return entidad.num  # Número de la fila
        elif column == 2:
            return entidad.id_marca  # Marca
        elif column == 3:
            return entidad.modelo  # Modelo
        elif column == 4:
            return entidad.id_tipo  # Tipo de filtro
        elif column == 5:
            return entidad.es_thermo  # Es termofiltro
        elif column == 6:
            return entidad.num_serie  # Número de serie
        elif column == 7:
            return entidad.vol_min_acuario  # Volumen de acuario
        elif column == 8:
            return entidad.caudal  # Caudal del filtro
        elif column == 9:
            return entidad.altura_bombeo  # Altura de bombeo
        elif column == 10:
            return entidad.consumo  # Consumo de la bomba
        elif column == 11:
            return entidad.consumo_calentador  # COnsumo del calentador
        elif column == 12:
            return entidad.vol_filtrante  # Volumen de material filtrante
        elif column == 13:
            return entidad.ancho  # Dimensiones del filtro
        elif column == 14:
            return entidad.fecha_compra  # Fecha de compra del filtro
        elif column == 15:
            return entidad.fecha_baja  # Fecha de baja del filtro
        elif column == 16:
            return entidad.motivo_baja  # Motivo de la baja
        elif column == 17:
            return entidad.descripcion  # Descripción del filtro

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
                16: "Motivo de baja del filtro",
                17: "Descripción general"
            }
            return tooltips.get(section, "")

        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]

        # Número de fila
        return str(section + 1)
