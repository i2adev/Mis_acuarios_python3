"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Commentarios:
    Módulo para la validación del formulario de acuario.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from CustomControls.nullable_date_edit import NullableDateEdit
from Services.Result.result import Result


class AcuarioValidator:
    """ Clase validadora del formulario de acuario. """

    @staticmethod
    def validate_nombre(widget: QLineEdit):
        """ Válida el nombre del acuario. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NOMBRE DEL ACUARIO' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'NOMBRE DEL ACUARIO' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_urna(widget: QComboBox):
        """ Válida la urna. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'URNA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_tipo_acuario(widget: QComboBox):
        """ Válida el tipo de acuario. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'TIPO DE ACUARIO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_vol_neto(widget: QLineEdit):
        """ Válida el volumen neto. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Valida el rango del volumen
        n = int(widget.text())

        if (n < 10) or (n > 2_000):
            return Result.failure("EL VOLUMEN NETO DEL ACUARIO DEBE SER "
                                  "DE 10 A 1.0000 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_fecha_montaje(widget: NullableDateEdit):
        """ Válida la fecha de inicio del proyecto. """

        # Sí el texto está vacío
        if not widget.date():
            return Result.failure("EL CAMPO 'FECHA DE MONTAJE' NO PUEDE ESTAR "
                                  "VACÍO.")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_motivo_desmontaje(widget: QLineEdit):
        """ Válida el motivo de desmontaje. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Controla la longitud del texto
        if len(widget.text()) > 64:
            return Result.failure("EL CAMPO 'MOTIVO DE DESMONTAJE' NO "
                                  "PUEDE CONTENER MAS DE 64 CARACTERES")

        # Validación exitosa
        return Result.success(1)
