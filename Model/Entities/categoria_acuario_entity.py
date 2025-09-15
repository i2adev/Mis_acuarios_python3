"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Commentarios:
    Módulo que contiene la entidad CATEGORÍA DE ACUARIO.
"""

from Model.Entities.base_entity import BaseEntity


class CategoriaAcuarioEntity(BaseEntity):
    """ Entidad de categoría de acuario. """

    def __init__(self, id: int = None, num: int = None, categoria: str = None,
                 observaciones: str = None):
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param categoria: Categoría del acuario.
        :param observaciones: Observaciones de la categoría.
        """

        super().__init__()

        # Inicializamos las variables
        self.id = id
        self.num = num
        self.categoria = categoria
        self.observaciones = observaciones

    def __str__(self):
        return f""""
            ID:             {self.id}
            CATEGORIA:      {self.categoria}
            OBSERVACIONES:  {self.observaciones}
        """