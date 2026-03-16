"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/03/2026
Comentarios:
    Módulo para la validación del formulario de la categoría de acuario.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class GrupoTaxonomicoValidator:
    """ Valida el formulario del grupo taxonómico. """

    @staticmethod
    def validate_grupo(widget: QLineEdit):
        """ Valida el grupo taxonómico. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'GRUPO TAXONÓMICO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(0)
