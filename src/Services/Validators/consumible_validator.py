"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Comentarios:
    Módulo para la validación del formulario de acuario.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from Services.Result.result import Result


class ConsumibleValidator:
    """ Clase validadora del formulario de consumible. """

    @staticmethod
    def validate_marca(widget: QComboBox) -> Result:
        """ Válida la marca. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_producto(widget: QLineEdit) -> Result:
        """ Válida el nombre comercial del producto. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NOMBRE DEL PRODUCTO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_contenido(widget: QLineEdit) -> Result:
        """ Válida el contenido del consumible. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'CONTENIDO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_unidad(widget: QComboBox) -> Result:
        """ Válida la unidad del contenido. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "DEBE SELECCIONAR LA UNIDAD EN LA QUE ESTÁ MEDIDA EL "
                "CONTENIDO."
            )

        # Validación exitosa
        return Result.success(0)
