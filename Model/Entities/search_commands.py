"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      12/09/2025
Commentarios:
    Módulo que contiene la clase Paginator, que se encarga de manejar
    los datos paginados de las entidades.
"""

class SearchCmd:
    """ Clase que contiene los commandos de búsqueda. """

    # Atributos estáticos
    ## Categoría acuario
    SEARCH_CATEGORIA_ACUARIO = """
    SELECT ID, NUM, CATEGORIA, OBSERVACIONES
    FROM
    (
        SELECT    ID_CATEGORIA_ACUARIO AS ID,
                  ROW_NUMBER() OVER(ORDER BY CATEGORIA_ACUARIO) AS NUM,
                  CATEGORIA_ACUARIO AS CATEGORIA,
                  OBSERVACIONES AS OBSERVACIONES,
                  UPPER(CATEGORIA_ACUARIO || OBSERVACIONES) AS FIELD
        FROM      CATEGORIAS_ACUARIO
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """
