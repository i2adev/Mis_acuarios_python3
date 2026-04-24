"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/10/2025
Comentarios:
    Módulo que contiene la entidad ACUARIO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class AcuarioEntity(BaseEntity):
    """ Entidad del acuario. """

    id: int | None = None
    num: int | None = None
    cod_color: str | None = None
    id_proyecto: int | None = None
    nombre: str | None = None
    id_urna: int | None = None
    id_tipo: int | None = None
    volumen_neto: int | None = None
    fecha_montaje: int | None = None
    fecha_inicio_ciclado: int | None = None
    fecha_fin_ciclado: int | None = None
    ubicacion_acuario: str | None = None
    fecha_desmontaje: int | None = None
    motivo_desmontaje: str | None = None
    descripcion: str | None = None
