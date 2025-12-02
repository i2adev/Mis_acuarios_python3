"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Comentarios:
    Módulo que contiene la entidad SUBCATEGORÍA DE ACUARIO.
"""
from Model.Entities.base_entity import BaseEntity


class SubcategoriaAcuarioEntity(BaseEntity):
    """ Entidad de la categoría de acuario. """

    # Anotaciones de tipo
    id: int | None
    num: int | None
    id_categoria: int | None
    subcategoria: str | None
    observaciones: str | None

    def __init__(self, id: int = None, num: int = None, id_cat: int = None,
                 subcategoria: str = None, observaciones: str = None):
        """ 
        Constructor de clase. 
        
        Parámetros:
        :param id: Id de la entidad.
        :param id_cat: Id de la categoria de acuario.
        :param subcategoria: Subcategoría de acuario.
        :param observaciones: Observaciones de la subcategoría.
        """

        super().__init__()
        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__id_categoria = id_cat
        self.__subcategoria = subcategoria
        self.__observaciones = observaciones

    @property
    def id(self) -> int | None:
        """ Id de la entidad. """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ Id de la entidad. """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Número de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Número de la entidad. """
        self.__num = new_num

    @property
    def id_categoria(self) -> int | None:
        """ Id de la categoria de acuario. """
        return self.__id_categoria

    @id_categoria.setter
    def id_categoria(self, new_id: int) -> None:
        """ Id de la categoria de acuario. """
        self.__id_categoria = new_id

    @property
    def subcategoria(self) -> str | None:
        """ Subcategoria de acuario. """
        return self.__subcategoria

    @subcategoria.setter
    def subcategoria(self, new_subcategoria: str) -> None:
        """ Subcategoria de acuario. """
        self.__subcategoria = new_subcategoria

    @property
    def observaciones(self) -> str | None:
        """ Observaciones de la subcategoria. """
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones: str) -> None:
        """ Observaciones de la subcategoria. """
        self.__observaciones = new_observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            SUBCATEGORIA:   {self.subcategoria}
            OBSERVACIONES:  {self.observaciones}
        """
