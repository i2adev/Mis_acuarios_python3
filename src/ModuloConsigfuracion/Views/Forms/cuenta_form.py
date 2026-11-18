"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/10/2026
Comentarios:
    Frame que contiene los datos de la cuenta
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
                             QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, )

import globales
from CustomControls.combo_box import ComboBox
from CustomControls.str_line_edit import StrLineEdit


class CuentaForm(QFrame):
    """
    Clase que contiene los controles de la cuenta de usuario.
    """

    def __init__(self):
        super().__init__()

        # Política de expansión del control
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """Se encarga de crear los controles del formulario."""

        # Layouts
        self.layout_form = QVBoxLayout(self)
        self.layout_form.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.layout_primera_linea = QHBoxLayout()

        self.layout_personal_1 = QVBoxLayout()
        self.layout_personal_2 = QVBoxLayout()
        self.layout_seguridad = QVBoxLayout()
        self.layout_passwords = QHBoxLayout()
        self.layout_proyecto_acuario = QHBoxLayout()

        # Grupo de usuario
        self.usuario_group_box = QGroupBox("USUARIO")
        self.layout_gr_usuario = QVBoxLayout(self.usuario_group_box)

        ## Nombre
        self.label_nombre = QLabel("NOMBRE")
        self.edit_nombre = StrLineEdit(
            control_name="nombre",
            max_length=20,
            is_nullable=False,
        )
        self.edit_nombre.setToolTip(
            """
            <h2>Nombre real del usuario</h2>
            En este campo se inserta el nombre real del usuario. Este es un 
            campo <b>obligatorio</b>.
            """
        )
        self.layout_nnombre = QVBoxLayout()

        ## Primer apellido
        self.label_apellido_1 = QLabel("PRIMER APELLIDO")
        self.edit_apellido_1 = StrLineEdit(
            control_name="primer_apellido",
            max_length=32,
            is_nullable=False,
        )
        self.edit_apellido_1.setToolTip(
            """
            <h2>Primer apellido del usuario</h2>
            En este campo se inserta el primer apellido del usuario. 
            Este es un campo <b>obligatorio</b>.
            """
        )
        self.layout_apellido_1 = QVBoxLayout()

        ## Segundo apellido
        self.label_apellido_2 = QLabel("SEGUNDO APELLIDO")
        self.edit_apellido_2 = StrLineEdit(
            control_name="segundo_apellido",
            max_length=32,
            is_nullable=False,
        )
        self.edit_apellido_2.setToolTip(
            """
            <h2>Segundo apellido del usuario</h2>
            En este campo se inserta el segundo apellido del usuario. 
            Este es un campo <b>obligatorio</b>.
            """
        )
        self.layout_apellido_2 = QVBoxLayout()

        ## Nick del usuario
        self.label_nick = QLabel("NICK DEL USUARIO")
        self.edit_nick = StrLineEdit(
            control_name="nick_usuario",
            max_length=15,
        )
        self.edit_nick.setToolTip(
            """
            <h2>Nick del usuario</h2>
            En este campo se inserta el nick del usuario. Este es un
            campo <b>obligatorio</b>.
            """
        )
        self.layout_nick = QVBoxLayout()

        # Grupo de seguridad
        self.seguridad_group_box = QGroupBox("SEGURIDAD")
        self.layout_gr_seguridad = QVBoxLayout(self.seguridad_group_box)

        ## Check contraseña
        self.check_password = QCheckBox("REQUIERE CONTRASEÑA")

        ## Contraseña
        self.label_password = QLabel("CONTRASEÑA")
        self.edit_password = StrLineEdit(
            control_name="contrasena",
            max_length=32,
        )
        self.edit_password.setEchoMode(StrLineEdit.EchoMode.Password)
        self.layout_password_1 = QVBoxLayout()

        ## Repetir contraseña
        self.label_password_2 = QLabel("REPITE CONTRASEÑA")
        self.edit_password_2 = StrLineEdit(
            control_name="repite_contrasena",
            max_length=32,
        )
        self.edit_password_2.setEchoMode(StrLineEdit.EchoMode.Password)
        self.layout_password_2 = QVBoxLayout()

        # Grupo de proyecto y acuario
        self.proyectro_group_box = QGroupBox("PROYECTO Y ACUARIO")
        self.layout_gr_proyecto = QVBoxLayout(self.proyectro_group_box)

        # Proyecto
        self.label_proyecto = QLabel("PROYECTO POR DEFECTO")
        self.combo_proyecto = ComboBox("combo_proyecto")
        self.layout_proyecto = QVBoxLayout()

        ## Check último proyecto
        self.check_ultimo_proyecto = QCheckBox("ABRIR APLICACIÓN CON EL "
                                               "ÚLTIMO PROYECTO")

        # Acuario
        self.label_acuario = QLabel("ACUARIO POR DEFECTO")
        self.combo_acuario = ComboBox("combo_acuario")
        self.layout_acuario = QVBoxLayout()

    def build_layout(self):
        """Monta el layout del formulario."""

        # Datos del usuario
        ## Primera columna
        self.layout_nnombre.addWidget(self.label_nombre)
        self.layout_nnombre.addWidget(self.edit_nombre)

        self.layout_apellido_1.addWidget(self.label_apellido_1)
        self.layout_apellido_1.addWidget(self.edit_apellido_1)
        self.layout_apellido_1.setContentsMargins(0, 10, 0, 0)

        self.layout_personal_1.addLayout(self.layout_nnombre)
        self.layout_personal_1.addLayout(self.layout_apellido_1)

        # Segunda columna
        self.layout_apellido_2.addWidget(self.label_apellido_2)
        self.layout_apellido_2.addWidget(self.edit_apellido_2)

        self.layout_nick.addWidget(self.label_nick)
        self.layout_nick.addWidget(self.edit_nick)
        self.layout_nick.setContentsMargins(0, 10, 0, 0)

        self.layout_personal_2.addLayout(self.layout_apellido_2)
        self.layout_personal_2.addLayout(self.layout_nick)

        self.layout_primera_linea.addLayout(self.layout_personal_1)
        self.layout_primera_linea.addLayout(self.layout_personal_2)

        # Monta la información de usuario
        self.layout_gr_usuario.addLayout(self.layout_primera_linea)

        # Seguridad
        self.layout_password_1.addWidget(self.label_password)
        self.layout_password_1.addWidget(self.edit_password)

        self.layout_password_2.addWidget(self.label_password_2)
        self.layout_password_2.addWidget(self.edit_password_2)

        self.layout_passwords.addLayout(self.layout_password_1)
        self.layout_passwords.addLayout(self.layout_password_2)

        self.layout_seguridad.addWidget(self.check_password)
        self.layout_seguridad.addLayout(self.layout_passwords)

        # Montaje seguridad
        self.layout_gr_seguridad.addLayout(self.layout_seguridad)

        # Datos del proyecto
        self.layout_proyecto.addWidget(self.label_proyecto)
        self.layout_proyecto.addWidget(self.combo_proyecto)

        # Datos del acuario
        self.layout_acuario.addWidget(self.label_acuario)
        self.layout_acuario.addWidget(self.combo_acuario)

        # Añade proyecto y acuario al grupo
        self.layout_proyecto_acuario.addLayout(self.layout_proyecto)
        self.layout_proyecto_acuario.addLayout(self.layout_acuario)
        self.layout_gr_proyecto.addWidget(self.check_ultimo_proyecto)
        self.layout_gr_proyecto.addLayout(self.layout_proyecto_acuario)

        # Añade los grupos al formulario
        self.layout_form.addWidget(self.usuario_group_box)
        self.layout_form.addWidget(self.seguridad_group_box)
        self.layout_form.addWidget(self.proyectro_group_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = CuentaForm()
    ventana.setMinimumWidth(600)
    # ventana.setMinimumHeight(400)
    ventana.show()

    sys.exit(app.exec())
