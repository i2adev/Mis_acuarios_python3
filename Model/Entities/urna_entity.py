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
                 modelo: str = None, anchura: int = None, profundidad :int= None,
                 altura: int = None, grosor_cristal: int = None,
                 volumen_tanque: int = None, id_material:int = None,
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
        self.id = id
        self.num = num
        self.id_marca = id_marca
        self.modelo = modelo
        self.anchura = anchura
        self.profundidad = profundidad
        self.altura = altura
        self.volumen_tanque = volumen_tanque
        self.grosor_cristal = grosor_cristal
        self.id_material = id_material
        self.descripcion = descripcion

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