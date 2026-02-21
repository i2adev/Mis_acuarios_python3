"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  01/10/2025
Comentarios:
    Controlador base del tipo de filtro.
"""

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.estado_proyecto_dao import EstadoProyectoDAO
from Model.Entities.estado_proyecto_entity import EstadoProyectoEntity
from Services.Result.result import Result
from Services.Validators.estado_proyecto_validator import \
    EstadoProyectoValidator
from Views.Dialogs.estado_proyecto_dialog import EstadoProyectoDialog
from Views.Masters.estado_proyecto_view import EstadoProyectoView


class EstadoProyectoController(BaseController):
    """ 
    Controlador base del formulario maestro del estado del proyecto. 
    """

    def __init__(self, view: EstadoProyectoDialog | EstadoProyectoView,
                 dao: EstadoProyectoDAO,
                 model: EstadoProyectoEntity):
        """
        Inicializa el controlador de tipo de filtro.
        :param view: EstadoProyectoDialog | EstadoProyectoView
        :param dao: EstadoProyectoDAO
        :param model: EstadoProyectoEntity
        """

        # Atributos
        self._estado_proyecto_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> EstadoProyectoEntity:
        """ Configura la entidad. """

        ent = EstadoProyectoEntity()
        ctrs = self._view.frame

        # ID
        if ctrs.edit_id.text():
            ent.id = int(ctrs.edit_id.text())
        else:
            ent.id = None

        # Estado del proyecto
        if ctrs.edit_estado_proyecto.text():
            ent.estado = ctrs.edit_estado_proyecto.text()
        else:
            ent.estado = None

        # Descripción del estado
        if ctrs.text_observaciones.toPlainText():
            ent.descripcion = ctrs.text_observaciones.toPlainText()
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
        self._clean_view(self._view.frame.edit_estado_proyecto)

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
        self._clean_view(self._view.frame.edit_estado_proyecto)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida el tipo de filtro
        res = EstadoProyectoValidator.validate_estado(
            self._view.frame.edit_estado_proyecto
        )

        if not res.is_success:
            self._view.frame.edit_estado_proyecto.setFocus()
            return res

        return Result.success(1)

    def _get_row_id(self, sender: QPushButton | QAction) -> Result:
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

    def _get_estado_proyecto(self):
        """ Devuelve la categoría de filtro resultante. """

        return self._estado_proyecto_result

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
        ide = modelo.index(fila, 0).data()
        estado = modelo.index(fila, 2).data()  # La columna 1 es el
        # númer correlativo.
        observaciones = modelo.index(fila, 3).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(ide) if ide is not None else ""
        )

        self._view.frame.edit_estado_proyecto.setText(
            str(estado) if estado else ""
        )

        self._view.frame.text_observaciones.setPlainText(
            str(observaciones) if observaciones is not None else ""
        )

        return Result.success(ide)
