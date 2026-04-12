"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/04/2026
Comentarios:
    Módulo para la validación del formulario de la tasa de crecimiento.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class TasaCrecimientoValidator:
    """ Valida el formulario de la tasa de crecimiento. """

    @staticmethod
    def validate_crecimiento(widget: QLineEdit):
        """ Valida la tasa de crecimiento """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'TASA DE CRECIMIENTO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
