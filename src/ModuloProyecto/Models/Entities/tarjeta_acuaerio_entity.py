"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      29/09/2026
Comentarios:
    Entidad de la tarjeta de acuario
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class TarjetaAcuarioEntity(BaseEntity):
    """ Entidad de la tarjeta de acuario. """

    id: int | None = None
    num: int | None = None
    id_proyecto: int | None = None
    cod_color: str | None = None
    nombre: str | None = None
    modelo: str | None = None
    fotografia: bytes | None = None
