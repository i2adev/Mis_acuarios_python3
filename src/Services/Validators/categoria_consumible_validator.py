"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      04/03/2026
Comentarios:
    Módulo para la validación del formulario de categoria de consumible.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class CategoriaConsumibleValidator:
    """ Clase validadora del formulario de categoría de consumible. """

    @staticmethod
    def validate_categoria_consumible(widget: QLineEdit):
        """ Valida la categoría de consumible. """

        # Si el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'CATEGORÍA DE CONSUMIBLE' NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(0)
