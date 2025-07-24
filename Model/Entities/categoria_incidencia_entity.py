"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Commentarios:
    Módulo que contiene la entidad CATEGORÍA DE INCIDENCIA.
"""
from Model.Entities.base_entity import BaseEntity


class CategoriaIncidenciaEntity(BaseEntity):
    """ Entidad de la categoría de incidencia. """

    # ANotaciones de tipo
    id: int | None
    num: int | None
    categoria_incidencia: str | None
    observaciones: str | None

    def __init__(self, id = None, num = None, categoria_incidencia = None,
                 observaciones = None):
        """
        Constructor de clase:

        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param categoria_incidencia: Categoría de la incidencia
        :param observaciones: Observaciones de la incidencia
        """

        super().__init__()

        # Inicializamos los atributos
        self.id = id
        self.num = num
        self.categoria_incidencia = categoria_incidencia
        self.observaciones = observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            CATEGORÍA:   {self.categoria_incidencia}
            OBSERVACIONES:  {self.observaciones}
        """