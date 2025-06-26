# MIS ACUARIOS
## 1. OBJETO
Este programa surge de la necesidad que tiene el autor para la gestión y control de los parámetros del acuario que mantiene en su casa.

## 2. REQUERIMIENTOS
Esta aplicación tiene los siguientes requerimientos:

- Capacidad de gestionar mas de un acuario.
- Capacidad de gestionar mas de un usuario.
- Capacidad de almacenar los parámetros medidos sobre los acuarios.
- Capacidad de gestionar planes de mantenimiento para cada uno de los 
  acuarios. Se implementara un scheduler con capacidades visuales para 
  identificar facilmente las tareas de mantenimiento.

## 3. VERSIONES
### 0.1.1   
- TESTEO Y DE LA LÓGICA DE TIPOS DE FILTRO
- SE AÑADE LA OPCIÓN DE EXPORTAR A SQL LA ESTRUCTURA Y DATOS DE LA BASE DE 
DATOS.

BUG FIXES:
- CUANDO SE ELIMINA UN REGISTRO DE LA PRIMERA PÁGINA DE LA TABLA, ESTA NO SE 
ACTUALIZA.
- SE ELIMINA EL ERROR DE LA CARGA DE UNA TABLA VACÍA.
- ~~~~ERROR: CUANDO SE INSERTA UN REGISTRO ESTANDO EN LA ÚLTIMA PÁGINA, NO SE 
ACTUALIZA LA TABLA.

**0.1.0**   
- SE IMPLEMENTA LA PAGINACIÓN EN LA VISTA DE TIPOS DE FILTRO

**0.0.6**
-   SE CREA LA CLASE PAGINATOR QUE SE UTILIZA PARA MOSTRAR LOS DATOS DE LOS 
DISTINTOS LISTADOS.
-   SE CREA LA CLASE BASEDAO DE LA QUE DEPENDERÁN TODOS LOS DAOS.

0.0.5   
-   SE IMPLEMENTA EL MENÚ CONTEXTUAL EN LA TABLA PARA PERMITIR CARGAR Y ELIMINAR 
UN REGISTRO.
-   SE CONECTA LA TABLA CON EL MENÚ CONTEXTUAL.

**0.0.4**
- SE IMPLEMENTA EL CRUD DE LA ENTIDAD TIPO DE FILTRO.

**0.0.3**
- SE IMPLEMENTA LA CARGA DE DATOS EN LA TABLA.

**0.0.2**
- SE CREA LA CLASE RESULT PARA APLICAR EL PATRÓN RESULTADO.
- SE CREA EL DAO DEL TIPO DE FILTRO.

**0.0.1**
- SE MODIFICA LA VISTA TIPOFILTROVIEW.
- SE UNIFICAN LOS MÉTODOS DE CREACIÓN Y CONFIGURACIÓN DE LOS WIDGETS.
