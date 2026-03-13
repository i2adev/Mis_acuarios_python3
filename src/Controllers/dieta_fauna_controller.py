"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  13/03/2026
Comentarios:
    Controlador base de la dieta de fauna.
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.dieta_fauna_dao import DietaFaunaDAO
from Model.Entities.dieta_fauna_entity import DietaFaunaEntity
from Services.Result.result import Result
from Services.Validators.dieta_fauna_validator import DietaFaunaValidator
from Views.Dialogs.dieta_fauna_dialog import DietaFaunaDialog
from Views.Masters.dieta_fauna_view import DietaFaunaView


class DietaFaunaController(BaseController):
    """ Controlador base del formulario maestro de dieta de fauna. """

    def __init__(self,
                 view: DietaFaunaDialog | DietaFaunaView,
                 dao: DietaFaunaDAO,
                 model: DietaFaunaEntity):
        """
        Inicializa el controlador de dieta de fauna.
        :param view: DietaFaunaDialog | DietaFaunaView
        :param dao: DietaFaunaDAO
        :param model: DietaFaunaEntity
        """

        # Atributos
        self._dieta_fauna = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> DietaFaunaEntity:
        """ Configura la entidad. """

        ent = DietaFaunaEntity()
        ctrs = self._view.frame

        # ID
        if ctrs.edit_id.text():
            ent.id = int(ctrs.edit_id.text())
        else:
            ent.id = None

        # dieta
        ent.dieta = ctrs.edit_dieta.value()

        # Descripción
        if ctrs.text_descripcion.toPlainText():
            ent.descripcion = ctrs.text_descripcion.toPlainText()
        else:
            ent.descripcion = None

        return ent

    # INICIO DE CRUD ---------------------------------------------------
    def _insert(self) -> Result:
        """ Inserta un registro en la base de datos. """

        # Validamos el formulario
        val = self._validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self._entity_configuration()

        # Inserta el registro
        res = self._dao.insert(ent)
        if not res.is_success:
            return res

        return Result.success(res.value)

    def _update(self) -> Result:
        """ Actualiza el registro en la base de datos. """
        # Valida el formulario
        val = self._validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self._entity_configuration()

        # Actualiza el registro
        res = self._dao.update(ent)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view(self._view.frame.edit_dieta)

        return Result.success(ent.id)

    def _delete(self, ide: int) -> Result:
        """
        Elimina un registro de la base de datos.
        :param ide: Id del registro a eliminar.
        """

        # Solicitamos doble confirmación
        res = QMessageBox.question(
            self._view,
            self._view.window_title,
            "¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        res = QMessageBox.question(
            self._view,
            self._view.window_title,
            "R E P I T O\n¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        # Elimina el registro
        res = self._dao.delete(ide)

        if not res.is_success:
            return Result.failure(res.error_msg)

        # Limpiamos el formulario
        self._clean_view(self._view.frame.edit_dieta)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida la dieta del animal
        val = DietaFaunaValidator.validate_dieta(
            self._view.frame.edit_dieta
        )

        return val

    def _get_row_id(self, sender: QPushButton | QAction) -> Result:
        """ Obtiene el id de la fila. """

        control = type(sender).__name__

        if control == "QPushButton":
            # Sí tenemos un registro cargado
            if not self._view.frame.edit_id.text():
                return Result.failure("DEBES SELECCIONAR UN REGISTRO DE LA "
                                      "TABLA ANTES DE ELIMINARLO.")

            # Obtener el ID desde el cuadro de texto id_parent
            id_row = int(self._view.frame.edit_id.text())
            return Result.success(id_row)
        elif control == "QAction":
            # Carga el modelo de la fila seleccionada
            selection_model = self._view.data_table.selectionModel()

            # Chequea si se ha seleccionado una fila
            if not selection_model.hasSelection():
                return Result.failure("ANTES DE ELIMINAR UN REGISTRO, DEBES "
                                      "SELECCIONAR UN REGISTRO EN LA TABLA.")

            # Configuramos la fila
            index = selection_model.currentIndex()
            fila = index.row()
            modelo = self._view.data_table.model()

            # Lee los datos del modelo
            id_row = modelo.index(fila, 0).data()
            return Result.success(id_row)
        else:
            return Result.failure("DEBE SELECCIONAR O CARGAR UN REGISTRO")

    def _get_dieta(self):
        """ Devuelve la dieta del animal resultante. """

        return self._dieta_fauna

    def _load_record(self) -> Result:
        """ Carga el registro en el formulario. """

        # Carga el modelo de la fila seleccionada
        selection_model = self._view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            return Result.failure(
                "ANTES DE CARGAR UN REGISTRO, DEBES "
                "SELECCIONAR UN REGISTRO EN LA TABLA."
            )

        # Configuramos la fila
        index = selection_model.currentIndex()
        fila = index.row()
        modelo = self._view.data_table.model()

        # Lee los datos del modelo
        id_cat = modelo.index(fila, 0).data()
        dieta = modelo.index(fila, 2).data()  # La columna 1 es el
        # númer correlativo.
        descripcion = modelo.index(fila, 3).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_cat) if id_cat is not None else ""
        )
        self._view.frame.edit_dieta.setValue(dieta)
        self._view.frame.text_descripcion.setPlainText(
            str(descripcion) if descripcion is not None else ""
        )

        return Result.success(id_cat)
