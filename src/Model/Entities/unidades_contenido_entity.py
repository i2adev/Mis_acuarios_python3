"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      03/03/2026
Comentarios:
    Módulo que contiene la entidad FORMATOS DE CONSUMIBLE.
"""

from Model.Entities.base_entity import BaseEntity


class UnidadContenidoEntity(BaseEntity):
    """ Entidad de la unidad de medición de contenido. """

    def __init__(self, id: int = None, num: int = None, unidad: str = None,
                 descripcion: str = None):
        """
        Constructor de clase.
        :param id: Id de la entidad.
        :param unidad: Unidad de contenido.
        :param descripcion: Descripción de la unidad de contenido.
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__unidad = unidad
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
    def unidad(self) -> str:
        """ Unidad de medida. """

        return self.__unidad

    @unidad.setter
    def unidad(self, new_unidad: str):
        """ Unidad de medida. """

        self.__unidad = new_unidad

    @property
    def descripcion(self) -> str:
        """ Descripción de la unidad de contenido. """

        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripción de la unidad de contenido. """

        self.__descripcion = new_descripcion

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self):
        return f""""
            ID:             {self.id}
            UNIDAD:      {self.unidad}
            OBSERVACIONES:  {self.observaciones}
        """
