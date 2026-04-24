"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/09/2025
Comentarios:
    Módulo que contiene la entidad USUARIO
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class UsuarioEntity(BaseEntity):
    """ Entidad de usuario. """

    id: int | None = None
    num: int | None = None
    nombre: str | None = None
    apellido1: str | None = None
    apellido2: str | None = None
    nick: str | None = None
    password: str | None = None

    def __str__(self):
        return f"{self.apellido1.upper()} {self.apellido2.upper()}, " \
               f"{self.nombre.upper()}"
