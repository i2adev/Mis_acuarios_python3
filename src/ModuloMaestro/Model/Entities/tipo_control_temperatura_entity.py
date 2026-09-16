"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      04/06/2026
Comentarios:
    Módulo que contiene la entidad TIPO DE CONTROL DE TEMPERATURA.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class TipoControlTemperaturaEntity(BaseEntity):
    """ Entidad del tipo de control de temperatura """

    id: int | None = None
    num: int | None = None
    tipo_control_temperatura: str | None = None
    descripcion: str | None = None
