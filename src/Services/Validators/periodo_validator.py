"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      07/04/2026
Comentarios:
    Módulo para la validación del formulario del periodo.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class PeriodoValidator:
    """ Valida el formulario del periodo. """

    @staticmethod
    def validate_periodo(widget: QLineEdit):
        """ Valida el periodo. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'PERIODO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
