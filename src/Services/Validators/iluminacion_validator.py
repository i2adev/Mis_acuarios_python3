"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/02/2026
Comentarios:
    Módulo para la validación de la iluminación.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from CustomControls.nullable_date_edit import NullableDateEdit
from Services.Result.result import Result


class IluminacionValidator:
    """ Clase validadora del formulario de iluminación. """

    @staticmethod
    def validate_tipo_iluminacion(widget: QComboBox):
        """ Valida el tipo de iluminación. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'TIPO DE ILUMINACIÓN' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_marca(widget: QComboBox):
        """ Valida la marca de la luminaria. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_modelo(widget: QLineEdit):
        """ Valida el modelo de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MODELO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_serial_number(widget: QLineEdit):
        """ Valida el numero de serie de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NÚMERO DE SERIE' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_fecha_alta(widget: NullableDateEdit) -> Result:
        """ Válida la fecha de alta del proyecto. """

        # Sí el texto está vacío
        if not widget.date():
            return Result.failure("EL CAMPO 'FECHA DE ALTA' NO PUEDE ESTAR "
                                  "VACÍO.")

        # Validación exitosa
        return Result.success(0)
