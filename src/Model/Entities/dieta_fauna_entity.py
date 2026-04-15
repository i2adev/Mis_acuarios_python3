"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      13/03/2026
Comentarios:
    Módulo que contiene la entidad DIETA DE FAUNA.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class DietaFaunaEntity(BaseEntity):
    """ Entidad de dieta de fauna """

    id: int | None = None
    num: int | None = None
    dieta: str | None = None
    descripcion: str | None = None

    # def __init__(self, id: int = None, num: int = None, dieta: str = None,
    #              descripcion: str = None):
    #     """
    #     Constructor de clase.
    #
    #     Parámetros:
    #     :param id: Id de la entidad.
    #     :param dieta: Dieta de los animales.
    #     :param descripcion: Descripción de la dieta.
    #     """
    #
    #     super().__init__()
    #
    #     # Inicializamos las variables
    #     self.__id = id
    #     self.__num = num
    #     self.__dieta = dieta
    #     self.__descripcion = descripcion
    #
    # # INICIO DE PROPIEDADES --------------------------------------------
    # @property
    # def id(self) -> int:
    #     """ Id de la entidad. """
    #     return self.__id
    #
    # @id.setter
    # def id(self, new_id: int):
    #     """ Id de la entidad. """
    #     self.__id = new_id
    #
    # @property
    # def num(self) -> int:
    #     """ Número de la entidad. """
    #     return self.__num
    #
    # @num.setter
    # def num(self, new_num: int):
    #     """ Número de la entidad. """
    #     self.__num = new_num
    #
    # @property
    # def dieta(self) -> str:
    #     """ Dieta del animal. """
    #     return self.__dieta
    #
    # @dieta.setter
    # def dieta(self, new_dieta: str):
    #     """ Dieta del animal. """
    #     self.__dieta = new_dieta
    #
    # @property
    # def descripcion(self) -> str:
    #     """ Descripción de la dieta """
    #     return self.__descripcion
    #
    # @descripcion.setter
    # def descripcion(self, new_descripcion: str):
    #     """ Descripción de la dieta """
    #     self.__descripcion = new_descripcion
    #
    # # FIN DE PROPIEDADES -----------------------------------------------
    #
    # def __str__(self):
    #     return f""""
    #     ID:         {self.id}
    #     DIETA:      {self.dieta}
    #     DESCRIPCION:{self.descripcion}
    #     """
