"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Comentarios:
    Módulo que contiene la entidad estado de proyecto.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class EstadoProyectoEntity(BaseEntity):
    """ Entidad de estado de proyecto. """

    # Anotaciones de tipo
    id: int | None = None
    num: int | None = None
    estado: str | None = None
    descripcion: str | None = None
