"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      11/06/2025
Comentarios:
    Módulo para la validación del formulario de tipo de filtro.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class TipoFiltroValidator:
    """ Clase validadora del formulario de tipo de filtro. """

    @staticmethod
    def validate_tipo_filtro(widget: QLineEdit):
        """ Valida el tipo de filtro. """

        # Si el texto está vacio
        if not widget.text():
            return Result.failure("EL CAMPO 'TIPO DE FILTRO' NO PUEDE ESTAR "
                                  "VACIO")

        # Validación exitosa
        return Result.success(0)
