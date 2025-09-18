"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/09/2025
Commentarios:
    Módulo que contiene los controles del formulario de la entidad USUARIO.
"""
import sys

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QApplication, \
    QLabel, QLineEdit


class UsuarioFOrm(QFrame):
    """ Clase que contiene los controles de la entidad usuario. """

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """

        # Layouts
        self.layout_main = QVBoxLayout()
        self.layout_personal = QVBoxLayout()
        self.layout_cuenta = QVBoxLayout()

        # Frames
        self.frame_personal = QFrame()
        self.frame_cuenta = QFrame()

        # Controles de información personal
        ## Nombre
        self.label_nombre = QLabel("NOMBRE")
        self.edit_nombre = QLineEdit()

        ## Primer apellido
        self.label_apellido_1 = QLabel("PRIMER APELLIDO")
        self.edit_apellido_1 = QLineEdit()

        ## Segundo apellido
        self.label_apellido_2 = QLabel("SEGUNDO APELLIDO")
        self.edit_apellido_2 = QLineEdit()

        ## E-mail
        self.label_mail = QLabel("E-MAIL")
        self.edit_mail = QLineEdit()

        # Controles con la información de la cuenta
        ## Usuario
        self.label_usuario = QLabel("USUARIO")
        self.edit_usuario = QLineEdit()

        ## Usuario
        self.label_password = QLabel("CONTRASEÑA")
        self.edit_password = QLineEdit()

    def build_layout(self):
        """ Construye el layout del frame. """

        # Monta el frame de información personal
        self.layout_personal.addWidget(self.label_nombre)
        self.layout_personal.addWidget(self.edit_nombre)
        self.layout_personal.addWidget(self.label_apellido_1)
        self.layout_personal.addWidget(self.edit_apellido_1)
        self.layout_personal.addWidget(self.label_apellido_2)
        self.layout_personal.addWidget(self.edit_apellido_2)
        self.frame_personal.setLayout(self.layout_personal)

        # Monta el frame de cuenta
        self.layout_cuenta.addWidget(self.label_mail)
        self.layout_cuenta.addWidget(self.edit_mail)
        self.layout_cuenta.addWidget(self.label_usuario)
        self.layout_cuenta.addWidget(self.edit_usuario)
        self.layout_cuenta.addWidget(self.label_password)
        self.layout_cuenta.addWidget(self.edit_password)
        self.frame_cuenta.setLayout(self.layout_cuenta)

        # Montamos el layout principal
        self.layout_main.addWidget(self.frame_personal)
        self.layout_main.addWidget(self.frame_cuenta)

        self.setLayout(self.layout_main)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = UsuarioFOrm()
    ventana.setFixedWidth(400)
    ventana.setFixedHeight(600)
    ventana.show()

    sys.exit(app.exec())