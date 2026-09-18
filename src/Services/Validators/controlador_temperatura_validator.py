"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      17/09/2026
Comentarios:
    Módulo para la validación del formulario de controlador de
    temperatura.
"""
from PyQt6.QtWidgets import QComboBox, QLineEdit

from Services.Result.result import Result


class ControladorTemperaturaValidator:
    """ Clase validadora del formulario de controlador de temperatura. """

    @staticmethod
    def validate_tipo_controlador(widget: QComboBox) -> Result:
        """
        Válida el tipo al que pertenece el controlador de temperatura.
        """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'TIPO DE CONTROLADOR' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_marca(widget: QComboBox) -> Result:
        """ Válida la marca del equipo. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_modelo(widget: QLineEdit) -> Result:
        """ Válida el modelo del equipo. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MODELO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_numero_serie(widget: QLineEdit) -> Result:
        """ Válida el número de serie del filtro. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NÚMERO DE SERIE' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_fecha_alta(widget: QLineEdit) -> Result:
        """ Válida la fecha en la que se le ha dado de alta al equipo."""
        if not widget.text():
            return Result.failure(
                """EL CAMPO 'FECHA DE ALTA' NO PUEDE ESTAR VACÍO"""
            )

        return Result.success(0)
