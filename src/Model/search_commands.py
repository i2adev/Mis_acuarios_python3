"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      12/09/2025
Comentarios:
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

    SEARCH_ACUARIO = """
    SELECT 
        S.ID, S.PROYECTO, S.NUM, S.COLOR, S.NOMBRE,  S.URNA, S.TIPO, S.VOLUMEN_B_N, 
        S.FECHA_MONTAJE, S.FECHA_INICIO_CICLADO, S.FECHA_FIN_CICLADO, S.UBICACION, 
        S.FECHA_DESMONTAJE, S.MOTIVO_DESMONTAJE, S.DESCRIPCION
    FROM
    (
        SELECT    A.ID_ACUARIO AS ID, 
                  P.NOMBRE AS PROYECTO, 
                  ROW_NUMBER()  OVER (ORDER BY A.NOMBRE) AS NUM, 
                  A.COD_COLOR AS COLOR, 
                  A.NOMBRE AS NOMBRE, 
                  MC.MARCA || ' ' || U.MODELO AS URNA, 
                  CA.CATEGORIA_ACUARIO || ' > ' || SA.SUBCATEGORIA_ACUARIO AS TIPO, 
                  U.VOLUMEN_TANQUE || '/' || A.VOLUMEN_NETO AS VOLUMEN_B_N, 
                  IFNULL(strftime('%d/%m/%Y', A.FECHA_MONTAJE, 'unixepoch', 'localtime'), '') AS FECHA_MONTAJE,
                  IFNULL(strftime('%d/%m/%Y', A.FECHA_INICIO_CICLADO, 'unixepoch', 'localtime'), '') AS FECHA_INICIO_CICLADO,
                  IFNULL(strftime('%d/%m/%Y', A.FECHA_FIN_CICLADO, 'unixepoch', 'localtime'), '') AS FECHA_FIN_CICLADO,
                  A.UBICACION_ACUARIO AS UBICACION,  
                  IFNULL(strftime('%d/%m/%Y', A.FECHA_DESMONTAJE, 'unixepoch', 'localtime'), '') AS FECHA_DESMONTAJE,
                  A.MOTIVO_DESMONTAJE AS MOTIVO_DESMONTAJE, 
                  A.DESCRIPCION AS DESCRIPCION,
                  UPPER(
                      IFNULL(A.NOMBRE, '') 
                      || IFNULL(P.NOMBRE, '')
                      || IFNULL(MC.MARCA, '') 
                      || IFNULL(U.MODELO, '') 
                      || IFNULL(CA.CATEGORIA_ACUARIO, '') 
                      || IFNULL(SA.SUBCATEGORIA_ACUARIO, '') 
                      || IFNULL(U.VOLUMEN_TANQUE, '') 
                      || IFNULL(A.VOLUMEN_NETO, '') 
                      || IFNULL(A.UBICACION_ACUARIO, '') 
                      || IFNULL(A.MOTIVO_DESMONTAJE, '') 
                      || IFNULL(A.DESCRIPCION, '') 
                      || IFNULL(A.FECHA_MONTAJE, '') 
                      || IFNULL(A.FECHA_INICIO_CICLADO, '') 
                      || IFNULL(A.FECHA_FIN_CICLADO, '') 
                      || IFNULL(A.FECHA_DESMONTAJE, '')
                   ) AS FIELD
      FROM ACUARIOS A
           LEFT JOIN
           PROYECTOS P ON A.ID_PROYECTO = P.ID_PROYECTO
           LEFT JOIN
           URNAS U ON A.ID_URNA = U.ID_URNA
           LEFT JOIN
           MARCAS_COMERCIALES MC ON U.ID_MARCA = MC.ID_MARCA
           LEFT JOIN
           TIPOS_ACUARIO TA ON A.ID_TIPO = TA.ID_TIPO
           LEFT JOIN
           CATEGORIAS_ACUARIO CA ON TA.ID_CATEGORIA_ACUARIO = CA.ID_CATEGORIA_ACUARIO
           LEFT JOIN
           SUBCATEGORIAS_ACUARIO SA ON TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO
           WHERE P.ID_USUARIO = :id_dep
    ) AS S
    WHERE FIELD LIKE '%' || :pattern || '%';
    """

    SEARCH_FILTRO = """
    SELECT  ID, NUM, MARCA, MODELO, TIPO_FILTRO, TERMOFILTRO, NUMERO_SERIE, 
            VOLUMEN_ACUARIO, CAUDAL, ALTURA_BOMBEO, CONSUMO, CONSUMO_CALENTADOR,
            VOLUMEN_FILTRANTE, DIMENSIONES, FECHA_COMPRA, FECHA_BAJA, 
            MOTIVO_BAJA, DESCRIPCION
    FROM
    (
        SELECT    F.ID_FILTRO AS ID,
                  ROW_NUMBER() OVER(ORDER BY MC.MARCA, F.MODELO) AS NUM,
                  MC.MARCA AS MARCA,
                  F.MODELO AS MODELO,
                  TF.TIPO_FILTRO AS TIPO_FILTRO,
                  F.ES_THERMOFILTRO AS TERMOFILTRO,
                  F.NUMERO_SERIE AS NUMERO_SERIE,
                  F.VOLUMEN_MIN_ACUARIO || '/' || F.VOLUMEN_MAX_ACUARIO AS VOLUMEN_ACUARIO,
                  F.CAUDAL AS CAUDAL,
                  F.ALTURA_BOMBEO AS ALTURA_BOMBEO,
                  F.CONSUMO AS CONSUMO,
                  F.CONSUMO_CALENTADOR AS CONSUMO_CALENTADOR,
                  F.VOLUMEN_FILTRANTE AS VOLUMEN_FILTRANTE,
                  F.ANCHO || 'x' || F.FONDO || 'x' || F.ALTO AS DIMENSIONES,
                  IFNULL(strftime('%d/%m/%Y', F.FECHA_COMPRA, 'unixepoch', 'localtime'), '') AS FECHA_COMPRA,
                  IFNULL(strftime('%d/%m/%Y', F.FECHA_BAJA, 'unixepoch', 'localtime'), '') AS FECHA_BAJA,
                  F.MOTIVO_BAJA AS MOTIVO_BAJA,
                  F.DESCRIPCION AS DESCRIPCION,
                  UPPER(
                      IFNULL(MC.MARCA, '')
                      || IFNULL(TF.TIPO_FILTRO, '')
                      || IFNULL(F.MODELO, '')
                      || IFNULL(F.VOLUMEN_MIN_ACUARIO || '/' || F.VOLUMEN_MAX_ACUARIO, '')
                      || IFNULL(F.CAUDAL, '')
                      || IFNULL(F.ALTURA_BOMBEO, '')
                      || IFNULL(F.CONSUMO, '')
                      || IFNULL(F.CONSUMO_CALENTADOR, '')
                      || IFNULL(F.VOLUMEN_FILTRANTE, '')
                      || IFNULL(F.ANCHO || 'x' || F.FONDO || 'x' || F.ALTO, '')
                      || IFNULL(F.MOTIVO_BAJA, '')
                      || IFNULL(F.DESCRIPCION, '')
                  ) AS FIELD
        FROM      FILTROS F
        LEFT JOIN MARCAS_COMERCIALES MC ON F.ID_MARCA = MC.ID_MARCA
        LEFT JOIN TIPOS_FILTRO TF ON F.ID_TIPO = TF.ID_TIPO
    )
    WHERE FIELD LIKE'%' || :pattern || '%';
    """

    SEARCH_CATEGORIA_EQUIPAMIENTO = """
    SELECT  ID, NUM, CATEGORIA, DESCRIPCION
    FROM
    (
        SELECT  ID_CATEGORIA_EQUIPAMIENTO AS ID,
                ROW_NUMBER() OVER(ORDER BY CATEGORIA_EQUIPAMIENTO) AS NUM,
                CATEGORIA_EQUIPAMIENTO AS CATEGORIA,
                DESCRIPCION AS DESCRIPCION,
                UPPER(IFNULL(CATEGORIA_EQUIPAMIENTO, '') 
                    || IFNULL(DESCRIPCION, '')) AS FIELD
        FROM    CATEGORIAS_EQUIPAMIENTO
    )
    WHERE     FIELD LIKE '%' || :pattern || '%';
    """

    SEARCH_EQUIPAMIENTO = """
    SELECT    ID, NUM, CATEGORIA, MARCA, MODELO, NUMERO_SERIE, FECHA_ALTA, FECHA_BAJA,
          MOTIVO_BAJA, DESCRIPCION
    FROM
    (
        SELECT  E.ID_EQUIPAMIENTO AS ID,
                ROW_NUMBER() OVER(ORDER BY E.ID_MARCA, E.MODELO) AS NUM,
                C.CATEGORIA_EQUIPAMIENTO AS CATEGORIA,
                M.MARCA AS MARCA,
                E.MODELO AS MODELO,
                E.NUMERO_SERIE AS NUMERO_SERIE,
                IFNULL(strftime('%d/%m/%Y', E.FECHA_ALTA, 'unixepoch', 'localtime'), '') AS FECHA_ALTA, 
                IFNULL(strftime('%d/%m/%Y', E.FECHA_BAJA, 'unixepoch', 'localtime'), '') AS FECHA_BAJA,
                E.MOTIVO_BAJA AS MOTIVO_BAJA,
                E.DESCRIPCION AS DESCRIPCION,
                UPPER(
                  IFNULL( C.CATEGORIA_EQUIPAMIENTO, '')
                  || IFNULL(M.MARCA, '')
                  || IFNULL(E.MODELO, '')
                  || IFNULL(E.NUMERO_SERIE, '')
                  || IFNULL(E.MOTIVO_BAJA, '')
                  || IFNULL(E.DESCRIPCION, '')
               ) AS FIELD
        FROM    EQUIPAMIENTOS E
        LEFT JOIN CATEGORIAS_EQUIPAMIENTO C 
            ON E.ID_CATEGORIA_EQUIPAMIENTO = C.ID_CATEGORIA_EQUIPAMIENTO
        LEFT JOIN MARCAS_COMERCIALES M ON 
            E.ID_MARCA = M.ID_MARCA
    )
    WHERE   FIELD LIKE'%' || :pattern || '%';
    """

    SEARCH_COMERCIO = """
    SELECT  ID, NUM, COMERCIO, DIRECCION, COD_POSTAL, POBLACION,
            PROVINCIA, PAIS, OBSERVACIONES
    FROM
    (
        SELECT  C.ID_COMERCIO AS ID,
                ROW_NUMBER() OVER(ORDER BY C.COMERCIO) AS NUM,
                C.COMERCIO AS COMERCIO,
                C.DIRECCION AS DIRECCION,
                C.COD_POSTAL AS COD_POSTAL,
                C.POBLACION AS POBLACION,
                C.PROVINCIA AS PROVINCIA,
                P.PAIS AS PAIS,
                C.OBSERVACIONES AS OBSERVACIONES,
                UPPER(
                    IFNULL(C.COMERCIO, '')
                    || IFNULL(C.DIRECCION, '')
                    || IFNULL(C.COD_POSTAL, '')
                    || IFNULL(C.POBLACION, '')
                    || IFNULL(C.PROVINCIA, '')
                    || IFNULL(P.PAIS, '')
                    || IFNULL(C.OBSERVACIONES, '')
                ) AS FIELD
        FROM        COMERCIOS C
        LEFT JOIN   PAISES P ON C.ID_PAIS = P.ID_PAIS
    )
    WHERE   FIELD LIKE'%' || :pattern || '%';
    """

    SEARCH_TIPO_ILUMINACION = """
    SELECT  ID, NUM, TIPO_ILUMINACION, DESCRIPCION
    FROM
        (
        SELECT  ID_TIPO_ILUMINACION AS ID,
                ROW_NUMBER() OVER(ORDER BY TIPO_ILUMINACION) AS NUM,
                TIPO_ILUMINACION AS TIPO_ILUMINACION,
                DESCRIPCION AS DESCRIPCION,
                UPPER(
                    IFNULL(TIPO_ILUMINACION, '')
                    || IFNULL(DESCRIPCION, '')
                ) AS FIELD
        FROM    TIPOS_ILUMINACION
        )
    WHERE   FIELD LIKE'%' || :pattern || '%';
    """

    SEARCH_CONTROL_ILUMINACION = """
    SELECT  ID, NUM, TIPO_CONTROL, DESCRIPCION
    FROM
        (
        SELECT  ID_CONTROL_ILUMINACION AS ID,
                ROW_NUMBER() OVER(ORDER BY TIPO_CONTROL) AS NUM,
                TIPO_CONTROL AS TIPO_CONTROL,
                DESCRIPCION AS DESCRIPCION,
                UPPER(
                    IFNULL(TIPO_CONTROL, '')
                    || IFNULL(DESCRIPCION, '')
                ) AS FIELD
        FROM    CONTROLES_ILUMINACION
        )
    WHERE    FIELD LIKE '%' || :pattern || '%';
    """

    SEARCH_ILUMINACION = """
    SELECT    ID, NUM, MARCA, MODELO, NUMERO_SERIE, TIPO_ILUMINACION, POTENCIA, 
              FLUJO_LUMINOSO, TEMPERATURA, VIDA_UTIL, LONGITUD, ANCHO, 
              CONTROL_ILUMINACION, INTENSIDAD_REGULABLE, ESPECTRO_COMPLETO, 
              FECHA_ALTA, FECHA_BAJA, MOTIVO_BAJA, DESCRIPCION
    FROM
        (SELECT I.ID_ILUMINACION AS ID, 
                ROW_NUMBER()  OVER (ORDER BY M.MARCA, I.MODELO) AS NUM, 
                M.MARCA AS MARCA, 
                I.MODELO AS MODELO, 
                I.NUMERO_SERIE AS NUMERO_SERIE, 
                TI.TIPO_ILUMINACION AS TIPO_ILUMINACION, 
                I.POTENCIA_W AS POTENCIA, 
                I.FLUJO_LUMINOSO_LM AS FLUJO_LUMINOSO, 
                I.TEMPERATURA_K AS TEMPERATURA, 
                I.VIDA_UTIL AS VIDA_UTIL, 
                I.LONGITUD_CM AS LONGITUD, 
                I.ANCHO_CM AS ANCHO, 
                CI.TIPO_CONTROL AS CONTROL_ILUMINACION, 
                I.INTENSIDAD_REGULABLE AS INTENSIDAD_REGULABLE, 
                I.ESPECTRO_COMPLETO AS ESPECTRO_COMPLETO, 
                IFNULL(strftime('%d/%m/%Y', I.FECHA_ALTA, 'unixepoch', 'localtime'), '') AS FECHA_ALTA, 
                IFNULL(strftime('%d/%m/%Y', I.FECHA_BAJA, 'unixepoch', 'localtime'), '') AS FECHA_BAJA, 
                I.MOTIVO_BAJA AS MOTIVO_BAJA, 
                I.DESCRIPCION AS DESCRIPCION,
                UPPER(
                    IFNULL(M.MARCA, '') ||
                    IFNULL(I.MODELO, '') ||
                    IFNULL(I.NUMERO_SERIE, '') ||
                    IFNULL(TI.TIPO_ILUMINACION, '') ||
                    IFNULL(I.POTENCIA_W, '') ||
                    IFNULL(I.FLUJO_LUMINOSO_LM, '') ||
                    IFNULL(I.TEMPERATURA_K, '') ||
                    IFNULL(I.VIDA_UTIL, '') ||
                    IFNULL(I.LONGITUD_CM, '') ||
                    IFNULL(I.ANCHO_CM, '') ||
                    IFNULL(CI.TIPO_CONTROL, '') ||
                    IFNULL(I.FECHA_ALTA, '') ||
                    IFNULL(I.FECHA_BAJA, '') || 
                    IFNULL(I.MOTIVO_BAJA, '') ||
                    IFNULL(I.DESCRIPCION, '')
                ) AS FIELD
        FROM    ILUMINACIONES I LEFT JOIN TIPOS_ILUMINACION TI ON I.ID_TIPO_ILUMINACION = TI.ID_TIPO_ILUMINACION 
                LEFT JOIN MARCAS_COMERCIALES M ON I.ID_MARCA = M.ID_MARCA 
                LEFT JOIN CONTROLES_ILUMINACION CI ON I.ID_CONTROL_ILUMINACION = CI.ID_CONTROL_ILUMINACION
        )
    WHERE    FIELD LIKE '%' || :pattern || '%';
    """
