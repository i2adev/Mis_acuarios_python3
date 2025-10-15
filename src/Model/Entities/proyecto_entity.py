"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/10/2025
Commentarios:
    Módulo que contiene la entidad PROYECTO.
"""
from datetime import datetime

from Model.Entities.base_entity import BaseEntity

class ProyectoEntity(BaseEntity):
    """ Entidad del tipo de filtro. """

    # Anotaciones de tipo (atributos con sus tipos esperados)
    ide: int | None
    num: int | None
    id_usuario: int | None
    nombre: str | None
    id_estado: int | None
    fecha_inicio: datetime | None
    fecha_fin: datetime | None
    motivo_cierre: str | None
    descripcion: str | None

    def __init__(self, ide: int = None, num: int = None,
                 id_usuario: int = None, nombre: str = None,
                 id_estado: int = None, fecha_inicio: datetime = None,
                 fecha_fin: datetime = None, motivo_cierre: str = None,
                 descripcion: str = None):
        """
        Constructor de clase:
        :param ide: ide del proyecto
        :param num: Número correlativo del tipo de filtro
        :param id_usuario: Id del usuario
        :param nombre: Nombre del proyecto
        :param id_estado: Id del estado del proyecto
        :param fecha_inicio: Fecha de inicio del proyecto
        :param fecha_fin: Fecha de fin del proyecto
        :param motivo_cierre: Motivo del cierre del proyecto
        :param descripcion: Observaciones del proyecto
        """
        super().__init__()

        # Inicializamos las variables
        self.__id = ide
        self.__num = num
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__id_estado = id_estado
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__motivo_cierre = motivo_cierre
        self.__descripcion = descripcion

    # INICIO PROPIEDADES
    @property
    def ide(self) -> int:
        return self.__id

    @ide.setter
    def ide(self, new_id: int):
        self.__id = new_id

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, new_num: int):
        self.__num = new_num

    @property
    def id_usuario(self) -> int:
        """ ide del usuario. """
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, new_id_usuario: int):
        """ ide del usuario. """
        self.__id_usuario = new_id_usuario

    @property
    def nombre(self) -> str:
        """ Nombre del usuario. """
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str):
        """ Nombre del usuario. """
        self.__nombre = new_nombre

    @property
    def id_estado(self) -> int:
        """ ide del estado del proyecto. """
        return self.__id_estado

    @id_estado.setter
    def id_estado(self, new_id_estado: int):
        """ ide del estado del proyecto. """
        self.__id_estado = new_id_estado

    @property
    def fecha_inicio(self) -> int:
        """ Fecha de inicio del proyecto. """
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, new_fecha_inicio: int):
        """ Fecha de inicio del proyecto. """
        self.__fecha_inicio = new_fecha_inicio

    @property
    def fecha_fin(self) -> int:
        """ Fecha de fim del proyecto. """
        return self.__fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, new_fecha_fin: int):
        """ Fecha de fim del proyecto. """
        self.__fecha_fin = new_fecha_fin

    @property
    def motivo_cierre(self) -> int:
        """ Motivo cierre del proyecto. """
        return self.__motivo_cierre

    @motivo_cierre.setter
    def motivo_cierre(self, new_motivo_cierre: int):
        """ Motivo cierre del proyecto. """
        self.__motivo_cierre = new_motivo_cierre

    @property
    def descripcion(self) -> str:
        """ Observaciones del proyecto. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Observaciones del proyecto. """
        self.__descripcion = new_descripcion
    # FIN PROPIEDADES

    def __str__(self):
        """ Muestra información de la clase. """

        return f"""
            ide:             {self.ide}
            NUM:            {self.num}
            NOMBRE:         {self.nombre}
            DESCRIPCIÓN:    {self.descripcion:50}
            ------------------------------------------------------------
        """