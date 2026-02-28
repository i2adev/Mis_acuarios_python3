"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/08/2025
Comentarios:
    Módulo para la validación del formulario de material de la urna.
"""

from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class MaterialUrnaValidator:
    """ Clase que valida los datos del formulario de material de urna.
    """

    @staticmethod
    def validate_material(widget: QLineEdit):
        """ Valida el material de la urna. """

        # Si el campo está vacío
        if not widget.text():
            return Result.failure("EL CAMPO 'MATERIAL' NO PUEDE ESTAR "
                                  "VACÍO")

        # Validación exitosa
        return Result.success(0)
