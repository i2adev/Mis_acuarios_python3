"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  07/10/2025
Comentarios:
    Controlador base de urna.
"""
from PyQt6.QtCore import QDate, QDateTime, QTime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

import globals
from Controllers.base_controller import BaseController
from Controllers.estado_proyecto_dialog_controller import \
    EstadoProyectoDialogController
from Model.DAO.estado_proyecto_dao import EstadoProyectoDAO
from Model.DAO.proyecto_dao import ProyectoDAO
from Model.Entities.estado_proyecto_entity import EstadoProyectoEntity
from Model.Entities.proyecto_entity import ProyectoEntity
from Services.Result.result import Result
from Services.Validators.proyecto_validator import ProyectoValidator
from Views.Dialogs.estado_proyecto_dialog import EstadoProyectoDialog
from Views.Dialogs.proyecto_dialog import ProyectoDialog
from Views.Masters.proyecto_view import ProyectoView


class ProyectoController(BaseController):
    """ 
    Controlador base del cuadro de diálogo y formulario maestro de proyecto. 
    """

    def __init__(self, view: ProyectoDialog | ProyectoView,
                 dao: ProyectoDAO,
                 model: ProyectoEntity):
        """
        Inicializa el controlador de la urna.
        :param view: ProyectoDialog | ProyectoView
        :param dao: ProyectoDAO
        :param model: ProyectoEntity
        """

        # Atributos
        self._proyecto_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llena los combos
        self._fill_combos()

    def _entity_configuration(self) -> ProyectoEntity:
        """ Configura la entidad. """

        ent = ProyectoEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.ide = None
        ent.id_usuario = globals.CURRENT_USER.id
        ent.nombre = self._view.frame.edit_nombre_proyecto.text()
        ent.id_estado = self._view.frame.combo_estado_proyecto.currentData()

        inicio = self._view.frame.date_inicio.date()
        if inicio.isValid():
            time_inicio = QDateTime(inicio, QTime(0, 0))
            ent.fecha_inicio = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_inicio = None

        fin = self._view.frame.date_fin.date()
        if fin:
            time_fin = QDateTime(fin, QTime(0, 0))
            ent.fecha_fin = int(time_fin.toSecsSinceEpoch())
        else:
            ent.fecha_fin = None

        ent.motivo_cierre = self._view.frame.edit_motivo_cierre.text()
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
        res_urna = self._dao.insert(ent)
        if not res_urna.is_success:
            return res_urna

        # Insertamos las fotografías
        res_foto = self._view.frame_image.insert_images(res_urna.value)
        if not res_foto.is_success:
            return res_foto

        return Result.success(res_urna.value)

    def _update(self) -> Result:
        """ Actualiza el registro en la base de datos. """

        # Valida el formulario
        val = self._validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self._entity_configuration()

        # Actualiza el registro
        res_urna = self._dao.update(ent)

        if not res_urna.is_success:
            return res_urna

        # Actualizamos las fotografías
        res_foto = self._view.frame_image.insert_images(res_urna.value)
        if not res_foto.is_success:
            return res_foto

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

        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida el nombre del proyecto
        res = ProyectoValidator.validate_nombre_proyecto(
            self._view.frame.edit_nombre_proyecto
        )

        if not res.is_success:
            self._view.frame.edit_nombre_proyecto.setFocus()
            return res

        # Valida el estado del proyecto
        res = ProyectoValidator.validate_estado_proyecto(
            self._view.frame.combo_estado_proyecto
        )

        if not res.is_success:
            self._view.frame.combo_estado_proyecto.setFocus()
            return res

        # Valida la fecha de inicio
        res = ProyectoValidator.validate_fecha_inicio(
            self._view.frame.date_inicio
        )

        if not res.is_success:
            self._view.frame.date_inicio.edit_date.setFocus()
            return res

        # Valida el motivo de cierre del proyecto
        res = ProyectoValidator.validate_motivo_cierre(
            self._view.frame.edit_motivo_cierre
        )

        if not res.is_success:
            self._view.frame.edit_motivo_cierre.setFocus()
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

    def _get_proyecto(self):
        """ Devuelve el proyecto resultante. """

        return self._proyecto_result

    def _load_record(self):
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_estado()

    def _fill_combo_estado(self):
        """ Llena el combo del estado del proyecto. """

        # Vaciamos el combo
        self._view.frame.combo_estado_proyecto.clear()

        # Obtenemos los datos
        dao = EstadoProyectoDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'ESTADOS DE PROYECTO'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_estado_proyecto.addItem(
                ent.estado, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_estado_proyecto)

        # Deseleccionamos el valor
        self._view.frame.combo_estado_proyecto.setCurrentIndex(-1)

    def _open_estado_proyecto_dialog(self):
        """ Abrimos el diálogo del estado del proyecto. """

        # Configuramos el CONTROLADOR
        view = EstadoProyectoDialog("INSERTAR ESTADO DE PROYECTO")
        dao = EstadoProyectoDAO()
        mod = EstadoProyectoEntity()

        ctrl = EstadoProyectoDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_marca

        self._fill_combo_estado()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _load_data(self) -> Result:
        """ Carga los datos. """

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
        id_ent = modelo.index(fila, 0).data()
        nombre = modelo.index(fila, 3).data()
        estado = modelo.index(fila, 4).data()

        fecha_inicio = QDate.fromString(
            str(modelo.index(fila, 5).data()), "dd/MM/yyyy")

        fecha_fin = QDate.fromString(
            str(modelo.index(fila, 6).data()), "dd/MM/yyyy")
        motivo_cierre = modelo.index(fila, 7).data()
        descripcion = modelo.index(fila, 8).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ent) if id_ent is not None else ""
        )
        self._view.frame.edit_nombre_proyecto.setText(
            str(nombre) if nombre is not None else ""
        )
        self._view.frame.combo_estado_proyecto.setCurrentIndex(
            self._view.frame.combo_estado_proyecto.findText(estado)
        )
        self._view.frame.date_inicio.setDate(fecha_inicio)
        self._view.frame.date_fin.setDate(fecha_fin)

        self._view.frame.edit_motivo_cierre.setText(
            str(motivo_cierre) if motivo_cierre is not None else ""
        )
        self._view.frame.text_descripcion.setPlainText(
            str(descripcion) if descripcion is not None else ""
        )

        return Result.success(id_ent)

    def _load_images(self, id_: int):
        """
        Carga las imágenes de la base de datos.
        :param id_: ID de la entidad relacionada con la fotografía
        """

        # Chequea que el registro contiene imágenes
        self.lista_fotos = (self.fdao.get_list_by_id(id_)).value

        # Mostramos las imágenes
        if len(self.lista_fotos) > 0:
            # Configurar linea de datos
            self.label_num_imagen.setText("1")
            self.label_num_total_imegenes.setText(
                str(len(self.lista_fotos))
            )
            self.show_image()
