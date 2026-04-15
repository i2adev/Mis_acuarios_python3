"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      12/03/2026

Comentarios:
    Módulo que contiene la entidad COMPORTAMIENTO DE FAUNA.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class ComportamientoFaunaEntity(BaseEntity):
    """ Entidad del comportamiento de fauna. """

    id: int | None = None
    num: int | None = None
    comportamiento: str | None = None
    descripcion: str | None = None
