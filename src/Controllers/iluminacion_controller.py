"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  20/12/2025
Comentarios:
    Controlador base del control de iluminación.
"""
from PyQt6.QtCore import QDate, QDateTime, QTime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Controllers.control_iluminacion_dialog_controller import \
    ControlIluminacionDialogController
from Controllers.marca_comercial_dialog_controller import \
    MarcaComercialDialogController
from Controllers.tipo_iluminacion_dialog_controler import \
    TipoIluminacionDialogController
from Model.DAO.control_iluminacion_dao import ControlIluminacionDAO
from Model.DAO.iluminacion_dao import IluminacionDAO
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Model.DAO.tipo_iluminacion_dao import TipoIluminacionDAO
from Model.Entities.control_iluminacion_entity import ControlIluminacionEntity
from Model.Entities.iluminacion_entity import IluminacionEntity
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.Entities.tipo_iluminacion_entity import TipoIluminacionEntity
from Services.Result.result import Result
from Services.Validators.iluminacion_validator import IluminacionValidator
from Views.Dialogs.control_iluminacion_dialog import ControlIluminacionDialog
from Views.Dialogs.iluminacion_dialog import IluminacionDialog
from Views.Dialogs.marca_comercial_dialog import MarcaComercialDialog
from Views.Dialogs.tipo_iluminacion_dialog import TipoIluminacionDialog
from Views.Masters.iluminacion_view import IluminacionView


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

    def _entity_configuration(self) -> IluminacionEntity:
        """ Configura la entidad. """

        ent = IluminacionEntity()
        ctrs = self._view.frame

        # ID
        if ctrs.edit_id.text():
            ent.id = int(ctrs.edit_id.text())
        else:
            ent.id = None

        # Marca
        if ctrs.combo_marca.currentIndex() != -1:
            ent.id_marca = int(ctrs.combo_marca.currentData())
        else:
            ent.id_marca = None

        # Modelo
        if ctrs.edit_modelo.text():
            ent.modelo = ctrs.edit_modelo.text()
        else:
            ent.modelo = None

        # Número de serie
        if ctrs.edit_num_serie.text():
            ent.num_serie = ctrs.edit_num_serie.text()
        else:
            ent.num_serie = None

        # Tipo de iluminación
        if ctrs.combo_tipo_iluminacion.currentIndex() != -1:
            ent.id_tipo_iluminacion = int(
                ctrs.combo_tipo_iluminacion.currentData())
        else:
            ent.id_tipo_iluminacion = None

        # Control de laa iluminación
        if ctrs.combo_control_iluminacion.currentIndex() != -1:
            ent.id_control_iluminacion = int(
                ctrs.combo_control_iluminacion.currentData())
        else:
            ent.id_control_iluminacion = None

        # Potencia de la luminaria
        if ctrs.edit_potencia.text():
            ent.potencia = int(ctrs.edit_potencia.text())
        else:
            ent.potencia = None

        # Flujo luminico
        if ctrs.edit_flujo_luminico.text():
            ent.flujo_luminico = int(ctrs.edit_flujo_luminico.text())
        else:
            ent.flujo_luminico = None

        # Temperatura de color
        if ctrs.edit_temperatura.text():
            ent.temperatura = int(ctrs.edit_temperatura.text())
        else:
            ent.temperatura = None

        # Vida útil de la luminaria
        if ctrs.edit_vida_util.text():
            ent.vida_util = int(ctrs.edit_vida_util.text())
        else:
            ent.vida_util = None

        # Dimensiones: Longitud
        if ctrs.edit_longitud.text():
            ent.longitud = float(ctrs.edit_longitud.text())
        else:
            ent.longitud = None

        # Dimensiones: Anchura
        if ctrs.edit_anchura.text():
            ent.anchura = float(ctrs.edit_anchura.text())
        else:
            ent.anchura = None

        # Fecha de instalación
        instalacion = ctrs.fecha_alta.date()
        if instalacion.isValid():
            time_inicio = QDateTime(instalacion, QTime(0, 0))
            ent.fecha_alta = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_alta = None

        # Fecha de baja
        baja = ctrs.fecha_baja.date()
        if baja.isValid():
            time_inicio = QDateTime(baja, QTime(0, 0))
            ent.fecha_baja = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_baja = None

        # Motivo de la baja
        if ctrs.edit_motivo_baja.text():
            ent.motivo_baja = ctrs.edit_motivo_baja.text()
        else:
            ent.motivo_baja = None

        # Espectro completo
        ent.espectro_completo = 1 if (
            ctrs.check_espectro_completo.isChecked()) else 0

        # Intensidad regulable
        ent.intensidad_regulable = 1 if (
            ctrs.check_intensidad_regulable.isChecked()) else 0

        # Descripción
        ent.descripcion = ctrs.text_descripcion.toPlainText() if (
            ctrs.text_descripcion.toPlainText()) else None

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

        # Valida la potencia de la luminaria
        res = IluminacionValidator.validate_potencia(
            self._view.frame.edit_potencia
        )

        if not res.is_success:
            self._view.frame.edit_potencia.setFocus()
            return res

        # Valida el flujo lumínico
        res = IluminacionValidator.validate_flujo_luminoso(
            self._view.frame.edit_flujo_luminico
        )

        if not res.is_success:
            self._view.frame.edit_flujo_luminico.setFocus()
            return res

        # Valida la temperatura
        res = IluminacionValidator.validate_temperatura(
            self._view.frame.edit_temperatura
        )

        if not res.is_success:
            self._view.frame.edit_temperatura.setFocus()
            return res

        # Valida la longitud
        res = IluminacionValidator.validate_longitud(
            self._view.frame.edit_longitud
        )

        if not res.is_success:
            self._view.frame.edit_longitud.setFocus()
            return res

        # Valida la anchura
        res = IluminacionValidator.validate_anchura(
            self._view.frame.edit_anchura
        )

        if not res.is_success:
            self._view.frame.edit_anchura.setFocus()
            return res

        # Valida la fecha de alta
        res = IluminacionValidator.validate_fecha_alta(
            self._view.frame.fecha_alta
        )

        if not res.is_success:
            self._view.frame.fecha_alta.setFocus()
            return res

        # Valida el motivo de la baja
        res = IluminacionValidator.validate_motivo_baja(
            self._view.frame.edit_motivo_baja
        )

        if not res.is_success:
            self._view.frame.edit_motivo_baja.setFocus()
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
        table_model = self._view.data_table.model()

        # Lee los datos del table_model
        id_ta = table_model.index(fila, 0).data()
        marca = table_model.index(fila, 2).data()
        modelo = table_model.index(fila, 3).data()
        num_serie = table_model.index(fila, 4).data()
        tipo = table_model.index(fila, 5).data()
        potencia = table_model.index(fila, 6).data()
        flujo_luminico = table_model.index(fila, 7).data()
        temperatura = table_model.index(fila, 8).data()
        vida_util = table_model.index(fila, 9).data()
        longitud = table_model.index(fila, 10).data()
        anchura = table_model.index(fila, 11).data()
        control = table_model.index(fila, 12).data()
        regulable = table_model.index(fila, 13).data()
        espectro_completo = table_model.index(fila, 14).data()

        fecha_alta = QDate.fromString(
            str(table_model.index(fila, 15).data()), "dd/MM/yyyy")
        fecha_baja = QDate.fromString(
            str(table_model.index(fila, 16).data()), "dd/MM/yyyy")

        motivo_baja = table_model.index(fila, 17).data()
        descripcion = table_model.index(fila, 18).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ta) if id_ta is not None else ""
        )

        self._view.frame.combo_marca.setCurrentIndex(
            self._view.frame.combo_marca.findText(marca)
        )

        self._view.frame.edit_modelo.setText(
            str(modelo) if modelo is not None else ""
        )

        self._view.frame.edit_num_serie.setText(
            str(num_serie) if num_serie is not None else ""
        )

        self._view.frame.combo_tipo_iluminacion.setCurrentIndex(
            self._view.frame.combo_tipo_iluminacion.findText(tipo)
        )

        self._view.frame.edit_potencia.setText(
            str(potencia) if potencia is not None else ""
        )

        self._view.frame.edit_flujo_luminico.setText(
            str(flujo_luminico) if flujo_luminico is not None else ""
        )

        self._view.frame.edit_temperatura.setText(
            str(temperatura) if temperatura is not None else ""
        )

        self._view.frame.edit_vida_util.setText(
            str(vida_util) if vida_util is not None else ""
        )

        self._view.frame.edit_longitud.setText(
            str(longitud) if longitud is not None else ""
        )

        self._view.frame.edit_anchura.setText(
            str(anchura) if anchura is not None else ""
        )

        self._view.frame.check_intensidad_regulable.setChecked(regulable)
        self._view.frame.check_espectro_completo.setChecked(
            espectro_completo)

        self._view.frame.fecha_alta.setDate(fecha_alta)
        self._view.frame.fecha_baja.setDate(fecha_baja)

        self._view.frame.edit_motivo_baja.setText(
            str(motivo_baja) if motivo_baja is not None else ""
        )

        self._view.frame.combo_control_iluminacion.setCurrentIndex(
            self._view.frame.combo_control_iluminacion.findText(control)
        )

        self._view.frame.text_descripcion.setPlainText(
            str(descripcion) if descripcion is not None else ""
        )

        return Result.success(id_ta)

    # ********************************
    # CONTINUA CON LA CARGA DE REGISTRO
    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_marca()
        self._fill_combo_tipo_iluminacion()
        self._fill_combo_control_iluminacion()
        self._fill_combo_control_iluminacion()

    def _fill_combo_marca(self):
        """ Llena el combo de tipos de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_marca.clear()

        # Obtenemos los datos
        dao = MarcaComercialDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'MARCAS COMERCIALES'."
            )

        # Llena el combo
        for ent in lista.value:
            self._view.frame.combo_marca.addItem(ent.nombre_marca, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_marca)

        # Deselecciona el valor
        self._view.frame.combo_marca.setCurrentIndex(-1)

    def _fill_combo_tipo_iluminacion(self):
        """ Llena el combo del tipo de iluminación. """

        # Vaciamos el combo
        self._view.frame.combo_tipo_iluminacion.clear()

        # Obtenemos los datos
        dao = TipoIluminacionDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE ILUMINACIÓN'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_tipo_iluminacion.addItem(
                ent.tipo_iluminacion,
                ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_tipo_iluminacion)

        # Deselecciona el valor
        self._view.frame.combo_tipo_iluminacion.setCurrentIndex(-1)

    def _fill_combo_control_iluminacion(self):
        """ Llena el combo del tipo de iluminación. """

        # Vaciamos el combo
        self._view.frame.combo_control_iluminacion.clear()

        # Obtenemos los datos
        dao = ControlIluminacionDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE ILUMINACIÓN'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_control_iluminacion.addItem(ent.material,
                                                               ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_control_iluminacion)

        # Deselecciona el valor
        self._view.frame.combo_control_iluminacion.setCurrentIndex(-1)

    def _fill_combo_control_iluminacion(self):
        """ Llena el combo del control de iluminación. """

        # Vaciamos el combo
        self._view.frame.combo_control_iluminacion.clear()

        # Obtenemos los datos
        dao = ControlIluminacionDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'CONTROLES DE ILUMINACIÓN'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_control_iluminacion.addItem(
                ent.control_iluminacion,
                ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_control_iluminacion)

        # Deselecciona el valor
        self._view.frame.combo_control_iluminacion.setCurrentIndex(-1)

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
