"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/02/2026
Comentarios:
    Módulo para la validación de la iluminación.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from CustomControls.nullable_date_edit import NullableDateEdit
from Services.Result.result import Result


class IluminacionValidator:
    """ Clase validadora del formulario de iluminación. """

    @staticmethod
    def validate_tipo_iluminacion(widget: QComboBox):
        """ Valida el tipo de iluminación. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'TIPO DE ILUMINACIÓN' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_marca(widget: QComboBox):
        """ Valida la marca de la luminaria. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_modelo(widget: QLineEdit):
        """ Valida el modelo de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MODELO' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MODELO' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_serial_number(widget: QLineEdit):
        """ Valida el numero de serie de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NÚMERO DE SERIE' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'NÚMERO DE SERIE' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_potencia(widget: QLineEdit):
        """ Valida el potencia (w) de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Válida el rango del volumen
        n = float(widget.text().replace(",", "."))

        if (n < 2.0) or (n > 400.0):
            return Result.failure("LA POTENCIA DE LA LUMINARIA DEBE SER "
                                  "DE 2 A 400 VATIOS.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_flujo_luminoso(widget: QLineEdit):
        """ Valida el flujo luminoso (lm/l) de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Válida el rango del volumen
        n = int(widget.text())

        if (n < 5) or (n > 200):
            return Result.failure("EL FLUJO LUMINOSO DE LA LUMINARIA DEBE SER "
                                  "DE 2 A 200 LÚMENES POR LITRO.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_temperatura(widget: QLineEdit):
        """ Valida la temperatura (K) de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Válida el rango del volumen
        n = int(widget.text())

        if (n < 4_000) or (n > 12_000):
            return Result.failure("LA TEMPERATURA DE COLOR DE LA LUMINARIA "
                                  "DEBE SER DE 4.000 A 12.000 GRADOS KELVIN.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_vida_util(widget: QLineEdit):
        """ Valida la vida util (horas) de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Válida el rango del volumen
        n = int(widget.text())

        if (n < 1_000) or (n > 200_000):
            return Result.failure("LA VIDA UTIL DE LA LUMINARIA DEBE SER "
                                  "DE 1.000 A 200.000 HORAS.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_longitud(widget: QLineEdit):
        """ Valida la longitud (cm) de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Válida el rango del volumen
        n = float(widget.text().replace(",", "."))

        if (n < 20.0) or (n > 200.0):
            return Result.failure("LA LONGITUD DE LA LUMINARIA DEBE SER "
                                  "DE 20 A 200 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_anchura(widget: QLineEdit):
        """ Valida la anchura (cm) de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Válida el rango del volumen
        n = float(widget.text().replace(",", "."))

        if (n < 5.0) or (n > 100.0):
            return Result.failure("LA ANCHURA DE LA LUMINARIA DEBE SER "
                                  "DE 5 A 100 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_fecha_alta(widget: NullableDateEdit) -> Result:
        """ Válida la fecha de alta del proyecto. """

        # Sí el texto está vacío
        if not widget.date():
            return Result.failure("EL CAMPO 'FECHA DE ALTA' NO PUEDE ESTAR "
                                  "VACÍO.")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_motivo_baja(widget: QLineEdit) -> Result:
        """ Valida el motivo baja de la luminaria. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MOTIVO DE BAJA ' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
