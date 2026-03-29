"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      13/03/2026
Comentarios:
    Módulo que contiene la entidad DIFICULTAD DE PLANTA.
"""
from Model.Entities.base_entity import BaseEntity


class DificultadPlantaEntity(BaseEntity):
    """" Entidad de la dificultad de planta. """

    def __init__(self, id: int | None = None, num: int | None = None,
                 nivel: int | None = None, dificultad: str | None = None,
                 descripcion: str | None = None):
        """
        Constructor de la clase Dificultad de planta.
        :param id: ID de la dificultad de planta
        :param num: Número de la dificultad de planta
        :param nivel: Nivel de la dificultad de planta
        :param dificultad: Dificultad de planta
        :param descripcion: Descripcion de la dificultad de planta
        """

        self.__id = id
        self.__num = num
        self.__nivel = nivel
        self.__dificultad = dificultad
        self.__descripcion = descripcion

    # ---- INICIO DE PROPIEDADES ---------------------------------------
    @property
    def id(self) -> int | None:
        """ ID de la dificultad de planta """
        return self.__id

    @id.setter
    def id(self, new_id: int | None) -> None:
        """ ID de la dificultad de planta """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Número de la dificultad de planta """
        return self.__num

    @num.setter
    def num(self, new_num: int | None) -> None:
        """ Número de la dificultad de planta """
        self.__num = new_num

    @property
    def nivel(self) -> int | None:
        """ Nivel de la dificultad de planta """
        return self.__nivel

    @nivel.setter
    def nivel(self, new_nivel: int | None) -> None:
        """ Nivel de la dificultad de planta """
        self.__nivel = new_nivel

    @property
    def dificultad(self) -> str | None:
        """ Dificultad de planta """
        return self.__dificultad

    @dificultad.setter
    def dificultad(self, new_dificultad: str | None) -> None:
        """ Dificultad de planta """
        self.__dificultad = new_dificultad

    @property
    def descripcion(self) -> str | None:
        """ Descripcion de la dificultad de planta """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str | None) -> None:
        """ Descripcion de la dificultad de planta """
        self.__descripcion = new_descripcion

    # ---- FIN DE PROPIEDADES ------------------------------------------

    def __str__(self):
        return f"""
        ID:         {self.id}
        DIFICULTAD: {self.dificultad}
        DESCRICION: {self.descripcion}
        """
