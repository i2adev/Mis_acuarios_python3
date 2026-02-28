"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo para la validación del formulario de comercio.
"""
from PyQt6.QtWidgets import QComboBox, QLineEdit

from Services.Result.result import Result


class ComercioValidator:
    """ Clase validadora del formulario de acuario """

    @staticmethod
    def validate_comercio(widget: QLineEdit):
        """ Valída el nombre del comercio """

        # Si el combo está vacío
        if not widget.text():
            return Result.failure("EL CAMPO 'COMERCIO' NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_pais(widget: QComboBox):
        """ Valída el país """

        # Si el combo está vacío
        if not widget.currentText():
            return Result.failure("EL CAMPO 'PAÍS' NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(0)
