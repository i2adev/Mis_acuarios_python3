"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/12/2025
Comentarios:
    Módulo que contiene la entidad EQUIPAMIENTO.
"""

from Model.Entities.base_entity import BaseEntity


class EquipamientoEntity(BaseEntity):
    """ Entidad de equipamiento. """

    def __init__(self, id: int = None, num: int = None,
                 id_categoria: int = None, id_marca: int = None,
                 modelo: str = None, numero_serie: str = None,
                 fecha_alta: int = None, fecha_baja: int = None,
                 motivo_baja: str = None, descripcion: str = None):
        """
        Constructor de clase:
        :param id: ID de la entidad equipamiento
        :param num: Número correlativo del equipamiento
        :param id_categoria: ID de la categoría del equipamientgto
        :param id_marca: ID de la marca del equipamiento
        :param modelo: Modelo del equipamiento
        :param numero_serie: Número de serie del equipamiento
        :param fecha_alta: Fecha de alta del equipamiento
        :param fecha_baja: Fecha de baja del equipamiento
        :param motivo_baja: Motivo de la baja del equipamiento
        :param descripcion: Descripcion del equipamiento
        """

        super().__init__()

        # Inicializamos las variables
        self._id = id
        self._num = num
        self._id_categoria = id_categoria
        self._id_marca = id_marca
        self._modelo = modelo
        self._numero_serie = numero_serie
        self._fecha_alta = fecha_alta
        self._fecha_baja = fecha_baja
        self._motivo_baja = motivo_baja
        self._descripcion = descripcion

    # INICIO PROPIEDADES
    @property
    def id(self) -> int | None:
        """ ID de la entidad de equipamiento. """
        return self._id

    @id.setter
    def id(self, new_id: int) -> None:
        """ ID de la entidad de equipamiento. """
        self._id = new_id

    @property
    def num(self) -> int | None:
        """ Número correlativo de la entidad de equipamiento. """
        return self._num

    @num.setter
    def num(self, new_num: int) -> None:
        """ Número correlativo de la entidad de equipamiento. """
        self._num = new_num

    @property
    def id_categoria(self) -> int | None:
        """ ID de la categoría de equipamiento. """
        return self._id_categoria

    @id_categoria.setter
    def id_categoria(self, new_id: int) -> None:
        """ ID de la categoría de equipamiento. """
        self._id_categoria = new_id

    @property
    def id_marca(self) -> int | None:
        """ ID de la marca de equipamiento. """
        return self._id_marca

    @id_marca.setter
    def id_marca(self, new_id: int) -> None:
        """ ID de la marca de equipamiento. """
        self._id_marca = new_id

    @property
    def modelo(self) -> str:
        """ Modelo del equipamiento. """
        return self._modelo

    @modelo.setter
    def modelo(self, new_modelo: str) -> None:
        """ Modelo del equipamiento. """
        self._modelo = new_modelo

    @property
    def numero_serie(self) -> str:
        """ Numero de serie del equipamiento. """
        return self._numero_serie

    @numero_serie.setter
    def numero_serie(self, new_numero_serie: str) -> None:
        """ Numero de serie del equipamiento. """
        self._numero_serie = new_numero_serie

    @property
    def fecha_alta(self) -> int | None:
        """ Fecha de alta del equipamiento. """
        return self._fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, new_fecha_alta: int) -> None:
        """ Fecha de alta del equipamiento. """
        self._fecha_alta = new_fecha_alta

    @property
    def fecha_baja(self) -> int | None:
        """ Fecha de baja del equipamiento. """
        return self._fecha_baja

    @fecha_baja.setter
    def fecha_baja(self, new_fecha_baja: int) -> None:
        """ Fecha de baja del equipamiento. """
        self._fecha_baja = new_fecha_baja

    @property
    def motivo_baja(self) -> int | None:
        """ Motivo de la baja del equipamiento. """
        return self._motivo_baja

    @motivo_baja.setter
    def motivo_baja(self, new_motivo_baja: int) -> None:
        """ Motivo de la baja del equipamiento. """
        self._motivo_baja = new_motivo_baja

    @property
    def descripcion(self) -> str:
        """ Descripción del equipamiento. """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, new_descripcion: str) -> None:
        """ Descripción del equipamiento. """
        self._descripcion = new_descripcion

    # FIN PROPIEDADES

    def __str__(self):
        """ Muestra información de la clase. """

        return f"""
            ID:             {self.id}
            NUM:            {self.num}
            ID DE LA MARCA: {self.id_marca}
            MODELO:         {self.modelo}
            DESCRICIÓN:     {self.descripcion:50}
            ------------------------------------------------------------
        """
