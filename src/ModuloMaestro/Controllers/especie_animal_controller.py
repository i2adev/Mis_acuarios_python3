"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  23/03/2026
Comentarios:
    Controlador base de especie animal.
"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Controllers.comportamiento_fauna_dialog_controller import \
    ComportamientoFaunaDialogController
from ModuloMaestro.Controllers.dieta_fauna_dialog_controller import \
    DietaFaunaDialogController
from ModuloMaestro.Controllers.grupo_taxonómico_dialog_controller import \
    GrupoTaxonomicoDialogController
from ModuloMaestro.Controllers.nivel_nado_dialog_controller import \
    NivelNadoDialogController
from ModuloMaestro.Model.DAO.comportamiento_fauna_dao import \
    ComportamientoFaunaDAO
from ModuloMaestro.Model.DAO.dieta_fauna_dao import DietaFaunaDAO
from ModuloMaestro.Model.DAO.especie_animal_dao import EspecieAnimalDAO
from ModuloMaestro.Model.DAO.grupo_taxonomico_dao import GrupoTaxonomicoDAO
from ModuloMaestro.Model.DAO.niveles_nado_dao import NivelNadoDAO
from ModuloMaestro.Model.Entities.comprtamiento_fauna_entity import \
    ComportamientoFaunaEntity
from ModuloMaestro.Model.Entities.dieta_fauna_entity import DietaFaunaEntity
from ModuloMaestro.Model.Entities.especie_animal_entity import \
    EspecieAnimalEntity
from ModuloMaestro.Model.Entities.grupo_taxonomico_entity import \
    GrupoTaxonomicoEntity
from ModuloMaestro.Model.Entities.nivel_nado_entity import NivelNadoEntity
from Services.Result.result import Result
from Services.Validators.especie_animal_validator import EspecieAnimalValidator
from ModuloMaestro.Views.Dialogs.comportamiento_fauna_dialog import \
    ComportamientoFaunaDialog
from ModuloMaestro.Views.Dialogs.dieta_fauna_dialog import DietaFaunaDialog
from ModuloMaestro.Views.Dialogs.especie_animal_dialog import \
    EspecieAnimalDialog
from ModuloMaestro.Views.Dialogs.grupo_taxonomico_dialog import \
    GrupoTaxonomicoDialog
from ModuloMaestro.Views.Dialogs.nivel_nado_dialog import NivelNadoDialog
from ModuloMaestro.Views.Masters.especie_animal_view import EspecieAnimalView


