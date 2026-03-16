"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/03/2026

Comentarios:
    Módulo que contiene la entidad GRUPO TAXONÓMICO.
"""

from Model.Entities.base_entity import BaseEntity


class GrupoTaxonomicoEntity(BaseEntity):
    """ Entidad del grupo taxonómico """

    def __init__(self, id: int = None, num: int = None,
                 grupo_taxo: str = None, descripcion: str = None):
        """
        Constructor de clase.

        Parámetros:
        :param id: Id de la entidad.
        :param num: Número de la entidad.
        :param grupo_taxo: Grupo taxonómico.
        :param descripcion: Descripción del grupo taxonómico.
        """

        super().__init__()

        # Inicializamos las variables
        self.__id = id
        self.__num = num
        self.__grupo_taxo = grupo_taxo
        self.__descripcion = descripcion

    # INICIO DE PROPIEDADES --------------------------------------------
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
        """ Número de la entidad. """
        return self.__num

    @num.setter
    def num(self, new_num: int):
        """ Número de la entidad. """
        self.__num = new_num

    @property
    def grupo_taxonomico(self) -> str:
        """ Grupo taxonómico. """
        return self.__grupo_taxo

    @grupo_taxonomico.setter
    def grupo_taxonomico(self, new_grupo: str):
        """ Grupo taxonómico. """
        self.__grupo_taxo = new_grupo

    @property
    def descripcion(self) -> str:
        """ Descripción del grupo taxonómico. """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str):
        """ Descripción del grupo taxonómico. """
        self.__descripcion = new_descripcion

    # FIN DE PROPIEDADES -----------------------------------------------

    def __str__(self):
        return f""""
            ID:             {self.id}
            GRUPO:          {self.grupo_taxonomico}
            DESCRIPCIÓN:    {self.descripcion}
        """
