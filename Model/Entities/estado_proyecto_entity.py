"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Commentarios:
    Módulo que contiene la entidad estado de proyecto.
"""
from base_entity import BaseEntity


class EstadoProyectoEntity(BaseEntity):
    """ Entidad de estado de proyecto. """

    # Anotaciones de tipo
    id: int | None
    num: int | None
    estado: str | None
    descripcion: str | None

    def __init__(self, id: int = None, num: int = None, estado: str = None,
                 descripcion: str = None) -> None:
        """ Constructor de clase. """
        self.__id = id
        self.__num = num
        self.__estado = estado
        self.__descripcion = descripcion

    @property
    def id(self) -> int | None:
        """ ID de estado de proyecto. """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ ID de estado de proyecto. """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Numero de estado de proyecto. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Numero de estado de proyecto. """
        self.__num = new_num

    @property
    def estado(self) -> str:
        """ Estado de proyecto. """
        return self.__estado

    @estado.setter
    def estado(self, new_estado: str) -> None:
        """ Estado de proyecto. """
        self.__estado = new_estado

    @property
    def descripcion(self) -> str:
        """ Descripcion de estado de proyecto. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str) -> None:
        """ Descripcion de estado de proyecto. """
        self.__descripcion = new_descripcion

    def __str__(self) -> str:
        """ Retorna el string de la clase. """
        return f"""
            ID: {self.id}
            ESTADO: {self.estado}
            DESCRIPCIÓN: {self.descripcion}
        """

