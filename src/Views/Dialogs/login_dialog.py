"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/09/2025
Commentarios:
    Módulo que contiene la vista de inicio de sesión.
"""

import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFrame, QSizePolicy,
                             QHBoxLayout, QPushButton, QLabel, QSpacerItem,
                             QApplication, QLineEdit, QWidget)


class LoginDialog(QDialog):
    """ Formulario de tipo de filtro """

    def __init__(self):
        """ Constructor de clase """

        super().__init__()

        self.create_widgets()
        self.build_layout()
        self.set_tab_order()



    def create_widgets(self):
        """ Crea los elementos del formulario"""
        self.layout_main = QVBoxLayout()  # Layout principal

        self.frame_main = QFrame()
        self.frame_main.setObjectName("frame_main")
        self.frame_main.setSizePolicy(QSizePolicy.Policy.Expanding,
                                      QSizePolicy.Policy.Expanding)
        self.frame_main.setLayout(self.layout_main)
        self.frame_main.setStyleSheet("""
            #frame_main {
                border: 1px solid #4a4a4a;
                border-radius: 0px;
                background-color: transparent;
            }
        """)

        self.layout_form_data = QVBoxLayout()  # Layout del frame de controles
        self.frame_form = QFrame()  # Frame que contiene los controles
        self.frame_form.setStyleSheet(
            """
            border-radius: 0px;
            background-color: transparent;
            """
        )

        self.layout_footer = QVBoxLayout()  # Layout pie de formulario

        # Controles del frame
        ## Imagen
        self.label_image = QLabel()
        self.label_image.setPixmap(
                QPixmap("../../Resources/Images/cuenta.png").scaled(
                    QSize(100,100),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
            )
        )
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_image.setFixedHeight(100)

        ## Correo electrónico
        self.label_nick = QLabel("NICK DEL USUARIO")
        self.edit_nick = QLineEdit()

        ## Contraseña
        self.label_password = QLabel("CONTRASEÑA")
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        # self.label_window_title = QLabel(self.window_title)

        ## Icono de la ventana
        self.label_icon = QLabel()
        icon5 = QPixmap(":/Images/Window_icon.png")
        self.label_icon.setPixmap(icon5)

        ## Botón Aceptar
        self.button_entrar = QPushButton("&ENTRAR")
        self.button_entrar.setFlat(True)
        self.button_entrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ## Botón Cancelar
        self.button_cancel = QPushButton("&CANCELAR")
        self.button_cancel.setFlat(True)
        self.button_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ## Botón Crear usuario
        self.button_crear_usuario = QPushButton("CREAR NUEVO USUARIO")
        self.button_crear_usuario.setFlat(True)
        self.button_crear_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def build_layout(self):
        """ Construye el layout de la ventana """

        # Ocultar barra de título
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Configuramos los controles
        self.layout_form_data.addWidget(self.label_image)
        self.layout_form_data.addWidget(self.label_nick)
        self.layout_form_data.addWidget(self.edit_nick)
        self.layout_form_data.addSpacerItem(
            QSpacerItem(10, 10, QSizePolicy.Policy.Fixed,
                        QSizePolicy.Policy.Fixed)
        )
        self.layout_form_data.addWidget(self.label_password)
        self.layout_form_data.addWidget(self.edit_password)
        self.layout_form_data.addSpacerItem(
            QSpacerItem(10, 10, QSizePolicy.Policy.Fixed,
                        QSizePolicy.Policy.Fixed)
        )

        self.frame_form.setLayout(self.layout_form_data)

        # Configulamos el layout del pie de formulario
        self.layout_footer.addWidget(self.button_entrar)
        self.layout_footer.addWidget(self.button_cancel)
        self.layout_footer.addWidget(self.button_crear_usuario)

        # Cargamos los layout en la ventana
        self.layout_main.addWidget(self.frame_form)
        self.layout_main.addLayout(self.layout_footer)

        layout_root = QVBoxLayout(self)
        layout_root.setContentsMargins(0, 0, 0, 0)
        layout_root.setSpacing(0)
        layout_root.addWidget(self.frame_main)

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las politicas de focus
        self.edit_nick.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.edit_password.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.edit_nick, self.edit_password
        )


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = LoginDialog()

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())