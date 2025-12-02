"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Comentarios:
    Módulo que contiene la entidad SUBCATEGORÍA DE INCIDENCIA.
"""
from Model.Entities.base_entity import BaseEntity


class SubcategoriaIncidenciaEntity(BaseEntity):
    """ Entidad de la categoría de incidencia. """

    # ANotaciones de tipo
    id: int | None
    num: int | None
    id_categoria: int | None
    subcategoria: str | None
    observaciones: str | None

    def __init__(self, id=None, num=None, id_categoria=None,
                 subcategoria=None, observaciones=None):
        """
        Constructor de clase:

        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param id_categoria: ID de la ategoría de la incidencia
        :param subcategoria: Subcategoria de incidencia
        :param observaciones: Observaciones de la incidencia
        """

        super().__init__()

        # Inicializamos los atributos
        self.__id = id
        self.__num = num
        self.__id_categoria = id_categoria
        self.__subcategoria = subcategoria
        self.__observaciones = observaciones

    @property
    def id(self) -> int | None:
        """ Id de la entidad. """
        return self.__id

    @id.setter
    def id(self, new_id) -> None:
        """ Id de la entidad. """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Número correlativo de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num) -> None:
        """ Número correlativo de la entidad. """
        self.__num = new_num

    @property
    def id_categoria(self) -> int | None:
        """ Id de la categoría de incidencia. """
        return self.__id_categoria

    @id_categoria.setter
    def id_categoria(self, new_id) -> None:
        """ Id de la categoría de incidencia. """
        self.__id_categoria = new_id

    @property
    def subcategoria(self) -> str | None:
        """ Subcategoría de incidencia. """
        return self.__subcategoria

    @subcategoria.setter
    def subcategoria(self, new_subcategoria) -> None:
        """ Subcategoria de incidencia. """
        self.__subcategoria = new_subcategoria

    @property
    def observaciones(self) -> str | None:
        """ Observaciones de la incidencia. """
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones) -> None:
        """ Observaciones de la incidencia. """
        self.__observaciones = new_observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            CATEGORÍA:      {self.id_categoria}
            SUBCATEGORÍA:   {self.subcategoria}
            OBSERVACIONES:  {self.observaciones}
        """
