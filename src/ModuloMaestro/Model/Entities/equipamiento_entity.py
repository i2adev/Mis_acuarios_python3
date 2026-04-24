"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/12/2025
Comentarios:
    Módulo que contiene la entidad EQUIPAMIENTO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class EquipamientoEntity(BaseEntity):
    """ Entidad de equipamiento. """

    id: int | None = None
    num: int | None = None
    id_categoria: int | None = None
    id_marca: int | None = None
    modelo: str | None = None
    numero_serie: str | None = None
    fecha_alta: int | None = None
    fecha_baja: int | None = None
    motivo_baja: str | None = None
    descripcion: str | None = None
