"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/08/2025
Commentarios:
    Módulo para la validación del formulario de material de la urna.
"""
from PyQt6.QtWidgets import QLineEdit
from Tools.scripts.generate_opcode_h import write_int_array_from_ops

from Services.Result.result import Result


class MaterialUrnaValidator:
    """ Clase que valida los datos del formulario de material de urna.
    """

    @staticmethod
    def validate_material (widget: QLineEdit):
        """ Valida el material de la urna. """

        # Si el campo está vacío
        if not widget.text():
            return Result.failure("EL CAMPO 'MATERIAL' NO PUEDE ESTAR "
                                  "VACÍO")

        # Sí contiene más de 32 caracteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MATERIAL' NO PUEDE "
                                  "CONTENER MAS DE 32 CARÁCTERES")

        # Validación exitosa
        return Result.success(1)
