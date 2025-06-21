"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contien la entidad TIPO DE FILTRO.
"""
from pathlib import Path
from Model.Entities.base_entity import BaseEntity

class TipoFiltroEntity(BaseEntity):
    """ Entidad del tipo de filtro. """

    # Anotaciones de tipo (atributos con sus tipos esperados)
    id: int | None
    num: int | None
    tipo_filtro: str | None
    observaciones: str | None

    def __init__(self, id_tf: int = None, num_tf: int = None, tipo_filtro:
    str = None,
                 observaciones: str = None):
        """
        Constructor:
            - Parámetro tipo_filtro: Cadena con el tipo de filtro.
            - Parámetro observaciones: Cadena con las observaciones
              sobre el tipo de filtro.
        """
        super().__init__()

        # Inicializamos las variables
        self.id = id_tf
        self.num = num_tf
        self.tipo_filtro = tipo_filtro
        self.observaciones = observaciones

    def __str__(self):
        """ Muestra información de la clase. """

        return f"""
            ID:             {self.id}
            NUM:            {self.num}
            TIPO FILTRO:    {self.tipo_filtro}
            OBSERVACIONES:  {self.observaciones:50}
            ------------------------------------------------------------
        """