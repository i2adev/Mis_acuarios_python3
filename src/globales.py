"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/09/2025
Comentarios:
    Módulo que contiene las variables globales de la aplicación.
"""

from pathlib import Path
from PyQt6.QtCore import QLocale

from Main.Model.Entities.dimension_configuration_entity import \
    DimensionConfigurationEntity
from Main.Model.Entities.usuario_entity import UsuarioEntity
from Services.ConfigManager.config_manager import ConfigManager

# Declaramos el usuario y proyecto
CURRENT_USER: UsuarioEntity | None = None
CURRENT_PROJECT_ID: int | None = None
CURRENT_ACUARIUM_ID: int | None = None

CONFIG_MANAGER: ConfigManager | None = None

# Configuración de la aplicacion
CONF_UNIDADES_DIMENSIONES: DimensionConfigurationEntity | None = None

# Establecemos la configuración local
LOCALE = QLocale(QLocale.Language.Spanish, QLocale.Country.Spain)

# Rutas
BASE_PATH = Path(__file__).resolve().parent
PATH_RESOURCES = BASE_PATH / "Resources"
PATH_IMAGES = PATH_RESOURCES / "Images"
PATH_FONTS = PATH_RESOURCES / "Fonts"
PATH_STYLES = PATH_RESOURCES / "Styles"

# Colores de los estados de proyecto
COLOR_PLANIFICACION = "#f2e605"
COLOR_EN_CURSO = "#169100"
COLOR_FINALIZADO = "#0540f2"
COLOR_CANCELADO = "#f20505"

# Valor máximo de un int32
INT32_MAX_VALUE = 2 ** 32 - 1
