"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      20/12/2025
Comentarios:
    Módulo que contiene la entidad CONTROL DE ILUMINACIÓN.
"""
from Model.Entities.base_entity import BaseEntity


class ControlIluminacionEntity(BaseEntity):
    """ Entidad control de iluminación """

    def __init__(self, id: int = None, num: int = None,
                 control_iluminacion: str = None, descripcion: str = None, ):
        """
        Constructor base.
        :param id: ID del tipo de iluminación
        :param num: Número correlativo del tipo de iluminación
        :param control_iluminacion: Tipo de control de iluminación
        :param descripcion: Descripción del control de iluminación
        """

        self._id = id
        self._num = num
        self._control_iluminacion = control_iluminacion
        self._descripcion = descripcion

    @property
    def id(self) -> int:
        """ ID del control de iluminación """
        return self._id

    @id.setter
    def id(self, new_id: int):
        """ ID del control de iluminación """
        self._id = new_id

    @property
    def num(self) -> int:
        """ Número correlativo del control de iluminación """
        return self._num

    @num.setter
    def num(self, new_num: int):
        """ Número correlativo del control de iluminación """
        self._num = new_num

    @property
    def control_iluminacion(self) -> str:
        """ Control de iluminación """
        return self._control_iluminacion

    @control_iluminacion.setter
    def control_iluminacion(self, new_tipo_iluminacion: str):
        """ Control de iluminación """
        self._control_iluminacion = new_tipo_iluminacion

    @property
    def descripcion(self) -> str:
        """ Descripción del Control de iluminación """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripción del Control de iluminación """
        self._descripcion = new_descripcion

    def __str__(self):
        """ Retorna el string del control de iluminación """

        return f"""
        ID:                    {self.id}
        Número:                {self.num}
        Control de iluminación:{self.control_iluminación}
        Descripcion:           {self.descripcion:50}
        """
