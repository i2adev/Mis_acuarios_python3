"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/07/2025
Comentarios:
    Módulo que contiene la entidad MARCA DE PRODUCTO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class MarcaComercialEntity(BaseEntity):
    """ Entidad de la marca de producto. """

    id: int | None = None
    num: int | None = None
    nombre_marca: str | None = None
    direccion: str | None = None
    cod_postal: str | None = None
    poblacion: str | None = None
    provincia: str | None = None
    id_pais: int | None = None
    observaciones: str | None = None
