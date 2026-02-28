"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/12/2025
Comentarios:
    Módulo para la validación del formulario de tipo de equipamiento.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class CategoriaEquipamientoValidator:
    """ Clase validadora del formulario de tipo de equipamiento. """

    @staticmethod
    def validate_tipo_equipamiento(widget: QLineEdit):
        """ Valida el tipo de equipamiento. """

        # Si el texto está vacio
        if not widget.text():
            return Result.failure("EL CAMPO 'CATEGORÍA DE EQUIPAMIENTO' "
                                  "NO PUEDE ESTAR VACÍO")

        # Validación exitosa
        return Result.success(0)
