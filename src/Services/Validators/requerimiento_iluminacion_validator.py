"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/03/2026
Comentarios:
    Módulo para la validación del formulario del requerimiento de iluminación.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class RequerimientoIluminacionValidator:
    """ Valida el formulario del requerimiento de iluminación. """

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
