"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      13/03/2026
Comentarios:
    Módulo que contiene la entidad DIFICULTAD DE PLANTA.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class DificultadPlantaEntity(BaseEntity):
    """" Entidad de la dificultad de planta. """

    id: int | None = None
    num: int | None = None
    nivel: int | None = None
    dificultad: str | None = None
    descripcion: str | None = None
