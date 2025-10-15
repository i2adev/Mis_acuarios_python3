"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Commentarios:
    Módulo para la validación del formulario de usuario.
"""
import re

from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QLineEdit

from Services.Result.result import Result


class UsuarioValidator:
    """ Valida el formulario de la creación de cuenta de usuario. """

    @staticmethod
    def validate_nombre(widget: QLineEdit):
        """ Válida el nombre del usuario. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'NOMBRE' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 20:
            return Result.failure("EL CAMPO 'NOMBRE' NO "
                                "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_primer_apellido(widget: QLineEdit):
        """ Válida el primer apellido del usuario. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'PRIMER APELLIDO' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'PRIMER APELLIDO' NO "
                                "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_segundo_apellido(widget: QLineEdit):
        """ Válida el segundo apellido del usuario. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'SEGUNDO APELLIDO' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'SEGUNDO APELLIDO' NO "
                                "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_nick(widget: QLineEdit):
        """ Válida el nick del usuario. """

        # Controla la longitud del texto
        if len(widget.text()) > 15:
            return Result.failure("EL CAMPO 'NICK DE USUARIO' NO "
                                "PUEDE CONTENER MAS DE 32 CARACTERES")

        return Result.success(1)

    @staticmethod
    def validate_mail(widget: QLineEdit):
        """ Válida el mail del usuario. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.failure(
                "EL CAMPO 'E-MAIL' NO PUEDE ESTAR VACÍO"
            )

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'E-MAIL' NO "
                                "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Comprobamos el formato de la dirección e-mail
        pattern = QRegularExpression(
            r"^(?:[a-zA-Z0-9_'^&+/=?`{|}~.-]+)@"
            r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
        )

        if not re.match(pattern, widget.text()):
            return Result.failure("EL CAMPO 'E-MAIL' NO "
                                "TIENE EL FORMATO CORRECTO")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_password(widget1: QLineEdit, widget2: QLineEdit):
        """ Valida la contraseña. """
        password = widget1.text()
        password_confirm = widget2.text()

        # Determina si las 2 contraseñas son iguales
        if password != password_confirm:
            return Result.failure("AMBAS CONTRASEÑAS HAN DE SER IGUALES")

        # Verifica la longitud de la contraseña
        if len(password) < 6 or len(password) > 8:
            return Result.failure("LA LONGITUD DE LA CONTRASEÑA HA DE ESTAR "
                                  "ENTRE 6 Y 8 CARÁCTERES")

        return Result.success(1)



