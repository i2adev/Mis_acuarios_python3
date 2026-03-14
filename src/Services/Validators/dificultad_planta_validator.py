"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      14/03/2026
Comentarios:
    Módulo para la validación del formulario de la dificultad de planta.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class DificultadPlantaValidator:
    """ Valida el formulario de dificultad de planta. """

    @staticmethod
    def validate_nivel(widget: QLineEdit):
        """ Valida el nivel de dificultad. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NIVEL' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_dificultad(widget: QLineEdit):
        """ Valida la dificultad de mantenimiento de la planta. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'DIFICULTAD' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
