"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/10/2025
Comentarios:
    Módulo que contiene la entidad PROYECTO.
"""
from dataclasses import dataclass

from ModuloMaestro.Model.Entities.base_entity import BaseEntity


@dataclass
class ProyectoEntity(BaseEntity):
    """ Entidad del tipo de filtro. """

    # Anotaciones de tipo (atributos con sus tipos esperados)
    id: int | None = None
    num: int | None = None
    id_usuario: int | None = None
    nombre: str | None = None
    id_estado: int | None = None
    fecha_inicio: int | None = None
    fecha_fin: int | None = None
    motivo_cierre: str | None = None
    descripcion: str | None = None