class EspecieAnimalController(BaseController):
    """
    Controlador base del cuadro de diálogo y formulario maestro de proyecto.
    """

    def __init__(self, view: EspecieAnimalDialog | EspecieAnimalView,
                 dao: EspecieAnimalDAO,
                 model: EspecieAnimalEntity):
        """
        Inicializa el controlador de la urna.
        :param view: EspecieAnimalDialog | EspecieAnimalView
        :param dao: EspecieAnimalDAO
        :param model: EspecieAnimalEntity
        """

        # Atributos
        self._especie_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos_async()

    def _entity_configuration(self) -> EspecieAnimalEntity:
        """ Configura la entidad. """

        ent = EspecieAnimalEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.reino = ctrs.edit_reino.value()
        ent.filo = ctrs.edit_filo.value()
        ent.clase = ctrs.edit_clase.value()
        ent.orden = ctrs.edit_orden.value()
        ent.familia = ctrs.edit_familia.value()
        ent.genero = ctrs.edit_genero.value()
        ent.especie = ctrs.edit_especie.value()
        ent.nombre_comun = ctrs.edit_n_comun.value()
        ent.es_hibrida = True if ctrs.check_hibrida.isChecked() else False
        ent.nombre_especie_hibrida = ctrs.edit_n_e_hibrida.value()
        ent.id_grupo_taxonomico = ctrs.combo_grupo_taxo.value()
        ent.ph_min = ctrs.edit_ph_min.value()
        ent.ph_max = ctrs.edit_ph_max.value()
        ent.kh_min = ctrs.edit_kh_min.value()
        ent.kh_max = ctrs.edit_kh_max.value()
        ent.gh_min = ctrs.edit_gh_min.value()
        ent.gh_max = ctrs.edit_gh_max.value()
        ent.temp_min = ctrs.edit_temp_min.value()
        ent.temp_max = ctrs.edit_temp_max.value()
        ent.origen = ctrs.edit_origen.value()
        ent.tamano_cm = ctrs.edit_tamano.value()
        ent.id_comportamiento = ctrs.combo_comportamiento.value()
        ent.id_dieta = ctrs.combo_dieta.value()
        ent.id_nivel_nado = ctrs.combo_nivel_nado.value()
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
        res = EspecieAnimalValidator.validate_genero(
            self._view.frame.edit_genero
        )

        if not res.is_success:
            self._view.frame.edit_genero.setFocus()
            return res

        # Valida la especie
        res = EspecieAnimalValidator.validate_especie(
            self._view.frame.edit_especie
        )

        if not res.is_success:
            self._view.frame.edit_especie.setFocus()
            return res

        # Valida el grupo taxonómico
        res = EspecieAnimalValidator.validate_grupo_taxonomico(
            self._view.frame.combo_grupo_taxo
        )

        if not res.is_success:
            self._view.frame.combo_grupo_taxo.setFocus()
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
            combo=self._view.frame.combo_grupo_taxo,
            worker_fn=lambda: GrupoTaxonomicoDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_comportamiento,
            worker_fn=lambda: ComportamientoFaunaDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_dieta,
            worker_fn=lambda: DietaFaunaDAO().get_list_combo()
        )

        self._load_combo(
            combo=self._view.frame.combo_nivel_nado,
            worker_fn=lambda: NivelNadoDAO().get_list_combo()
        )

    def _open_grupo_taxo_dialog(self):
        """ Abrimos el diálogo del grupo taxonómico. """

        # Configuramos el CONTROLADOR
        view = GrupoTaxonomicoDialog("INSERTAR GRUPO TAXONÓMICO")
        dao = GrupoTaxonomicoDAO()
        mod = GrupoTaxonomicoEntity()

        ctrl = GrupoTaxonomicoDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_grupo_taxo

        self._fill_combo_grupo_taxo()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_comportamiento_dialog(self):
        """ Abrimos el diálogo del comportamiento de la fauna. """

        # Configuramos el CONTROLADOR
        view = ComportamientoFaunaDialog("INSERTAR COMPORTAMIENTO DE FAUNA")
        dao = ComportamientoFaunaDAO()
        mod = ComportamientoFaunaEntity()

        ctrl = ComportamientoFaunaDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_comportamiento

        self._fill_combo_comportamiento()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_dieta_dialog(self):
        """ Abrimos el diálogo de la dieta de la fauna. """

        # Configuramos el CONTROLADOR
        view = DietaFaunaDialog("INSERTAR DIETA DE FAUNA")
        dao = DietaFaunaDAO()
        mod = DietaFaunaEntity()

        ctrl = DietaFaunaDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_dieta

        self._fill_combo_dieta()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_nivel_nado_dialog(self):
        """ Abrimos el diálogo del nivel de nado de los peces. """

        # Configuramos el CONTROLADOR
        view = NivelNadoDialog("INSERTAR NIVEL DE NADO")
        dao = NivelNadoDAO()
        mod = NivelNadoEntity()

        ctrl = NivelNadoDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_nivel_nado

        self._fill_combo_nivel_nado()
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
        self._view.frame.edit_id.setValue(ent.id)
        self._view.frame.edit_reino.setValue(ent.reino)
        self._view.frame.edit_filo.setValue(ent.filo)
        self._view.frame.edit_clase.setValue(ent.clase)
        self._view.frame.edit_orden.setValue(ent.orden)
        self._view.frame.edit_familia.setValue(ent.familia)
        self._view.frame.edit_genero.setValue(ent.genero)
        self._view.frame.edit_especie.setValue(ent.especie)
        self._view.frame.edit_n_cientifico.setValue(ent.nombre_cientifico)
        self._view.frame.edit_n_comun.setValue(ent.nombre_comun)
        self._view.frame.check_hibrida.setChecked(ent.es_hibrida)
        self._view.frame.edit_n_e_hibrida.setValue(ent.nombre_especie_hibrida)
        self._view.frame.combo_grupo_taxo.setValue(ent.id_grupo_taxonomico)
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
        self._view.frame.edit_tamano.setValue(ent.tamano_cm)
        self._view.frame.combo_comportamiento.setValue(ent.id_comportamiento)
        self._view.frame.combo_dieta.setValue(ent.id_dieta)
        self._view.frame.combo_nivel_nado.setValue(ent.id_nivel_nado)
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

    def _check_state_changed(self, state):
        """ Se ejecuta cuando el estado del checkbox cambia"""

        if state == Qt.CheckState.Checked.value:
            self._setDisabledControl(self._view.frame.layout_n_e_hibrida,
                                     False)
        else:
            self._setDisabledControl(self._view.frame.layout_n_e_hibrida,
                                     True)
