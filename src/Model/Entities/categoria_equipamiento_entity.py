"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/12/2025
Comentarios:
    Módulo que contiene la entidad CATEGORÍA EQUIPAMIENTO.
"""
from Model.Entities.base_entity import BaseEntity


class CategoriaEquipamientoEntity(BaseEntity):
    """ Categoría de equipamiento """

    # Anotaciones de tipo
    id: int | None
    num: int | None
    categoria_equipamiento: str | None
    descripcion: str | None

    def __init__(self, id: int = None, num: int = None,
                 categoria: str = None, descripcion: str = None):
        """
        Constructor de la clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param categoria: Categoría a la que pertenece el equipamiento
        :param descripcion: Descripción de la categoría de equipamiento
        """

        super().__init__()

        # Inicializa las variables
        self._id = id
        self._num = num
        self._categoria_equipamiento = categoria
        self._descripcion = descripcion

    @property
    def id(self) -> int | None:
        """ Id de la entidad. """

        return self._id

    @id.setter
    def id(self, new_id: int) -> None:
        """ Id de la entidad. """

        self._id = new_id

    @property
    def num(self) -> int | None:
        """ Número correlativo de la entidad. """
        return self._num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Número correlativo de la entidad. """
        self._num = new_num

    @property
    def categoria_equipamiento(self) -> str:
        """ Categoría de equipamiento. """

        return self._categoria_equipamiento

    @categoria_equipamiento.setter
    def categoria_equipamiento(self, new_categoria_equipamiento: str) -> None:
        """ Categoría de equipamiento. """

        self._categoria_equipamiento = new_categoria_equipamiento

    @property
    def descripcion(self) -> str:
        """ Descripción de la categoría. """

        return self._descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str) -> None:
        """ Descripción de la categoría. """

        self._descripcion = new_descripcion

    def __str__(self):
        """ Muestra información de la clase. """

        return f"""
        ID:             {self.id}
        NUM:            {self.num}
        CATEGORÍA:      {self.categoria_equipamiento}
        DESCRIPCIÓN:    {self.descripcion:50}
        ----------------------------------------------------------------
        """
