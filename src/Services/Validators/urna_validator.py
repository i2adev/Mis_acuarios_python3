"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Commentarios:
    Módulo para la validación del formulario de acuario.
"""

from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox, QMessageBox

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

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MODELO DE ACUARIO' NO "
                                "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_anchura(widget: QLineEdit):
        """ Válida la anchura de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())

        if (n < 10) or (n > 1_000):
            return Result.failure("LA ANCHURA DE LA URNA DEBE SER "
                                  "DE 10 A 1.0000 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_profundidad(widget: QLineEdit):
        """ Válida la profundidad de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())

        if (n < 10) or (n > 2_000):
            return Result.failure("LA PROFUNDIDAD DE LA URNA DEBE SER "
                                  "DE 10 A 2.0000 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_altura(widget: QLineEdit):
        """ Válida la altura de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())

        if (n < 10) or (n > 2_000):
            return Result.failure("LA ALTURA DE LA URNA DEBE SER "
                                  "DE 10 A 2.0000 cm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_grosor(widget: QLineEdit):
        """ Válida el grosor del cristal de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())

        if (n < 2) or (n > 200):
            return Result.failure("EL GROSOR DEL CRISTAL DE LA URNA DEBE SER "
                                  "DE 2 A 200 mm.")

            # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_volumen(widget: QLineEdit):
        """ Válida el volumen de la urna. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Valida el rango de la anchura
        n = int(widget.text())

        if (n < 10) or (n > 2_000):
            return Result.failure("EL VOLUMEN de la urna DEBE SER "
                                  "DE 10 A 2.000 LITROS.")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_material(widget: QComboBox):
        """ Valida el material de lal urna. """

        # Sí el texto esta vacio
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'MATERIAL DE URNA' NO PUEDE ESTAR VACIO"
            )

        # Validación exitosa
        return Result.success(1)