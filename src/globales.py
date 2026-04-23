"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/09/2025
Comentarios:
    Módulo que contiene las variables globales de la aplicación.
"""

from pathlib import Path
from PyQt6.QtCore import QLocale

# Declaramos el usuario y proyecto
CURRENT_USER = None
CURRENT_PROYECT = None

# Establecemos la configuración local
LOCALE = QLocale(QLocale.Language.Spanish, QLocale.Country.Spain)

# Rutas
BASE_PATH = Path(__file__).resolve().parent
PATH_RESOURCES = BASE_PATH / "Resources"
PATH_IMAGES = PATH_RESOURCES / "Images"
PATH_FONTS = PATH_RESOURCES / "Fonts"
PATH_STYLES = PATH_RESOURCES / "Styles"

# Valor máximo de un int32
INT32_MAX_VALUE = 2 ** 32 - 1
