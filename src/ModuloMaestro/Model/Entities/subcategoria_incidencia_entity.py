"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Comentarios:
    Módulo que contiene la entidad SUBCATEGORÍA DE INCIDENCIA.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class SubcategoriaIncidenciaEntity(BaseEntity):
    """ Entidad de la categoría de incidencia. """

    # ANotaciones de tipo
    id: int | None = None
    num: int | None = None
    id_categoria: int | None = None
    subcategoria: str | None = None
    observaciones: str | None = None
