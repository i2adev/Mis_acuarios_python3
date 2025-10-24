"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      12/09/2025
Commentarios:
    Módulo que contiene la clase SearchCmd, que contiene los commandos
    de búsqueda.
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
                  UPPER(IFNULL(CATEGORIA_ACUARIO, '') 
                  || IFNULL(OBSERVACIONES, '')) AS FIELD
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
                  UPPER(IFNULL(CATEGORIA_INCIDENCIA, '') 
                        || IFNULL(OBSERVACIONES, '')) AS FIELD
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
               UPPER(IFNULL(C.CATEGORIA_INCIDENCIA, '') 
                    || IFNULL(S.NOMBRE_SUBCATEGORIA, '') 
                    || IFNULL(S.DESCRIPCION, '')) AS FIELD
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
                     ROW_NUMBER() OVER (ORDER BY CA.CATEGORIA_ACUARIO, 
                        SA.SUBCATEGORIA_ACUARIO) AS NUM,
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

    ## Tipo de filtro
    SEARCH_TIPO_FILTR0 = """
    SELECT  ID, NUM, TIPO, OBSERVACIONES
    FROM
    (
        SELECT  ID_TIPO AS ID,
                ROW_NUMBER() OVER(ORDER BY TIPO_FILTRO) AS NUM,
                TIPO_FILTRO AS TIPO,
                OBSERVACIONES AS OBSERVACIONES,
                UPPER(IFNULL(TIPO_FILTRO, '') 
                    || IFNULL(OBSERVACIONES, '')) AS FIELD
        FROM    TIPOS_FILTRO
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    ## Urna
    SEARCH_URNA = """
    SELECT    ID, NUM, MARCA, MODELO, ANCHURA, PROFUNDIDAD, ALTURA, 
          GROSOR, VOLUMEN_BRUTO, MATERIAL, DESCRIPCION
    FROM
    (
        SELECT    A.ID_URNA AS ID,
                  ROW_NUMBER() OVER (ORDER BY M.MARCA, A.MODELO) AS NUM,
                  M.MARCA AS MARCA,
                  A.MODELO AS MODELO,
                  A.ANCHURA AS ANCHURA,
                  A.PROFUNDIDAD AS PROFUNDIDAD,
                  A.ALTURA AS ALTURA,
                  A.GROSOR_CRISTAL AS GROSOR,
                  A.VOLUMEN_TANQUE AS VOLUMEN_BRUTO,
                  T.MATERIAL AS MATERIAL,
                  A.DESCRIPCION AS DESCRIPCION,
                  UPPER(IFNULL(M.MARCA, '') || IFNULL(A.MODELO, '')
                      || IFNULL(A.ANCHURA, '') || IFNULL(A.PROFUNDIDAD, '')
                      || IFNULL(A.ALTURA, '') || IFNULL(A.GROSOR_CRISTAL, '')
                      || IFNULL(A.VOLUMEN_TANQUE, '') || IFNULL(T.MATERIAL, '')
                      || IFNULL(A.DESCRIPCION, '')) AS FIELD
        FROM      URNAS AS A
        LEFT JOIN MARCAS_COMERCIALES AS M ON A.ID_MARCA = M.ID_MARCA
        LEFT JOIN MATERIALES_URNA T ON A.ID_MATERIAL = T.ID_MATERIAL
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    ## Estado del proyecto
    SEARCH_ESTADO_PROYECTO = """
    SELECT    ID, NUM, ESTADO, DESCRIPCION
    FROM
    (
        SELECT    ID_ESTADO AS ID,
                  ROW_NUMBER() OVER (ORDER BY NOMBRE_ESTADO) AS NUM,
                  NOMBRE_ESTADO AS ESTADO,
                  DESCRIPCION AS DESCRIPCION,
                  UPPER(IFNULL(NOMBRE_ESTADO, '') || IFNULL(DESCRIPCION, '')) AS FIELD
        FROM      ESTADOS_PROYECTO
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    ## Proyecto
    SEARCH_PROYECTO = """
    SELECT  ID, NUM, ID_USUARIO, NOMBRE, ESTADO, FECHA_INICIO, FECHA_FIN, 
            MOTIVO_CIERRE, DESCRIPCION
    FROM
    (
        SELECT P.ID_PROYECTO AS ID,
               ROW_NUMBER() OVER(ORDER BY P.ID_PROYECTO) AS NUM,
               P.ID_USUARIO AS ID_USUARIO,
               P.NOMBRE AS NOMBRE,
               E.NOMBRE_ESTADO AS ESTADO,
               IFNULL(
                strftime('%Y-%m-%d', P.FECHA_INICIO, 'unixepoch', 'localtime'), 
                '') AS FECHA_INICIO,
               IFNULL(
                strftime('%Y-%m-%d', P.FECHA_FIN, 'unixepoch', 'localtime'), 
                '') AS FECHA_FIN,
               P.MOTIVO_CIERRE AS MOTIVO_CIERRE,
               P.DESCRIPCION AS DESCRIPCION,
               UPPER(IFNULL(P.NOMBRE, '' ) || IFNULL(E.NOMBRE_ESTADO, '') || 
               IFNULL(strftime('%Y-%m-%d', P.FECHA_INICIO, 'unixepoch', 'localtime'), '') || 
               IFNULL(strftime('%Y-%m-%d', P.FECHA_FIN, 'unixepoch', 'localtime'), '') ||
               IFNULL(P.MOTIVO_CIERRE, '') || IFNULL(P.DESCRIPCION, '')) AS FIELD
        FROM   PROYECTOS P
        LEFT JOIN ESTADOS_PROYECTO E
        ON     P.ID_ESTADO = E.ID_ESTADO
    )
    WHERE ID_USUARIO = :id_dep AND FIELD LIKE '%' || :pattern || '%';
    """