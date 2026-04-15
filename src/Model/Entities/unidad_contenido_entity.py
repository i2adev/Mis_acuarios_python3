"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      03/03/2026
Comentarios:
    Módulo que contiene la entidad FORMATOS DE CONSUMIBLE.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class UnidadContenidoEntity(BaseEntity):
    """ Entidad de la unidad de medición de contenido. """

    id: int | None = None
    num: int | None = None
    unidad: str | None = None
    descripcion: str | None = None
