"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo para la validación del formulario de comercio.
"""
from PyQt6.QtWidgets import QComboBox, QLineEdit

from Services.Result.result import Result


class ComercioValidator:
    """ Clase validadora del formulario de acuario """

    @staticmethod
    def validate_comercio(widget: QLineEdit):
        """ Valída el nombre del comercio """

        # Si el combo está vacío
        if not widget.text():
            return Result.failure("EL CAMPO 'COMERCIO' NO PUEDE ESTAR VACÍO")

        # Válida la longitud del campo
        if len(widget.text()) > 32:
            return Result.failure(
                "EL CAMPO 'COMERCIO' NO PUEDE CONTENER MAS DE 32 CARÁCTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_direccion(widget: QLineEdit):
        """ Valída la dirección del comercio """

        # Si el combo está vacío
        if not widget.text():
            return Result.success(1)

        # Válida la longitud del campo
        if len(widget.text()) > 64:
            return Result.failure(
                "EL CAMPO 'DIRECCIÓN' NO PUEDE CONTENER MAS DE 64 CARÁCTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_cod_postal(widget: QLineEdit):
        """ Valída el código postal """

        # Si el combo está vacío
        if not widget.text():
            return Result.success(1)

        # Válida la longitud del campo
        if len(widget.text()) > 15:
            return Result.failure(
                "EL CAMPO 'COD. POSTAL' NO PUEDE CONTENER MAS DE 15 "
                "CARÁCTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_poblacion(widget: QLineEdit):
        """ Valída la población """

        # Si el combo está vacío
        if not widget.text():
            return Result.success(1)

        # Válida la longitud del campo
        if len(widget.text()) > 25:
            return Result.failure(
                "EL CAMPO 'POBLACIÓN' NO PUEDE CONTENER MAS DE 25 CARÁCTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_provincia(widget: QLineEdit):
        """ Valída la provincia """

        # Si el combo está vacío
        if not widget.text():
            return Result.success(1)

        # Válida la longitud del campo
        if len(widget.text()) > 25:
            return Result.failure(
                "EL CAMPO 'PROVINCIA' NO PUEDE CONTENER MAS DE 25 CARÁCTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_pais(widget: QComboBox):
        """ Valída el país """

        # Si el combo está vacío
        if not widget.currentText():
            return Result.failure("")

        # Válida la longitud del campo
        if len(widget.text()) > 25:
            return Result.failure("EL CAMPO 'PAÍS' NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(1)
