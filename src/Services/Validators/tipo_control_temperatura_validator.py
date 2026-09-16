"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      14/09/2026
Comentarios:
    Módulo para la validación del formulario de tipo de iluminación.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class TipoControlTemperaturaValidator:
    """ Clase validadora del formulario de tipo de control de temperatura. """

    @staticmethod
    def validate_tipo_control_temperatura(widget: QLineEdit):
        """ Valida el tipo de control de la temperatura. """

        # Si el texto está vacio
        if not widget.text():
            return Result.failure("EL CAMPO 'TIPO DE CONTROL DE TEMPERATURA' "
                                  "NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(0)
