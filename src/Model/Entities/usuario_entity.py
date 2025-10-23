"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/09/2025
Commentarios:
    Módulo que contiene la entidad USUARIO
"""
from Model.Entities.base_entity import BaseEntity


class UsuarioEntity(BaseEntity):
    """ Entidad de usuario. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    nombre: str | None
    apellido1: str | None
    apellido2: str | None
    nick: str | None
    password: str | None

    def __init__(self, id: int = None, num: int = None, nombre: str = None,
                 apellido1: str = None, apellido2: str = None,
                 nick: str = None, password: str = None):
        """
        Constructor de clase
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param nombre: Nombre del usuario
        :param apellido1: Primer apellido del usuario
        :param apellido2: Segundo apellido del usuario
        :param nick: Nombre de usuario en la aplicación
        :param password: Contraseña de acceso a la aplicación
        """

        # Inicializa las variables
        self.__id = id
        self.__num = num
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__nick = nick
        self.__password = password

    @property
    def id(self) -> int | None:
        """ Id del usuario. """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ Id del usuario. """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Número correlativo de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Núymero correlativo de la entidad. """
        self.__num = new_num

    @property
    def nombre(self) -> str | None:
        """ Nombre del usuario. """
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        """ Nombre del usuario. """
        self.__nombre = new_nombre

    @property
    def apellido1(self) -> str | None:
        """ Primer apellido del usuario. """
        return self.__apellido1

    @apellido1.setter
    def apellido1(self, new_apellido1: str) -> None:
        """ Primer apellido del usuario. """
        self.__apellido1 = new_apellido1

    @property
    def apellido2(self) -> str | None:
        """ Segundo apellido del usuario. """
        return self.__apellido2

    @apellido2.setter
    def apellido2(self, new_apellido2: str) -> None:
        """ Segundo apellido del usuario. """
        self.__apellido2 = new_apellido2

    @property
    def nick(self) -> str | None:
        """ Nick de usuario. """
        return self.__nick

    @nick.setter
    def nick(self, new_nick: str) -> None:
        """ Nick de usuario. """
        self.__nick = new_nick

    @property
    def password(self) -> str | None:
        """ Contraseña del usuario. """
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        """ Contraseña del usuario. """
        self.__password = new_password

    @password.deleter
    def password(self) -> None:
        """ Contraseñaa del usuario. """
        del self.__password


    def __str__(self):
        return f"{self.apellido1.upper()} {self.apellido2.upper()}, " \
               f"{self.nombre.upper()}"