"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/09/2025
Comentarios:
    Módulo que contiene las variables globales de la aplicación
"""
from PyQt6.QtCore import QLocale

CURRENT_USER = None
CURRENT_PROYECT = None
LOCALE = QLocale(QLocale.Language.Spanish, QLocale.Country.Spain)
