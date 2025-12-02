"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      08/10/2025
Comentarios:
    Módulo para la validación del formulario de estado de proyecto.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class EstadoProyectoValidator:
    """ Clase validadora del formulario de tipo de filtro. """

    @staticmethod
    def validate_estado(widget: QLineEdit):
        """ Valida el tipo de filtro. """

        # Si el texto está vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'ESTADO DE PROYECTO' NO PUEDE ESTAR "
                "VACÍO")

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'ESTADO DE PROYECTO' NO PUEDE "
                                  "CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
