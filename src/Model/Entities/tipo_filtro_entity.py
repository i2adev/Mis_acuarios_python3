"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Comentarios:
    Módulo que contien la entidad TIPO DE FILTRO.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class TipoFiltroEntity(BaseEntity):
    """ Entidad del tipo de filtro. """

    id: int | None = None
    num: int | None = None
    tipo_filtro: str | None = None
    observaciones: str | None = None
