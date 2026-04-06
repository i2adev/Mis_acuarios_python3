"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/04/2026
Comentarios:
    Módulo para la validación del formulario del seco del animal.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class SexoAnimalValidator:
    """ Valida el formulario del sexo del animal. """

    @staticmethod
    def validate_sexo(widget: QLineEdit):
        """ Valida el sexo del animal. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'SEXO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
