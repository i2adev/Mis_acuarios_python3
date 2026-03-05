"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/03/2026
Comentarios:
    Módulo para la validación del formulario de foramto de consumible.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class UnidadContenidoValidator:
    """ Clase validadora del formulario de unidad contenido . """

    @staticmethod
    def validate_unidad_contenido(widget: QLineEdit):
        """ Valida la unidad de contenido """

        # Si el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'UNIDAD DE CONTENIDO' NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(0)
