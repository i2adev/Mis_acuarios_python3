"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene la entidad COMERCIO.
"""
from Model.Entities.base_entity import BaseEntity


class ComercioEntity(BaseEntity):
    """ Entidad de comercio. """

    def __init__(self, id: int = None, num: int = None,
                 nombre_comercio: str = None, direccion: str = None,
                 cod_postal: str = None, poblacion: str = None,
                 provincia: str = None, id_pais: int = None,
                 observaciones: str = None):
        """
        Constructor de clase.
        """

        super().__init__()

        # Inicializamos los atributos
        self._id = id
        self._num = num
        self._nombre_comercio = nombre_comercio
        self._direccion = direccion
        self._cod_postal = cod_postal
        self._poblacion = poblacion
        self._provincia = provincia
        self._id_pais = id_pais
        self._observaciones = observaciones

    @property
    def id(self):
        """ Id de la entidad """
        return self._id

    @id.setter
    def id(self, new_id):
        """ Id de la entidad """
        self._id = new_id

    @property
    def num(self):
        """ Número correlativo de la entidad """
        return self._num

    @num.setter
    def num(self, new_num):
        """ Número correlativo de la entidad """
        self._num = new_num

    @property
    def nombre_comercio(self):
        """ Nombre del comercio """
        return self._nombre_comercio

    @nombre_comercio.setter
    def nombre_comercio(self, new_nombre_comercio):
        """ Nombre del comercio """
        self._nombre_comercio = new_nombre_comercio

    @property
    def direccion(self):
        """ Dirección de la razón social del comercio """
        return self._direccion

    @direccion.setter
    def direccion(self, new_direccion):
        """ Dirección de la razón social del comercio """
        self._direccion = new_direccion

    @property
    def cod_postal(self):
        """ Código postal """
        return self._cod_postal

    @cod_postal.setter
    def cod_postal(self, new_cod_postal):
        """ Código postal """
        self._cod_postal = new_cod_postal

    @property
    def poblacion(self):
        """ Poblacion """
        return self._poblacion

    @poblacion.setter
    def poblacion(self, new_poblacion):
        """ Poblacion """
        self._poblacion = new_poblacion

    @property
    def provincia(self):
        """ Provincia """
        return self._provincia

    @provincia.setter
    def provincia(self, new_provincia):
        """ Provincia """
        self._provincia = new_provincia

    @property
    def id_pais(self):
        """ Id del páis """
        return self._id_pais

    @id_pais.setter
    def id_pais(self, new_id_pais):
        """ Id del páis """
        self._id_pais = new_id_pais

    @property
    def observaciones(self):
        """ Observaciones del comercio """
        return self._observaciones

    @observaciones.setter
    def observaciones(self, new_observaciones):
        """ Observaciones del comercio """
        self._observaciones = new_observaciones

    def __str__(self):
        return f"""
            ID:             {self.id}
            COMERCIO:       {self.nombre_comercio}
            OBSERVACIONES:  {self.observaciones:50}
        """
