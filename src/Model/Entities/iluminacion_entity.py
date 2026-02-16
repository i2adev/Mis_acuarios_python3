"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      21/12/2025
Comentarios:
    Módulo que contiene la entidad ILUMINACIÓN.
"""

from Model.Entities.base_entity import BaseEntity


class IluminacionEntity(BaseEntity):
    """ Entidad iluminación """

    def __init__(self, id: int = None, num: int = None,
                 id_tipo_iluminacion: int = None, id_marca: int = None,
                 modelo: str = None, num_serie: str = None,
                 potencia: int = None, flujo_luminico: int = None,
                 temperatura: int = None, vida_util: int = None,
                 longitud: int = None, anchura: int = None,
                 id_control_iluminacion: int = None,
                 intensidad_regulable: bool = None,
                 espectro_completo: bool = None, fecha_alta: int = None,
                 fecha_baja: int = None, motivo_baja: str = None,
                 descripcion: str = None, ):
        """
        Constructor base.
        """

        self._id = id
        self._num = num
        self._id_tipo_iluminacion = id_tipo_iluminacion
        self._id_marca = id_marca
        self._modelo = modelo
        self._num_serie = num_serie
        self._potencia = potencia
        self._flujo_luminico = flujo_luminico
        self._temperatura = temperatura
        self._vida_util = vida_util
        self._longitud = longitud
        self._anchura = anchura
        self._id_control_iluminacion = id_control_iluminacion
        self._fecha_alta = fecha_alta
        self._fecha_baja = fecha_baja
        self._motivo_baja = motivo_baja
        self._intensidad_regulable = intensidad_regulable
        self._espectro_completo = espectro_completo
        self._descripcion = descripcion

    @property
    def id(self) -> int:
        """ ID de iluminación """
        return self._id

    @id.setter
    def id(self, new_id: int):
        """ ID de iluminación """
        self._id = new_id

    @property
    def num(self) -> int:
        """ Número correlativo de iluminación """
        return self._num

    @num.setter
    def num(self, new_num: int):
        """ Número correlativo de iluminación """
        self._num = new_num

    @property
    def id_tipo_iluminacion(self) -> int:
        """ ID del tipo de iluminación """
        return self._id_tipo_iluminacion

    @id_tipo_iluminacion.setter
    def id_tipo_iluminacion(self, new_id_tipo_iluminacion: int):
        """ ID del tipo de iluminación """
        self._id_tipo_iluminacion = new_id_tipo_iluminacion

    @property
    def id_marca(self) -> int:
        """ ID de la marca de la luminaria """
        return self._id_marca

    @id_marca.setter
    def id_marca(self, new_id_marca: int):
        """ ID de la marca de la luminaria """
        self._id_marca = new_id_marca

    @property
    def modelo(self) -> str:
        """ Modelo de la luminaria """
        return self._modelo

    @modelo.setter
    def modelo(self, new_modelo: str):
        """ Modelo de la luminaria """
        self._modelo = new_modelo

    @property
    def num_serie(self) -> str:
        """ Número de serie de la luminaria"""
        return self._num_serie

    @num_serie.setter
    def num_serie(self, new_num_serie: str):
        """ Número de serie de la luminaria"""
        self._num_serie = new_num_serie

    @property
    def potencia(self) -> int:
        """ Potencia de la luminaria """
        return self._potencia

    @potencia.setter
    def potencia(self, new_potencia: int):
        """ Potencia de la luminaria """
        self._potencia = new_potencia

    @property
    def flujo_luminico(self) -> int:
        """ Flujo lumínico de la luminaria """
        return self._flujo_luminico

    @flujo_luminico.setter
    def flujo_luminico(self, new_flujo_luminico: int):
        """ Flujo lumínico de la luminaria """
        self._flujo_luminico = new_flujo_luminico

    @property
    def temperatura(self) -> int:
        """ Temperatura de la luminaria """
        return self._temperatura

    @temperatura.setter
    def temperatura(self, new_temperatura: int):
        """ Temperatura de la luminaria """
        self._temperatura = new_temperatura

    @property
    def vida_util(self) -> int:
        """ Vida util (horas) de la luminaria """
        return self._vida_util

    @vida_util.setter
    def vida_util(self, new_vida_util: int):
        """ Vida util (horas) de la luminaria """
        self._vida_util = new_vida_util

    @property
    def longitud(self) -> int:
        """ Longitud de la luminaria en cms """
        return self._longitud

    @longitud.setter
    def longitud(self, new_longitud: int):
        """ Longitud de la luminaria en cms """
        self._longitud = new_longitud

    @property
    def anchura(self) -> int:
        """ Anchura de la luminaria en cms """
        return self._anchura

    @anchura.setter
    def anchura(self, new_anchura: int):
        """ Anchura de la luminaria en cms """
        self._anchura = new_anchura

    @property
    def id_control_iluminacion(self) -> int:
        """ ID tipo de iluminación """
        return self._id_control_iluminacion

    @id_control_iluminacion.setter
    def id_control_iluminacion(self, new_id: int):
        """ ID tipo de iluminación """
        self._id_control_iluminacion = new_id

    @property
    def fecha_alta(self) -> int:
        """ Fecha de la alta """
        return self._fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, new_fecha_alta: int):
        """ Fecha de la alta """
        self._fecha_alta = new_fecha_alta

    @property
    def fecha_baja(self) -> int:
        """ Fecha de la baja """
        return self._fecha_baja

    @fecha_baja.setter
    def fecha_baja(self, new_fecha_baja: int):
        """ Fecha de la baja """
        self._fecha_baja = new_fecha_baja

    @property
    def motivo_baja(self) -> str:
        """ Motivo baja """
        return self._motivo_baja

    @motivo_baja.setter
    def motivo_baja(self, new_motivo_baja: str):
        """ Motivo baja """
        self._motivo_baja = new_motivo_baja

    @property
    def intensidad_regulable(self) -> bool:
        """ Especifica si la luz es regulable """
        return self._intensidad_regulable

    @intensidad_regulable.setter
    def intensidad_regulable(self, new_intensidad_regulable: bool):
        """ Especifica si la luz es regulable """
        self._intensidad_regulable = new_intensidad_regulable

    @property
    def espectro_completo(self) -> bool:
        """ Espectro completo de iluminación """
        return self._espectro_completo

    @espectro_completo.setter
    def espectro_completo(self, new_espectro_completo: bool):
        """ Espectro completo de iluminación """
        self._espectro_completo = new_espectro_completo

    @property
    def descripcion(self) -> str:
        """ Descripción de la luminaria """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripción de la luminaria """
        self._descripcion = new_descripcion

    def __str__(self):
        """ Retorna el string de la iluminación """

        return f"""
        ID:         {self.id}
        Número:     {self.num}
        Modelo:     {self.modelo}
        Descripcion:{self.descripcion:50}
        """
