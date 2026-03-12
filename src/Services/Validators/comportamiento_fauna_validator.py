"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Comentarios:
    Módulo para la validación del formulario de la categoría de acuario.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class ComportamientoFaunaValidator:
    """ Valida el formulario de comportamiento de fauna. """

    @staticmethod
    def validate_comportamiento(widget: QLineEdit):
        """ Valida el comportamiento.. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'COMPORTAMIENTO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
