"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  15/12/2025
Comentarios:
    Controlador base de la categoría de equipamiento.
"""

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.categoria_equipamiento_dao import CategoriaEquipamientoDAO
from Model.Entities.categoria_equipamiento_entity import \
    CategoriaEquipamientoEntity
from Services.Result.result import Result
from Services.Validators.categoria_equipamiento_validator import \
    CategoriaEquipamientoValidator
from Views.Dialogs.cattegoria_equipamiento_dialog import \
    CategoriaEquipamientoDialog
from Views.Masters.categoria_equipamiento_view import CategoriaEquipamientoView


class CategoriaEquipamientoController(BaseController):
    """ 
    Controlador base del formulario maestro de categoría de equipamiento. 
    """

    def __init__(self,
                 view: CategoriaEquipamientoDialog | CategoriaEquipamientoView,
                 dao: CategoriaEquipamientoDAO,
                 model: CategoriaEquipamientoEntity):
        """
        Inicializa el controlador de categoría de equipamiento
        :param view: CategoriaEquipamientoDialog | CategoriaEquipamientoView
        :param dao: CategoriaEquipamientoDAO
        :param model: CategoriaEquipamientoEntity
        """

        # Atributos
        self._cat_equipamiento_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> CategoriaEquipamientoEntity:
        """ Configura la entidad. """

        ent = CategoriaEquipamientoEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.categoria_equipamiento = self._view.frame.edit_categoria_equipamiento.text()
        ent.descripcion = self._view.frame.text_descripcion.toPlainText()

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
        self._clean_view(self._view.frame.edit_categoria_equipamiento)

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
        self._clean_view(self._view.frame.edit_categoria_equipamiento)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida la categoría de equipamiento
        res = CategoriaEquipamientoValidator.validate_tipo_equipamiento(
            self._view.frame.edit_categoria_equipamiento
        )

        if not res.is_success:
            self._view.frame.edit_categoria_equipamiento.setFocus()
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

    def _get_cat_equipamiento(self):
        """ Devuelve la categoría de filtro resultante. """

        return self._cat_equipamiento_result

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
        id = modelo.index(fila, 0).data()
        cat_equipamiento = modelo.index(fila, 2).data()
        descripcion = modelo.index(fila, 3).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id) if id is not None else ""
        )

        self._view.frame.edit_categoria_equipamiento.setText(
            str(cat_equipamiento) if cat_equipamiento else ""
        )

        self._view.frame.text_descripcion.setPlainText(
            str(descripcion) if descripcion is not None else ""
        )

        return Result.success(id)
