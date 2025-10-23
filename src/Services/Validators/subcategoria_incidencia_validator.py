"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo para la validación del formulario de la subcategoría de
    acuario.
"""

from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox

from Services.Result.result import Result


class SubcategoriaIncidenciaValidator:
    """ Valida el formulario de categoría de acuario. """

    @staticmethod
    def validate_categoria_incidencia(widget: QComboBox):
        """ Valida la categoría de acuario. """

        # Sí el texto esta vacio
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'CATEGORÍA DE INCIDENCIA' NO PUEDE ESTAR VACIO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_subcategoria_incidencia(widget: QLineEdit):
        """ Valida la subcategoría de acuario. """

        # Sí el texto esta vacio
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'SUBCATEGORÍA DE INCIDENCIA' NO PUEDE ESTAR VACIO"
            )

        # Si el texto contiene más de 32 carácteres
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'SUBCATEGORÍA DE INCIDENCIA' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
