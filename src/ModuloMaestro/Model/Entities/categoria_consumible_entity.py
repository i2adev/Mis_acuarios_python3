"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      03/03/2026
Comentarios:
    Módulo que contiene la entidad CATEGORÍA DE CONSUMIBLE.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class CategoriaConsumibleEntity(BaseEntity):
    """ Entidad de categoría de acuario. """

    id: int | None = None
    num: int | None = None
    categoria: str | None = None
    observaciones: str | None = None
