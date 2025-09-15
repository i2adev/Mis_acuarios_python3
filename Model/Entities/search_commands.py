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

    ## Categoría de incidencia
    SEARCH_CATEGORIA_INCIDENCIA = """
        SELECT ID, NUM, CATEGORIA, OBSERVACIONES
    FROM
    (
        SELECT    ID_CATEGORIA AS ID,
                  ROW_NUMBER() OVER(ORDER BY CATEGORIA_INCIDENCIA) AS NUM,
                  CATEGORIA_INCIDENCIA AS CATEGORIA,
                  OBSERVACIONES AS OBSERVACIONES,
                  UPPER(CATEGORIA_INCIDENCIA || OBSERVACIONES) AS FIELD
        FROM      CATEGORIAS_INCIDENCIA
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    ## Marca comercial
    SEARCH_MARCA_COMERCIAL = """
    SELECT  ID, NUM, MARCA, DIRECCION, CODIGO_POSTAL, 
            POBLACION, PROVINCIA, PAIS, OBSERVACIONES
    FROM
    (
        SELECT  M.ID_MARCA AS ID,
                ROW_NUMBER() OVER(ORDER BY M.MARCA) AS NUM,
                M.MARCA AS MARCA,
                M.DIRECCION AS DIRECCION,
                M.COD_POSTAL AS CODIGO_POSTAL,
                M.POBLACION AS POBLACION,
                M.PROVINCIA AS PROVINCIA,
                P.PAIS AS PAIS,
                M.OBSERVACIONES AS OBSERVACIONES,
                UPPER(
                    IFNULL(M.MARCA, '') || IFNULL(M.DIRECCION, '') 
                    || IFNULL(M.COD_POSTAL, '') || IFNULL(M.POBLACION, '') 
                    || IFNULL(M.PROVINCIA, '') || IFNULL(P.PAIS, '') 
                    || IFNULL(M.OBSERVACIONES, '')
                ) AS FIELD
        FROM          MARCAS_COMERCIALES M
        LEFT JOIN     PAISES P
        ON            M.ID_PAIS = P.ID_PAIS
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    ## Material de urna
    SEARCH_MATERIAL_URNA = """
    SELECT    ID, NUM, MATERIAL, DESCRIPCION
    FROM
    (
        SELECT    ID_MATERIAL AS ID,
                  ROW_NUMBER() OVER(ORDER BY MATERIAL) AS NUM,
                  MATERIAL AS MATERIAL,
                  DESCRIPCION AS DESCRIPCION,
                  UPPER(IFNULL(MATERIAL, '') || IFNULL(DESCRIPCION, '')) 
                    AS FIELD
        FROM      MATERIALES_URNA
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    ## Subacategoría de acuarios
    SEARCH_SUBCATEGORIA_ACUARIO = """
    SELECT    ID, NUM, CATEGORIA, SUBCATEGORIA, OBSERVACIONES
    FROM
    (
        SELECT      S.ID_SUBCATEGORIA_ACUARIO AS ID,
                    ROW_NUMBER() OVER(ORDER BY S.ID_SUBCATEGORIA_ACUARIO) AS NUM,
                    C.CATEGORIA_ACUARIO AS CATEGORIA,
                    S.SUBCATEGORIA_ACUARIO AS SUBCATEGORIA,
                    S.OBSERVACIONES AS OBSERVACIONES,
                    UPPER(IFNULL(C.CATEGORIA_ACUARIO, '') 
                        || IFNULL(S.SUBCATEGORIA_ACUARIO, '') 
                        || IFNULL(S.OBSERVACIONES, '')) AS FIELD
        FROM        SUBCATEGORIAS_ACUARIO S
        LEFT JOIN   CATEGORIAS_ACUARIO C
            ON      S.ID_CATEGORIA_ACUARIO = C.ID_CATEGORIA_ACUARIO
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';   
    """

    ## Subcategoría incidencia
    SEARCH_SUBCATEGORIA_INCIDENCIA = """
    SELECT  ID, NUM, CATEGORIA, SUBCATEGORIA, OBSERVACIONES
    FROM
    (
        SELECT S.ID_SUBCATEGORIA AS ID,
               ROW_NUMBER() OVER (ORDER BY S.NOMBRE_SUBCATEGORIA) AS NUM,
               C.CATEGORIA_INCIDENCIA AS CATEGORIA,
               S.NOMBRE_SUBCATEGORIA AS SUBCATEGORIA,
               S.DESCRIPCION AS OBSERVACIONES,
               UPPER(IFNULL(C.CATEGORIA_INCIDENCIA, '') || IFNULL(S.NOMBRE_SUBCATEGORIA, '') || IFNULL(S.DESCRIPCION, '')) AS FIELD
        FROM   SUBCATEGORIAS_INCIDENCIA S
        LEFT JOIN CATEGORIAS_INCIDENCIA C 
        ON     S.ID_CATEGORIA = C.ID_CATEGORIA
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    ## Tipo de acuario
    SEARCH_TIPO_ACUARIO = """
    SELECT       ID, NUM, CATEGORIA, SUBCATEGORIA, OBSERVACIONES
    FROM
    (
        SELECT       ID_TIPO AS ID,
                     ROW_NUMBER() OVER (ORDER BY CA.CATEGORIA_ACUARIO, SA.SUBCATEGORIA_ACUARIO) AS NUM,
                     CA.CATEGORIA_ACUARIO AS CATEGORIA,
                     SA.SUBCATEGORIA_ACUARIO AS SUBCATEGORIA,
                     TA.OBSERVACIONES AS OBSERVACIONES,
                     UPPER(IFNULL(CA.CATEGORIA_ACUARIO, '') 
                        || IFNULL(SA.SUBCATEGORIA_ACUARIO, '' 
                        || IFNULL(TA.OBSERVACIONES, ''))) AS FIELD
        FROM         TIPOS_ACUARIO AS TA
        LEFT JOIN    CATEGORIAS_ACUARIO AS CA
        ON           TA.ID_CATEGORIA_aCUARIO = CA.ID_CATEGORIA_ACUARIO
        LEFT JOIN    SUBCATEGORIAS_ACUARIO AS SA
            ON       TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """