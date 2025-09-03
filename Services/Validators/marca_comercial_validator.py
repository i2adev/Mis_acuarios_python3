"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/07/2025
Commentarios:
    Módulo para la validación del formulario de marca comercial.
"""
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox

from Services.Result.result import Result


class MarcaComercialValidator:
    """ Clase validadora del formulario tipo de acuario. """

    @staticmethod
    def validate_marca(widget: QLineEdit):
        """ Valida el nombre de la marca comercial. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MARCA COMERCIAL' NO PUEDE ESTAR VACÍO"
            )

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MARCA COMERCIAL' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_direccion(widget: QLineEdit):
        """ Valida la dirección. """

        # Si el texto contiene más de 128 carácteres
        if len(widget.text()) > 128:
            return Result.failure("EL CAMPO 'DIRECCIÓN' NO PUEDE "
                                  "CONTENER MAS DE 128 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_cod_postal(widget: QLineEdit):
        """ Valida el código postal. """

        # Si el texto contiene más de 16 carácteres
        if len(widget.text()) > 16:
            return Result.failure("EL CAMPO 'CÓDIGO POSTAL' NO PUEDE "
                                  "CONTENER MAS DE 16 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_poblacion(widget: QLineEdit):
        """ Valida la población. """

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'POBLACIÓN' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_provincia(widget: QLineEdit):
        """ Valida la población. """

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'PROVINCIA' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_pais(widget: QComboBox):
        """ Valida el país. """

        # Sí el texto está vacÍo
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'PAÍS' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

