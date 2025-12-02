"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Comentarios:
    Módulo que contiene la entidad CATEGORÍA DE ACUARIO.
"""

from Model.Entities.base_entity import BaseEntity


class CategoriaAcuarioEntity(BaseEntity):
    """ Entidad de categoría de acuario. """

    def __init__(self, id: int = None, num: int = None, categoria: str = None,
                 observaciones: str = None):
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param categoria: Categoría del acuario.
        :param observaciones: Observaciones de la categoría.
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__categoria = categoria
        self.__observaciones = observaciones

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
    def categoria(self) -> str:
        """ Categoria del acuario. """
        return self.__categoria

    @categoria.setter
    def categoria(self, new_categoria: str):
        """ Categoria del acuario. """
        self.__categoria = new_categoria

    @property
    def observaciones(self) -> str:
        """ Categoria del acuario. """
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones: str):
        """ Categoria del acuario. """
        self.__observaciones = new_observaciones

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self):
        return f""""
            ID:             {self.id}
            CATEGORIA:      {self.categoria}
            OBSERVACIONES:  {self.observaciones}
        """
