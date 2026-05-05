"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/04/2026
Comentarios:
    Módulo que contiene la entidad COMBO DATA ENTITY.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class ComboDataEntity(BaseEntity):
    """ Entidad de los datos de los combos. """

    id: int = None
    value: str = None
