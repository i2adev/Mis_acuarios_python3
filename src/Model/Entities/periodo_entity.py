"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      06/04/2026

Comentarios:
    Módulo que contiene la entidad PERIODO.
"""
from Model.Entities.base_entity import BaseEntity


class PeriodoEntity(BaseEntity):
    """ Entidad de periodo. """

    def __init__(self, id: int | None = None, num: int | None = None,
                 periodo: str | None = None) -> None:
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param num: Número de la entidad.
        :param periodo: Periodo de tiempo.
        """

        self.__id = id
        self.__num = num
        self.__periodo = periodo

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
    def periodo(self) -> str:
        """ Periodo de tiempo. """
        return self.__periodo

    @periodo.setter
    def periodo(self, new_periodo: str):
        """ Requerimiento de iluminación. """
        self.__periodo = new_periodo

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self):
        return f""""
            ID:         {self.id}
            PERIODO:    {self.periodo}
        """
