"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  30/03/2026
Comentarios:
    Controlador base del requerimiento de CO2
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.requerimiento_co2_dao import RequerimientoCO2DAO
from Model.Entities.requerimiento_co2_entity import RequerimientoCO2Entity
from Services.Result.result import Result
from Services.Validators.requerimiento_co2_validator import \
    RequerimientoCO2Validator
from Views.Dialogs.requerimiento_co2_dialog import RequerimientoCO2Dialog
from Views.Masters.requerimiento_co2_view import RequerimientoCO2View


class RequerimientoCO2Controller(BaseController):
    """ 
    Controlador base del formulario maestro del requerimiento de CO2
    """

    def __init__(self,
                 view: RequerimientoCO2Dialog | RequerimientoCO2View,
                 dao: RequerimientoCO2DAO,
                 model: RequerimientoCO2Entity):
        """
        Inicializa el controlador de comportamiento de fauna.
        :param view: RequerimientoCO2Dialog | RequerimientoCO2View
        :param dao: RequerimientoCO2DAO
        :param model: RequerimientoCO2Entity
        """

        # Atributos
        self._requerimiento_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> RequerimientoCO2Entity:
        """ Configura la entidad. """

        ent = RequerimientoCO2Entity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.requerimiento = ctrs.edit_requerimiento.value()
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
        self._clean_view(self._view.frame.edit_requerimiento)

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
        self._clean_view(self._view.frame.edit_requerimiento)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida la categoría de acuario
        val = RequerimientoCO2Validator.validate_requerimiento(
            self._view.frame.edit_requerimiento
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

    def _get_requerimiento(self):
        """ Devuelve la posición de la planta en el acuario resultante. """

        return self._requerimiento_result

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
        self._view.frame.edit_requerimiento.setValue(ent.requerimiento)
        self._view.frame.text_descripcion.setValue(ent.descripcion)

        return Result.success(ent.id)
