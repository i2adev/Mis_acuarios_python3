"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/07/2025
Comentarios:
    Módulo para la validación del formulario de marca comercial.
"""

from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox

from Services.Result.result import Result


class MarcaComercialValidator:
    """ Clase validadora del formulario tipo de acuario. """

    @staticmethod
    def validate_marca(widget: QLineEdit):
        """ Valida el nombre de la marca comercial. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MARCA COMERCIAL' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_pais(widget: QComboBox):
        """ Valida el país. """

        # Sí el texto está vacÍo
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'PAÍS' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
