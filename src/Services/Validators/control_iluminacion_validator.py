"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      20/12/2025
Comentarios:
    Módulo para la validación del formulario de control de iluminación.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class ControlIluminacionValidator:
    """ Clase validadora del formulario de control de iluminación. """

    @staticmethod
    def validate_control_iluminacion(widget: QLineEdit):
        """ Valida el control de iluminación. """

        # Si el texto está vacío
        if not widget.text():
            return Result.failure("EL CAMPO 'CONTROL DE ILUMINACIÓN' NO PUEDE "
                                  "ESTAR VACÍO")

        # Se valida la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'CONTROL DE ILUMINACIÓN' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
