"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/06/2025
Commentarios:
    Módulo que contiene la clase Paginator, que se encarga de manejar
    los datos paginados de las entidades.
"""
from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.base_entity import BaseEntity
from Model.Entities.material_urna_entity import MaterialUrnaEntity
from Model.Entities.search_commands import SearchCmd
from Model.Entities.urna_entity import UrnaEntity
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.Entities.categoria_incidencia_entity import CategoriaIncidenciaEntity
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.Entities.subcategoria_acuario_entity import SubcategoriaAcuarioEntity
from Model.Entities.subcategoria_incidencia import SubcategoriaIncidenciaEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity


class Paginator:
    """ Clase que gestiona la paginación del listado de entidades. """

    def __init__(self, procedure: str, records_page: int,
                 id_parent: int = None):
        """ Constructor de la clase. """

        self._id = id_parent                # Id, por sí hay que obtener
                                            # un listado dependiente de
                                            # otro.
        self._db = DBManager()              # Base de datos
        self._status = "UNFILTERED"         # Estado del paginador:
                                            #   UNFILTERED
                                            #   FILTERED
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

    # Base de datos
    @property
    def db(self):
        """ Devuelve la base de datos. """

        return self._db

    @db.setter
    def db(self, new_db):
        """ Válida y asigna la base de datos. """

        self._db = new_db

    # Estado del paginador
    @property
    def status(self):
        """ Devuelve el estado del páginador. """

        return self._status

    @status.setter
    def status(self, new_status: str):
        """ Válida y asigna el estado del paginador. """

        if new_status != "UNFILTERED" and new_status != "FILTERED":
            raise ValueError("El valor de la propiedad 'status' solo admite "
                             "los valores 'FILTERED' o 'UNFILTERED'.")

        self._status = new_status

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

        self._page_index = new_index

    # Número final
    @property
    def end(self) -> int:
        """ Devuelve el número final de la página. """

        return self._end

    @end.setter
    def end(self, new_end: int) -> None:
        """ Valida y asigna el número final de la página. """

        self._end = new_end

    # Número inicial
    @property
    def start(self) -> int:
        """ Obtiene el número inicial de la página. """

        return self._start

    @start.setter
    def start(self, new_start: int) -> None:
        """ Valida y asigna el número inicial de la página. """

        self._start = new_start

    # Página actual
    @property
    def current_page(self) -> int:
        """ Devuelve la página actual. """

        return self._current_page

    @current_page.setter
    def current_page(self, new_page: int) -> None:
        """ Valida y asigna el número de página actual. """

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

        if not new_pages or new_pages == 0:
            self.total_pages = 1

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
        :param page: Número de página a representar. Por defecto 1
        """

        # Comprueba que el número de página este dentro del rango
        if page < 1 or page > self.total_pages:
            self.total_pages = 1

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
        :param page: Número de página a representar. Por defecto 1
        """

        # Obtiene los datos
        res = BaseDAO.get_total_data(self.procedure)
        if not res.is_success:
            QMessageBox.warning(
                None,
                "ERROR DE PAGINACIÓN",
                res.error_msg
            )
            return

        # Mapea los datos a entidades
        data_list = self.map_entity_list(res.value)

        # Configura el paginador
        self.configure_paginator(data_list, page)

    def get_filtered_list(self, pattern: str, page: int = 1):
        """
        Obtiene la lista filtrada.
        :param pattern: Patrón de búsqueda
        :param page: Página a mostrar
        """

        # Obtenemos la instrucción sql
        sql = self.get_sql_command()

        # Obtiene los datos
        res = BaseDAO.get_filtered_data(sql, pattern)

        if not res.is_success:
            QMessageBox.warning(
                None,
                "ERROR DE PAGINACIÓN",
                res.error_msg
            )
            return

        # Mapea los datos a entidades
        data_list = self.map_entity_list(res.value)

        # Configura el paginador
        self.configure_paginator(data_list, page)

    def configure_paginator(self, data_list: list[BaseEntity], page: int)->None:
        """
        Configura el paginador.
        :param data_list: La lista de los datos
        :param page: Número de página a mostrar
        """

        self.total_data = data_list
        self.records = len(self.total_data)
        self.current_page = page
        self.current_data = self.get_paged_list(page)

    def map_entity_list(self, rows) -> list[BaseEntity]:
        """
        Mapea el resultado de la consulta a entidades.
        :param rows: Lista a mapear
        """

        # Configuramos la lista total
        if self.procedure == "VISTA_TIPOS_FILTRO":
            data_list = [TipoFiltroEntity(
                    id = ["ID"],
                    num = f["NUM"],
                    tipo_filtro = f["TIPO"],
                    observaciones = f["OBSERVACIONES"]
                )
                for f in rows
            ]
        elif self.procedure == "VISTA_TIPOS_ACUARIO":
            data_list = [TipoAcuarioEntity(
                    id=f["ID"],
                    num=f["NUM"],
                    id_cat_acuario=f["CATEGORIA"],
                    id_subcat_acuario=f["SUBCATEGORIA"],
                    observaciones=f["OBSERVACIONES"]
                )
                for f in rows
            ]

        elif self.procedure == "VISTA_CATEGORIAS_ACUARIO":
            data_list = [CategoriaAcuarioEntity(
                    id=f["ID"],
                    num=f["NUM"],
                    categoria=f["CATEGORIA"],
                    observaciones=f["OBSERVACIONES"]
                )
                for f in rows
            ]
        elif self.procedure == "VISTA_SUBCATEGORIAS_ACUARIO":
            data_list = [SubcategoriaAcuarioEntity(
                    id=f["ID"],
                    num=f["NUM"],
                    id_cat=f["CATEGORIA"],
                    subcategoria=f["SUBCATEGORIA"],
                    observaciones=f["OBSERVACIONES"]
                )
                for f in rows
            ]
        elif self.procedure == "VISTA_CATEGORIAS_INCIDENCIA":
            data_list = [CategoriaIncidenciaEntity(
                id=f["ID"],
                num=f["NUM"],
                categoria_incidencia=f["CATEGORIA"],
                observaciones=f["OBSERVACIONES"]
                )
                for f in rows
            ]
        elif self.procedure == "VISTA_SUBCATEGORIAS_INCIDENCIA":
            data_list = [SubcategoriaIncidenciaEntity(
                    id=f["ID"],
                    num=f["NUM"],
                    id_categoria=f["CATEGORIA"],
                    subcategoria=f["SUBCATEGORIA"],
                    observaciones=f ["OBSERVACIONES"]
                )
                for f in rows
            ]
        elif self.procedure == "VISTA_MARCAS_COMERCIALES":
            data_list = [MarcaComercialEntity(
                    id=["ID"],
                    num=f["NUM"],
                    nombre_marca=f["MARCA"],
                    direccion=f["DIRECCION"],
                    cod_postal=f["CODIGO_POSTAL"],
                    poblacion=f["POBLACION"],
                    provincia=f["PROVINCIA"],
                    id_pais=f["PAIS"],
                    observaciones=f["OBSERVACIONES"]
                )
                for f in rows
            ]
        elif self.procedure == "VISTA_URNAS":
            data_list = [UrnaEntity(
                    id=f["ID"],
                    num=f["NUM"],
                    id_marca=f["MARCA"],
                    modelo=f["MODELO"],
                    anchura=f["ANCHURA"],
                    profundidad=f["PROFUNDIDAD"],
                    altura=f["ALTURA"],
                    grosor_cristal=f["GROSOR"],
                    volumen_tanque=f["VOLUMEN_BRUTO"],
                    id_material=f["MATERIAL"],
                    descripcion=f["DESCRIPCION"]
                )
                for f in rows
            ]
        if self.procedure == "VISTA_MATERIALES_URNA":
            data_list = [MaterialUrnaEntity(
                    id=f["ID"],
                    num=f["NUM"],
                    material=f["MATERIAL"],
                    descripcion=f["DESCRIPCION"]
                )
                for f in rows
            ]
        return data_list

    def get_page_number_by_num(self, num: int) -> int:
        """
        Obtiene el número de página del paginator.
        :param num: Número de registro de la entidad
        """

        # Obtenemos el número de página
        page = num // self.records_page

        # En caso de que la página sea 0
        if page == 0:
            return 1

        # En caso de que la página no sea entera
        if num % self.records_page > 0:
            page += 1

        return page

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

    def get_sql_command(self) -> str:
        """ Obtiene la instrucción sql dependiendo del procedimiento. """

        # Configuramos la lista total
        if self.procedure == "VISTA_TIPOS_FILTRO":
            pass
        elif self.procedure == "VISTA_TIPOS_ACUARIO":
            return SearchCmd.SEARCH_TIPO_ACUARIO
        elif self.procedure == "VISTA_CATEGORIAS_ACUARIO":
            return SearchCmd.SEARCH_CATEGORIA_ACUARIO
        elif self.procedure == "VISTA_SUBCATEGORIAS_ACUARIO":
            return SearchCmd.SEARCH_SUBCATEGORIA_ACUARIO
        elif self.procedure == "VISTA_CATEGORIAS_INCIDENCIA":
            return SearchCmd.SEARCH_CATEGORIA_INCIDENCIA
        elif self.procedure == "VISTA_SUBCATEGORIAS_INCIDENCIA":
            return SearchCmd.SEARCH_SUBCATEGORIA_INCIDENCIA
        elif self.procedure == "VISTA_MARCAS_COMERCIALES":
            return SearchCmd.SEARCH_MARCA_COMERCIAL
        elif self.procedure == "VISTA_URNAS":
            pass
        elif self.procedure == "VISTA_MATERIALES_URNA":
            return SearchCmd.SEARCH_MATERIAL_URNA
