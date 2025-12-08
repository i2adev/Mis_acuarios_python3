"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/11/2025
Comentarios:
    Módulo para la validación del formulario de filtro.
"""
from PyQt6.QtWidgets import QComboBox, QLineEdit

from Services.Result.result import Result


class FiltroValidator:
    """ Clase validadora del formulario de acuario. """

    @staticmethod
    def validate_tipo_filtro(widget: QComboBox) -> Result:
        """ Válida el tipo de filtro. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'TIPO DE FILTRO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_marca(widget: QComboBox) -> Result:
        """ Válida la marca del filtro. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_modelo(widget: QLineEdit) -> Result:
        """ Válida el modelo del filtro. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MODELO' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MODELO' NO PUEDE CONTENER MAS DE "
                                  "32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_numero_serie(widget: QLineEdit) -> Result:
        """ Válida el número de serie del filtro. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NÚMERO DE SERIE' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure(
                "EL CAMPO 'NÚMERO DE SERIE' NO PUEDE CONTENER MAS DE "
                "32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_motivo_baja(widget: QLineEdit) -> Result:
        """ Válida el motivo de la baja del filtro. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MOTIVO DE LA BAJA' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
