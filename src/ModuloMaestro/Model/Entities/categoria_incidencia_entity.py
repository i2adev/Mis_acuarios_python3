"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Comentarios:
    Módulo que contiene la entidad CATEGORÍA DE INCIDENCIA.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class CategoriaIncidenciaEntity(BaseEntity):
    """ Entidad de la categoría de incidencia. """

    # ANotaciones de tipo
    id: int | None = None
    num: int | None = None
    categoria_incidencia: str | None = None
    observaciones: str | None = None
