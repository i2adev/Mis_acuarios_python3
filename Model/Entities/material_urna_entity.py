"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/08/2025
Commentarios:
    Módulo que contiene la entidad MATERIAL DE URNA.
"""
from Model.Entities.base_entity import BaseEntity


class MaterialUrnaEntity(BaseEntity):
    """ Clase del material de la urna. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    material: str | None
    descripcion: str | None

    def __init__(self, id: int = None, num: int = None, material: str = None,
                 descripcion: str = None):
        """
        Constructor de clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad en listas
        :param material: Material con el que se fabricó la urna
        :param descripcion: Descripción del material
        """

        super().__init__()

        self.id = id
        self.num = num
        self.material = material
        self.descripcion = descripcion

    def __str__(self):
        return f"""
            ID:         {self.id}
            MATERIAL:   {self.material}
        """