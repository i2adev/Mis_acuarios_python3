"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      07/04/2026
Comentarios:
    Módulo que contiene la entidad especie vegetal.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class EspecieVegetalEntity(BaseEntity):
    """ Entidad de la especie vegetal. """
    
    id: int | None = None
    num: int | None = None
    reino: str | None = None
    division: str | None = None
    clase: str | None = None
    orden: str | None = None
    familia: str | None = None
    tribu: str | None = None
    genero: str | None = None
    especie: str | None = None
    nombre_cientifico: str | None = None
    nombre_comun: str | None = None
    ph_min: float | None = None
    ph_max: float | None = None
    kh_min: int | None = None
    kh_max: int | None = None
    gh_min: int | None = None
    gh_max: int | None = None
    temp_min: float | None = None
    temp_max: float | None = None
    origen: str | None = None
    id_posicion_acuario: int | str | None = None
    id_req_iluminacion: int | str | None = None
    id_req_co2: int | str | None = None
    id_tasa_crecimiento: int | str | None = None
    id_dificultad: int | str | None = None
    descripcion: str | None = None
