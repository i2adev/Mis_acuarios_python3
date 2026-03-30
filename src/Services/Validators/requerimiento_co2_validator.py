"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/03/2026
Comentarios:
    Módulo para la validación del formulario del requerimiento de CO2.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class RequerimientoCO2Validator:
    """ Valida el formulario del requerimiento de CO2. """

    @staticmethod
    def validate_requerimiento(widget: QLineEdit):
        """ Valida la posición. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'REQUERIMIENTO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
