"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene el DAO de la ESPECIE ANIMAL.
"""
from Model.Entities.base_entity import BaseEntity


class EspecieAnimalEntity(BaseEntity):
    """ Entidad de la especie animal. """

    def __init__(self, id: int | None = None, num: int | None = None,
                 reino: str | None = None, filo: str | None = None,
                 clase: str | None = None, orden: str | None = None,
                 familia: str | None = None, genero: str | None = None,
                 especie: str | None = None, nombre_cientifico: str | None =
                 None, nombre_comun: str | None = None,
                 es_hibrida: bool = False,
                 nombre_especie_hibrida: str | None = None,
                 id_grupo_taxonomico: int | None = None,
                 origen: str | None = None,
                 ph_min: float | None = None, ph_max: float | None = None,
                 kh_min: int | None = None, kh_max: int | None = None,
                 gh_min: int | None = None, gh_max: int | None = None,
                 temp_min: int | None = None, temp_max: int | None = None,
                 tamano_cm: float | None = None,
                 id_comportamiento: int | None = None,
                 id_dieta: int | None = None,
                 id_nivel_nado: int | None = None,
                 descripcion: str | None = None, ) -> None:
        """
        Constructor de clase.
        :param id: ID de la entidad de la especie
        :param num: Número correlativo de la entidad
        :param reino: Reino al que pertenece la especie
        :param filo: Filo al que pertenece la especie
        :param clase: Clase al que pertenece la especie
        :param orden: Orden al que pertenece la especie
        :param familia: Familia al que pertenece la especie
        :param genero: Género al que pertenece la especie
        :param especie: Especie del animal
        :param nombre_cientifico: Nombre del científico de la especie
        :param nombre_comun: Nombre del común de la especie
        :param es_hibrida: Especifica sí la especie es resultado de la hibridación
        :param nombre_especie_hibrida: Nombre de la especie hibridada
        :param id_grupo_taxonomico: ID del grupo taxonomico de la especie
        :param origen: Origen geográfico de la especie
        :param ph_min: pH mínimo recomendado para la especie
        :param ph_max: pH máximo recomendado para la especie
        :param kh_min: KH mínimo recomendado para la especie
        :param kh_max: KH máximo recomendado para la especie
        :param gh_min: GH mínimo recomendado para la especie
        :param gh_max: GH máximo recomendado para la especie
        :param temp_min: Temperatura mínima recomendada para la especie
        :param temp_max: Temperatura máxima recomendada para la especie
        :param tamano_cm: Tamaño que alcanza la especie en edad adulta
        :param id_comportamiento: ID del comportamiento de la especie
        :param id_dieta: ID de la dieta de la especie
        :param id_nivel_nado: ID del nivel de nado de la especie
        :param descripcion: Descripción de la especie
        """

        self.__id = id
        self.__num = num
        self.__reino = reino
        self.__filo = filo
        self.__clase = clase
        self.__orden = orden
        self.__familia = familia
        self.__genero = genero
        self.__especie = especie
        self.__nombre_cientifico = nombre_cientifico
        self.__nombre_comun = nombre_comun
        self.__es_hibrida = es_hibrida
        self.__nombre_especie_hibrida = nombre_especie_hibrida
        self.__id_grupo_taxonomico = id_grupo_taxonomico
        self.__origen = origen
        self.__ph_min = ph_min
        self.__ph_max = ph_max
        self.__kh_min = kh_min
        self.__kh_max = kh_max
        self.__gh_min = gh_min
        self.__gh_max = gh_max
        self.__temp_min = temp_min
        self.__temp_max = temp_max
        self.__tamano_cm = tamano_cm
        self.__id_comportamiento = id_comportamiento
        self.__id_dieta = id_dieta
        self.__id_nivel_nado = id_nivel_nado
        self.__descripcion = descripcion

    # INICIO DE PROPIEDADES --------------------------------------------
    @property
    def id(self) -> int:
        """ ID de la entidad de la especie """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ ID de la entidad de la especie """
        self.__id = new_id

    @property
    def num(self) -> int:
        """ Número correlativo de la entidad """
        return self.__num

    @num.setter
    def num(self, new_num: str) -> None:
        """ Número correlativo de la entidad """
        self.__num = new_num

    @property
    def reino(self) -> str:
        """ Reino al que pertenece la especie """
        return self.__reino

    @reino.setter
    def reino(self, new_reino: str) -> None:
        """ Reino al que pertenece la especie """
        self.__reino = new_reino

    @property
    def filo(self) -> str:
        """ Filo al que pertenece la especie """
        return self.__filo

    @filo.setter
    def filo(self, new_filo: str) -> None:
        """ Filo al que pertenece la especie """
        self.__filo = new_filo

    @property
    def clase(self) -> str:
        """ Clase al que pertenece la especie """
        return self.__clase

    @clase.setter
    def clase(self, new_clase: str) -> None:
        """ Clase al que pertenece la especie """
        self.__clase = new_clase

    @property
    def orden(self) -> str:
        """ Orden al que pertenece la especie """
        return self.__orden

    @orden.setter
    def orden(self, new_orden: str) -> None:
        """ Orden al que pertenece la especie """
        self.__orden = new_orden

    @property
    def familia(self) -> str:
        """ Familia al que pertenece la especie """
        return self.__familia

    @familia.setter
    def familia(self, new_familia: str) -> None:
        """ Familia al que pertenece la especie """
        self.__familia = new_familia

    @property
    def genero(self) -> str:
        """ Género al que pertenece la especie """
        return self.__genero

    @genero.setter
    def genero(self, new_genero: str) -> None:
        """ Género al que pertenece la especie """
        self.__genero = new_genero

    @property
    def especie(self) -> str:
        """ Especie del animal """
        return self.__especie

    @especie.setter
    def especie(self, new_especie: str) -> None:
        """ Especie del animal """
        self.__especie = new_especie

    @property
    def nombre_cientifico(self) -> str:
        """ Nombre del científico de la especie """
        return self.__nombre_cientifico

    @nombre_cientifico.setter
    def nombre_cientifico(self, new_cientifico: str) -> None:
        """ Nombre del científico de la especie """
        self.__nombre_cientifico = new_cientifico

    @property
    def nombre_comun(self) -> str:
        """ Nombre del común de la especie """
        return self.__nombre_comun

    @nombre_comun.setter
    def nombre_comun(self, new_nombre_comun: str) -> None:
        """ Nombre del común de la especie """
        self.__nombre_comun = new_nombre_comun

    @property
    def es_hibrida(self) -> bool:
        """ Especifica sí la especie es resultado de la hibridación """
        return self.__es_hibrida

    @es_hibrida.setter
    def es_hibrida(self, new_es_hibrida: bool) -> None:
        """ Especifica sí la especie es resultado de la hibridación """
        self.__es_hibrida = new_es_hibrida

    @property
    def nombre_especie_hibrida(self) -> str:
        """ Nombre de la especie hibridada """
        return self.__nombre_especie_hibrida

    @nombre_especie_hibrida.setter
    def nombre_especie_hibrida(self, new_name_hibrida: str) -> None:
        """ Nombre de la especie hibridada """
        self.__nombre_especie_hibrida = new_name_hibrida

    @property
    def id_grupo_taxonomico(self) -> int:
        """ ID del grupo taxonómico de la especie """
        return self.__id_grupo_taxonomico

    @id_grupo_taxonomico.setter
    def id_grupo_taxonomico(self, new_id: int) -> None:
        """ ID del grupo taxonómico de la especie """
        self.__id_grupo_taxonomico = new_id

    @property
    def origen(self) -> str:
        """ Origen geográfico de la especie """
        return self.__origen

    @origen.setter
    def origen(self, new_origen: str) -> None:
        """ Origen geográfico de la especie """
        self.__origen = new_origen

    @property
    def ph_min(self) -> float:
        """ pH mínimo recomendado para la especie """
        return self.__ph_min

    @ph_min.setter
    def ph_min(self, new_ph_min: float) -> None:
        """ pH mínimo recomendado para la especie """
        self.__ph_min = new_ph_min

    @property
    def ph_max(self) -> float:
        """ pH máximo recomendado para la especie """
        return self.__ph_max

    @ph_max.setter
    def ph_max(self, new_ph_max: float) -> None:
        """ pH máximo recomendado para la especie """
        self.__ph_max = new_ph_max

    @property
    def kh_min(self) -> int:
        """ KH mínimo recomendado para la especie """
        return self.__kh_min

    @kh_min.setter
    def kh_min(self, new_kh_min: int) -> None:
        """ KH mínimo recomendado para la especie """
        self.__kh_min = new_kh_min

    @property
    def kh_max(self) -> int:
        """ KH máximo recomendado para la especie """
        return self.__kh_max

    @kh_max.setter
    def kh_max(self, new_kh_max: int) -> None:
        """ KH máximo recomendado para la especie """
        self.__kh_max = new_kh_max

    @property
    def gh_min(self) -> int:
        """ GH mínimo recomendado para la especie """
        return self.__gh_min

    @gh_min.setter
    def gh_min(self, new_gh_min: int) -> None:
        """ GH mínimo recomendado para la especie """
        self.__gh_min = new_gh_min

    @property
    def gh_max(self) -> int:
        """ GH máximo recomendado para la especie """
        return self.__gh_max

    @gh_max.setter
    def gh_max(self, new_gh_max: int) -> None:
        """ GH máximo recomendado para la especie """
        self.__gh_max = new_gh_max

    @property
    def temp_min(self) -> float:
        """ Temperatura mínima recomendada para la especie """
        return self.__temp_min

    @temp_min.setter
    def temp_min(self, new_temp_min: float) -> None:
        """ Temperatura mínima recomendada para la especie """
        self.__temp_min = new_temp_min

    @property
    def temp_max(self) -> float:
        """ Temperatura máxima recomendada para la especie """
        return self.__temp_max

    @temp_max.setter
    def temp_max(self, new_temp_max: float) -> None:
        """ Temperatura máxima recomendada para la especie """
        self.__temp_max = new_temp_max

    @property
    def tamano_cm(self) -> float:
        """ Tamaño que alcanza la especie en edad adulta """
        return self.__tamano_cm

    @tamano_cm.setter
    def tamano_cm(self, new_tamano_cm: float) -> None:
        """ Tamaño que alcanza la especie en edad adulta """
        self.__tamano_cm = new_tamano_cm

    @property
    def id_comportamiento(self) -> int:
        """ ID del comportamiento de la especie """
        return self.__id_comportamiento

    @id_comportamiento.setter
    def id_comportamiento(self, new_id_comportamiento: int) -> None:
        """ ID del comportamiento de la especie """
        self.__id_comportamiento = new_id_comportamiento

    @property
    def id_dieta(self) -> int:
        """ ID de la dieta de la especie """
        return self.__id_dieta

    @id_dieta.setter
    def id_dieta(self, new_id_dieta: int) -> None:
        """ ID de la dieta de la especie """
        self.__id_dieta = new_id_dieta

    @property
    def id_nivel_nado(self) -> int:
        """ ID del nivel de nado de la especie """
        return self.__id_nivel_nado

    @id_nivel_nado.setter
    def id_nivel_nado(self, new_id_nivel_nado: int) -> None:
        """ ID del nivel de nado de la especie """
        self.__id_nivel_nado = new_id_nivel_nado

    @property
    def descripcion(self) -> str:
        """ Descripción de la especie """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str) -> None:
        """ Descripción de la especie """
        self.__descripcion = new_descripcion

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self) -> str:
        return self.__nombre_cientifico
