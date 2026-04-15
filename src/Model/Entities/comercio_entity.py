"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene la entidad COMERCIO.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class ComercioEntity(BaseEntity):
    """ Entidad de comercio. """

    id: int | None = None
    num: int | None = None
    nombre_comercio: str | None = None
    direccion: str | None = None
    cod_postal: str | None = None
    poblacion: str | None = None
    provincia: str | None = None
    id_pais: int | None = None
    observaciones: str | None = None
