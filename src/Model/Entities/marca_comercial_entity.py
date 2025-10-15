"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/07/2025
Commentarios:
    Módulo que contiene la entidad MARCA DE PRODUCTO.
"""
from Model.Entities.base_entity import BaseEntity


class MarcaComercialEntity(BaseEntity):
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
        self.__id = id
        self.__num = num
        self.__nombre_marca = nombre_marca
        self.__direccion = direccion
        self.__cod_postal = cod_postal
        self.__poblacion = poblacion
        self.__provincia = provincia
        self.__id_pais = id_pais
        self.__observaciones = observaciones

    @property
    def id(self) -> int | None:
        """ Id de la entidad. """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """ Id de la entidad. """
        self.__id = new_id

    @property
    def num(self) -> int | None:
        """ Número correlativo de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Número correlativo de la entidad. """
        self.__num = new_num

    @property
    def nombre_marca(self) -> str | None:
        """ Nombre de la marca. """
        return self.__nombre_marca
    @nombre_marca.setter
    def nombre_marca(self, new_nombre_marca: str) -> None:
        """ Nombre de la marca. """
        self.__nombre_marca = new_nombre_marca

    @property
    def direccion(self) -> str | None:
        """ Dirección de la sede de la marca. """
        return self.__direccion

    @direccion.setter
    def direccion(self, new_direccion: str) -> None:
        """ Dirección de la sede de la marca. """
        self.__direccion = new_direccion

    @property
    def cod_postal(self) -> str | None:
        """ Código postal de la ciudad de la marca. """
        return self.__cod_postal

    @cod_postal.setter
    def cod_postal(self, new_cod_postal: str) -> None:
        """ Código postal de la ciudad de la marca. """

    @property
    def poblacion(self) -> str | None:
        """ Población donde se encuentra la sede de la marca. """
        return self.__poblacion

    @poblacion.setter
    def poblacion(self, new_poblacion: str) -> None:
        """ Población donde se encuentra la sede de la marca. """
        self.__poblacion = new_poblacion

    @property
    def provincia(self) -> str | None:
        """ Provincia donde se encuentra la sede de la marca. """
        return self.__provincia

    @provincia.setter
    def provincia(self, new_provincia: str) -> None:
        """ Provincia donde se encuentra la sede de la marca. """
        self.__provincia = new_provincia

    @property
    def id_pais(self) -> int | None:
        """ Id del país donde se encuentra la sede de la marca. """
        return self.__id_pais

    @id_pais.setter
    def id_pais(self, new_id: int) -> None:
        """ Id del país donde se encuentra la sede de la marca. """
        self.__id_pais = new_id

    @property
    def observaciones(self) -> str | None:
        """ Observaciones sobre la marca. """
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones: str) -> None:
        """ Observaciones sobre la marca. """
        self.__observaciones = new_observaciones

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