"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/09/2025
Commentarios:
    Módulo que contiene la clase controladora del formulario de login.
"""

from PyQt6.QtWidgets import (QWidget, QMessageBox, QComboBox)

from Controllers.base_controller import BaseController
from Controllers.usuario_controller import UsuarioDialogController
from Model.DAO.usuario_dao import UsuarioDAO
from Model.Entities.usuario_entity import UsuarioEntity
import globals
from Services.Result.result import Result
from Views.Dialogs.login_dialog import LoginDialog
from Views.Dialogs.usuario_dialog import UsuarioDialog


class LoginDialogController(BaseController):
    """ Controlador del diálogo de usuario. """

    def __init__(self, view: LoginDialog, dao: UsuarioDAO,
                 mod: UsuarioEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista tipo Usuario
        :param dao: DAO de la entidad UrnaDAO
        :param mod: Modelo de la entidad UsuarioEntity
        """

        # inicializamos la vista y pasamos al constructor padre
        super().__init__(view, dao, mod)

        # Atributos
        self.usuario_result = None

        # Inicializamos los eventos
        self.init_basic_handlers()

    def init_basic_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        self.init_imput_handlers()

        if isinstance(self._view, LoginDialog):
            self.init_dialog_handlers()

    def init_dialog_handlers(self):
        """ Inicializa los controles del cuadro de diálogo. """

        # Botones
        self._view.button_entrar.clicked.connect(self.button_entrar_click)
        self._view.button_cancel.clicked.connect(self.dialog_cancel)
        self._view.button_crear_usuario.clicked.connect(
            self.button_crear_usuario_click
        )

    def init_imput_handlers(self):
        """ Inicializa los controles de entrada. """

        # Controles de entrada de texto
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)
            if isinstance(widget, QComboBox):
                widget.installEventFilter(self)

    def get_user_by_nick(self, nick: str) -> Result(UsuarioEntity):
        """ Devuelve el usuario con el nick suministrado. """

        # Obtenemos el usuario con el nick
        res = self._dao.get_validated_user(nick)

        if not res.is_success:
            return res

        if not res.value:
            return Result.failure("NO SE HAN PODIDO OBTENER LAS CREDENCIALES "
                                  "CON EL NICK Y CONTRASEÑA ESPECIFICADOS")

        return res

    def button_entrar_click(self):
        """ Se acepta el diálogo. """

        nick = self._view.edit_nick.text()
        pwd = self._view.edit_password.text()

        # Chequea que ambos campos están rellenados
        if not nick or not pwd:
            QMessageBox.information(
                self._view,
                "LOGIN DE USUARIO",
                "SE DEBEN RELLENAR AMBOS CAMPOS"
            )
            return

        # Obtiene el usuario con el nick
        res = self._dao.get_validated_user(nick, pwd)

        if not res.is_success:
            QMessageBox.information(
                self._view,
                "LOGIN DE USUARIO",
                res.error_msg
            )
            self._clean_view(self._view.edit_nick)
            return
        globals.CURRENT_USER = res.value
        self._view.accept()

    def button_crear_usuario_click(self):
        """ Cuando se pulsa el botón de crear usuario. """

        view = UsuarioDialog(
            "INSERTAR USUARIO"
        )

        ctrl = UsuarioDialogController(view, self._dao, self._mod)
        res = ctrl.show_modal()

        if not res.is_success:
            return res

    def get_usuario(self):
        """ Devuelve la categoría de filtro resultante. """

        return self.usuario_result

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

    def show_modal(self) -> None:
        """ Abre la ventana. """

        return self._view.exec()