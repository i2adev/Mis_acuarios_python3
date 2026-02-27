"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Comentarios:
    Módulo para la validación del formulario de acuario.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from Services.Result.result import Result


class UrnaValidator:
    """ Clase validadora del formulario de urna. """

    @staticmethod
    def validate_marca(widget: QComboBox):
        """ Válida la marca de la urna. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA DE URNA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_modelo_urna(widget: QLineEdit):
        """ Válida el modelo de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MODELO DE URNA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_material(widget: QComboBox):
        """ Valida el material de lal urna. """

        # Sí el texto está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MATERIAL DE URNA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
