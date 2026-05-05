"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  10/04/2026
Comentarios:
    Controlador base de especie vegetal.
"""

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Controllers.dificultad_planta_dialog_controller import \
    DificultadPlantaDialogController
from ModuloMaestro.Controllers.posicion_planta_acuario_dialog_controller import \
    PosicionPlantaAcuarioDialogController
from ModuloMaestro.Controllers.requerimiento_co2_dialog_controller import \
    RequerimientoCO2DialogController
from ModuloMaestro.Controllers.requerimiento_iluminacion_dialog_controller import \
    RequerimientoIluminacionDialogController
from ModuloMaestro.Controllers.tasa_crecimiento_dialog_controller import \
    TasaCrecimientoDialogController
from ModuloMaestro.Model.DAO.dificultad_plantas_dao import DificultadPlantaDAO
from ModuloMaestro.Model.DAO.especie_vegetal_dao import EspecieVegetalDAO
from ModuloMaestro.Model.DAO.posicion_planta_acuario_dao import \
    PosicionPlantaAcuarioDAO
from ModuloMaestro.Model.DAO.requerimiento_co2_dao import RequerimientoCO2DAO
from ModuloMaestro.Model.DAO.requerimiento_iluminacion_dao import \
    RequerimientoIluminacionDAO
from ModuloMaestro.Model.DAO.tasa_crecimiento_dao import TasaCrecimientoDAO
from ModuloMaestro.Model.Entities.dificultad_planta_entity import \
    DificultadPlantaEntity
from ModuloMaestro.Model.Entities.especie_vegetal_entity import \
    EspecieVegetalEntity
from ModuloMaestro.Model.Entities.posicion_planta_acuario_entity import \
    PosicionPlantaAcuarioEntity
from ModuloMaestro.Model.Entities.requerimiento_co2_entity import \
    RequerimientoCO2Entity
from ModuloMaestro.Model.Entities.requerimiento_iluminacion_entity import \
    RequerimientoIluminacionEntity
from ModuloMaestro.Model.Entities.tasa_crecimiento_entity import \
    TasaCrecimientoEntity
from Services.Result.result import Result
from Services.Validators.especie_vegetal_validator import \
    EspecieVegetalValidator
from ModuloMaestro.Views.Dialogs.dificultad_planta_dialog import \
    DificultadPlantaDialog
from ModuloMaestro.Views.Dialogs.especie_vegetal_dialog import \
    EspecieVegetalDialog
from ModuloMaestro.Views.Dialogs.posicion_planta_acuario_dialog import \
    PosicionPlantaAcuarioDialog
from ModuloMaestro.Views.Dialogs.requerimiento_co2_dialog import \
    RequerimientoCO2Dialog
from ModuloMaestro.Views.Dialogs.requerimiento_iluminacon_dialog import \
    RequerimientoIluminacionDialog
from ModuloMaestro.Views.Dialogs.tasa_crecimiento_dialog import \
    TasaCrecimientoDialog
from ModuloMaestro.Views.Masters.especie_vegetal_view import EspecieVegetalView


class EspecieVegetalController(BaseController):
    """
    Controlador base del cuadro de diálogo y formulario maestro de proyecto.
    """

    def __init__(self, view: EspecieVegetalDialog | EspecieVegetalView,
                 dao: EspecieVegetalDAO,
                 model: EspecieVegetalEntity):
        """
        Inicializa el controlador de la urna.
        :param view: EspecieVegetalDialog | EspecieVegetalView
        :param dao: EspecieVegetalDAO
        :param model: EspecieVegetalEntity
        """

        # Atributos
        self._especie_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos_async()

    def _entity_configuration(self) -> EspecieVegetalEntity:
        """ Configura la entidad. """

        ent = EspecieVegetalEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.reino = ctrs.edit_reino.value()
        ent.division = ctrs.edit_division.value()
        ent.clase = ctrs.edit_clase.value()
        ent.orden = ctrs.edit_orden.value()
        ent.familia = ctrs.edit_familia.value()
        ent.genero = ctrs.edit_genero.value()
        ent.especie = ctrs.edit_especie.value()
        ent.nombre_comun = ctrs.edit_n_comun.value()
        ent.ph_min = ctrs.edit_ph_min.value()
        ent.ph_max = ctrs.edit_ph_max.value()
        ent.kh_min = ctrs.edit_kh_min.value()
        ent.kh_max = ctrs.edit_kh_max.value()
        ent.gh_min = ctrs.edit_gh_min.value()
        ent.gh_max = ctrs.edit_gh_max.value()
        ent.temp_min = ctrs.edit_temp_min.value()
        ent.temp_max = ctrs.edit_temp_max.value()
        ent.origen = ctrs.edit_origen.value()
        ent.id_posicion_acuario = ctrs.combo_posicion.value()
        ent.id_req_iluminacion = ctrs.combo_req_iluminacion.value()
        ent.id_req_co2 = ctrs.combo_req_co2.value()
        ent.id_tasa_crecimiento = ctrs.combo_crecimiento.value()
        ent.id_dificultad = ctrs.combo_dificultad.value()
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
        val = self._validate_view()

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

    def _validate_view(self) -> Result:
        """
        Valida el formulario.
        :param val_color: Indica si valida el color.
        :param val_is_mounted: Indica si valida si la urna está montada.
        """

        # Valida el género
        res = EspecieVegetalValidator.validate_genero(
            self._view.frame.edit_genero
        )

        if not res.is_success:
            self._view.frame.edit_genero.setFocus()
            return res

        # Valida la especie
        res = EspecieVegetalValidator.validate_especie(
            self._view.frame.edit_especie
        )

        if not res.is_success:
            self._view.frame.edit_especie.setFocus()
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

    def _get_especie(self):
        """ Devuelve la especie resultante. """

        return self._especie_result

    def _load_record(self):
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos_async(self):
        """ Llena los combos del formulario"""

        self._load_combo(
            combo=self._view.frame.combo_posicion,
            worker_fn=lambda: PosicionPlantaAcuarioDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_req_iluminacion,
            worker_fn=lambda: RequerimientoIluminacionDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_req_co2,
            worker_fn=lambda: RequerimientoCO2DAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_crecimiento,
            worker_fn=lambda: TasaCrecimientoDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_dificultad,
            worker_fn=lambda: DificultadPlantaDAO().get_list_combo()
        )

    def _open_posicion_dialog(self):
        """ Abrimos el diálogo de la posición de la planta en el acuario. """

        # Configuramos el CONTROLADOR
        view = PosicionPlantaAcuarioDialog(
            "INSERTAR POSICIONES DE LAS PLANTAS")
        dao = PosicionPlantaAcuarioDAO()
        mod = PosicionPlantaAcuarioEntity()

        ctrl = PosicionPlantaAcuarioDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_posicion

        self._fill_combo_posicion()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_req_iluminacion_dialog(self):
        """ Abrimos el diálogo del comportamiento de la fauna. """

        # Configuramos el CONTROLADOR
        view = RequerimientoIluminacionDialog("INSERTAR REQUERIMIENTO DE "
                                              "ILUMKINACIÓN")
        dao = RequerimientoIluminacionDAO()
        mod = RequerimientoIluminacionEntity()

        ctrl = RequerimientoIluminacionDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_req_iluminacion

        self._fill_combo_req_iluminacion()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_req_co2_dialog(self):
        """ Abrimos el diálogo del requerimiento de CO2 """

        # Configuramos el CONTROLADOR
        view = RequerimientoCO2Dialog("INSERTAR REQUERIMIENTO DE CO2")
        dao = RequerimientoCO2DAO()
        mod = RequerimientoCO2Entity()

        ctrl = RequerimientoCO2DialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_req_co2

        self._fill_combo_req_co2()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_tasa_crecimiento_dialog(self):
        """ Abrimos el diálogo de tasa de crecimiento. """

        # Configuramos el CONTROLADOR
        view = TasaCrecimientoDialog("INSERTAR TASA DE CRECIMIENTO")
        dao = TasaCrecimientoDAO()
        mod = TasaCrecimientoEntity()

        ctrl = TasaCrecimientoDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_crecimiento

        self._fill_combo_crecimiento()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_dificultad_dialog(self):
        """ Abrimos el diálogo de la dificultad de mantenimiento. """

        # Configuramos el CONTROLADOR
        view = DificultadPlantaDialog("INSERTAR DIFICULTAD DE LA PLANTA")
        dao = DificultadPlantaDAO()
        mod = DificultadPlantaEntity()

        ctrl = DificultadPlantaDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_dificultad

        self._fill_combo_dificultad()
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

        # Obtiene la entidad
        id_ent = modelo.index(fila, 0).data()

        val = self._dao.get_entity_by_id(id_ent)
        if not val.is_success:
            return val

        ent = val.value

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ent) if id_ent is not None else ""
        )
        self._view.frame.edit_reino.setValue(ent.reino)
        self._view.frame.edit_division.setValue(ent.division)
        self._view.frame.edit_clase.setValue(ent.clase)
        self._view.frame.edit_orden.setValue(ent.orden)
        self._view.frame.edit_familia.setValue(ent.familia)
        self._view.frame.edit_genero.setValue(ent.genero)
        self._view.frame.edit_especie.setValue(ent.especie)
        self._view.frame.edit_n_cientifico.setValue(ent.nombre_cientifico)
        self._view.frame.edit_n_comun.setValue(ent.nombre_comun)
        self._view.frame.edit_ph_min.setValue(ent.ph_min)
        self._view.frame.edit_ph_max.setValue(ent.ph_max)
        self._view.frame.edit_kh_min.setValue(ent.kh_min)
        self._view.frame.edit_kh_max.setValue(ent.kh_max)
        self._view.frame.edit_gh_min.setValue(ent.gh_min)
        self._view.frame.edit_gh_max.setValue(ent.gh_max)
        self._view.frame.edit_gh_max.setValue(ent.gh_max)
        self._view.frame.edit_temp_min.setValue(ent.temp_min)
        self._view.frame.edit_temp_max.setValue(ent.temp_max)
        self._view.frame.edit_origen.setValue(ent.origen)
        self._view.frame.combo_posicion.setValue(ent.id_posicion_acuario)
        self._view.frame.combo_req_iluminacion.setValue(ent.id_req_iluminacion)
        self._view.frame.combo_req_co2.setValue(ent.id_req_co2)
        self._view.frame.combo_crecimiento.setValue(ent.id_tasa_crecimiento)
        self._view.frame.combo_dificultad.setValue(ent.id_dificultad)
        self._view.frame.text_descripcion.setValue(ent.descripcion)

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
