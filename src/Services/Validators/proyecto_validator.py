"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      21/10/2025
Comentarios:
    Módulo para la validación del formulario de proyecto.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from CustomControls.nullable_date_edit import NullableDateEdit
from Services.Result.result import Result


class ProyectoValidator:
    """ Clase validadora del formulario de urna. """

    @staticmethod
    def validate_estado_proyecto(widget: QComboBox):
        """ Válida el estado del proyecto. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'ESTADO DEL PROYECTO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_nombre_proyecto(widget: QLineEdit):
        """ Válida el nombre del proyecto. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NOMBRE DEL PROYECTO' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'NOMBRE DEL PROYECTO' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_fecha_inicio(widget: NullableDateEdit):
        """ Válida la fecha de inicio del proyecto. """

        # Sí el texto está vacío
        if not widget.date():
            return Result.failure("EL CAMPO 'FECHA DE INIUIO' NO PUEDE ESTAR "
                                  "VACÍO.")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_motivo_cierre(widget: QLineEdit):
        """ Válida la profundidad de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Controla la longitud del texto
        if len(widget.text()) > 64:
            return Result.failure("EL CAMPO 'MOTIVO DE CIERRE' NO "
                                  "PUEDE CONTENER MAS DE 64 CARACTERES")

        # Validación exitosa
        return Result.success(1)
