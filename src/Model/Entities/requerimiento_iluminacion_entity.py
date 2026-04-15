"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/03/2026

Comentarios:
    Módulo que contiene la entidad REQUERIMIENTO ILUMINACIÓN.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class RequerimientoIluminacionEntity(BaseEntity):
    """ Entidad de requerimiento de iluminación. """

    id: int | None = None
    num: int | None = None
    requerimiento: str | None = None
    descripcion: str | None = None
