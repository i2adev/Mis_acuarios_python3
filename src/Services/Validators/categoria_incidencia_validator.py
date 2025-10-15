"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Commentarios:
    Módulo para la validación del formulario de la categoría de acuario.
"""
from PyQt6.QtWidgets import QWidget, QLineEdit

from Services.Result.result import Result


class CategoriaIncidenciaValidator:
    """ Valida el formulario de categoría de incidencia. """

    @staticmethod
    def validate_categoria_incidencia(widget: QLineEdit):
        """ Valida la categoría de acuario. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'CATEGORÍA DE INCIDENCIA' NO PUEDE ESTAR VACIO"
            )

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure(
                "EL CAMPO 'CATEGORÍA DE INCIDENCIA' NO PUEDE CONTENER MAS DE " 
                "32 CARACTERES"
            )

        # Validación exitosa
        return Result.success(1)