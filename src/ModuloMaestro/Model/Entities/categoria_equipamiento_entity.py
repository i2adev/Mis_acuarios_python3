"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/12/2025
Comentarios:
    Módulo que contiene la entidad CATEGORÍA EQUIPAMIENTO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class CategoriaEquipamientoEntity(BaseEntity):
    """ Categoría de equipamiento """

    # Anotaciones de tipo
    id: int | None = None
    num: int | None = None
    categoria_equipamiento: str | None = None
    descripcion: str | None = None
