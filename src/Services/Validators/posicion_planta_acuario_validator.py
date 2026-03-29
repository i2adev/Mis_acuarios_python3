"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      29/03/2026
Comentarios:
    Módulo para la validación del formulario de la posición de la planta en
    el acuario.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class PosicionPlantaAcuarioValidator:
    """ Valida el formulario de la posición de la fauna. """

    @staticmethod
    def validate_posicion(widget: QLineEdit):
        """ Valida la posición. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'POSICIÓN' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
