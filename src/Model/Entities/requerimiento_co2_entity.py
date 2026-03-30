"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/03/2026

Comentarios:
    Módulo que contiene la entidad REQUERIMIENTO CO2.
"""
from Model.Entities.base_entity import BaseEntity


class RequerimientoCO2Entity(BaseEntity):
    """ Entidad de requerimiento de CO2. """

    def __init__(self, id: int | None = None, num: int | None = None,
                 requerimiento: str | None = None,
                 descripcion: str | None = None) -> None:
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param num: Número de la entidad.
        :param requerimiento: Requerimiento de CO2.
        :param descripcion: Descripción del requerimiento.
        """

        self.__id = id
        self.__num = num
        self.__requerimiento = requerimiento
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
    def requerimiento(self) -> str:
        """ Requerimiento de CO2. """
        return self.__requerimiento

    @requerimiento.setter
    def requerimiento(self, new_requerimiento: str):
        """ Requerimiento de CO2. """
        self.__requerimiento = new_requerimiento

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
            REQUERIMIENTO:  {self.requerimiento}
            DESCRIPCIÓN:    {self.descripcion}
        """
