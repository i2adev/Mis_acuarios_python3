"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  14/03/2026
Comentarios:
    Controlador base del dificultad de planta.
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.dificultad_plantas_dao import DificultadPlantaDAO
from Model.Entities.dificultad_planta_entity import DificultadPlantaEntity
from Services.Result.result import Result
from Services.Validators.dificultad_planta_validator import \
    DificultadPlantaValidator
from Views.Dialogs.dificultad_planta_dialog import DificultadPlantaDialog
from Views.Masters.dificultad_planta_view import DificultadPlantaView


class DificultadPlantaController(BaseController):
    """ Controlador base del formulario maestro de dificultad de planta. """

    def __init__(self,
                 view: DificultadPlantaDialog | DificultadPlantaView,
                 dao: DificultadPlantaDAO,
                 model: DificultadPlantaEntity):
        """
        Inicializa el controlador de comportamiento de fauna.
        :param view: DificultadPlantaDialog | DificultadPlantaView
        :param dao: DificultadPlantaDAO
        :param model: DificultadPlantaEntity
        """

        # Atributos
        self._dificultad_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> DificultadPlantaEntity:
        """ Configura la entidad. """

        ent = DificultadPlantaEntity()
        ctrs = self._view.frame

        # ID
        if ctrs.edit_id.text():
            ent.id = int(ctrs.edit_id.text())
        else:
            ent.id = None

        # Nivel
        ent.nivel = ctrs.edit_nivel.value()

        # Dificultad
        ent.dificultad = ctrs.edit_dificultad.value()

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
        self._clean_view(self._view.frame.edit_comportamiento)

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
        self._clean_view(self._view.frame.edit_comportamiento)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida el nivel de dificultad
        val = DificultadPlantaValidator.validate_nivel(
            self._view.frame.edit_nivel
        )

        if not val.is_success:
            self._view.frame.edit_nivel.setFocus()
            return val

        # Valida la dificultad
        val = DificultadPlantaValidator.validate_dificultad(
            self._view.frame.edit_dificultad
        )

        if not val.is_success:
            self._view.frame.edit_dificultad.setFocus()
            return val

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

    def _get_dificultad(self):
        """ Devuelve la dificultad de mantenimiento de la planta. """

        return self._dificultad_result

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
        idc = modelo.index(fila, 0).data()
        nivel = modelo.index(fila, 2).data()  # La columna 1 es el
        # númer correlativo.
        dificultad = modelo.index(fila, 3).data()
        descripcion = modelo.index(fila, 4).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(idc) if idc is not None else ""
        )
        self._view.frame.edit_nivel.setValue(nivel)
        self._view.frame.edit_dificultad.setValue(dificultad)
        self._view.frame.text_descripcion.setPlainText(
            str(descripcion) if descripcion is not None else ""
        )

        return Result.success(idc)
