"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      29/07/2025
Comentarios:
    Módulo que contiene la entidad PAÍS.
"""
from Model.Entities.base_entity import BaseEntity


class PaisEntity(BaseEntity):
    """ Entidad país. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    pais: str | None
    continente: str | None

    def __init__(self, id, num, pais, continente):
        """
        Constructor de clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param pais: Nombre del país
        :param continente: Continente donde se encuentra el país
        """

        super().__init__()

        # Inicializamos las variables
        self.id = id
        self.num = num
        self.pais = pais
        self.continente = continente

    def __str__(self):
        return f"""
            ID:         {self.id}
            PAÍS:       {self.nombre_marca}
            CONTINENTE: {self.direccion}
        """
