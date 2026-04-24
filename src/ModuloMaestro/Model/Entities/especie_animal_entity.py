"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene el DAO de la ESPECIE ANIMAL.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class EspecieAnimalEntity(BaseEntity):
    """ Entidad de la especie animal. """

    id: int | None = None
    num: int | None = None
    reino: str | None = None
    filo: str | None = None
    clase: str | None = None
    orden: str | None = None
    familia: str | None = None
    genero: str | None = None
    especie: str | None = None
    nombre_cientifico: str | None = None
    nombre_comun: str | None = None
    es_hibrida: bool = False
    nombre_especie_hibrida: str | None = None
    id_grupo_taxonomico: int | None = None
    origen: str | None = None
    ph_min: float | None = None
    ph_max: float | None = None
    kh_min: int | None = None
    kh_max: int | None = None
    gh_min: int | None = None
    gh_max: int | None = None
    temp_min: float | None = None
    temp_max: float | None = None
    tamano_cm: int | None = None
    id_comportamiento: int | None = None
    id_dieta: int | None = None
    id_nivel_nado: int | None = None
    descripcion: str | None = None
