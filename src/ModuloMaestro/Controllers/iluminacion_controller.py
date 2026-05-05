"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  20/12/2025
Comentarios:
    Controlador base del control de iluminación.
"""
from PyQt6.QtCore import QDateTime, QTime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Controllers.control_iluminacion_dialog_controller import \
    ControlIluminacionDialogController
from ModuloMaestro.Controllers.marca_comercial_dialog_controller import \
    MarcaComercialDialogController
from ModuloMaestro.Controllers.tipo_iluminacion_dialog_controler import \
    TipoIluminacionDialogController
from Main.Model.DAO.base_dao import BaseDAO
from ModuloMaestro.Model.DAO.control_iluminacion_dao import \
    ControlIluminacionDAO
from ModuloMaestro.Model.DAO.iluminacion_dao import IluminacionDAO
from ModuloMaestro.Model.DAO.marca_comercial_dao import MarcaComercialDAO
from ModuloMaestro.Model.DAO.tipo_iluminacion_dao import TipoIluminacionDAO
from ModuloMaestro.Model.Entities.control_iluminacion_entity import \
    ControlIluminacionEntity
from ModuloMaestro.Model.Entities.iluminacion_entity import IluminacionEntity
from ModuloMaestro.Model.Entities.marca_comercial_entity import \
    MarcaComercialEntity
from ModuloMaestro.Model.Entities.tipo_iluminacion_entity import \
    TipoIluminacionEntity
from Services.Result.result import Result
from Services.Validators.iluminacion_validator import IluminacionValidator
from ModuloMaestro.Views.Dialogs.control_iluminacion_dialog import \
    ControlIluminacionDialog
from ModuloMaestro.Views.Dialogs.iluminacion_dialog import IluminacionDialog
from ModuloMaestro.Views.Dialogs.marca_comercial_dialog import \
    MarcaComercialDialog
from ModuloMaestro.Views.Dialogs.tipo_iluminacion_dialog import \
    TipoIluminacionDialog
from ModuloMaestro.Views.Masters.iluminacion_view import IluminacionView


class IluminacionController(BaseController):
    """ Controlador base del formulario maestro de control de iluminación. """

    def __init__(self, view: IluminacionDialog | IluminacionView,
                 dao: IluminacionDAO,
                 model: IluminacionEntity):
        """
        Inicializa el controlador de tipo de filtro.
        :param view: IluminacionDialog | IluminacionView
        :param dao: IluminacionDAO
        :param model: IluminacionEntity
        """

        # Atributos
        self._iluminacion_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos_async()

    def _entity_configuration(self) -> IluminacionEntity:
        """ Configura la entidad. """

        ent = IluminacionEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.id_marca = ctrs.combo_marca.value()
        ent.modelo = ctrs.edit_modelo.value()
        ent.num_serie = ctrs.edit_num_serie.value()
        ent.id_tipo_iluminacion = ctrs.combo_tipo_iluminacion.value()
        ent.id_control_iluminacion = ctrs.combo_control_iluminacion.value()
        ent.potencia = ctrs.edit_potencia.value()
        ent.flujo_luminico = ctrs.edit_flujo_luminico.value()
        ent.temperatura = ctrs.edit_temperatura.value()
        ent.vida_util = ctrs.edit_vida_util.value()
        ent.longitud = ctrs.edit_longitud.value()
        ent.anchura = ctrs.edit_anchura.value()

        instalacion = ctrs.fecha_alta.date()
        if instalacion.isValid():
            time_inicio = QDateTime(instalacion, QTime(0, 0))
            ent.fecha_alta = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_alta = None

        baja = ctrs.fecha_baja.date()
        if baja.isValid():
            time_inicio = QDateTime(baja, QTime(0, 0))
            ent.fecha_baja = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_baja = None

        ent.motivo_baja = ctrs.edit_motivo_baja.value()
        ent.espectro_completo = True if (
            ctrs.check_espectro_completo.isChecked()) else False
        ent.intensidad_regulable = True if (
            ctrs.check_intensidad_regulable.isChecked()) else False
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
        res_iluminacion = self._dao.insert(ent)
        if not res_iluminacion.is_success:
            return res_iluminacion

        # Insertamos las fotografías
        res_foto = self._view.frame_image.insert_images(res_iluminacion.value)
        if not res_foto.is_success:
            return res_foto

        return Result.success(res_iluminacion.value)

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
        self._clean_view(self._view.frame.combo_control_iluminacion)

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
        self._clean_view(self._view.frame.combo_control_iluminacion)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valida la marca
        res = IluminacionValidator.validate_marca(
            self._view.frame.combo_marca
        )

        if not res.is_success:
            self._view.frame.combo_marca.setFocus()
            return res

        # Valida el modelo
        res = IluminacionValidator.validate_modelo(
            self._view.frame.edit_modelo
        )

        if not res.is_success:
            self._view.frame.edit_table_model.setFocus()
            return res

        # Valida el número de serie
        res = IluminacionValidator.validate_serial_number(
            self._view.frame.edit_num_serie
        )

        if not res.is_success:
            self._view.frame.edit_num_serie.setFocus()
            return res

        # Valida el tipo de iluminación
        res = IluminacionValidator.validate_tipo_iluminacion(
            self._view.frame.combo_tipo_iluminacion
        )

        if not res.is_success:
            self._view.frame.combo_tipo_iluminacion.setFocus()
            return res

        # Valida la fecha de alta
        res = IluminacionValidator.validate_fecha_alta(
            self._view.frame.fecha_alta
        )

        if not res.is_success:
            self._view.frame.fecha_alta.setFocus()
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
            # Carga el table_model de la fila seleccionada
            selection_model = self._view.data_table.selectionModel()

            # Chequea si se ha seleccionado una fila
            if not selection_model.hasSelection():
                return Result.failure("ANTES DE ELIMINAR UN REGISTRO, DEBES "
                                      "SELECCIONAR UN REGISTRO EN LA TABLA.")

            # Configuramos la fila
            index = selection_model.currentIndex()
            fila = index.row()
            table_model = self._view.data_table.model()

            # Lee los datos del table_model
            id_row = table_model.index(fila, 0).data()
            return Result.success(id_row)
        else:
            return Result.failure("DEBE SELECCIONAR O CARGAR UN REGISTRO")

    def _get_iluminacion(self):
        """ Devuelve el control de iluminación resultante. """

        return self._iluminacion_result

    # ********************************
    # CONTINUA CON LA CARGA DE REGISTRO
    def _load_record(self) -> Result:
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _load_data(self) -> Result:
        # Carga el table_model de la fila seleccionada
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
        self._view.frame.combo_marca.setValue(ent.id_marca)
        self._view.frame.edit_modelo.setValue(ent.modelo)
        self._view.frame.edit_num_serie.setValue(ent.num_serie)
        self._view.frame.combo_tipo_iluminacion.setValue(
            ent.id_tipo_iluminacion)
        self._view.frame.edit_potencia.setValue(ent.potencia)
        self._view.frame.edit_flujo_luminico.setValue(ent.flujo_luminico)
        self._view.frame.edit_temperatura.setValue(ent.temperatura)
        self._view.frame.edit_vida_util.setValue(ent.vida_util)
        self._view.frame.edit_longitud.setValue(ent.longitud)
        self._view.frame.edit_anchura.setValue(ent.anchura)
        self._view.frame.check_intensidad_regulable.setChecked(
            ent.intensidad_regulable)
        self._view.frame.check_espectro_completo.setChecked(
            ent.espectro_completo)
        self._view.frame.fecha_alta.setDate(
            BaseDAO._seconds_to_date(ent.fecha_alta))
        self._view.frame.fecha_baja.setDate(
            BaseDAO._seconds_to_date(ent.fecha_baja))
        self._view.frame.edit_motivo_baja.setValue(ent.motivo_baja)
        self._view.frame.combo_control_iluminacion.setValue(
            ent.id_control_iluminacion)
        self._view.frame.text_descripcion.setValue(ent.descripcion)

        return Result.success(ent.id)

    # ********************************
    # CONTINUA CON LA CARGA DE REGISTRO
    def _fill_combos_async(self):
        """ Llena los combos del formulario"""

        self._load_combo(
            combo=self._view.frame.combo_marca,
            worker_fn=lambda: MarcaComercialDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_tipo_iluminacion,
            worker_fn=lambda: TipoIluminacionDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_control_iluminacion,
            worker_fn=lambda: ControlIluminacionDAO().get_list_combo()
        )

    def _open_marca_comercial_dialog(self):
        """ Abrimos el diálogo de marca comercial. """

        # Configuramos el CONTROLADOR
        view = MarcaComercialDialog("INSERTAR MARCA COMERCIAL")
        dao = MarcaComercialDAO()
        mod = MarcaComercialEntity()

        ctrl = MarcaComercialDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_marca

        self._fill_combo_marca()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_tipo_iluminacion_dialog(self):
        """ Abre el diálogo de tipo iluminación. """

        # Configuramos el CONTROLADOR
        view = TipoIluminacionDialog("INSERTAR TIPO DE ILUMINACIÓN")
        dao = TipoIluminacionDAO()
        mod = TipoIluminacionEntity()

        ctrl = TipoIluminacionDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_tipo_iluminacion

        self._fill_combo_tipo_iluminacion()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_control_iluminacion_dialog(self):
        """ Abre el diálogo de control de iluminación. """

        # Configuramos el CONTROLADOR
        view = ControlIluminacionDialog("INSERTAR CONTROL DE ILUMINACIÓN")
        dao = ControlIluminacionDAO()
        mod = ControlIluminacionEntity()

        ctrl = ControlIluminacionDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_control_iluminacion

        self._fill_combo_control_iluminacion()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _on_text_changed(self):
        """
        Se ejecuta cuando se modifica el texto.
        """

        if self._view.frame.fecha_baja.edit_date.text():
            self._setDisabledControl(
                self._view.frame.layout_motivo_baja, False)
        else:
            self._setDisabledControl(
                self._view.frame.layout_motivo_baja, True)
