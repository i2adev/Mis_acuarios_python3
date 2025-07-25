"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Commentarios:
    Módulo que contiene la entidad SUBCATEGORÍA DE INCIDENCIA.
"""
from Model.Entities.base_entity import BaseEntity


class SubcategoriaIncidenciaEntity(BaseEntity):
    """ Entidad de la categoría de incidencia. """

    # ANotaciones de tipo
    id: int | None
    num: int | None
    id_categoria: int | None
    subcategoria: str | None
    observaciones: str | None

    def __init__(self, id = None, num = None, id_categoria = None,
                 subcategoria = None, observaciones = None):
        """
        Constructor de clase:

        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param id_categoria: ID de la ategoría de la incidencia
        :param subcategoria: Subcategoria de incidencia
        :param observaciones: Observaciones de la incidencia
        """

        super().__init__()

        # Inicializamos los atributos
        self.id = id
        self.num = num
        self.id_categoria = id_categoria
        self.subcategoria = subcategoria
        self.observaciones = observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            CATEGORÍA:      {self.id_categoria}
            SUBCATEGORÍA:   {self.subcategoria}
            OBSERVACIONES:  {self.observaciones}
        """