"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/10/2025
Commentarios:
    Módulo que contiene la entidad ACAURIO.
"""
from Model.Entities.base_entity import BaseEntity


class AcuarioEntity(BaseEntity):
    """ Entidad del acuario. """

    # Anotaciones de tipo (atributos con sus tipos esperados)
    id: int | None
    num: int | None
    cod_color: str | None
    id_proyecto: int | None
    nombre: str | None
    id_urna: int | None
    id_tipo: int | None
    volumen_neto: int | None
    fecha_montaje: int | None
    fecha_inicio_ciclado: int | None
    fecha_fin_ciclado: int | None
    ubicacion_acuario: str | None
    fecha_desmontaje: int | None
    motivo_desmontaje: str | None
    descripcion: str | None

    def __init__(self, id: int = None, cod_color=None, num: int = None,
                 id_proyecto: int = None, nombre: str = None,
                 id_urna: int = None, id_tipo: int = None,
                 volumen_neto: int = None, fecha_montaje: int = None,
                 fecha_inicio_ciclado: int = None,
                 fecha_fin_ciclado: int = None,
                 ubicacion_acuario: str = None, fecha_desmontaje: int = None,
                 motivo_desmontaje: str = None, descripcion: str = None):
        """
        Constructor de la clase
        :param id: ID de la entidad acuario
        :param cod_color: Código hexadecimal del color de la etiqueta acuario
        :param num: Num de la entidad acuario
        :param id_proyecto: ID del proyecto
        :param nombre: Nombre asignado al acuario
        :param id_urna: ID de la urna
        :param id_tipo: ID del tipo de acuario
        :param volumen_neto: Volumen de neto del acuario
        :param fecha_montaje: Fecha del montaje del acuario
        :param fecha_inicio_ciclado: Fecha inicio del ciclado del acuario
        :param fecha_fin_ciclado: Fecha final del ciclado del acuario
        :param ubicacion_acuario: Ubicacion del acuario
        :param fecha_desmontaje: Fecha del desmontajo del acuario
        :param motivo_desmontaje: Motivo del desmontajo del acuario
        :param descripcion: Descripcion del acuario
        """

        super().__init__()

        # Inicializamos las variables
        self._id = id
        self._num = num
        self._cod_color = cod_color
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._id_urna = id_urna
        self._id_tipo = id_tipo
        self._volumen_neto = volumen_neto
        self._fecha_montaje = fecha_montaje
        self._fecha_inicio_ciclado = fecha_inicio_ciclado
        self._fecha_fin_ciclado = fecha_fin_ciclado
        self._ubicacion_acuario = ubicacion_acuario
        self._fecha_desmontaje = fecha_desmontaje
        self._motivo_desmontaje = motivo_desmontaje
        self._descripcion = descripcion

    @property
    def id(self) -> int | None:
        """ ID de la entidad acuario """
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        """ ID de la entidad acuario """
        self._id = id

    @property
    def num(self) -> int | None:
        """ Num de la entidad acuario """
        return self._num

    @num.setter
    def num(self, num: int) -> None:
        """ Num de la entidad acuario """
        self._num = num

    @property
    def cod_color(self) -> str:
        """ Código de la color de la etiqueta de acuario """
        return self._cod_color

    @cod_color.setter
    def cod_color(self, cod_color: str) -> None:
        """ Código de la color de la etiqueta de acuario """
        self._cod_color = cod_color

    @property
    def id_proyecto(self) -> int | None:
        """ ID del proyecto """
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, id_proyecto) -> None:
        """ ID del proyecto """
        self._id_proyecto = id_proyecto

    @property
    def nombre(self) -> str:
        """ Nombre de la entidad acuario """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre) -> None:
        """ Nombre de la entidad acuario """
        self._nombre = nombre

    @property
    def id_urna(self) -> int | None:
        """ ID de la urna """
        return self._id_urna

    @id_urna.setter
    def id_urna(self, id_urna) -> None:
        """ ID de la urna """
        self._id_urna = id_urna

    @property
    def id_tipo(self) -> int | None:
        """ ID del tipo de acuario """
        return self._id_tipo

    @id_tipo.setter
    def id_tipo(self, id_tipo) -> None:
        """ ID del tipo de acuario """
        self._id_tipo = id_tipo

    @property
    def volumen_neto(self) -> int | None:
        """ Volumen de neto """
        return self._volumen_neto

    @volumen_neto.setter
    def volumen_neto(self, volumen_neto) -> None:
        """ Volumen de neto """
        self._volumen_neto = volumen_neto

    @property
    def fecha_montaje(self) -> int | None:
        """ Fecha de montaje """
        return self._fecha_montaje

    @fecha_montaje.setter
    def fecha_montaje(self, fecha_montaje) -> None:
        """ Fecha de montaje """
        self._fecha_montaje = fecha_montaje

    @property
    def fecha_inicio_ciclado(self) -> int | None:
        """ Fecha inicio del ciclado """
        return self._fecha_inicio_ciclado

    @fecha_inicio_ciclado.setter
    def fecha_inicio_ciclado(self, fecha_inicio) -> None:
        """ Fecha inicio del ciclado """
        self._fecha_inicio_ciclado = fecha_inicio

    @property
    def fecha_fin_ciclado(self) -> int | None:
        """ Fecha final del ciclado """
        return self._fecha_fin_ciclado

    @fecha_fin_ciclado.setter
    def fecha_fin_ciclado(self, fecha_fin_ciclado) -> None:
        """ Fecha final del ciclado """
        self._fecha_fin_ciclado = fecha_fin_ciclado

    @property
    def ubicacion_acuario(self) -> str | None:
        """ Ubicacion del acuario """
        return self._ubicacion_acuario

    @ubicacion_acuario.setter
    def ubicacion_acuario(self, ubicacion_acuario) -> None:
        """ Ubicacion del acuario """
        self._ubicacion_acuario = ubicacion_acuario

    @property
    def fecha_desmontaje(self) -> int | None:
        """ Fecha de desmontajo """
        return self._fecha_desmontaje

    @fecha_desmontaje.setter
    def fecha_desmontaje(self, fecha_desmontaje) -> None:
        """ Fecha de desmontajo """
        self._fecha_desmontaje = fecha_desmontaje

    @property
    def motivo_desmontaje(self) -> str | None:
        """ Motivo del desmontajo """
        return self._motivo_desmontaje

    @motivo_desmontaje.setter
    def motivo_desmontaje(self, motivo_desmontaje) -> None:
        """ Motivo del desmontajo """
        self._motivo_desmontaje = motivo_desmontaje

    @property
    def descripcion(self) -> str:
        """ Descripcion del acuario """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion) -> None:
        """ Descripcion del acuario """
        self._descripcion = descripcion
