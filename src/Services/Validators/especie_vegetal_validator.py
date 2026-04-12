"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/04/2026
Comentarios:
    Módulo para la validación del formulario de especie vegeetal.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from Services.Result.result import Result


class EspecieVegetalValidator:
    """ Clase validadora del formulario de especie animal. """

    @staticmethod
    def validate_genero(widget: QLineEdit) -> Result:
        """ Válida el género. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'GÉNERO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_especie(widget: QLineEdit) -> Result:
        """ Válida la especie. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'ESPECIE' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
