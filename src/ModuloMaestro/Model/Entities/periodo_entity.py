"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      06/04/2026

Comentarios:
    Módulo que contiene la entidad PERIODO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class PeriodoEntity(BaseEntity):
    """ Entidad de periodo. """

    id: int | None = None
    num: int | None = None
    periodo: str | None = None
