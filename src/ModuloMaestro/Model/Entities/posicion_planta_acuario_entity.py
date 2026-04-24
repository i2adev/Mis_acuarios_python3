"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/03/2026

Comentarios:
    Módulo que contiene la entidad POSICIÓN PLANTA ACUARIO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class PosicionPlantaAcuarioEntity(BaseEntity):
    """ Entidad de la posición de la planta en el acuario. """

    id: int | None = None
    num: int | None = None
    posicion: str | None = None
    descripcion: str | None = None
