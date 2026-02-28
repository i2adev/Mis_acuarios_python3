"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Comentarios:
    Módulo para la validación del formulario de la categoría de acuario.
"""

from PyQt6.QtWidgets import QWidget, QLineEdit

from Services.Result.result import Result


class CategoriaAcuarioValidator:
    """ Valida el formulario de categoría de acuario. """

    @staticmethod
    def validate_categoria_acuario(widget: QLineEdit):
        """ Valida la categoría de acuario. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'CATEGORÍA DE ACUARIO' NO PUEDE ESTAR VACIO"
            )

        # Validación exitosa
        return Result.success(0)
