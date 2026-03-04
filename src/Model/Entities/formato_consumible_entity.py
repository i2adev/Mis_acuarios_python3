"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      03/03/2026
Comentarios:
    Módulo que contiene la entidad FORMATOS DE CONSUMIBLE.
"""

from Model.Entities.base_entity import BaseEntity


class FormatoConsumibleEntity(BaseEntity):
    """ Entidad de formato de consumible. """

    def __init__(self, id: int = None, num: int = None, formato: str = None,
                 descripcion: str = None):
        """
        Constructor de clase.
        Parámetros:
        :param id: Id de la entidad.
        :param formato: Formato del consumible.
        :param descripcion: Descripción de la categoría.
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__formato = formato
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
    def formato(self) -> str:
        """ Categoríaa del consumible. """

        return self.__categoria

    @formato.setter
    def formato(self, new_formato: str):
        """ Formato del consumible. """

        self.__formato = new_formato

    @property
    def descripcion(self) -> str:
        """ Observaciones de la ctaegoría. """

        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Observaciones de la ctaegoría. """

        self.__descripcion = new_descripcion

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self):
        return f""""
            ID:             {self.id}
            FORMATO:      {self.formato}
            OBSERVACIONES:  {self.observaciones}
        """
