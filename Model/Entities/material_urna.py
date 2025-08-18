"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      12/08/2025
Commentarios:
    Módulo que contiene la entidad MATERIAL DE URNA.
"""

class MaterialUrnaEntity:
    """ Entidad de material de urna. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    material: str | None
    descripcion: str | None

    def __init__(self, id: int = None, num: int = None, material: int = None,
                 descripcion: str = None):
        """
        Constructor de clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param material: Material de la urna
        :param descripcion: Observaciones sobre el material
        """

        super().__init__()

        # Inicializamos las variables
        self.id = id
        self.num = num
        self.material = material
        self.descripcion = descripcion

    def __str__(self):
        return f"""
            ID:             {self.id}
            MATERIAL:       {self.material}
        """