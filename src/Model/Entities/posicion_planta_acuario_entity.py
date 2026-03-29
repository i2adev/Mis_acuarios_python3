"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/03/2026

Comentarios:
    Módulo que contiene la entidad POSICIÓN PLANTA ACUARIO.
"""

from Model.Entities.base_entity import BaseEntity


class PosicionPlantaAcuarioEntity(BaseEntity):
    """ Entidad de la posición de la planta en el acuario. """

    def __init__(self, id: int = None, num: int = None,
                 posicion: str = None, descripcion: str = None):
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param num: Número de la entidad.
        :param posicion: Posición de la planta en el acaurio.
        :param descripcion: Descripción de la planta en el acaurio.
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__posicion = posicion
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
    def posicion(self) -> str:
        """ Posición de la planta en el acaurio. """
        return self.__posicion

    @posicion.setter
    def posicion(self, new_posicion: str):
        """ Posición de la planta en el acaurio. """
        self.__posicion = new_posicion

    @property
    def descripcion(self) -> str:
        """ Descripción de la posición de la planta en el acuario. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripción de la posición de la planta en el acuario. """
        self.__descripcion = new_descripcion

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self):
        return f""""
            ID:         {self.id}
            POSICION:   {self.posicion}
            DESCRIPCIÓN:{self.descripcion}
        """
