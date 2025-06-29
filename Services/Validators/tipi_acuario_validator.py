"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo para la validación del formulario de tipo de acuario.
"""
from PyQt6.QtWidgets import QWidget, QLineEdit

from Services.Result.result import Result


class TipoAcuarioValidator:
    """ Clase validadora del formulario tipo de acuario. """

    @staticmethod
    def ValidateTipoAcuario(widget: QLineEdit):
        """ Valida el tipo de acuario. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure("EL CAMPO 'TIPO DE ACUARIO' NO PUEDE ESTAR "
                                  "VACIO")

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'TIPO DE ACUARIO' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def ValidateSubtipoAcuario(widget: QLineEdit):
        """ Valida el tipo de acuario. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure("EL CAMPO 'SUBTIPO DE ACUARIO' NO PUEDE ESTAR "
                                  "VACIO")

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'SUBTIPO DE ACUARIO' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

            # Validación exitosa
        return Result.success(1)