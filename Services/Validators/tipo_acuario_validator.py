"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo para la validación del formulario de tipo de acuario.
"""
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox

from Services.Result.result import Result


class TipoAcuarioValidator:
    """ Clase validadora del formulario tipo de acuario. """

    @staticmethod
    def ValidateCategoriaAcuario(widget: QComboBox):
        """ Valida el tipo de acuario. """

        # Sí el texto esta vacio
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'CATEGORÍA DE ACUARIO' NO PUEDE ESTAR VACIO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def ValidateSubcategoriaAcuario(widget: QComboBox):
        """ Valida el tipo de acuario. """

        # Sí el texto esta vacio
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'SUBCATEGORÍA DE ACUARIO' NO PUEDE ESTAR VACIO"
            )

            # Validación exitosa
        return Result.success(1)