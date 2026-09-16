"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  16/09/2026
Comentarios:
    Controlador base del tipo de control de iluminación.
"""

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Model.DAO.tipo_control_temperatura_dao import \
    TipoControlTemperaturaDAO
from ModuloMaestro.Model.Entities.tipo_control_temperatura_entity import \
    TipoControlTemperaturaEntity
from ModuloMaestro.Views.Dialogs.tipo_control_temperatura_dialog import \
    TipoControlTemperaturaDialog
from ModuloMaestro.Views.Masters.tipo_control_temperatura_view import \
    TipoControlTemperaturaView
from Services.Result.result import Result
from Services.Validators.tipo_control_temperatura_validator import \
    TipoControlTemperaturaValidator


class TipoControlTemperaturaController(BaseController):
    """ 
    Controlador base del formulario maestro de tipo de control de 
    iluminación. 
    """

    def __init__(self,
                 view: TipoControlTemperaturaDialog | TipoControlTemperaturaView,
                 dao: TipoControlTemperaturaDAO,
                 model: TipoControlTemperaturaEntity):
        """
        Inicializa el controlador de tipo de filtro.
        :param view: TipoControlTemperaturaDialog | TipoControlTemperaturaView
        :param dao: TipoControlTemperaturaDAO
        :param model: TipoControlTemperaturaEntity
        """

        # Atributos
        self._tipo_control_temperatura_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> TipoControlTemperaturaEntity:
        """ Configura la entidad. """

        ent = TipoControlTemperaturaEntity()
        ctrs = self._view.frame

        ent.id = ctrs.edit_id.value()
        ent.tipo_control_temperatura = ctrs.edit_tipo_control_temperatura.value()
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
        self._clean_view(self._view.frame.edit_tipo_control_temperatura)

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
        self._clean_view(self._view.frame.edit_tipo_control_temperatura)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida el tipo de control de temperatura
        res = TipoControlTemperaturaValidator.validate_tipo_control_temperatura(
            self._view.frame.edit_tipo_control_temperatura
        )

        if not res.is_success:
            self._view.frame.edit_tipo_control_temperatura.setFocus()
            return res

        return Result.success(0)

    def _get_row_id(self, sender: QPushButton | QAction) -> Result:
        control = type(sender).__name__

        if control == "QPushButton":
            # Sí tenemos un registro cargado
            if not self._view.frame.edit_id.text():
                return Result.failure("DEBES SELECCIONAR UN REGISTRO DE LA "
                                      "TABLA ANTES DE ELIMINARLO.")

            # Obtener el ID desde el cuadro de texto id_parent
            id_row = int(self._view.frame.edit_id.value())
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

    def _get_tipo_control_temperatura(self):
        """ Devuelve el tipo de control de temperatura resultante. """

        return self._tipo_control_temperatura_result

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
        self._view.frame.edit_tipo_control_temperatura.setValue(
            ent.tipo_control_temperatura)
        self._view.frame.text_descripcion.setValue(ent.descripcion)

        return Result.success(ent.id)
