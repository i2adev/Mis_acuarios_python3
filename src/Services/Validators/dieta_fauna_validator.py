"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      13/02/2026
Comentarios:
    Módulo para la validación del formulario de la dieta de fauna.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class DietaFaunaValidator:
    """ Valida el formulario de la dieta de fauna. """

    @staticmethod
    def validate_dieta(widget: QLineEdit):
        """ Valida la dieta de fauna. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'DIETA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
