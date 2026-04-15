"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Comentarios:
    Módulo que contiene la entidad CATEGORÍA DE ACUARIO.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class CategoriaAcuarioEntity(BaseEntity):
    """ Entidad de categoría de acuario. """

    id: int | None = None
    num: int | None = None
    categoria: str | None = None
    observaciones: str | None = None
