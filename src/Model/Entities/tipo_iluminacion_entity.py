"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/12/2025
Comentarios:
    Módulo que contiene la entidad TIPO DE ILUMINACIÓN.
"""
from Model.Entities.base_entity import BaseEntity


class TipoIluminacionEntity(BaseEntity):
    """ Entidad del tipo de iluminacion """

    def __init__(self, id: int = None, num: int = None,
                 tipo_iluminacion: str = None, descripcion: str = None, ):
        """
        Constructor base.
        :param id: ID del tipo de iluminacion
        :param num: Número correlativo del tipo de iluminación
        :param tipo_iluminacion: Tipo de iluminacion
        :param descripcion: Descripción del tipo de iluminacion
        """

        self._id = id
        self._num = num
        self._tipo_iluminacion = tipo_iluminacion
        self._descripcion = descripcion

    @property
    def id(self) -> int:
        """ ID del tipo de iluminacion """
        return self._id

    @id.setter
    def id(self, new_id: int):
        """ ID del tipo de iluminacion """
        self._id = new_id

    @property
    def num(self) -> int:
        """ Número correlativo del tipo de iluminacion """
        return self._num

    @num.setter
    def num(self, new_num: int):
        """ Número correlativo del tipo de iluminacion """
        self._num = new_num

    @property
    def tipo_iluminacion(self) -> str:
        """ Tipo de iluminacion """
        return self._tipo_iluminacion

    @tipo_iluminacion.setter
    def tipo_iluminacion(self, new_tipo_iluminacion: str):
        """ Tipo de iluminacion """
        self._tipo_iluminacion = new_tipo_iluminacion

    @property
    def descripcion(self) -> str:
        """ Descripción del tipo de iluminación """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripción del tipo de iluminación """
        self._descripcion = new_descripcion

    def __str__(self):
        """ Retorna el string del tipo de iluminacion """

        return f"""
        ID:                 {self.id}
        Número:             {self.num}
        Tipo de iluminacion:{self.tipo_iluminacion}
        Descripcion:        {self.descripcion:50}
        """
