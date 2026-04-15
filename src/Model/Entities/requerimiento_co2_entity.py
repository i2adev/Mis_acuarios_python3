"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/03/2026

Comentarios:
    Módulo que contiene la entidad REQUERIMIENTO CO2.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class RequerimientoCO2Entity(BaseEntity):
    """ Entidad de requerimiento de CO2. """

    id: int | None = None
    num: int | None = None
    requerimiento: str | None = None
    descripcion: str | None = None
