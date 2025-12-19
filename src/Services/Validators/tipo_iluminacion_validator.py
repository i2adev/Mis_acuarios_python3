"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/12/2025
Comentarios:
    Módulo para la validación del formulario de tipo de iluminación.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class TipoIluminacionValidator:
    """ Clase validadora del formulario de tipo de iluminación. """

    @staticmethod
    def validate_tipo_iluminacion(widget: QLineEdit):
        """ Valida el tipo de iluminación. """

        # Si el texto está vacio
        if not widget.text():
            return Result.failure("EL CAMPO 'TIPO DE ILUMINACIÓN' NO PUEDE "
                                  "ESTAR VACÍO")

        # Se valida la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'TIPO DE ILUMINACIÓN' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
