"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      11/08/2025
Commentarios:
    Módulo que contiene la entidad ACUARIO.
"""
from Model.Entities.base_entity import BaseEntity


class UrnaEntity(BaseEntity):
    """ Entidad de urna. """

    # Notaciones de tipo
    id: int | None
    num: int | None
    id_marca: int | None
    modelo: str | None
    anchura: int | None
    profundidad: int | None
    altura: int | None
    grosor_cristal: int | None
    volumen_tanque: int | None
    id_material: int | None
    descripcion: str | None

    def __init__(self, id: int = None, num: int = None, id_marca: int = None,
                 modelo: str = None, anchura: int = None,
                 profundidad: int = None,
                 altura: int = None, grosor_cristal: int = None,
                 volumen_tanque: int = None, id_material: int = None,
                 descripcion: str = None):
        """
        Constructor de clase.
        :param id: Id de la entidad
        :param num: Número correlativo de la entidad
        :param id_marca: Id de la marca del acuario
        :param modelo: Modelo del acuario
        :param anchura: Anchura del acuario en cm
        :param profundidad: Profundidad del acuario en cm
        :param altura: Altura del acuario en cm
        :param grosor_cristal: Grosor que tiene el cristal del acuario
        :param volumen_tanque: Volumen del tanque en litros
        :param id_material: Id del material de la urna
        :param observaciones: Observaciones sobre la marca
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__id_marca = id_marca
        self.__modelo = modelo
        self.__anchura = anchura
        self.__profundidad = profundidad
        self.__altura = altura
        self.__volumen_tanque = volumen_tanque
        self.__grosor_cristal = grosor_cristal
        self.__id_material = id_material
        self.__descripcion = descripcion

    @property
    def id(self) -> int:
        """ Id de la entidad. """
        return self.__id

    @id.setter
    def id(self, new_id: int):
        """ Id de la entidad. """
        self.__id = new_id

    @property
    def num(self) -> int:
        """ Número correlativo de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num: int):
        """ Número correlativo de la entidad. """
        self.__num = new_num

    @property
    def id_marca(self) -> int:
        """ Id de la marca. """
        return self.__id_marca

    @id_marca.setter
    def id_marca(self, new_id: int):
        """ Id de la marca. """
        self.__id_marca = new_id

    @property
    def modelo(self) -> str:
        """ Modelo del acuario. """
        return self.__modelo

    @modelo.setter
    def modelo(self, new_modelo: str):
        """ Modelo del acuario. """
        self.__modelo = new_modelo

    @property
    def anchura(self) -> int:
        """ Anchura del acuario. """
        return self.__anchura

    @anchura.setter
    def anchura(self, new_anchura: int):
        """ Anchura del acuario. """
        self.__anchura = new_anchura

    @property
    def profundidad(self) -> int:
        """ Profundidad del acuario. """
        return self.__profundidad

    @profundidad.setter
    def profundidad(self, new_profundidad: int):
        """ Profundidad del acuario. """
        self.__profundidad = new_profundidad

    @property
    def altura(self) -> int:
        """ Altura del acuario. """
        return self.__altura

    @altura.setter
    def altura(self, new_altura: int):
        """ Altura del acuario. """
        self.__altura = new_altura

    @property
    def grosor_cristal(self) -> int:
        """ Grosor que tiene el cristal del acuario. """
        return self.__grosor_cristal

    @grosor_cristal.setter
    def grosor_cristal(self, new_grosor_cristal: int):
        """ Grosor que tiene el cristal del acuario. """
        self.__grosor_cristal = new_grosor_cristal

    @property
    def volumen_tanque(self) -> int:
        """ Volumen del tanque en litros. """
        return self.__volumen_tanque

    @volumen_tanque.setter
    def volumen_tanque(self, new_volumen_tanque: int):
        """ Volumen del tanque en litros. """
        self.__volumen_tanque = new_volumen_tanque

    @property
    def id_material(self) -> int:
        """ Id del material de la urna. """
        return self.__id_material

    @id_material.setter
    def id_material(self, new_id: int):
        """ Id del material de la urna. """
        self.__id_material = new_id

    @property
    def descripcion(self) -> str:
        """ Descripcion de la entidad. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripcion de la entidad. """
        self.__descripcion = new_descripcion

    def __str__(self):
        return f"""
            ID:             {self.id}
            ID_MARCA:       {self.id_marca}
            MODELO:         {self.modelo}
            ANCHURA.:       {self.anchura} cm
            PROFUNDIDAD:    {self.profundidad} cm
            ALTURA:         {self.altura} cm
            VOLUMEN:        {self.volumen_tanque} litros
        """
