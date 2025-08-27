"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/06/2025
Commentarios:
    Módulo que contiene la entidad SUBCATEGORÍA DE ACUARIO.
"""
from Model.Entities.base_entity import BaseEntity


class SubcategoriaAcuarioEntity(BaseEntity):
    """ Entidad de la categoría de acuario. """

    # Anotaciones de tipo
    id: int | None
    num: int | None
    id_categoria: int | None
    subcategoria: str | None
    observaciones: str | None

    def __init__(self, id_: int = None, num: int = None, id_cat: int = None,
                 subcategoria: str = None, observaciones: str = None):
        """ 
        Constructor de clase. 
        
        Parámetros:
        :param id: Id de la entidad.
        :param id_cat: Id de la categoria de acuario.
        :param subcategoria: Subcategoría de acuario.
        :param observaciones: Observaciones de la subcategoría.
        """

        super().__init__()
        # Inicializamos las variables
        self.id = id_
        self.num = num
        self.id_categoria = id_cat
        self.subcategoria = subcategoria
        self.observaciones = observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            SUBCATEGORIA:   {self.subcategoria}
            OBSERVACIONES:  {self.observaciones}
        """
