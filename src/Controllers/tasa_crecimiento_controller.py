"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  10/04/2026
Comentarios:
    Controlador base del requerimiento de TASA DE CRECIMIENTO
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.tasa_crecimiento_dao import TasaCrecimientoDAO
from Model.Entities.tasa_crecimiento_entity import TasaCrecimientoEntity
from Services.Result.result import Result
from Services.Validators.tasa_crecimiento_validator import \
    TasaCrecimientoValidator
from Views.Dialogs.tasa_crecimiento_dialog import TasaCrecimientoDialog
from Views.Masters.tasa_crecimiento_view import TasaCrecimientoView


class TasaCrecimientoController(BaseController):
    """ 
    Controlador base del formulario maestro de la tasa de crecimiento.
    """

    def __init__(self,
                 view: TasaCrecimientoDialog | TasaCrecimientoView,
                 dao: TasaCrecimientoDAO,
                 model: TasaCrecimientoEntity):
        """
        Inicializa el controlador de la tasa de crecimiento.
        :param view: TasaCrecimientoDialog | TasaCrecimientoView
        :param dao: TasaCrecimientoDAO
        :param model: TasaCrecimientoEntity
        """

        # Atributos
        self._crecimiento_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> TasaCrecimientoEntity:
        """ Configura la entidad. """

        ent = TasaCrecimientoEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.tasa_crecimiento = ctrs.edit_tasa_crecimiento.value()
        ent.descripcion = ctrs.text_descripcion.value()

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
        self._clean_view(self._view.frame.edit_tasa_crecimiento)

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
        self._clean_view(self._view.frame.edit_tasa_crecimiento)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida la categoría de acuario
        val = TasaCrecimientoValidator.validate_crecimiento(
            self._view.frame.edit_tasa_crecimiento
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

    def _get_crecimiento(self):
        """ Devuelve la tasa de crecimiento de la planta. """

        return self._crecimiento_result

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

        # Obtenemos la entidad
        id_ent = modelo.index(fila, 0).data()

        val = self._dao.get_entity_by_id(id_ent)
        if not val.is_success:
            return val

        ent = val.value

        # Cargamos los widgets
        self._view.frame.edit_id.setValue(ent.id)
        self._view.frame.edit_tasa_crecimiento.setValue(ent.tasa_crecimiento)
        self._view.frame.text_descripcion.setValue(ent.descripcion)

        return Result.success(ent.id)
