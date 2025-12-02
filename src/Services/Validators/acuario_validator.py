"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Comentarios:
    Módulo para la validación del formulario de acuario.
"""

from PyQt6.QtWidgets import QLineEdit, QComboBox

from CustomControls.nullable_date_edit import NullableDateEdit
from Model.DAO.acuario_dao import AcuarioDAO
from Model.DAO.urna_dao import UrnaDAO
from Services.Result.result import Result


class AcuarioValidator:
    """ Clase validadora del formulario de acuario. """

    @staticmethod
    def validate_color(widget: QLineEdit, id_proyecto: int,
                       val_color: bool) -> Result:
        """ Valida el color. """

        if val_color:
            # Sí el texto está vacío
            if not widget.text():
                return Result.failure(
                    "DEBE SELECCIONAR UN COLOR PARA EL ACUARIO"
                )

            # Determina si el proyecto actual contiene el mismo color
            dao = AcuarioDAO()
            existe = dao.color_exists(widget.text(), id_proyecto)
            if existe.value:
                return Result.failure(
                    "YA EXISTE UN COLOR PARA EL ACUARIO. SELECCIONE OTRO."
                )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_proyecto(widget: QComboBox) -> Result:
        """ Válida el proyecto. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'PROYECTO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_nombre(widget: QLineEdit) -> Result:
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
    def validate_urna(widget: QComboBox, val_is_mounted: bool = True) -> Result:
        """ Válida la urna. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'URNA' NO PUEDE ESTAR VACÍO"
            )

        if val_is_mounted:
            # Valida de que no se inserta una urna que está aún montada
            id_urna = int(widget.currentData())
            dao = UrnaDAO()

            if dao.is_mounted(id_urna).value:
                return Result.failure(
                    f"lA URNA '{widget.currentText().upper()}' ESTÁ SIENDO UTILIZADA."
                )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_tipo_acuario(widget: QComboBox) -> Result:
        """ Válida el tipo de acuario. """

        # Sí el combo está vacío
        if not widget.currentData():
            return Result.failure(
                "EL CAMPO 'TIPO DE ACUARIO' NO PUEDE ESTAR VACÍO"
            )

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_vol_neto(widget: QLineEdit) -> Result:
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
    def validate_fecha_montaje(widget: NullableDateEdit) -> Result:
        """ Válida la fecha de inicio del proyecto. """

        # Sí el texto está vacío
        if not widget.date():
            return Result.failure("EL CAMPO 'FECHA DE MONTAJE' NO PUEDE ESTAR "
                                  "VACÍO.")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_motivo_desmontaje(widget: QLineEdit) -> Result:
        """ Válida el motivo de desmontaje. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'MOTIVO DE DESMONTAJE' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)

    @staticmethod
    def validate_ubicación_acuarfio(widget: QLineEdit) -> Result:
        """ Válida la ubicación del acuario. """

        # Sí el texto está vacío
        if not widget.text():
            return Result.success(1)

        # Controla la longitud del texto
        if len(widget.text()) > 32:
            return Result.failure("EL CAMPO 'UBICACIÓN DE ACUARIO' NO "
                                  "PUEDE CONTENER MAS DE 32 CARACTERES")

        # Validación exitosa
        return Result.success(1)
