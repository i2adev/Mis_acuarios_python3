# MIS ACUARIOS

## 1. OBJETO

Este programa surge de la necesidad que tiene el autor para la gestión y
control
de los parámetros del acuario que mantiene en su casa.

## 2. REQUERIMIENTOS

Esta aplicación tiene los siguientes requerimientos:

- Capacidad de gestionar más de un acuario.
- Capacidad de gestionar más de un usuario.
- Capacidad de almacenar los parámetros medidos sobre los acuarios.
- Capacidad de gestionar planes de mantenimiento para cada uno de los
  acuarios. Se implementará un scheduler con capacidades visuales para
  identificar fácilmente las tareas de mantenimiento.

## 3. VERSIONES

### 0.16.2b

Refactorizaciones:

- Se reconfigura la tabla de filtros en el formulario maestro para
  adaptarlo a tamaño disponible.
- Se ponen tooltips a los controles del formulario.
- Se implementa el estilo de color rojo a los controles deshabilitados.

### 0.16.1

Testeo manual del formulario maestro de filtro.

### 0.16.0

Se añade la lógica de filtro.

### 0.15.2

A los formularios de acuario se les añade la lógica de inserción de urna y
tipo de acuario.

### 0.15.1

Testeo manual de acuario.

### 0.15.0

Se añade la lógica de acuario.

### 0.14.2a

Se modifican os formularios:

- Se dimensional los controles para adaptarlos al tamaño de su contenido.
- Se añade la lógica para habilitar/deshabilitar los controles en base a la
  fecha de baja.

### 0.14.1

Testeo manual de la lógica de proyecto.

### 0.14.0

Se añade la lógica del proyecto.

Bug fixes:

- Corregido el error que ocurria al pulsar en el botón de limpiar en el
  formulario maestro de material de urna.

### 0.13.5c

Se compilan los recursos desde otro ordenador.

### 1.13.5b

Se modifica el archivo de especificaciones de instalación.

### 1.13.5a

Se corrige la implementación de las fuentes de texto.

### 1.13.5

Se integran las fuentes de texto en el archivo de recursos.

### 0.13.4

Bug fixes:

- Se corrige el error de la carga de imágenes en los formularios.
- Se corrige el error de la inserción de imágenes en los formularios.

### 0.13.2

A todas las importaciones se les asigna la ruta absoluta.

### 0.13.1

Se mueven los archivos de código a la carpeta 'src'.

### 0.13.0

Se añade la lógica del estado de proyecto.

### 0.12.9

Tests:

- Se testea el nuevo sistema de controladores.

### 0.12.8

Refactorización:

- Se modifican el controlador de urna: El controlador se separa en 3 partes,
  controlador, controlador del diálogo y el controlador del formulario maestro.

### 0.12.7

Refactorización:

- Se modifican el controlador de tipo de acuario: El controlador se separa en 3
  partes, controlador, controlador del diálogo y el controlador del formulario
  maestro.

### 0.12.6

Refactorización:

- Se modifican el controlador de categoría de incidencia: El controlador se
  separa en 3 partes, controlador, controlador del diálogo y el controlador del
  formulario maestro.

### 0.12.5

Refactorización:

- Se modifican el controlador de subcategoría de acuario: El controlador se
  separa en 3 partes, controlador, controlador del diálogo y el controlador del
  formulario maestro.

### 0.12.4

Refactorización:

- Se modifican el controlador de material de urna: El controlador se separa en
  3 partes, controlador, controlador del diálogo y el controlador del
  formulario maestro.

### 0.12.3

Refactorización:

- Se modifican el controlador de marca comercial: El controlador se separa en 3
  partes, controlador, controlador del diálogo y el controlador del formulario
  maestro.

### 0.12.2

Refactorización:

- Se modifican el controlador de categoría de incidencia: El controlador se
  separa en 3 partes, controlador, controlador del diálogo y el controlador del
  formulario maestro.

### 0.12.1

Refactorización:

- Se modifican el controlador de categoría de acuario: El controlador se
  separa en 3 partes, controlador, controlador del diálogo y el controlador del
  formulario maestro.

### 0.12.0

Refactorización:

- Se modifican el controlador de tipo de filtro: El controlador se separa en 3
  partes, controlador, controlador del diálogo y el controlador del formulario
  maestro.

### 0.10.3

Se añade la licencia MIT.

### 0.10.2

Se implementa el 'gitignore':

- Se crea el archivo 'gitignore'.
- Se configura el archivo 'gitignore'.

### 0.10.1

En esta versión se termina con la lógica de usuario:

- Se crea el validador del formulario.
- Se crea el controlador de usuario.

Refactorizaciones:

- Se modifica el método de eliminación de registro desde el menú contextual.

### 0.10.0

Se añade la lógica parcial de los usuarios:

- Se crea el cuadro de diálogo.
- Se crea el controlador del usuario.

Bug fixes:

