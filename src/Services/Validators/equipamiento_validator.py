"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      17/12/2025
Comentarios:
    Módulo para la validación del formulario de equipamiento.
"""
from PyQt6.QtWidgets import QComboBox, QLineEdit

from Services.Result.result import Result


class EquipamientoValidator:
    """ Clase validadora del formulario de equipamiento. """

    @staticmethod
    def validate_categoria_equipamiento(widget: QComboBox) -> Result:
        """ Válida la categoría a la que pertenece el equipo. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'CATEGORÍA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_marca(widget: QComboBox) -> Result:
        """ Válida la marca del equipo. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_modelo(widget: QLineEdit) -> Result:
        """ Válida el modelo del equipo. """

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
    def validate_fecha_alta(widget: QLineEdit) -> Result:
        """ Válida la fecha en la que se le ha dado de alta al equipo."""
        if not widget.text():
            return Result.failure(
                """EL CAMPO 'FECHA DE ALTA' NO PUEDE ESTAR VACÍO"""
            )

        return Result.success(1)

    @staticmethod
    def validate_motivo_baja(widget: QLineEdit) -> Result:
        """ Válida el motivo de la baja del equipo. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MOTIVO DE LA BAJA' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
