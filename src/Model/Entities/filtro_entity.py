"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/11/2025
Comentarios:
    Módulo que contiene la entidad filtro.
"""
from Model.Entities.base_entity import BaseEntity


class FiltroEntity(BaseEntity):
    """ Entidad de filtro. """

    # Anotaciones de tipo
    id: int | None
    id_tipo: int | None
    id_marca: int | None
    modelo: str | None
    num_serie: str | None
    es_thermo: bool | None
    vol_min_acuario: int | None
    vol_max_acuario: int | None
    caudal: int | None
    altura_bombeo: float | None
    consumo: int | None
    consumo_calentador: int | None
    vol_filtrante: float | None
    ancho: int | None
    fondo: int | None
    alto: int | None
    fecha_instalacion: int | None
    fecha_baja: int | None
    motivo_baja: str | None
    descripcion: str | None

    def __init__(self, id: int = None, num: int = None, id_tipo: int = None,
                 id_marca: int = None,
                 modelo: str = None, num_serie: str = None,
                 es_thermo: bool = None,
                 vol_min_acuario: int = None, vol_max_acuario: int = None,
                 caudal: int = None, altura_bombeo: float = None,
                 consumo: float = None, consumo_calentador: float = None,
                 vol_filtrante: float = None, ancho: int = None,
                 fondo: int = None, alto: int = None,
                 fecha_instalacion: int = None, fecha_baja: int = None,
                 motivo_baja: str = None, descripcion: str = None):
        """
        Constructor de clase.
        :param id: ID de la entidad filtro.
        :param num: Numero de la entidad filtro.
        :param id_tipo: ID de la tipo de filtro.
        :param id_marca: ID de la marca de filtro.
        :param modelo: Modelo de filtro.
        :param num_serie: Numer de serie del filtro.
        :param es_thermo: Es termofiltro.
        :param vol_min_acuario: Volumen mínimo del acuario.
        :param vol_max_acuario: Volumen máximo del acuario.
        :param caudal: Caudad del filtro (l/h).
        :param altuna_bombeo: Altura del bombeo máxima del filtro (m).
        :param consumo: Consuma del filtro (w).
        :param consumo_calentador: Consuma del calentador del filtro (w).
        :param vol_filtrante: Volumen del filtro (l).
        :param ancho: Ancho del filtro (mm).
        :param fondo: Fondo del filtro (mm).
        :param alto: Alto del filtro (mm).
        :param fecha_instalacion: Fecha de la instalación del filtro.
        :param fecha_baja: Fecha de la baja del filtro.
        :motivo_baja: Motivo de la baja del filtro.
        :param descripción: Descripción del filtro.
        """

        super().__init__()
        self._id = id
        self._num = num
        self._id_tipo = id_tipo
        self._id_marca = id_marca
        self._modelo = modelo
        self._num_serie = num_serie
        self._es_thermo = es_thermo
        self._vol_min_acuario = vol_min_acuario
        self._vol_max_acuario = vol_max_acuario
        self._caudal = caudal
        self._altura_bombeo = altura_bombeo
        self._consumo = consumo
        self._consumo_calentador = consumo_calentador
        self._vol_filtrante = vol_filtrante
        self._ancho = ancho
        self._fondo = fondo
        self._alto = alto
        self._fecha_instalacion = fecha_instalacion
        self._fecha_baja = fecha_baja
        self._motivo_baja = motivo_baja
        self._descripcion = descripcion

    @property
    def id(self) -> int | None:
        """ ID de la entidad filtro. """
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        """ ID de la entidad filtro. """
        self._id = id

    @property
    def num(self) -> int | None:
        """ Numero de la entidad filtro. """
        return self._num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Numero de la entidad filtro. """
        self._num = new_num

    @property
    def id_tipo(self) -> int | None:
        """ ID de la tipo de filtro. """
        return self._id_tipo

    @id_tipo.setter
    def id_tipo(self, id_tipo: int) -> None:
        """ ID de la tipo de filtro. """
        self._id_tipo = id_tipo

    @property
    def id_marca(self) -> int | None:
        """ ID de la marca de filtro. """
        return self._id_marca

    @id_marca.setter
    def id_marca(self, id_marca: int) -> None:
        """ ID de la marca de filtro. """
        self._id_marca = id_marca

    @property
    def modelo(self) -> str | None:
        """ Modelo de filtro. """
        return self._modelo

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        """ Modelo de filtro. """
        self._modelo = modelo

    @property
    def num_serie(self) -> str | None:
        """ Numer de serie del filtro. """
        return self._num_serie

    @num_serie.setter
    def num_serie(self, num_serie: str) -> None:
        """ Numer de serie del filtro. """
        self._num_serie = num_serie

    @property
    def es_thermo(self) -> bool | None:
        """ Es thermofiltro. """
        return self._es_thermo

    @es_thermo.setter
    def es_thermo(self, es_thermo: bool) -> None:
        """ Es thermofiltro. """
        self._es_thermo = es_thermo

    @property
    def vol_min_acuario(self) -> int | None:
        """ Volumen mínimo del acuario. """
        return self._vol_min_acuario

    @vol_min_acuario.setter
    def vol_min_acuario(self, vol_min_acuario: int) -> None:
        """ Volumen mínimo del acuario. """
        self._vol_min_acuario = vol_min_acuario

    @property
    def vol_max_acuario(self) -> int | None:
        """ Volumen mánimo del acuario. """
        return self._vol_max_acuario

    @vol_max_acuario.setter
    def vol_max_acuario(self, vol_max_acuario: int) -> None:
        """ Volumen máximo del acuario. """
        self._vol_max_acuario = vol_max_acuario

    @property
    def caudal(self) -> int | None:
        """ Caudal del filtro. """
        return self._caudal

    @caudal.setter
    def caudal(self, caudal: int) -> None:
        """ Caudal del filtro. """
        self._caudal = caudal

    @property
    def altura_bombeo(self) -> int | None:
        """ Altuna bombeo. """
        return self._altura_bombeo

    @altura_bombeo.setter
    def altura_bombeo(self, altura_bombeo: int) -> None:
        """ Altuna bombeo. """
        self._altura_bombeo = altura_bombeo

    @property
    def consumo(self) -> int | None:
        """ Consumo. """
        return self._consumo

    @consumo.setter
    def consumo(self, consumo: int) -> None:
        """ Consumo. """
        self._consumo = consumo

    @property
    def consumo_calentador(self) -> int | None:
        """ Consumo calentado. """
        return self._consumo_calentador

    @consumo_calentador.setter
    def consumo_calentador(self, consumo_calentado: int) -> None:
        """ Consumo calentado. """
        self._consumo_calentador = consumo_calentado

    @property
    def vol_filtrante(self) -> int | None:
        """ Volumen filtrante. """
        return self._vol_filtrante

    @vol_filtrante.setter
    def vol_filtrante(self, vol_filtrante: int) -> None:
        """ Volumen filtrante. """
        self._vol_filtrante = vol_filtrante

    @property
    def ancho(self) -> int | None:
        """ Ancho. """
        return self._ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """ Ancho. """
        self._ancho = ancho

    @property
    def fecha_instalacion(self) -> int | None:
        """ Fecha instalación. """
        return self._fecha_instalacion

    @fecha_instalacion.setter
    def fecha_instalacion(self, new_fecha_instalacion: int) -> None:
        """ Fecha instalación. """
        self._fecha_instalacion = new_fecha_instalacion

    @property
    def fecha_baja(self) -> int | None:
        """ Fecha baja. """
        return self._fecha_baja

    @fecha_baja.setter
    def fecha_baja(self, fecha_baja: int) -> None:
        """ Fecha baja. """
        self._fecha_baja = fecha_baja

    @property
    def motivo_baja(self) -> int | None:
        """ Motivo baja. """
        return self._motivo_baja

    @motivo_baja.setter
    def motivo_baja(self, motivo_baja: int) -> None:
        """ Motivo baja. """
        self._motivo_baja = motivo_baja

    @property
    def descripcion(self) -> int | None:
        """ Descripción. """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: int) -> None:
        """ Descripción. """
        self._descripcion = descripcion
