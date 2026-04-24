"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/04/2026

Comentarios:
    Módulo que contiene la entidad TASA DE CRECIMIENTO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class TasaCrecimientoEntity(BaseEntity):
    """ Entidad de tasa de crecimiento. """
    id: int | None = None
    num: int | None = None
    tasa_crecimiento: str | None = None
    descripcion: str | None = None
