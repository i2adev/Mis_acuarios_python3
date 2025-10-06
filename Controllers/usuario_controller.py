"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/09/2025
Commentarios:
    Módulo que contiene la clase controladora de la entidad USUARIO.
"""

from PyQt6.QtWidgets import (QWidget, QMessageBox, QComboBox)

from Controllers.base_controller import BaseController
from Model.DAO.usuario_dao import UsuarioDAO
from Model.Entities.usuario_entity import UsuarioEntity

from Services.Result.result import Result
from Services.Validators.usuario_validator import UsuarioValidator
from Views.Dialogs.usuario_dialog import UsuarioDialog


class UsuarioDialogController(BaseController):
    """ Controlador del diálogo de usuario. """

    def __init__(self, view: UsuarioDialog, dao: UsuarioDAO,
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

        # Llenamo los combos
        # self._fill_combos()

        # Inicializamos los eventos
        self.init_basic_handlers()

    def show_modal(self) -> Result:
        """ Abre la centava modal. """

        if self._view.exec():
            # Obtenemos la subcategoría de usuario
            usuario = self.get_usuario()
            return Result.success(usuario)
        else:
            return Result.failure("NO SE HA PODIDO OBTENER LA ENTIDAD.")

    def init_basic_handlers(self):
        """
        Inicializa los eventos de los widgets de la vista.
        """

        self.init_imput_handlers()

        if isinstance(self._view, UsuarioDialog):
            self.init_dialog_handlers()

    def init_dialog_handlers(self):
        """ Inicializa los controles del cuadro de diálogo. """

        # Botones
        self._view.button_accept.clicked.connect(self.dialog_accept)
        self._view.button_cancel.clicked.connect(self.dialog_cancel)

    def init_imput_handlers(self):
        """ Inicializa los controles de entrada. """

        # Controles de entrada de texto
        for widget in self._view.findChildren(QWidget):
            if isinstance(widget, self._text_widgets):
                widget.installEventFilter(self)
            if isinstance(widget, QComboBox):
                widget.installEventFilter(self)

    def entity_configuration(self) -> UsuarioEntity:
        """ Configura la entidad. """

        ent = UsuarioEntity()

        # if self._view.frame.edit_id.text():
        #     ent.id = int(self._view.frame.edit_id.text())
        # else:
        #     ent.id = None

        ent.nombre = self._view.frame.edit_nombre.text()
        ent.apellido1 = self._view.frame.edit_apellido_1.text()
        ent.apellido2 = self._view.frame.edit_apellido_2.text()
        ent.nick = self._view.frame.edit_nick.text()
        ent.password = self._view.frame.edit_password.text()

        return ent

    def insert(self) -> Result(int):
        """ Inserta un registro en la base de datos. """

        # Validamos el formulario
        val = self.validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self.entity_configuration()

        # Inserta el registro
        res_urna = self._dao.insert(ent)
        if not res_urna.is_success:
            return res_urna

        # Limpiamos el formulario
        self._clean_view(self._view.frame.edit_nombre)

        return Result.success(res_urna.value)

    def validate_view(self):
        """ Valida el formulario. """

        # Válida el nombre del usuario
        res = UsuarioValidator.validate_nombre(
            self._view.frame.edit_nombre
        )

        if not res.is_success:
            self._view.frame.edit_nombre.setFocus()
            return res

        # Valida el primer apellido del usuario
        res = UsuarioValidator.validate_primer_apellido(
            self._view.frame.edit_apellido_1
        )

        if not res.is_success:
            self._view.frame.edit_apellido_1.setFocus()
            return res

        # Valida el segundo apellido del usuario
        res = UsuarioValidator.validate_segundo_apellido(
            self._view.frame.edit_apellido_2
        )

        if not res.is_success:
            self._view.frame.edit_ancho.edit_apellido_2.setFocus()
            return res

        # Válida el nick del usuario
        res = UsuarioValidator.validate_nick(
            self._view.frame.edit_nick
        )

        if not res.is_success:
            self._view.frame.edit_nick.setFocus()
            return res

        # Valida la contraseña
        res = UsuarioValidator.validate_password(
            self._view.frame.edit_password,
            self._view.frame.edit_password_2
        )

        if not res.is_success:
            self._view.frame.edit_password.setFocus()
            return res

        return Result.success(1)

    def dialog_accept(self):
        """ Se acepta el diálogo. """

        # Insertamos el registro
        res = self.insert()

        if not res.is_success:
            QMessageBox.warning(
                self._view,
                self._view.window_title,
                res.error_msg
            )
            return

        # Configuramos la entidad
        self.usuario_result = UsuarioEntity(
            id = res.value,
            num = None,
            nombre = self._view.frame.edit_nombre.text(),
            apellido1 = self._view.frame.edit_apellido_1.text(),
            apellido2 = self._view.frame.edit_apellido_2.text(),
            nick= self._view.frame.edit_nick.text(),
            password = self._view.frame.edit_password.text(),
        )

        # Aceptamos el diálogo
        self._view.accept()

    def get_usuario(self):
        """ Devuelve la categoría de filtro resultante. """

        return self.usuario_result

    def dialog_cancel(self):
        """ Cancela el dialogo. """

        self._view.reject()

