"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/07/2025
Commentarios:
    Módulo que contiene la entidad MARCA DE PRODUCTO.
"""

class MarcaComercialEntity:
    """ Entidad de la marca de producto. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    nombre_marca: str | None
    direccion: str | None
    cod_postal: str | None
    poblacion: str | None
    provincia: str | None
    id_pais: int | None
    observaciones: str | None

    def __init__(self, id = None, num = None, nombre_marca = None,
                 direccion = None, cod_postal = None, poblacion = None,
                 provincia = None, id_pais = None, observaciones = None):
        """
        Constructor de clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param nombre_marca: Nombre de la marca
        :param direccion: Dirección postal de la sede de la marca
        :param cod_postal: Codigo postal de la población
        :param poblacion: Población donde se encuentra la sede de la marca
        :param provincia: Provincia donde se encuentra la sede de la marca
        :param id_pais: Id del país donde se encuentra la sede central de la marca
        :param observaciones: Observaciones sobre la marca
        """

        super().__init__()

        # Inicializamos las variables
        self.id = id
        self.num = num
        self.nombre_marca = nombre_marca
        self.direccion = direccion
        self.cod_postal = cod_postal
        self.poblacion = poblacion
        self.provincia = provincia
        self.id_pais = id_pais
        self.observaciones = observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            MARCA:          {self.nombre_marca}
            DIRECCIÓN:      {self.direccion}
            CÓDIGO_POST.:   {self.cod_postal}
            POBLACIÓN:      {self.poblacion}
            PROVINCIA:      {self.provincia}
            ID_PAIS:        {self.id_pais}
        """