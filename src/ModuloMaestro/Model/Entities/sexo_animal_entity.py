"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/04/2026

Comentarios:
    Módulo que contiene la entidad SEXO ANIMAL.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class SexoAnimalEntity(BaseEntity):
    """ Entidad del soxo del animal. """

    id: int | None = None
    num: int | None = None
    sexo: str | None = None
    descripcion: str | None = None
