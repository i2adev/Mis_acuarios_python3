"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Comentarios:
    Módulo que contien la entidad TIPO DE FILTRO.
"""

from Model.Entities.base_entity import BaseEntity


class TipoFiltroEntity(BaseEntity):
    """ Entidad del tipo de filtro. """

    # Anotaciones de tipo (atributos con sus tipos esperados)
    id: int | None
    num: int | None
    tipo_filtro: str | None
    observaciones: str | None

    def __init__(self, id: int = None, num: int = None, tipo_filtro:
    str = None, observaciones: str = None):
        """
        Constructor de clase:
            - Parámetro id_tf: Id del tipo de filtro
            - Parámetro num_tf: Número correlativo del tipo de filtro
            - Parámetro tipo_filtro: Cadena con el tipo de filtro.
            - Parámetro descripcion: Cadena con las descripcion
              sobre el tipo de filtro.
        """
        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__tipo_filtro = tipo_filtro
        self.__observaciones = observaciones

    # INICIO PROPIEDADES

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, new_id: int):
        self.__id = new_id

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, new_num: int):
        self.__num = new_num

    @property
    def tipo_filtro(self) -> str:
        return self.__tipo_filtro

    @tipo_filtro.setter
    def tipo_filtro(self, new_tipo_filtro: str):
        self.__tipo_filtro = new_tipo_filtro

    @property
    def observaciones(self) -> str:
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones: str):
        self.__observaciones = new_observaciones

    # FIN PROPIEDADES

    def __str__(self):
        """ Muestra información de la clase. """

        return f"""
            ID:             {self.id}
            NUM:            {self.num}
            TIPO FILTRO:    {self.tipo_filtro}
            OBSERVACIONES:  {self.observaciones:50}
            ------------------------------------------------------------
        """
