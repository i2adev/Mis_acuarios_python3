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
        self.id = id
        self.num = num
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.nick = nick
        self.password = password

    def __str__(self):
        return f"{self.apellido1.upper()} {self.apellido2.upper()}, " \
               f"{self.nombre.upper()}"