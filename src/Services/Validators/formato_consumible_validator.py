"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      04/03/2026
Comentarios:
    Módulo para la validación del formulario de foramto de consumible.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class FormatoConsumibleValidator:
    """ Clase validadora del formulario de formato de consumible. """

    @staticmethod
    def validate_formato_consumible(widget: QLineEdit):
        """ Valida el formato de consumible. """

        # Si el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'FORMATO DE CONSUMIBLE' NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(0)
