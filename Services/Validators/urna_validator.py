"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Commentarios:
    Módulo para la validación del formulario de acuario.
"""
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox

from Services.Result.result import Result


class UrnaValidator:
    """ Clase validadora del formulario de urna. """

    @staticmethod
    def validate_marca(widget: QComboBox):
        """ Válida la marca de la urna. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MARCA DE ACUARIO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_modelo_urna(widget: QLineEdit):
        """ Válida el modelo de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'MODELO DE ACUARIO' NO PUEDE ESTAR VACÍO"
            )

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_anchura(widget: QLineEdit):
        """ Válida la anchura de la urna. """

        # Sí el texto está vacío
        if widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())
        if 0 > n > 10_000:
            return Result.failure("LA ANCHURA de la urna DEBE SER "
                                  "DE 0 A 10.0000 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_profundidad(widget: QLineEdit):
        """ Válida la profundidad de la urna. """

        # Sí el texto está vacío
        if widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())
        if 0 > n > 2_000:
            return Result.failure("LA PROFUNDIDAD de la urna DEBE SER "
                                  "DE 0 A 2.0000 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_altura(widget: QLineEdit):
        """ Válida la altura de la urna. """

        # Sí el texto está vacío
        if widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())
        if 0 > n > 2_000:
            return Result.failure("LA ALTURA de la urna DEBE SER "
                                  "DE 0 A 2.0000 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_grosor(widget: QLineEdit):
        """ Válida el grosor del cristal de la urna. """

        # Sí el texto está vacío
        if widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())
        if 0 > n > 200:
            return Result.failure("EL GROSOR DEL CRISTAL de la urna DEBE SER "
                                  "DE 0 A 200 mm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_volumen(widget: QLineEdit):
        """ Válida el volumen de la urna. """

        # Sí el texto está vacío
        if widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())
        if 0 > n > 10_000:
            return Result.failure("EL VOLUMEN de la urna DEBE SER "
                                  "DE 0 A 10.000 LITROS.")

            # Validación exitosa
        return Result.success(1)