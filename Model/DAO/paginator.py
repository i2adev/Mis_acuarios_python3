"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/06/2025
Commentarios:
    Módulo que contiene la clase Paginator, que se encarga de manejar
    los datos paginados de las entidades.
"""
from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO

class Paginator:
    """ Clase que gestiona la paginación del listado de entidades. """

    def __init__(self, procedure: str, records_page: int,
                 id_parent: int = None):
        """ Constructor de la clase. """

        self._id = id_parent                # Id, por sí hay que obtener
                                            # un listado dependiente de
                                            # otro.
        self._procedure = procedure         # Procedimiento.
        self._records_page = records_page   # Registros por página.
        self._total_data = None             # Lista total de elementos.
        self._current_data = None           # Lista de los datos de la
                                            # página actual.
        self._records = None                # Registros totales.
        self._total_pages = None            # Número de páginas totales.
        self._current_page = None           # Número de página actual.
        self._start = None                  # Numero inicial de registro.
        self._end = None                    # Número final de registro.
        self._page_index = None             # Ïndice de página.

    """ ****************************************************************
        * GETTERS Y SETTER DE LAS PROPIEDADES.                         *
        ****************************************************************
    """
    # Id de la entidad dependiente
    @property
    def id(self) -> int:
        """ Devuelve el id_parent dependiente. """

        return self._id

    @id.setter
    def id(self, new_id: int) -> None:
        """ Válida y asigna el ID. """

        self._id = new_id

    # Datos actuales
    @property
    def current_data(self) -> list:
        """ Devuelve el listado de la página actual. """

        return self._current_data

    @current_data.setter
    def current_data(self, data: list) -> None:
        """ Válida y asigna la lista con todos los datos. """

        self._current_data = data

    # Datos totales
    @property
    def total_data(self) -> list:
        """ Devuelve el listado completo. """

        return self._total_data

    @total_data.setter
    def total_data(self, data: list) -> None:
        """ Válida y asigna la lista con todos los datos. """

        self._total_data = data

    # Ïndice de página
    @property
    def page_index(self) -> int:
        """ Devuelve el índice de la página. """

        return self._page_index

    @page_index.setter
    def page_index(self, new_index) -> None:
        """ Válida y asigna el índice de página. """

        if not self.total_data:
            raise ValueError(
                """
                CLASE NO CONFIGURADA. DEBES INICIALIZAR LA CLASE PRIMERO.
                """
            )

        self._page_index = new_index

    # Número final
    @property
    def end(self) -> int:
        """ Devuelve el número final de la página. """

        return self._end

    @end.setter
    def end(self, new_end: int) -> None:
        """ Valida y asigna el número final de la página. """

        if not self.total_data:
            raise ValueError(
                """
                CLASE NO CONFIGURADA. DEBES INICIALIZAR LA CLASE PRIMERO.
                """
            )

        self._end = new_end

    # Número inicial
    @property
    def start(self) -> int:
        """ Obtiene el número inicial de la página. """

        return self._start

    @start.setter
    def start(self, new_start: int) -> None:
        """ Valida y asigna el número inicial de la página. """

        if not self.total_data:
            raise ValueError(
                """
                CLASE NO CONFIGURADA. DEBES INICIALIZAR LA CLASE PRIMERO.
                """
            )

        self._start = new_start

    # Página actual
    @property
    def current_page(self) -> int:
        """ Devuelve la página actual. """

        return self._current_page

    @current_page.setter
    def current_page(self, new_page: int) -> None:
        """ Valida y asigna el número de página actual. """

        if not self.total_data:
            raise ValueError(
                """
                CLASE NO CONFIGURADA. DEBES INICIALIZAR LA CLASE PRIMERO.
                """
            )

        if not new_page or new_page == 0:
            self.current_page = 1
            self.page_index = 0
        else:
            self._current_page = new_page
            self._page_index = new_page - 1

    # Número de registros
    @property
    def records(self) -> int:
        """ Devuelve el número de registros del listado. """

        return self._records

    @records.setter
    def records(self, new_records: int) -> None:
        """ Válida y asigna un nuevo número de registros. """

        self._records = new_records

        # Sí los registros totales son menor o igual a registros por
        # página
        if self.records <= self.records_page:
            self._total_pages = 1

        # Establece el número de páginas totales
        self.total_pages = self.records // self.records_page
        if self.records % self.records_page:
            self.total_pages += 1

    # Páginas totales
    @property
    def total_pages(self) -> int:
        """ Getter: Devuelve el número total de páginas. """

        return self._total_pages

    @total_pages.setter
    def total_pages(self, new_pages: int) -> None:
        """ Valida y asigna el número total de páginas. """

        if not self.total_data:
            raise ValueError(
                """
                CLASE NO CONFIGURADA. DEBES INICIALIZAR LA CLASE PRIMERO.
                """
            )

        if not new_pages or new_pages == 0:
            raise ValueError(
                "EL NÚMERO DE PÁGINAS NO PUEDE ESTAR VACíO NI SER 0. "
            )

        self._total_pages = new_pages

    # Procedure
    @property
    def procedure(self) -> str:
        """ Getter: Devuelve el valor de procedure. """

        return self._procedure

    @procedure.setter
    def procedure(self, new_procedure: str) -> None:
        """ Setter: Válida y asigna un nuevo procedimiento. """

        if not new_procedure:
            raise ValueError(
                "EL NOMBRE DEL PROCEDIMIENTO NO PUEDE ESTAR VACÍO."
            )

        self._procedure = new_procedure

    # Registros por página
    @property
    def records_page(self) -> int:
        """ Getter: Devuelve el número de registros por página. """

        return self._records_page

    @records_page.setter
    def records_page(self, new_records: int) -> None:
        """
        Setter: Valida y asigna un nuevo número para los registros por
        página (Máximo 20).
        """

        if new_records > 20:
            raise ValueError("NO SE PUEDEN PAGINAR MAS DE 20 REGISTROS.")

        self._records_page = new_records

    """ ****************************************************************
        * OBTENEMOS LAS LISTAS.                                        *
        ****************************************************************
    """

    def get_paged_list(self, page: int = 1) -> list:
        """
        Obtiene los datos de la página pasada como parámetro.

        Parámetros:
        - PAGE: Número de página a representar.
        - ID: Id de la entidad a filtrar
        """

        # Comprobamos los datos
        if not self.total_data:
            raise ValueError(
                """
                CLASE NO CONFIGURADA. DEBES INICIALIZAR LA CLASE PRIMERO.
                """
            )

        # Comprueba que el número de página este dentro del rango
        if page < 1 or page > self.total_pages:
            raise ValueError(
                """
                NÚMERO DE PA´GINA FUERA DE RANGO.
                - EL NÚMERO DE PÁGINA DEBE SER COMO MINIMO 1.
                - EL NÚMERO DE PÁGINA DEBE SER MENOR O IGUAL AL NÚMERO 
                  TOTAL DE PÁGINAS.
                """
            )

        # Inicializamos las variables
        self.current_page = page
        self.page_index = page -1
        self.start = (self.current_page - 1) * self.records_page + 1
        self.end = self.current_page * self.records_page
        paged_list = self.total_data[self.start - 1 : self.end]

        return paged_list

    def initialize_paginator(self, page: int = 1) -> None:
        """
        Inicializa el paginador.

        Parámetros:
        - PAGE: El número de página a mostrar
        """

        res = BaseDAO.get_total_data(self.procedure)
        if not res.is_success:
            QMessageBox.warning(
                None,
                "ERROR DE PAGINACIÓN",
                res.error_msg
            )
            return

        self.total_data = res.value
        self.records = len(self.total_data)

        if page < 1 or page > self.total_pages:
            QMessageBox.warning(
                None,
                "ERROR DE PAGINACIÓN",
                f"""ERROR EN EL NÚMERO DE PÁGINA {page}
                - EL NUMERO DE PÁGINA HA DE SER MAYOR QUE 0.
                - EL NUMERO DE PÁGINA HA DE SER MENOR O IGUAL QUE {self.total_pages}"""
            )
            return

        self.current_page = page
        self.current_data = self.get_paged_list(page)

    def __str__(self):
        """ Muestra el objeto en forma de texto. """

        return (
            f"""
            PROCEDURE:          {self.procedure}
            RECORDS BY PAGE:    {self.records_page}
            RECORDS:            {self.records}
            TOTAL PAGES:        {self.total_pages}    
            CURRENT PAGE:       {self.current_page}
                START:          {self.start}
                END:            {self.end}       
            """
        )

