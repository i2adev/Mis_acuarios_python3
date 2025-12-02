"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/06/2025
Comentarios:
    Módulo que contien la entidad TIPO DE ACUARIO.
"""
from Model.Entities.base_entity import BaseEntity


class TipoAcuarioEntity(BaseEntity):
    """ Entidad del tipo de acuario. """

    # Anotaciones de tipo (atributos con sus tipos esperados)
    id: int | None
    num: int | None
    id_categoria_acuario: int | None
    id_subcat_acuario: int | None
    observaciones: str | None

    def __init__(self, id: int = None, num: int = None,
                 id_cat_acuario: int = None,
                 id_subcat_acuario: int = None, observaciones: str = None):
        """
        Constructor de clase.
        :param id: ID del tipo de acuario
        :param num: Número del tipo de acuario
        :param id_cat_acuario: ID de la categoría de acuario
        :param id_subcat_acuario: ID de la subcategoría de acuario
        :param observaciones: Observaciones del tipo de acuario
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__id_categoria_acuario = id_cat_acuario
        self.__id_subcategoria_acuario = id_subcat_acuario
        self.__observaciones = observaciones

    @property
    def id(self) -> int | None:
        """ ID del tipo de acuario. """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ ID del tipo de acuario. """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Número correlativo de la entidad tipo de acuario. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Número correlativo de la entidad tipo de acuario. """
        self.__num = new_num

    @property
    def id_categoria_acuario(self) -> int | None:
        """ ID de la categoría de acuario. """
        return self.__id_categoria_acuario

    @id_categoria_acuario.setter
    def id_categoria_acuario(self, new_id: int) -> None:
        """ ID de la categoría de acuario. """
        self.__id_categoria_acuario = new_id

    @property
    def id_subcategoria_acuario(self) -> int | None:
        """ ID de la subcategoría de acuario. """
        return self.__id_subcategoria_acuario

    @id_subcategoria_acuario.setter
    def id_subcategoria_acuario(self, new_id: int) -> None:
        """ ID de la subcategoría de acuario. """
        self.__id_subcategoria_acuario = new_id

    @property
    def observaciones(self) -> str | None:
        """ Observaciones del tipo de acuario. """
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones: str) -> None:
        """ Observaciones del tipo de acuario. """
        self.__observaciones = new_observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            NUM:            {self.num}
            TIPO ACUARIO:   {self.id_categoria_acuario}
            SUBTIPO ACUA.:  {self.id_subcategoria_acuario}    
            OBSERVACIONES:  {self.observaciones:50}
            ------------------------------------------------------------
        """