- Se corrige el error de actualización de la tabla de los distintos
  formularios maestros.

Refactorizaciones:

- Se refactoriza la configuración del pie de tabla.
- Se refactoriza la configuración de la barra de estado.

### 0.9.6

Se implementa la función de búsqueda en el formulario de urna.

### 0.9.5

Se implementa la función de búsqueda en el formulario de tipo de filtro.

### 0.9.4

Se implementa la función de búsqueda en el formulario de tipo de acuario.

### 0.9.3

Se implementa la función de búsqueda en los siguientes formularios:

- En el formulario de subcategoría de acuario.
- En el formulario de subcategoría de acuario.

### 0.9.2

Se implementa la función de búsqueda en el formulario de marca comercial.

### 0.9.1

Se implementa la función de búsqueda en el formulario de categoría de
incidencia.

### 0.9.0

Se implementa la función de búsqueda en el formulario de categoría de acuario:

- Se modifica el formulario base de maestros para añadirle la barra de estado.
- Se añade la lógica de buscar categforías de acuario.

### 0.8.1

Se completa la lógica de los formularios subcategoria de acuario y subcategoria
de incidencias:

- Se añade la lógica de inserción de categoría de acuario desde el formulario
  de
  subcategoria de acuario.
- Se añade la lógica de inserción de categoría de incidencia desde el
  formulario
  de subcategoria de incidencia.

### 0.8.0

Refactorización

- Se modifica la lógica de los DAOS.
- Los botónes de los formularios muestran el icono de la mano.
- Los combos se hacen editables.
- Los combos responden a la inserción de texto, mostrando el autocompletado.
  Se configura para que cuando pierda el foco muestre el primer elemento que
  empieza con el texto insertado.
- Revisión de los validadores.
- Se implementa la lógica de las fotografías en el frame de los controles de
  imagen.

### 0.7.4

- Se añade la lógica de insertar o quitar imágenes a una urna existente.

### 0.7.3

- Se añade la lógica de cargar las imágenes de una urna cuando se carga la
  urna.

### 0.7.2

- Se añade la lógica de insertar imágenes en el diálogo y maestro de urna.

### 0.7.1

- Se añade la lógica de los materiales de la urna.

### 0.7.0

- Se añade la lógica básica de la urna.

### 0.6.2

Refactorización

- Se renombran las funciones de manejo de páginas.
- Se modifica el tamaño del diálogo y maestro de las marcas comerciales.

### 0.6.1

Refactorización

- Se modifica la función de limpieza de formulario para establecer el foco al
  final.
- Se pasan los controles de paginación y formateo de tabla al controlador base.

### 0.6.0

- Se añade la lógica de la marca comercial.

### 0.5.0

- Se añade la lógica de la subcategoría de la incidencia.

### 0.4.0

- Se añade la lógica de la categoría de la incidencia.

### 0.3.1

Mejoras

- Se mejora el redimensionado de las ventanas para poder redimensionarlos en
  todas las direcciones.
- Se mejora el tamaño automático de las ventanas.

### 0.3.0

- Se actualizan el controlador de tipo de filtro para adaptarlos al nuevo
  sistema de diálogos y maestros.

### 0.2.5

- Se testea la lógica hasta ahora creada.

### 0.2.4

- Se añade la lógica de subcategorías de acuario.

### 0.2.3

- Se vuelve a reiniciar los logs de Git para solucionar el problema surgido en
  el anterior commit.

### 0.2.2

- Se añade el maestro de categorías de acuario.

### 0.2.1

Refactorizacxión

- La categoría de acuario se migra una tabla independiente, junto con su
  lógica.
- La subcategoría de acuario se migra una tabla independiente, junto con su
  lógica.

### 0.2.0

- Se añade la lógica de tipos de acuario.

### 0.1.4

Refactorización

- Se modifican los formularios para adaptarlos al formulario base.

### 0.1.3

Refactorización:

- Se modifica la lógica de los formularios.
- Se le añaden las funcionalidades de redimensionamiento y movimiento a los
  formularios.

### 0.1.2

Se crea el formulario principal.

- Se crea la vista.
- Se crea el controlador.
- Se le añade funcionalidad básica.

### 0.1.1

- Testeo de la lógica de tipos de filtro.
- Corrección de bugs

### 0.1.0

- Se implementa la paginación en la vista tipos de filtro.

### 0.0.6

- Se crea la clase Paginator para mostrar los datos de las tablas de distintas
  entidades.

### 0.0.5

- Se implementa el menu contextual para permitir cargar o eliminar un registro
  desde la tabla.

### 0.0.4

- Se implementa el CRUD del tipo de filtro.

### 0.0.3

- Se implementa la carga de datos de la tabla.

### 0.0.2

- Se crea la clase Result, para aplicar el patrón del mismo nombre.
- Se crea el DAO del tipo de filtro.

### 0.0.1

- Se modifica la vista de tipo de filtro.

### 0.0.0

- Se inicia el proyecto.
