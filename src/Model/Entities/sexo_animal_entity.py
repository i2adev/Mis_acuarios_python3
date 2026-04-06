"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/04/2026

Comentarios:
    Módulo que contiene la entidad SEXO ANIMAL.
"""
from Model.Entities.base_entity import BaseEntity


class SexoAnimalEntity(BaseEntity):
    """ Entidad del soxo del animal. """

    def __init__(self, id: int | None = None, num: int | None = None,
                 sexo: str | None = None,
                 descripcion: str | None = None) -> None:
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param num: Número de la entidad.
        :param sexo: Sexo del animal.
        :param descripcion: Descripción del sexo del animal.
        """

        self.__id = id
        self.__num = num
        self.__sexo = sexo
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
    def sexo(self) -> str:
        """ Sexo del animal.
        :return: Sexo del animal.
        """
        return self.__sexo

    @sexo.setter
    def sexo(self, new_sexo: str):
        """ Sexo del animal.
        :param new_sexo: Sexo del animal."""
        self.__sexo = new_sexo

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
            ID:          {self.id}
            SEXO:        {self.sexo}
            DESCRIPCIÓN: {self.descripcion}
        """
