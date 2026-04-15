"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/08/2025
Comentarios:
    Módulo que contiene la entidad FOTOGRAFÍA.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class FotografiaEntity(BaseEntity):
    """ Entidad de fotografía. """

    # Notaciones de tipo
    id: int | None = None
    num: int | None = None
    id_foranea: int | None = None
    ruta: str | None = None
    fotografia: bytes | None = None
