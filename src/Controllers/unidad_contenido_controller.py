"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  04/03/2026
Comentarios:
    Controlador base del tipo de filtro.
"""

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.unidad_contenido_dao import UnidadContenidoDAO
from Model.Entities.unidad_contenido_entity import UnidadContenidoEntity
from Services.Result.result import Result
from Services.Validators.unidad_contenido_validator import \
    UnidadContenidoValidator
from Views.Dialogs.unidad_contenido_dialog import UnidadContenidoDialog
from Views.Masters.unidad_contenido_master import UnidadContenidoView


class UnidadContenidoController(BaseController):
    """ 
    Controlador base del formulario unidad de contenido. 
    """

    def __init__(self, view: UnidadContenidoDialog |
                             UnidadContenidoView,
                 dao: UnidadContenidoDAO,
                 model: UnidadContenidoEntity):
        """
        Inicializa el controlador de tipo de filtro.
        :param view: UnidadContenidoDialog | UnidadContenidoView
        :param dao: UnidadContenidoDAO
        :param model: UnidadContenidoDAO
        """

        # Atributos
        self._unidad_contenido_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> UnidadContenidoEntity:
        """ Configura la entidad. """

        ent = UnidadContenidoEntity()
        ctrs = self._view.frame

        # ID
        if ctrs.edit_id.text():
            ent.id = int(ctrs.edit_id.text())
        else:
            ent.id = None

        # Categoría de consumible
        ent.unidad = ctrs.edit_unidad_contenido.value()

        # Descripción de la categoría
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
        self._clean_view(self._view.frame.edit_unidad_contenido)

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
        self._clean_view(self._view.frame.edit_unidad_contenido)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida el tipo de filtro
        res = UnidadContenidoValidator.validate_unidad_contenido(
            self._view.frame.edit_unidad_contenido
        )

        if not res.is_success:
            self._view.frame.edit_unidad_contenido.setFocus()
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

    def _get_unidad_contenido(self):
        """ Devuelve la unidad de contenido. """

        return self._unidad_contenido_result

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
        unidad = modelo.index(fila, 2).data()  # La columna 1 es el
        # número correlativo.
        descripcion = modelo.index(fila, 3).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(ide) if ide is not None else ""
        )

        self._view.frame.edit_unidad_contenido.setValue(unidad)
        self._view.frame.text_descripcion.setValue(descripcion)

        return Result.success(ide)
