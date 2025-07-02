"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/06/2025
Commentarios:
    Módulo que contien la entidad TIPO DE ACUARIO.
"""
from Model.Entities.base_entity import BaseEntity


class TipoAcuarioEntity(BaseEntity):
    """ Entidad del tipo de acuario. """

    # Anotaciones de tipo (atributos con sus tipos esperados)
    id: int | None
    num: int | None
    id_categoria_acuario: int | None
    id_subcat_acuario: int | None
    observaciones: str | None

    def __init__(self, id: int = None, num: int = None, id_cat_acuario: int = None,
                 id_subcat_acuario: int = None, observaciones: str = None):
        """
        Constructor de clase.

        Parámetros:
        - id = Id del tipo de acuario.
        - Num: Número correlativo del tipo de acuario.
        - Tipo_acuario: Tipo de acuario.
        - Subtipo de acuario: Subtipo de acuario.
        - Observaciones: Observaciones relacionadas con el tipo de acuario.
        """

        super().__init__()

        # Inicializamos las variables
        self.id = id
        self.num = num
        self.id_categoria_acuario = id_cat_acuario
        self.id_subcategoria_acuario = id_subcat_acuario
        self.observaciones = observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            NUM:            {self.num}
            TIPO ACUARIO:   {self.id_categoria_acuario}
            SUBTIPO ACUA.:  {self.id_subcategoria_acuario}    
            OBSERVACIONES:  {self.observaciones:50}
            ------------------------------------------------------------
        """