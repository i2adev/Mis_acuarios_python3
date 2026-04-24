"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/11/2025
Comentarios:
    Módulo que contiene la entidad filtro.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class FiltroEntity(BaseEntity):
    """ Entidad de filtro. """

    # Anotaciones de tipo
    id: int | None = None
    num: int | None = None
    id_tipo: int | None = None
    id_marca: int | None = None
    modelo: str | None = None
    num_serie: str | None = None
    es_thermo: bool = None
    vol_min_acuario: int | None = None
    vol_max_acuario: int | None = None
    caudal: int | None = None
    altura_bombeo: float | None = None
    consumo: int | None = None
    consumo_calentador: int | None = None
    vol_filtrante: float | None = None
    ancho: int | None = None
    fondo: int | None = None
    alto: int | None = None
    fecha_instalacion: int | None = None
    fecha_baja: int | None = None
    motivo_baja: str | None = None
    descripcion: str | None = None
