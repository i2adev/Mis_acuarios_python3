"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      12/03/2026

Comentarios:
    Módulo que contiene la entidad COMPORTAMIENTO DE FAUNA.
"""

from Model.Entities.base_entity import BaseEntity


class ComportamientoFaunaEntity(BaseEntity):
    """ Entidad del comportamiento de fauna. """

    def __init__(self, id: int = None, num: int = None,
                 comportamiento: str = None, descripcion: str = None):
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param num: Número de la entidad.
        :param comportamiento: Comportamiento del animal.
        :param descripcion: Descripción del comportamiento.
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__comportamiento = comportamiento
        self.__descripcion = descripcion

    # INICIO DE PROPIEDADES --------------------------------------------
    @property
    def id(self) -> int:
        """ Id de la entidad. """
        return self.__id

    @id.setter
    def id(self, new_id: int):
        """ Id de la entidad. """
        self.__id = new_id

    @property
    def num(self) -> int:
        """ Número de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num: int):
        """ Número de la entidad. """
        self.__num = new_num

    @property
    def comportamiento(self) -> str:
        """ Comportamiento del animal. """
        return self.__comportamiento

    @comportamiento.setter
    def comportamiento(self, new_comportamiento: str):
        """ Comportamiento del animal. """
        self.__comportamiento = new_comportamiento

    @property
    def descripcion(self) -> str:
        """ Descripción del comportamiento. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripción del comportamiento. """
        self.__descripcion = new_descripcion

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self):
        return f""""
            ID:             {self.id}
            COMPORTAMIENTO: {self.comportamiento}
            DESCRIPCIÓN:    {self.descripcion}
        """
