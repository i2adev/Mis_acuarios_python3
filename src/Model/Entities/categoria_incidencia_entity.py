"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Comentarios:
    Módulo que contiene la entidad CATEGORÍA DE INCIDENCIA.
"""
from Model.Entities.base_entity import BaseEntity


class CategoriaIncidenciaEntity(BaseEntity):
    """ Entidad de la categoría de incidencia. """

    # ANotaciones de tipo
    id: int | None
    num: int | None
    categoria_incidencia: str | None
    observaciones: str | None

    def __init__(self, id=None, num=None, categoria_incidencia=None,
                 observaciones=None):
        """
        Constructor de clase:

        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param categoria_incidencia: Categoría de la incidencia
        :param observaciones: Observaciones de la incidencia
        """

        super().__init__()

        # Inicializamos los atributos
        self.__id = id
        self.__num = num
        self.__categoria_incidencia = categoria_incidencia
        self.__observaciones = observaciones

    @property
    def id(self):
        """ Id de la entidad """
        return self.__id

    @id.setter
    def id(self, new_id):
        """ Id de la entidad """
        self.__id = new_id

    @property
    def num(self):
        """ Número correlativo de la entidad """
        return self.__num

    @num.setter
    def num(self, new_num):
        """ Número correlativo de la entidad """
        self.__num = new_num

    @property
    def categoria_incidencia(self):
        """ Categoria de la incidencia """
        return self.__categoria_incidencia

    @categoria_incidencia.setter
    def categoria_incidencia(self, new_categ):
        """ Categoria de la incidencia """
        self.__categoria_incidencia = new_categ

    @property
    def observaciones(self):
        """ Observaciones de la incidencia """
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones):
        """ Observaciones de la incidencia """
        self.__observaciones = new_observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            CATEGORÍA:   {self.categoria_incidencia}
            OBSERVACIONES:  {self.observaciones}
        """
