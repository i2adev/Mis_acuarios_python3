"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/09/2026
Comentarios:
    Módulo que contiene la entidad CONTROL DE TEMPERATURA.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class ControladorTemperaturaEntity(BaseEntity):
    """ Entidad del control de temperatura """

    id: int | None = None
    num: int | None = None
    id_marca: int | None = None
    id_tipo_control_temperatura: int | None = None
    descripcion: str | None = None
    modelo: str | None = None
    numero_serie: str | None = None
    potencia: float | None = None
    temperatura_minima: float | None = None
    temperatura_maxima: float | None = None
    consumo: float | None = None
    fecha_alta: int | None = None
    fecha_baja: int | None = None
    motivo_baja: int | None = None
    descripcion: str | None = None
