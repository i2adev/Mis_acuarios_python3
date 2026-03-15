"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Comentarios:
    Módulo para la validación del formulario de la categoría de acuario.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class NivelNadoValidator:
    """ Valida el formulario de nivel de nado. """

    @staticmethod
    def validate_nivel(widget: QLineEdit):
        """ Valida el nivel de nado. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NIVEL DE NADO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
