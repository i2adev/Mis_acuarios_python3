"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/10/2026
Comentarios:
    Módulo que contiene la entidad CONFIGURACIÓN DE UNIDADES DE DISTANCIA.
"""
from dataclasses import dataclass


@dataclass
class DimensionConfigurationEntity:
    """ Entidad que almacena las medidas de distancia. """

    medidas_urna: str | None = None
    medidas_filtro: str | None = None
    medidas_luminaria: str | None = None
    medidas_grosor_cristal_urna: str | None = None
