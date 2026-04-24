"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Comentarios:
    Módulo que contiene la entidad SUBCATEGORÍA DE ACUARIO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class SubcategoriaAcuarioEntity(BaseEntity):
    """ Entidad de la categoría de acuario. """

    # Anotaciones de tipo
    id: int | None = None
    num: int | None = None
    id_categoria: int | None = None
    subcategoria: str | None = None
    observaciones: str | None = None
