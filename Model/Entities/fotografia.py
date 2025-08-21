"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/08/2025
Commentarios:
    Módulo que contiene la entidad FOTOGRAFÍA.
"""

class FotografiaEntity:
    """ Entidad de fotografía. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    id_foranea: int | None
    ruta: str | None
    fotografia: bytes | None

    def __init__(self, id: int = None, num: int = None, id_foranea: int = None,
                 ruta: str = None,fotografia: bytes = None):
        """
        Constructor de clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param id_foranea: Id de la tabla dependiente
        :param ruta: Ruta de la imagen a cargar
        :param fotografia: Fotografía
        """

        super().__init__()

        # Inicializamos las variables
        self.id = id
        self.num = num
        self.id_foranea = id_foranea
        self.ruta = ruta
        self.fotografia = fotografia

    def __str__(self):
        return f"""
            ID:         {self.id}
            NUM:        {self.num}
            RELACION:   {self.id_foranea}
            RUTA:       {self.ruta}
        """
