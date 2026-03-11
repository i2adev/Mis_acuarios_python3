"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene la entidad COMERCIO.
"""
from Model.Entities.base_entity import BaseEntity


class ConsumibleEntity(BaseEntity):
    """ Entidad de consumible. """

    def __init__(self, id: int | None = None, num: int | None = None,
                 id_marca: int | None = None, producto: str | None = None,
                 id_categoria: int | None = None,
                 id_formato: int | None = None,
                 contenido: int | None = None, id_unidad: int | None = None,
                 descripcion: str | None = None, ):
        super().__init__()

        # Inicializamos los atributos
        self.__id = id
        self.__num = num
        self.__id_marca = id_marca
        self.__producto = producto
        self.__id_categoria = id_categoria
        self.__id_formato = id_formato
        self.__contenido = contenido
        self.__id_unidad = id_unidad
        self.__descripcion = descripcion

    @property
    def id(self) -> int | None:
        """ Id de consumible. """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ Id de consumible. """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Num de consumible. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Num de consumible. """
        self.__num = new_num

    @property
    def id_marca(self) -> int | None:
        """ Marca de consumible. """
        return self.__id_marca

    @id_marca.setter
    def id_marca(self, new_marca: int) -> None:
        """ Marca de consumible. """
        self.__id_marca = new_marca

    @property
    def producto(self) -> str | None:
        """ Producto. """
        return self.__producto

    @producto.setter
    def producto(self, new_producto: str) -> None:
        """ Producto. """
        self.__producto = new_producto

    @property
    def id_categoria(self) -> int | None:
        """ Categoría de consumible. """
        return self.__id_categoria

    @id_categoria.setter
    def id_categoria(self, new_categoria: int) -> None:
        """ Categoría de consumible. """
        self.__id_categoria = new_categoria

    @property
    def id_formato(self) -> int | None:
        """ Formato de consumible. """
        return self.__id_formato

    @id_formato.setter
    def id_formato(self, new_formato: int) -> None:
        """ Formato de consumible. """
        self.__id_formato = new_formato

    @property
    def contenido(self) -> int | None:
        """ Contenido de consumible. """
        return self.__contenido

    @contenido.setter
    def contenido(self, new_contenido: int) -> None:
        """ Contenido de consumible. """
        self.__contenido = new_contenido

    @property
    def id_unidad(self) -> int | None:
        """ Unidad del contenido. """
        return self.__id_unidad

    @id_unidad.setter
    def id_unidad(self, new_id: int) -> None:
        """ Unidad del contenido. """
        self.__id_unidad = new_id

    @property
    def descripcion(self) -> str | None:
        """ Descripción de consumible. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str) -> None:
        """ Descripción de consumible. """
        self.__descripcion = new_descripcion
