"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  11/11/2025
Comentarios:
    Controlador base de acuario.
"""
from PyQt6.QtCore import QDate, QDateTime, QTime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton, QColorDialog

import globales
from Controllers.base_controller import BaseController
from Controllers.tipo_acuario_dialog_controller import \
    TipoAcuarioDialogController
from Controllers.urna_dialog_controller import UrnaDialogController
from Model.DAO.acuario_dao import AcuarioDAO
from Model.DAO.base_dao import BaseDAO
from Model.DAO.proyecto_dao import ProyectoDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.DAO.urna_dao import UrnaDAO
from Model.Entities.acuario_entity import AcuarioEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.Entities.urna_entity import UrnaEntity
from Services.Result.result import Result
from Services.Validators.acuario_validator import AcuarioValidator
from Views.Dialogs.acuario_dialog import AcuarioDialog
from Views.Dialogs.tipo_acuario_dialog import TipoAcuarioDialog
from Views.Dialogs.urna_dialog import UrnaDialog
from Views.Masters.acuario_view import AcuarioView


class AcuarioController(BaseController):
    """ 
    Controlador base del cuadro de diálogo y formulario maestro de proyecto. 
    """

    def __init__(self, view: AcuarioDialog | AcuarioView,
                 dao: AcuarioDAO,
                 model: AcuarioEntity):
        """
        Inicializa el controlador de la urna.
        :param view: AcuarioDialog | AcuarioView
        :param dao: AcuarioDAO
        :param model: AcuarioEntity
        """

        # Atributos
        self._acuario_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos()

    def _entity_configuration(self) -> AcuarioEntity:
        """ Configura la entidad. """

        ent = AcuarioEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.id_proyecto = ctrs.combo_proyecto.value()
        if ctrs.edit_cod_color.text():
            ent.cod_color = ctrs.edit_cod_color.text()
        else:
            ent.cod_color = None

        ent.nombre = ctrs.edit_nombre_acuario.value()
        ent.id_urna = int(ctrs.combo_urna.value())
        ent.id_tipo = int(ctrs.combo_tipo_acuario.value())
        ent.volumen_neto = ctrs.edit_vol_neto.value()

        f_montaje = ctrs.fecha_montaje.date()
        if f_montaje.isValid():
            time_inicio = QDateTime(f_montaje, QTime(0, 0))
            ent.fecha_montaje = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_montaje = None

        f_i_ciclado = ctrs.fecha_inicio_ciclado.date()
        if f_i_ciclado.isValid():
            time_inicio = QDateTime(f_i_ciclado, QTime(0, 0))
            ent.fecha_inicio_ciclado = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_inicio_ciclado = None

        f_f_ciclado = ctrs.fecha_fin_ciclado.date()
        if f_f_ciclado.isValid():
            time_inicio = QDateTime(f_f_ciclado, QTime(0, 0))
            ent.fecha_fin_ciclado = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_fin_ciclado = None

        f_desmontaje = ctrs.fecha_desmontaje.date()
        if f_desmontaje.isValid():
            time_inicio = QDateTime(f_desmontaje, QTime(0, 0))
            ent.fecha_desmontaje = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_desmontaje = None

        ent.motivo_desmontaje = ctrs.edit_motivo_desmontaje.value()
        ent.ubicacion_acuario = ctrs.edit_ubicacion_acuario.value()
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
        res_acuario = self._dao.insert(ent)
        if not res_acuario.is_success:
            return res_acuario

        # Insertamos las fotografías
        res_foto = self._view.frame_image.insert_images(res_acuario.value)
        if not res_foto.is_success:
            return res_foto

        return Result.success(res_acuario.value)

    def _update(self) -> Result:
        """ Actualiza el registro en la base de datos. """

        # Valida el formulario
        val = self._validate_view(False, False)

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self._entity_configuration()

        # Actualiza el registro
        res_acuario = self._dao.update(ent)

        if not res_acuario.is_success:
            return res_acuario

        # Actualizamos las fotografías
        res_foto = self._view.frame_image.insert_images(res_acuario.value)
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

    def _validate_view(self, val_color: bool = True,
                       val_is_mounted: bool = True) -> Result:
        """
        Valida el formulario.
        :param val_color: Indica si valida el color.
        :param val_is_mounted: Indica si valida si la urna está montada.
        """

        # Valida el color
        res = AcuarioValidator.validate_color(
            self._view.frame.edit_cod_color,
            int(self._view.frame.combo_proyecto.currentData()),
            val_color
        )

        if not res.is_success:
            self._view.frame.combo_proyecto.setFocus()
            return res

        # Valida el proyecto
        res = AcuarioValidator.validate_proyecto(
            self._view.frame.combo_proyecto
        )

        if not res.is_success:
            self._view.frame.combo_proyecto.setFocus()
            return res

        # Valida el nombre del acuario
        res = AcuarioValidator.validate_nombre(
            self._view.frame.edit_nombre_acuario
        )

        if not res.is_success:
            self._view.frame.edit_nombre_acuario.setFocus()
            return res

        # Valida la urna
        res = AcuarioValidator.validate_urna(
            self._view.frame.combo_urna, val_is_mounted
        )

        if not res.is_success:
            self._view.frame.combo_urna.setFocus()
            return res

        # Valida el tipo de acuario
        res = AcuarioValidator.validate_tipo_acuario(
            self._view.frame.combo_tipo_acuario
        )

        if not res.is_success:
            self._view.frame.combo_tipo_acuario.setFocus()
            return res

        # Valida la fecha de montaje
        res = AcuarioValidator.validate_fecha_montaje(
            self._view.frame.fecha_montaje
        )

        if not res.is_success:
            self._view.frame.fecha_montaje.edit_date.setFocus()
            return res

        return Result.success(0)

    def _get_row_id(self, sender: QPushButton | QAction) -> Result:
        """ Obtiene el ID del registro seleccionado."""

        control = type(sender).__name__

        if control == "QPushButton":
            # Sí tenemos un registro cargado
            if not self._view.frame.edit_id.text():
                return Result.failure("DEBES SELECCIONAR UN REGISTRO DE LA "
                                      "TABLA.")

            # Obtener el ID desde el cuadro de texto id_parent
            id_row = int(self._view.frame.edit_id.text())
            return Result.success(id_row)
        elif control == "QAction":
            # Carga el modelo de la fila seleccionada
            selection_model = self._view.data_table.selectionModel()

            # Chequea si se ha seleccionado una fila
            if not selection_model.hasSelection():
                return Result.failure("DEBES PULSAR SOBRE UN REGISTRO.")

            # Configuramos la fila
            index = selection_model.currentIndex()
            fila = index.row()
            modelo = self._view.data_table.model()

            # Lee los datos del modelo
            id_row = modelo.index(fila, 0).data()
            return Result.success(id_row)
        else:
            return Result.failure("DEBE SELECCIONAR O CARGAR UN REGISTRO")

    def _get_acuario(self):
        """ Devuelve el acuario resultante. """

        return self._acuario_result

    def _load_record(self):
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_urna()
        self._fill_combo_tipo_acuario()
        self._fill_combo_proyecto()

    def _fill_combo_proyecto(self):
        """ Llena el combo de los proyectos. """

        # Vaciamos el combo
        self._view.frame.combo_proyecto.clear()

        # Obtenemos los datos
        dao = ProyectoDAO()
        lista = dao.get_list_combo_by_user(globals.CURRENT_USER.id)

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'URNAS'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_proyecto.addItem(
                ent.nombre, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_proyecto)

        # Deselecciona el valor
        self._view.frame.combo_proyecto.setCurrentIndex(-1)

    def _fill_combo_urna(self):
        """ Llena el combo de la urna. """

        # Vaciamos el combo
        self._view.frame.combo_urna.clear()

        # Obtenemos los datos
        dao = UrnaDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'URNAS'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_urna.addItem(
                ent.modelo, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_urna)

        # Deselecciona el valor
        self._view.frame.combo_urna.setCurrentIndex(-1)

    def _fill_combo_tipo_acuario(self):
        """ Llena el combo del tipo de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_tipo_acuario.clear()

        # Obtenemos los datos
        dao = TipoAcuarioDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE ACUARIO'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_tipo_acuario.addItem(
                ent.observaciones, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_tipo_acuario)

        # Deselecciona el valor
        self._view.frame.combo_tipo_acuario.setCurrentIndex(-1)

    def _open_urna_dialog(self):
        """ Abrimos el diálogo de la urna. """

        # Configuramos el CONTROLADOR
        view = UrnaDialog("INSERTAR URNA")
        dao = UrnaDAO()
        mod = UrnaEntity()

        ctrl = UrnaDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_urna

        self._fill_combo_urna()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_tipo_acuario_dialog(self):
        """ Abrimos el diálogo del tipo de acuario. """

        # Configuramos el CONTROLADOR
        view = TipoAcuarioDialog("INSERTAR URNA")
        dao = TipoAcuarioDAO()
        mod = TipoAcuarioEntity()

        ctrl = TipoAcuarioDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_tipo_acuario

        self._fill_combo_tipo_acuario()
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
                "SELECCIONAR UNO EN LA TABLA."
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
        self._view.frame.combo_proyecto.setValue(ent.id_proyecto)
        if ent.cod_color:
            self._view.frame.edit_cod_color.setText(ent.cod_color)
            self._view.frame.button_color.setStyleSheet(
                f"background-color: {ent.cod_color};"
            )
        else:
            self._view.frame.edit_cod_color.setText(None)
            self._view.frame.button_color.setStyleSheet(
                "background-color: transparent;"
            )
        self._view.frame.edit_nombre_acuario.setValue(ent.nombre)
        self._view.frame.combo_urna.setValue(ent.id_urna)
        self._view.frame.combo_tipo_acuario.setValue(ent.id_tipo)
        self._view.frame.edit_vol_neto.setValue(ent.volumen_neto)
        self._view.frame.fecha_montaje.setDate(
            BaseDAO._seconds_to_date(ent.fecha_montaje))
        self._view.frame.fecha_inicio_ciclado.setDate(
            BaseDAO._seconds_to_date(ent.fecha_inicio_ciclado))
        self._view.frame.fecha_fin_ciclado.setDate(
            BaseDAO._seconds_to_date(ent.fecha_fin_ciclado))
        self._view.frame.edit_ubicacion_acuario.setValue(ent.ubicacion_acuario)
        self._view.frame.fecha_desmontaje.setDate(
            BaseDAO._seconds_to_date(ent.fecha_desmontaje))
        self._view.frame.edit_motivo_desmontaje.setValue(ent.motivo_desmontaje)
        self._view.frame.text_descripcion.setValue(ent.descripcion)

        return Result.success(ent.id)

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

    def _choose_color(self):
        """ Selecciona un color. """

        color = QColorDialog.getColor()

        if color.isValid():
            self._view.frame.edit_cod_color.setText(color.name())
            self._view.frame.button_color.setStyleSheet(
                f"background-color: {color.name()};"
            )
        else:
            QMessageBox(
                self._view,
                self._view.windowTitle(),
                "SE LA CANCELADO LA SELECCIÓN DE COLOR"
            )

    def brakdown_volumes(self, volumes: str) -> str:
        """
        Desmonta la celda del volumen y devuelve el volumen neto
        :param volumes: Cadena que representa las dimensiones del acuario
        """
        if not volumes:
            return ""

        lista = volumes.split("/")
        volumen_neto = lista[1]

        return volumen_neto

    def _on_text_changed(self):
        """
        Se ejecuta cuando se modifica el texto.
        """

        if self._view.frame.fecha_desmontaje.edit_date.text():
            self._setDisabledControl(
                self._view.frame.layout_motivo_desmontaje, False)
        else:
            self._setDisabledControl(
                self._view.frame.layout_motivo_desmontaje, True)
