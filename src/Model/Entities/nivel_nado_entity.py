"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/03/2026

Comentarios:
    Módulo que contiene la entidad NIVEL DE NADO.
"""

from Model.Entities.base_entity import BaseEntity


class NivelNadoEntity(BaseEntity):
    """ Entidad del nivel de nado. """

    def __init__(self, id: int | None = None, num: int | None = None,
                 nivel_nado: str | None = None,
                 descripcion: str | None = None) -> None:
        """
        Constructor de la clase NivelNadoEntity.
        :param id: ID del nivel de nado.
        :param num: Numero del nivel de nado.
        :param nivel_nado: Nivel de nado.
        :param descripcion: Descripción del nivel de nado.
        """

        self.__id = id
        self.__num = num
        self.__nivel_nado = nivel_nado
        self.__descripcion = descripcion

    # INICIO DE PROPIEDADES --------------------------------------------
    @property
    def id(self) -> int:
        """ ID del nivel de nado. """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ ID del nivel de nado. """
        self.__id = new_id

    @property
    def num(self) -> int:
        """ Numero del nivel de nado. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Numero del nivel de nado. """
        self.__num = new_num

    @property
    def nivel_nado(self) -> str:
        """ Nivel de nado. """
        return self.__nivel_nado

    @nivel_nado.setter
    def nivel_nado(self, new_nivel_nado: str) -> None:
        """ Nivel de nado. """
        self.__nivel_nado = new_nivel_nado

    @property
    def descripcion(self) -> str:
        """ Descripcion del nivel de nado. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str) -> None:
        """ Descripcion del nivel de nado. """
        self.__descripcion = new_descripcion

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self) -> str:
        return f"""
        ID:         {self.id}
        NIVEL:      {self.nivel_nado}
        DESCRICIÓN: {self.descripcion}
        """
