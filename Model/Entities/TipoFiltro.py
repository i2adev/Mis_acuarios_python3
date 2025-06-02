'''
Entidad del tipo de fiultro
'''
from pathlib import Path
from BaseEntity import BaseEntity

class TipoFiltro(BaseEntity):
    '''Entidad del tipo de filtro'''

    def __init__(self, tipo_filtro: str, observaciones: str, id_tf: int = None):
        '''Constructor:
            - Parámetro tipo_filtro: Cadena con el tipo de filtro.
            - Parámetro observaciones: Cadena con las observaciones debre el
              tipo de filtro.'''
        # Inicializamos las variables
        self.id_tf = id_tf
        self.tipo_filtro = tipo_filtro
        self.observaciones = observaciones

    def get_type(self: BaseEntity) -> str:
        return type(self).__name__

