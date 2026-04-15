"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene la entidad COMERCIO.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class ConsumibleEntity(BaseEntity):
    """ Entidad de consumible. """

    id: int | None = None
    num: int | None = None
    id_marca: int | None = None
    producto: str | None = None
    id_categoria: int | None = None
    id_formato: int | None = None
    contenido: str | None = None
    id_unidad: int | None = None
    descripcion: str | None = None
