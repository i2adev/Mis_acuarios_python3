"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/03/2026

Comentarios:
    Módulo que contiene la entidad GRUPO TAXONÓMICO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class GrupoTaxonomicoEntity(BaseEntity):
    """ Entidad del grupo taxonómico """

    id: int | None = None
    num: int | None = None
    grupo_taxo: str | None = None
    descripcion: str | None = None
