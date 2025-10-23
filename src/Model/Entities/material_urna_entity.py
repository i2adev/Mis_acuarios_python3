"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/08/2025
Commentarios:
    Módulo que contiene la entidad MATERIAL DE URNA.
"""
from Model.Entities.base_entity import BaseEntity


class MaterialUrnaEntity(BaseEntity):
    """ Clase del material de la urna. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    material: str | None
    descripcion: str | None

    def __init__(self, id: int = None, num: int = None, material: str = None,
                 descripcion: str = None):
        """
        Constructor de clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad en listas
        :param material: Material con el que se fabricó la urna
        :param descripcion: Descripción del material
        """

        super().__init__()

        self.__id = id
        self.__num = num
        self.__material = material
        self.__descripcion = descripcion

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
        """ Número correlativo de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Número correlativo de la entidad. """
        self.__num = new_num

    @property
    def material(self) -> str:
        """ Material de la urna. """
        return self.__material

    @material.setter
    def material(self, new_material) -> None:
        """ Material de la urna. """
        self.__material = new_material

    @property
    def descripcion(self) -> str:
        """ Descripción del material. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion) -> None:
        """ Descripción del material. """
        self.__descripcion = new_descripcion

    def __str__(self):
        return f"""
            ID:         {self.id}
            MATERIAL:   {self.material}
        """