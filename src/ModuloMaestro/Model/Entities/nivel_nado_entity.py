"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/03/2026

Comentarios:
    Módulo que contiene la entidad NIVEL DE NADO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class NivelNadoEntity(BaseEntity):
    """ Entidad del nivel de nado. """

    id: int | None = None
    num: int | None = None
    nivel_nado: str | None = None
    descripcion: str | None = None
