"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  29/03/2026
Comentarios:
    Controlador base de la posición de la planta en el acuario
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Model.DAO.posicion_planta_acuario_dao import \
    PosicionPlantaAcuarioDAO
from ModuloMaestro.Model.Entities.posicion_planta_acuario_entity import \
    PosicionPlantaAcuarioEntity
from Services.Result.result import Result
from Services.Validators.posicion_planta_acuario_validator import \
    PosicionPlantaAcuarioValidator
from ModuloMaestro.Views.Dialogs.posicion_planta_acuario_dialog import \
    PosicionPlantaAcuarioDialog
from ModuloMaestro.Views.Masters.posicion_pnalta_acuario_view import \
    PosicionPlantaAcuarioView


class PosicionPlantaAcuarioController(BaseController):
    """ 
    Controlador base del formulario maestro de la posición de la planta 
    en el acuario. 
    """

    def __init__(self,
                 view: PosicionPlantaAcuarioDialog | PosicionPlantaAcuarioView,
                 dao: PosicionPlantaAcuarioDAO,
                 model: PosicionPlantaAcuarioEntity):
        """
        Inicializa el controlador de comportamiento de fauna.
        :param view: PosicionPlantaAcuarioDialog | PosicionPlantaAcuarioView
        :param dao: PosicionPlantaAcuarioDAO
        :param model: PosicionPlantaAcuarioEntity
        """

        # Atributos
        self._posicion_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> PosicionPlantaAcuarioEntity:
        """ Configura la entidad. """

        ent = PosicionPlantaAcuarioEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.posicion = ctrs.edit_posicion.value()
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
        self._clean_view(self._view.frame.edit_posicion)

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
        self._clean_view(self._view.frame.edit_posicion)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida la categoría de acuario
        val = PosicionPlantaAcuarioValidator.validate_posicion(
            self._view.frame.edit_posicion
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

    def _get_posicion(self):
        """ Devuelve la posición de la planta en el acuario resultante. """

        return self._posicion_result

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
        self._view.frame.edit_posicion.setValue(ent.posicion)
        self._view.frame.text_descripcion.setValue(ent.descripcion)

        return Result.success(ent.id)
