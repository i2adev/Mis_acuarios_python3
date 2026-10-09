"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/10/2026
Comentarios:
    Módulo de acceso a datos de la tarjeta de proyecto
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class TarjetaProyectoEntity(BaseEntity):
    """ Entidad de la tarjeta de proyecto """
    id: int | None = None
    num: int | None = None
    id_usuario: int | None = None
    nombre: str | None = None
    estado: str | None = None
    fecha_inicio: str | None = None
    fecha_fin: str | None = None
    fotografia: bytes | None = None
