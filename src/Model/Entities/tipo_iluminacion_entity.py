"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/12/2025
Comentarios:
    Módulo que contiene la entidad TIPO DE ILUMINACIÓN.
"""
from dataclasses import dataclass

from Model.Entities.base_entity import BaseEntity


@dataclass
class TipoIluminacionEntity(BaseEntity):
    """ Entidad del tipo de iluminacion """

    id: int | None = None
    num: int | None = None
    tipo_iluminacion: str | None = None
    descripcion: str | None = None
