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

    def __init__(self, id_tf: int = None, tipo_filtro: str = None,
                 observaciones: str = None):
        """
        Constructor:
            - Parámetro tipo_filtro: Cadena con el tipo de filtro.
            - Parámetro observaciones: Cadena con las observaciones
              sobre el tipo de filtro.
        """
        super().__init__()

        # Inicializamos las variables
        self.id_tf = id_tf
        self.tipo_filtro = tipo_filtro
        self.observaciones = observaciones

    def get_type(self: BaseEntity) -> str:
        """ Obtiene el nombre de la clase. """
        return type(self).__name__

