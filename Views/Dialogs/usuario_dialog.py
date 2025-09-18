"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/09/2025
Commentarios:
    Módulo que contiene el diálogo de la entidad USUARIO.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Dialogs.base_dialog import BaseDialog
from Views.Forms.usuario_form import UsuarioFOrm


class UsuarioDialog(BaseDialog):
    """ Diálogo de categoría de acuario. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = UsuarioFOrm()
        self.frame.setFixedWidth(600)
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las politicas de focus
        self.frame.edit_nombre.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_apellido_1.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_apellido_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_mail.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_password_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_password.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_nombre, self.frame.edit_apellido_1
        )
        self.setTabOrder(
            self.frame.edit_apellido_1, self.frame.edit_apellido_2
        )
        self.setTabOrder(
            self.frame.edit_apellido_2, self.frame.edit_mail
        )
        self.setTabOrder(
            self.frame.edit_mail, self.frame.edit_password
        )
        self.setTabOrder(
            self.frame.edit_password, self.frame.edit_password_2
        )

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = UsuarioDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())