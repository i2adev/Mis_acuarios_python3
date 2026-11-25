"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/11/2026
Descripción:
    Define los valores predeterminados de la configuración
    de la aplicación.
"""

DEFAULT_CONFIG = {
    "version": 1,

    "general": {
        "idioma": "es-ES"
    },

    "cuenta": {
        "proyecto_por_defecto": None,
        "acuario_por_defecto": None
    },

    "unidades": {
        "dimension": "cm",
        "volumen": "L",
        "temperatura": "°C",
        "masa": "g",
        "potencia": "W",
        "energia": "kWh",
        "caudal": "L/h",
        "presion": "bar",
        "iluminacion": "lm",
        "concentracion": "mg/L",
        "dureza_general": "°dGH",
        "dureza_carbonatos": "°dKH",
        "conductividad": "µS/cm",
        "salinidad": "ppt",
        "densidad": "g/cm³",
    },

    "interfaz": {},

    "tablas": {},

    "funcionamiento": {},

    "regional": {
        "separador_decimal": ",",
        "formato_fecha": "dd/MM/yyyy"
    }
}
