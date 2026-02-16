"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/09/2025
Comentarios:
    Módulo que contiene la clase Paginator, que se encarga de manejar
    los datos paginados de las entidades.
"""


class InsertCmd:
    """
    CLase que contiene los comandos de inserción de los datos
    esenciales.
    """

    # Unidad del contenido
    INSERTAR_UNIDAD_CONTENIDO = """
    INSERT INTO UNIDADES_CONTENIDO (UNIDAD, DESCRIPCION) VALUES
    ('ml',  'Mililitros'),
    ('l',   'Litros'),
    ('g',   'Gramos'),
    ('kg',  'Kilogramos'),
    ('uds', 'Unidades'),
    ('tabs','Pastillas'),
    ('tiras','Tiras reactivas');
    """

    # Formato de consumible
    INSERT_FORMATO_CONSUMIBLE = """
    INSERT INTO FORMATOS (FORMATO, DESCRIPCION) VALUES
    ('Líquido', 'Producto en formato líquido'),
    ('Polvo', 'Producto en formato polvo'),
    ('Granulado', 'Producto granulado'),
    ('Pastillas', 'Producto en pastillas'),
    ('Tiras', 'Tiras reactivas para test'),
    ('Gotas', 'Reactivos en gotas'),
    ('Gel', 'Producto en formato gel'),
    ('Spray', 'Aplicación mediante spray');
    """

    # Tipos de consumible
    INSERT_TIPO_CONSUBIBLE = """
    INSERT INTO CATEGORIAS_CONSUMIBLE (CATEGORIA_CONSUMIBLE, DESCRIPCION) VALUES
    ('Tests', 'Kits y reactivos para medir parámetros del agua'),
    ('Acondicionadores', 'Productos para preparar y tratar el agua del acuario'),
    ('Antialgas', 'Productos destinados al control y eliminación de algas'),
    ('Bacterias', 'Cultivos bacterianos para filtración biológica y ciclado'),
    ('Fertilizantes', 'Aportes nutritivos para plantas acuáticas'),
    ('Medicacion', 'Tratamientos para enfermedades de peces e invertebrados'),
    ('Sales', 'Sales minerales para ajuste de parámetros y remineralización'),
    ('Reactivos', 'Sustancias químicas utilizadas en análisis o tratamientos'),
    ('Alimentos', 'Comida para peces e invertebrados'),
    ('Aditivos', 'Suplementos específicos como vitaminas o oligoelementos'),
    ('Clarificadores', 'Productos para mejorar la transparencia del agua'),
    ('Estabilizadores', 'Productos para estabilizar pH, KH, GH u otros parámetros'),
    ('Neutralizadores', 'Productos para neutralizar cloro, cloraminas o metales');
    """

    # Estados del proyecto
    INSERT_ESTADOS_PRYECTO = """
    INSERT INTO ESTADOS_PROYECTO (NOMBRE_ESTADO, DESCRIPCION) VALUES
    ('Planificación', 'Proyecto en fase de estudio y planificación'),
    ('En curso', 'Proyecto actualmente en ejecución'),
    ('Finalizado', 'Proyecto completado con éxito'),
    ('Cancelado', 'Proyecto interrumpido antes de su finalización');
    """

    # Sexos del animal
    INSERT_SEXOS_ANIMAL = """
    INSERT INTO SEXO_ANIMAL (SEXO_ANIMAL, DESCRIPCION) VALUES
    ('Macho', 'Animal de sexo masculino.'),
    ('Hembra', 'Animal de sexo femenino.'),
    ('Hermafrodita', 'Animal que posee órganos reproductores masculinos y femeninos.'),
    ('Desconocido', 'Sexo del animal no identificado.');
    """

    # Niveles de nado
    INSERT_NIVELES_NADO = """
    INSERT INTO NIVEL_NADO (NIVEL_NADO, DESCRIPCION) VALUES
    ('Superior', 'Peces que nadan principalmente en la zona superficial del acuario, cerca de la superficie del agua'),
    ('Medio', 'Peces que ocupan mayormente la zona central del acuario'),
    ('Inferior', 'Peces que nadan y se alimentan en la parte baja del acuario, cerca del sustrato'),
    ('Todo el acuario', 'Peces que nadan y se alimentan en todos los niveles del acuario');
    """

    # Dieta de la fauna
    INSERT_DIETAS_FAUNA = """
    INSERT INTO DIETAS_FAUNA (DIETA, DESCRIPCION) VALUES
    ('Herbívoro', 'Se alimenta principalmente de plantas, algas y vegetales.'),
    ('Carnívoro', 'Se alimenta de otros animales como insectos, crustáceos o peces pequeños.'),
    ('Omnívoro', 'Consume tanto alimentos de origen vegetal como animal.'),
    ('Planctívoro', 'Se alimenta principalmente de plancton suspendido en el agua.'),
    ('Detritívoro', 'Consume materia orgánica en descomposición y restos del fondo.'),
    ('Limpia-algas', 'Consume algas adheridas a superficies del acuario.'),
    ('Piscívoro', 'Se alimenta específicamente de otros peces.'),
    ('Frugívoro', 'Se alimenta de frutas y semillas.');
    """

    # Comportamiento de peces
    INSERT_COMPORTAMIENTOS_FAUNA = """
    INSERT INTO COMPORTAMIENTOS_FAUNA (COMPORTAMIENTO, DESCRIPCION) VALUES
    ('Pacífico', 'Convive sin problemas con otras especies, no muestra agresividad.'),
    ('Territorial', 'Defiende un área específica del acuario frente a otros peces.'),
    ('Agresivo', 'Ataca o acosa a otros peces con frecuencia.'),
    ('Sociable', 'Prefiere estar acompañado de otros peces de su especie o similares.'),
    ('Tímido', 'Se esconde o evita nadar en zonas abiertas.'),
    ('Depredador', 'Caza activamente a otros peces o invertebrados más pequeños.'),
    ('Activo', 'Nada constantemente y recorre todo el acuario.'),
    ('Nocturno', 'Más activo durante la noche y reposa durante el día.');
    """

    # Categorías de equipamiento
    INSERT_CATEGORIAS_EQUIPAMIENTO = """
    INSERT INTO CATEGORIAS_EQUIPAMIENTO (CATEGORIA_EQUIPAMIENTO, DESCRIPCION) 
    VALUES
    ('Filtración', 'Filtros internos, externos, de mochila, sump y accesorios relacionados'),
    ('Iluminación', 'Pantallas LED, fluorescentes, HQI y sistemas de control'),
    ('Calefacción', 'Calentadores sumergibles, externos y termostatos'),
    ('Refrigeración', 'Enfriadores, ventiladores y controladores de temperatura'),
    ('CO2', 'Botellas, difusores, válvulas, controladores y accesorios para CO2'),
    ('Aireación', 'Compresores de aire, piedras difusoras y tuberías'),
    ('Bombas', 'Bombas de recirculación, retorno, movimiento y wavemakers'),
    ('Test y Medición', 'Test químicos, medidores digitales, refractómetros, pH-metros, etc.'),
    ('Decoración Técnica', 'Fondos, soportes, sistemas de iluminación decorativa'),
    ('Otros', 'Cualquier equipamiento no incluido en las categorías anteriores');
    """

    # Materiales de urna
    INSERT_MATERIALES_URNA = """
    INSERT INTO MATERIALES_URNA (MATERIAL, DESCRIPCION) VALUES
    ('Cristal', 'Material transparente, resistente y con excelente visibilidad. Es el más común en acuarios domésticos.'),
    ('Cristal óptico', 'Vidrio de alta transparencia y bajo contenido en hierro, ofrece una visión más clara y sin tinte verdoso.'),
    ('Acrílico', 'Ligero y resistente a impactos. Permite formas curvas, pero es más propenso a rayarse.'),
    ('Vidrio templado', 'Más resistente que el cristal estándar. Se utiliza para mayor seguridad.'),
    ('Vidrio laminado', 'Formado por capas unidas con película plástica para evitar desprendimiento en caso de rotura.'),
    ('Policarbonato', 'Plástico muy resistente a impactos, pero menos transparente que el acrílico.');
    """

    # Subcategorías de incidencia
    INSERT_SUBCATEGORIAS_INCIDENCIA = """
    INSERT INTO SUBCATEGORIAS_INCIDENCIA (ID_CATEGORIA, NOMBRE_SUBCATEGORIA, DESCRIPCION) VALUES
    -- Problemas de agua (ID 10001)
    (10001, 'pH incorrecto', 'Nivel de pH fuera del rango recomendado para los peces'),
    (10001, 'Amoniaco elevado', 'Presencia de amoníaco por encima de niveles seguros'),
    (10001, 'Nitritos elevados', 'Nivel de nitritos que puede dañar a los peces'),
    (10001, 'Nitratos elevados', 'Acumulación de nitratos por falta de cambios de agua'),
    (10001, 'Temperatura inadecuada', 'Temperatura del agua fuera del rango óptimo'),
    (10001, 'Agua turbia', 'Poca claridad del agua debido a bacterias o partículas'),
    
    -- Problemas biológicos (ID 10002)
    (10002, 'Peces enfermos', 'Signos visibles de enfermedades en los peces'),
    (10002, 'Plantas en mal estado', 'Plantas con hojas podridas o sin crecimiento'),
    (10002, 'Algas excesivas', 'Presencia descontrolada de algas en el acuario'),
    (10002, 'Parásitos visibles', 'Presencia de parásitos como puntos blancos, gusanos, etc.'),
    
    -- Problemas técnicos (ID 10003)
    (10003, 'Filtro dañado', 'El filtro ha dejado de funcionar o funciona mal'),
    (10003, 'Iluminación defectuosa', 'Luces fundidas o mal configuradas'),
    (10003, 'Calentador averiado', 'Calentador no funciona o calienta en exceso'),
    (10003, 'Fugas en sistema CO2', 'Sistema de CO2 con escapes o mal calibrado'),
    
    -- Problemas estructurales (ID 10004)
    (10004, 'Fugas de agua', 'Agua saliendo por fisuras o bordes'),
    (10004, 'Cristales rayados o rotos', 'Daños físicos en los cristales del acuario'),
    (10004, 'Tapa o soporte dañado', 'Problemas con la tapa o estructura del acuario'),
    
    -- Problemas de comportamiento (ID 10005)
    (10005, 'Agresividad entre peces', 'Conflictos territoriales o ataques'),
    (10005, 'Falta de actividad', 'Peces inactivos o apáticos'),
    (10005, 'Comportamientos anómalos', 'Nadado errático, raspado contra objetos, etc.');
    """

    # Categorías de incidencia
    INSERT_CATEGORIAS_INCIDENCIA = """
    INSERT INTO CATEGORIAS_INCIDENCIA (CATEGORIA_INCIDENCIA, OBSERVACIONES) VALUES
    ('Problemas de agua', 'Incidencias relacionadas con parámetros o condiciones del agua'),
    ('Problemas biológicos', 'Enfermedades o alteraciones en los seres vivos del acuario'),
    ('Problemas técnicos', 'Fallos en los equipos o sistemas del acuario'),
    ('Problemas estructurales', 'Daños físicos en el acuario o su entorno'),
    ('Problemas de comportamiento', 'Comportamientos anómalos observados en los peces');
    """

    # Subcategorías de acuario
    INSERT_SUBCATEGORIAS_ACUARIO = """
    INSERT INTO SUBCATEGORIAS_ACUARIO (ID_CATEGORIA_ACUARIO, SUBCATEGORIA_ACUARIO, OBSERVACIONES) VALUES
    (10001, 'Plantado', 'Optimizado para el crecimiento de plantas acuáticas. Requiere luz intensa, CO₂ y sustrato fértil.'),
    (10001, 'Comunitario', 'Contiene varias especies de peces de agua dulce compatibles entre sí.'),
    (10001, 'Específico', 'Dedicado a una única especie o grupo. Facilita el cuidado y reproducción.'),
    (10001, 'Biotopo', 'Recrea un hábitat natural específico (Amazonas, África, Asia, etc.).'),
    (10002, 'Arrecife (reef)', 'Especializado en corales vivos. Muy exigente en iluminación, química del agua y mantenimiento.'),
    (10003, 'Acuaterrario (paludario)', 'Mezcla zona terrestre y acuática. Ideal para anfibios, reptiles y ciertas plantas.'),
    (10003, 'Nanoacuario', 'Acuarios de tamaño reducido (menos de 40 L), tanto dulce como salado. Estéticos y compactos.');
    """

    # Categorías de acuario
    INSERT_CATEGORIAS_ACUARIO = """
    INSERT INTO CATEGORIAS_ACUARIO (CATEGORIA_ACUARIO, OBSERVACIONES) VALUES
    ('Agua dulce', 'El más común y fácil de mantener. Contiene peces y plantas de agua dulce.'),
    ('Agua salada', 'Contiene peces marinos y, en algunos casos, invertebrados. Requiere preparación y experiencia.'),
    ('Otros sistemas híbridos', '');
    """

    # Marcas comerciales
    INSERT_MARCAS_COMERCIALES = """
    INSERT INTO MARCAS_COMERCIALES (MARCA, DIRECCION, COD_POSTAL, POBLACION, PROVINCIA, ID_PAIS, OBSERVACIONES)
    VALUES
    ('EHEIM', 'Plochinger Straße 54', '73779', 'Deizisau', 'Baden-Württemberg', 10003, 'Líder en filtros externos. Muy fiable.'),
    ('Tetra', 'Herrenteich 78', '49324', 'Melle', 'Baja Sajonia', 10003, 'Comida, acondicionadores, y test.'),
    ('Fluval', '20500 Transcanada Hwy', 'H9X 0A2', 'Baie d’Urfé', 'Quebec', 10035, 'Línea premium de Hagen.'),
    ('JBL', 'Dieselstr. 3', '67141', 'Neuhofen', 'Renania-Palatinado', 10003, 'Muy reconocida por sus test y filtración.'),
    ('Sera', 'Borsigstraße 49', '52525', 'Heinsberg', 'Renania del Norte-Westfalia', 10003, 'Test, alimentos, y productos de tratamiento.'),
    ('Aquael', 'Krasnowolska 50', '03-654', 'Varsovia', 'Mazowieckie', 10140, 'Filtros e iluminación para acuario dulce.'),
    ('Seachem', '1000 Seachem Dr', '30650', 'Madison', 'Georgia', 10059, 'Química avanzada. Muy valorada.'),
    ('API', '50 E Hamilton St', '18914', 'Chalfont', 'Pensilvania', 10059, 'Especialista en test y tratamientos.'),
    ('ADA', '2-6-1-5 Matsubara', '950-0861', 'Niigata', 'Prefectura de Niigata', 10092, 'Referente mundial en aquascaping.'),
    ('Dennerle', 'Industriestr. 5', '66981', 'Münchweiler', 'Renania-Palatinado', 10003, 'Fertilizantes, nano acuarios, plantas.'),
    ('Red Sea', 'Kibbutz Eilot', '88805', 'Eilot', 'Distrito Sur (Eilat)', 10089, 'Sistemas integrales para arrecife.'),
    ('Resun', 'Zhongshan, Guangdong', NULL, 'Zhongshan', 'Guangdong', 10039, 'Bombas, filtros y aireadores. Económicos.'),
    ('Boyu', 'Shunde, Foshan, Guangdong', NULL, 'Foshan', 'Guangdong', 10039, 'Acuarios, aireadores, iluminación.'),
    ('Aquaforest', 'ul. Mazurska 20', '43-300', 'Bielsko-Biała', 'Voivodato de Silesia', 10140, 'Suplementos y sales para acuarios marinos.'),
    ('Tunze', 'Seeshaupter Str. 68', '82377', 'Penzberg', 'Baviera', 10003, 'Equipos para acuario marino de alta gama.'),
    ('Giesemann', 'Im Gewerbepark 24–26', '52388', 'Nörvenich', 'Renania del Norte-Westfalia', 10003, 'Iluminación profesional (LED, T5).'),
    ('Korallen-Zucht', 'Golling 16', '83435', 'Bad Reichenhall', 'Baviera', 10003, 'Método ZEOvit para arrecife.'),
    ('Aquamedic', 'Gewerbepark 24', '49143', 'Bissendorf', 'Baja Sajonia', 10003, 'Skimmers, iluminación y bombas.'),
    ('Hailea', 'Shenzhen, Guangdong', NULL, 'Shenzhen', 'Guangdong', 10039, 'Enfriadores, aireadores y filtros.'),
    ('Ocean Nutrition', 'Plassendale 1', '8400', 'Oostende', 'Flandes Occidental', 10018, 'Alimentación congelada y seca.'),
    ('Tropical', 'ul. Opolska 25', '41-507', 'Chorzów', 'Voivodato de Silesia', 10140, 'Acondicionadores, comida y productos técnicos.'),
    ('Zolux', '217 rue de la Marlièrel', '59700', 'Marcq-en-Barœul', 'Alta Francia (Hauts-de-France)', 10066, 'Productos generalistas con línea acuariófila.'),
    ('Prodibio', 'Technopôle Château-Gombert', '13013', 'Marsella', 'Provenza-Alpes-Costa Azul', 10066, 'Ampollas y suplementos para acuarios de arrecife.'),
    ('Aquatlantis', 'Parque Industrial de Guimarães', NULL, 'Guimarães', 'Braga', 10141, 'Acuarios completos con mueble e iluminación.'),
    ('Interpet', 'Vincent Ln', 'RH4 3YX', 'Dorking', 'Surrey', 10142, 'Marca histórica británica.'),
    ('Hikari', 'Himeji', '670-0944', 'Himeji', 'Prefectura de Hyōgo', 10092, 'Muy reconocida en alimentos premium.'),
    ('Atman', 'Guangzhou, Guangdong', NULL, 'Guangzhou', 'Guangdong', 10039, 'Bombas, filtros y equipamiento accesible.'),
    ('Blue Life USA', '2700 Business Center Dr #130', '77584', 'Pearland', 'Texas', 10059, 'Resinas, aditivos y soluciones para marino.'),
    ('Deltec', 'Gutenbergstraße 7', '28844', 'Weyhe', 'Baja Sajonia', 10003, 'Skimmers y equipos para reef exigentes.'),
    ('Reef Octopus', 'CoralVue Inc., 20108', '70433', 'Covington', 'Luisiana', 10059, 'Skimmers, bombas, reactores.'),
    ('Nyos', 'Gärtnerstr. 62', '80992', 'Múnich', 'Baviera', 10003, 'Marca moderna con diseño elegante.'),
    ('Fauna Marin', 'Steinbeisstr. 1', '73614', 'Schorndorf', 'Baden-Württemberg', 10003, 'Test, suplementos y productos reef premium.'),
    ('Hagen', '20500 TransCanada Hwy', 'H9X 0A2', 'Baie d’Urfé', 'Quebec', 10035, 'Grupo multinacional. Dueño de Fluval, Marina y Nutrafin.'),
    ('Marina', '20500 TransCanada Hwy', 'H9X 0A2', 'Baie d’Urfé', 'Quebec', 10035, 'Línea básica de acuarios y accesorios.'),
    ('Nutrafin', '20500 TransCanada Hwy', 'H9X 0A2', 'Baie d’Urfé', 'Quebec', 10035, 'Test kits y acondicionadores.'),
    ('Ocean Free', 'No. 71 Jalan Lekar', '698950', 'Singapur', '-', 10161, 'Alimentos y productos técnicos. Alta presencia en Asia.');
    """

    # Tipos de filtro
    INSERT_TIPOS_FILTRO = """
    INSERT INTO TIPOS_FILTRO (TIPO_FILTRO, OBSERVACIONES) VALUES
    ('Filtro de esponja', 'Ideal para acuarios pequeños o de cría; bajo flujo y oxigenación suave.'),
    ('Filtro de cascada', 'Fácil de instalar; combina filtración mecánica, biológica y química.'),
    ('Filtro interno', 'Sumergido dentro del acuario; buena opción para acuarios medianos.'),
    ('Filtro externo', 'Alta capacidad de filtración; ideal para acuarios grandes.'),
    ('Filtro de fondo', 'Funciona mediante una placa bajo el sustrato; menos común actualmente.'),
    ('Filtro canister', 'Tipo de filtro externo presurizado, excelente capacidad de carga filtrante.'),
    ('Filtro de mochila', 'También llamado "de cascada"; se cuelga en el borde del acuario.'),
    ('Filtro UV', 'Usa luz ultravioleta para eliminar algas, bacterias y parásitos en suspensión.'),
    ('Filtro de lecho fluido', 'Alta eficiencia biológica; el material filtrante se mueve en suspensión.'),
    ('Filtro de sump', 'Sistema personalizado fuera del acuario principal; común en acuarios marinos.'),
    ('Filtro de aire', 'Usa burbujeo de aire para mover el agua a través del material filtrante.'),
    ('Filtro de movimiento lento', 'Filtración natural; muy usado en acuarios plantados tipo Walstad.'),
    ('Filtro Hamburg Mattenfilter', 'Filtro de esponja de gran superficie, muy usado en cría y gambarios.');
    """

    # Tasas de crecimiento
    INSERT_TASAS_CRECIMIENTO = """
    INSERT INTO TASAS_CRECIMIENTO (CRECIMIENTO, DESCRIPCION) VALUES
    ('Lenta', 'Crecimiento muy pausado, requiere poco mantenimiento y poda.'),
    ('Media', 'Crecimiento moderado, equilibrado para acuarios comunitarios.'),
    ('Rápida', 'Crecimiento veloz, ideal para controlar nutrientes, requiere podas frecuentes.');
    """

    # Requerimientos de CO2
    INSERT_REQUERIMIENTOS_CO2 = """
    INSERT INTO REQUERIMIENTOS_CO2 (REQUERIMIENTO_CO2, DESCRIPCION) VALUES
    ('Ninguno', 'No requiere adición de CO₂ para su desarrollo.'),
    ('Bajo', 'Puede beneficiarse de CO₂ adicional, pero no es imprescindible.'),
    ('Medio', 'Desarrolla mejor con aporte moderado de CO₂.'),
    ('Alto', 'Necesita aporte constante de CO₂ para crecer adecuadamente.');
    """

    # Requerimientos de iluminación
    INSERT_REQUERIMIENTOS_ILUMINACION = """
    INSERT INTO REQUERIMIENTOS_ILUMINACION (REQUERIMIENTO_ILUMINACION, DESCRIPCION) VALUES
    ('Baja', 'Requiere poca luz; ideal para acuarios con iluminación tenue o sin CO₂.'),
    ('Media', 'Requiere luz moderada; se recomienda buena iluminación estable.'),
    ('Alta', 'Necesita luz intensa; idealmente con CO₂ y fotoperiodo controlado.');
    """

    # Posiciones den el acuario
    INSERT_POSICIONES_ACUARIO = """
    INSERT INTO POSICIONES_ACUARIO (POSICION, OBSERVACIONES) VALUES
    ('Primer plano', 'Plantas que se colocan en la parte frontal del acuario.'),
    ('Medio', 'Plantas ubicadas en la zona central del acuario.'),
    ('Fondo', 'Plantas que se sitúan en la parte trasera o fondo del acuario.'),
    ('Flotante', 'Plantas que flotan en la superficie del agua.'),
    ('Adherida', 'Plantas que se adhieren a piedras, troncos u otras superficies.');
    """

    # Grupos taxonómicos
    INSERT_GRUPOS_TAXONOMICOS = """
    INSERT INTO GRUPOS_TAXONOMICOS (GRUPO_TAXONOMICO, DESCRIPCION) VALUES
    ('Pez', 'Animales vertebrados acuáticos con aletas y branquias.'),
    ('Invertebrado', 'Animales sin columna vertebral, como caracoles y medusas.'),
    ('Crustáceo', 'Invertebrados con exoesqueleto, como camarones y cangrejos.'),
    ('Molusco', 'Invertebrados de cuerpo blando, como caracoles y almejas.'),
    ('Anfibio', 'Vertebrados con ciclo de vida acuático y terrestre, como los ajolotes.'),
    ('Reptil', 'Vertebrados con escamas, como tortugas acuáticas.'),
    ('Cnidario', 'Invertebrados con células urticantes, como anémonas.'),
    ('Equinodermo', 'Invertebrados marinos como estrellas de mar.'),
    ('Otro', 'Organismo no clasificado en los grupos anteriores.');
    """

    # Tipos de control de la iluminación
    INSERT_CONTROLES_ILUMINACON = """
    INSERT INTO CONTROLES_ILUMINACION (TIPO_CONTROL, DESCRIPCION) VALUES
    ('Manual', 'Encendido y apagado realizado directamente por el usuario.'),
    ('Temporizador mecánico', 'Dispositivo simple que activa y desactiva la luz a horas fijas.'),
    ('Temporizador digital', 'Permite configurar múltiples franjas horarias y ciclos de luz.'),
    ('Controlador externo', 'Dispositivo dedicado al control de iluminación, como TC420 o similares.'),
    ('Control por aplicación móvil', 'Control mediante app por conexión Wi-Fi o Bluetooth.'),
    ('Integración domótica', 'Sistema de automatización del hogar como Alexa, Google Home o Home Assistant.'),
    ('Sensor de luz', 'Encendido automático según nivel de luz ambiental.'),
    ('Controlador con espectro programable', 'Permite ajustar colores y espectro de forma personalizada.'),
    ('Controlador de acuario integrado', 'Parte de un sistema integrado que gestiona otros parámetros del acuario.');
    """

    # Tipos de iluminación
    INSERT_TIPOS_ILUMINACON = """
    INSERT INTO TIPOS_ILUMINACION (TIPO_ILUMINACION, DESCRIPCION) VALUES
    ('LED', 'Tecnología de bajo consumo y larga vida útil. Disponible en diferentes espectros.'),
    ('Fluorescente', 'Tubos T5 o T8, buena distribución de luz, común en acuarios tradicionales.'),
    ('HQI', 'Lámparas de halogenuros metálicos, alta intensidad, ideal para acuarios marinos.'),
    ('Halógeno', 'Iluminación incandescente con poco uso actual por bajo rendimiento.'),
    ('Actínica', 'Luz azulada utilizada para acuarios de arrecife o efecto visual.'),
    ('RGB', 'Combinación de LED rojos, verdes y azules para controlar espectro y color.'),
    ('Plasma', 'Alta intensidad, poco común y costosa.'),
    ('Solar', 'Luz natural dirigida o complementada con sistemas de domótica.');
    """

    # Paises
    INSERT_PAISES = """
    INSERT INTO PAISES (PAIS, CONTINENTE) VALUES
    ('Afganistán', 'Asia'),
    ('Albania', 'Europa'),
    ('Alemania', 'Europa'),
    ('Andorra', 'Europa'),
    ('Angola', 'África'),
    ('Antigua y Barbuda', 'América'),
    ('Arabia Saudita', 'Asia'),
    ('Argelia', 'África'),
    ('Argentina', 'América'),
    ('Armenia', 'Asia'),
    ('Australia', 'Oceanía'),
    ('Austria', 'Europa'),
    ('Azerbaiyán', 'Asia'),
    ('Bahamas', 'América'),
    ('Bangladés', 'Asia'),
    ('Barbados', 'América'),
    ('Baréin', 'Asia'),
    ('Bélgica', 'Europa'),
    ('Belice', 'América'),
    ('Benín', 'África'),
    ('Bielorrusia', 'Europa'),
    ('Birmania', 'Asia'),
    ('Bolivia', 'América'),
    ('Bosnia y Herzegovina', 'Europa'),
    ('Botsuana', 'África'),
    ('Brasil', 'América'),
    ('Brunéi', 'Asia'),
    ('Bulgaria', 'Europa'),
    ('Burkina Faso', 'África'),
    ('Burundi', 'África'),
    ('Bután', 'Asia'),
    ('Cabo Verde', 'África'),
    ('Camboya', 'Asia'),
    ('Camerún', 'África'),
    ('Canadá', 'América'),
    ('Catar', 'Asia'),
    ('Chad', 'África'),
    ('Chile', 'América'),
    ('China', 'Asia'),
    ('Chipre', 'Asia'),
    ('Colombia', 'América'),
    ('Comoras', 'África'),
    ('Corea del Norte', 'Asia'),
    ('Corea del Sur', 'Asia'),
    ('Costa de Marfil', 'África'),
    ('Costa Rica', 'América'),
    ('Croacia', 'Europa'),
    ('Cuba', 'América'),
    ('Dinamarca', 'Europa'),
    ('Dominica', 'América'),
    ('Ecuador', 'América'),
    ('Egipto', 'África'),
    ('El Salvador', 'América'),
    ('Emiratos Árabes Unidos', 'Asia'),
    ('Eritrea', 'África'),
    ('Eslovaquia', 'Europa'),
    ('Eslovenia', 'Europa'),
    ('España', 'Europa'),
    ('Estados Unidos', 'América'),
    ('Estonia', 'Europa'),
    ('Esuatini', 'África'),
    ('Etiopía', 'África'),
    ('Filipinas', 'Asia'),
    ('Finlandia', 'Europa'),
    ('Fiyi', 'Oceanía'),
    ('Francia', 'Europa'),
    ('Gabón', 'África'),
    ('Gambia', 'África'),
    ('Georgia', 'Asia'),
    ('Ghana', 'África'),
    ('Granada', 'América'),
    ('Grecia', 'Europa'),
    ('Guatemala', 'América'),
    ('Guinea', 'África'),
    ('Guinea-Bisáu', 'África'),
    ('Guinea Ecuatorial', 'África'),
    ('Guyana', 'América'),
    ('Haití', 'América'),
    ('Honduras', 'América'),
    ('Hungría', 'Europa'),
    ('India', 'Asia'),
    ('Indonesia', 'Asia'),
    ('Irak', 'Asia'),
    ('Irán', 'Asia'),
    ('Irlanda', 'Europa'),
    ('Islandia', 'Europa'),
    ('Islas Marshall', 'Oceanía'),
    ('Islas Salomón', 'Oceanía'),
    ('Israel', 'Asia'),
    ('Italia', 'Europa'),
    ('Jamaica', 'América'),
    ('Japón', 'Asia'),
    ('Jordania', 'Asia'),
    ('Kazajistán', 'Asia'),
    ('Kenia', 'África'),
    ('Kirguistán', 'Asia'),
    ('Kiribati', 'Oceanía'),
    ('Kuwait', 'Asia'),
    ('Laos', 'Asia'),
    ('Lesoto', 'África'),
    ('Letonia', 'Europa'),
    ('Líbano', 'Asia'),
    ('Liberia', 'África'),
    ('Libia', 'África'),
    ('Liechtenstein', 'Europa'),
    ('Lituania', 'Europa'),
    ('Luxemburgo', 'Europa'),
    ('Madagascar', 'África'),
    ('Malasia', 'Asia'),
    ('Malaui', 'África'),
    ('Maldivas', 'Asia'),
    ('Malí', 'África'),
    ('Malta', 'Europa'),
    ('Marruecos', 'África'),
    ('Mauricio', 'África'),
    ('Mauritania', 'África'),
    ('México', 'América'),
    ('Micronesia', 'Oceanía'),
    ('Moldavia', 'Europa'),
    ('Mónaco', 'Europa'),
    ('Mongolia', 'Asia'),
    ('Montenegro', 'Europa'),
    ('Mozambique', 'África'),
    ('Namibia', 'África'),
    ('Nauru', 'Oceanía'),
    ('Nepal', 'Asia'),
    ('Nicaragua', 'América'),
    ('Níger', 'África'),
    ('Nigeria', 'África'),
    ('Noruega', 'Europa'),
    ('Nueva Zelanda', 'Oceanía'),
    ('Omán', 'Asia'),
    ('Países Bajos', 'Europa'),
    ('Pakistán', 'Asia'),
    ('Palaos', 'Oceanía'),
    ('Panamá', 'América'),
    ('Papúa Nueva Guinea', 'Oceanía'),
    ('Paraguay', 'América'),
    ('Perú', 'América'),
    ('Polonia', 'Europa'),
    ('Portugal', 'Europa'),
    ('Reino Unido', 'Europa'),
    ('República Centroafricana', 'África'),
    ('República Checa', 'Europa'),
    ('República del Congo', 'África'),
    ('República Democrática del Congo', 'África'),
    ('República Dominicana', 'América'),
    ('Ruanda', 'África'),
    ('Rumanía', 'Europa'),
    ('Rusia', 'Europa'),
    ('Samoa', 'Oceanía'),
    ('San Cristóbal y Nieves', 'América'),
    ('San Marino', 'Europa'),
    ('San Vicente y las Granadinas', 'América'),
    ('Santa Lucía', 'América'),
    ('Santo Tomé y Príncipe', 'África'),
    ('Senegal', 'África'),
    ('Serbia', 'Europa'),
    ('Seychelles', 'África'),
    ('Sierra Leona', 'África'),
    ('Singapur', 'Asia'),
    ('Siria', 'Asia'),
    ('Somalia', 'África'),
    ('Sri Lanka', 'Asia'),
    ('Sudáfrica', 'África'),
    ('Sudán', 'África'),
    ('Sudán del Sur', 'África'),
    ('Suecia', 'Europa'),
    ('Suiza', 'Europa'),
    ('Surinam', 'América'),
    ('Tailandia', 'Asia'),
    ('Tanzania', 'África'),
    ('Tayikistán', 'Asia'),
    ('Timor Oriental', 'Asia'),
    ('Togo', 'África'),
    ('Tonga', 'Oceanía'),
    ('Trinidad y Tobago', 'América'),
    ('Túnez', 'África'),
    ('Turkmenistán', 'Asia'),
    ('Turquía', 'Asia'),
    ('Tuvalu', 'Oceanía'),
    ('Ucrania', 'Europa'),
    ('Uganda', 'África'),
    ('Uruguay', 'América'),
    ('Uzbekistán', 'Asia'),
    ('Vanuatu', 'Oceanía'),
    ('Vaticano', 'Europa'),
    ('Venezuela', 'América'),
    ('Vietnam', 'Asia'),
    ('Yemen', 'Asia'),
    ('Yibuti', 'África'),
    ('Zambia', 'África'),
    ('Zimbabue', 'África');
    """

    # Comercios españoles
    INSERT_COMERCIOS = """
    INSERT INTO COMERCIOS (COMERCIO, DIRECCION, COD_POSTAL, POBLACION, PROVINCIA, 
            ID_PAIS, OBSERVACIONES) 
    VALUES
    ('Kiwoko', 'Calle Serrano 45', '28001', 'Madrid', 'Madrid', 10058,
     'Cadena nacional con sección de acuariofilia dulce y marina'),
    ('Tiendanimal', 'Avenida de la Ilustración 51', '28029', 'Madrid', 'Madrid', 10058,
     'Gran superficie especializada en animales y acuariofilia'),
    ('Acuarios Amazonas', 'Carrer de Mallorca 410', '08013', 'Barcelona', 'Barcelona', 10058,
     'Especialistas en acuarios plantados y peces tropicales'),
    ('Nascapers', 'Carrer de Pujades 77', '08005', 'Valencia', 'Valencia', 10058,
     'Referencia en aquascaping y productos ADA'),
    ('Coral Reef Aquarium', 'Calle Juan XXIII 12', '29003', 'Málaga', 'Málaga', 10058,
     'Especialistas en acuario marino y arrecife'),
    ('Acuariofilia Madrid', 'Calle Alcalá 520', '28027', 'Madrid', 'Madrid', 10058,
     'Tienda tradicional con peces, plantas y equipamiento'),
    ('Reef Planet', 'Avenida de Andalucía 98', '41007', 'Sevilla', 'Sevilla', 10058,
     'Especialistas en arrecife y sistemas marinos'),
    ('Planeta Azul Acuarios', 'Calle San Vicente 132', '46007', 'Valencia', 'Valencia', 10058,
     'Acuarios, peces tropicales y asesoramiento técnico'),
    ('Tropiacuarium Bilbao', 'Calle Juan de Garay 25', '48012', 'Bilbao', 
    'Bizkaia', 10058,
     'Acuariofilia dulce y marina'),
    ('Acuarios Tropical', 'Calle Aragón 215', '50010', 'Zaragoza', 'Zaragoza', 10058,
     'Peces tropicales, plantas y material técnico');
    """
