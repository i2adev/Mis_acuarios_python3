"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      25/02/2026
Comentarios:
    Clase validadora de campos de texto
"""
from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class Validator:
    """ Clase validadora generica. """

    @staticmethod
    def validate_integer_field(widget: QLineEdit,
                               nullable: bool = True) -> Result:
        """
        Valida un campo de texto que solo admite valores enteros
        """

        # Sí el texto está vacío
        if not widget.text():
            if nullable:
                return Result.success(0)
            else:
                return Result.failure(f"EL CAMPO <{widget.control_name}> "
                                      f"NO PUEDE ESTAR VACÍO.")

        # Valida el rango del volumen
        n = int(widget.text().replace('.', ''))

        if (n < widget.min_value) or (n > widget.max_value):
            min = "{:,}".format(widget.min_value).replace(",", ".")
            max = "{:,}".format(widget.max_value).replace(",", ".")
            return Result.failure(f"EL '{widget.control_name}' DEBE SER "
                                  f"DE {min} A {max} {widget.units}.")

        # Validación exitosa
        return Result.success(0)

    @staticmethod
    def validate_float_field(widget: QLineEdit,
                             nullable: bool = True) -> Result:
        """ Valida un campo de texto que solo admite valores decimales. """

        # Sí el texto está vacío
        if not widget.text():
            if nullable:
                return Result.success(0)
            else:
                return Result.failure(f"EL CAMPO '{widget.control_name}' "
                                      f"NO PUEDE ESTAR VACÍO.")

        # Valida el rango del volumen
        n = float(widget.text()
                  .replace(",", "X")
                  .replace(".", ",")
                  .replace("X", "."))

        if (n < widget.min_value) or (n > widget.max_value):
            min = "{:,}".format(widget.min_value).replace(",", ".")
            max = "{:,}".format(widget.max_value).replace(",", ".")
            return Result.failure(f"EL '{widget.control_name}' DEBE SER "
                                  f"DE {min} A {max} {widget.units}.")

        # Validación exitosa
        return Result.success(0)
