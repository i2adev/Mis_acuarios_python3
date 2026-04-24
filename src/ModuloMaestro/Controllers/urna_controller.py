"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  07/10/2025
Comentarios:
    Controlador base de urna.
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Controllers.marca_comercial_dialog_controller import \
    MarcaComercialDialogController
from ModuloMaestro.Controllers.material_urna_dialog_controller import \
    MaterialUrnaDialogController
from ModuloMaestro.Model.DAO.marca_comercial_dao import MarcaComercialDAO
from ModuloMaestro.Model.DAO.material_urna_dao import MaterialUrnaDAO
from ModuloMaestro.Model.DAO.urna_dao import UrnaDAO
from ModuloMaestro.Model.Entities.marca_comercial_entity import \
    MarcaComercialEntity
from ModuloMaestro.Model.Entities.material_urna_entity import \
    MaterialUrnaEntity
from ModuloMaestro.Model.Entities.urna_entity import UrnaEntity
from Services.Result.result import Result
from Services.Validators.urna_validator import UrnaValidator
from ModuloMaestro.Views.Dialogs.marca_comercial_dialog import \
    MarcaComercialDialog
from ModuloMaestro.Views.Dialogs.material_urna_dialog import MaterialUrnaDialog
from ModuloMaestro.Views.Dialogs.urna_dialog import UrnaDialog
from ModuloMaestro.Views.Masters.urna_view import UrnaView


class UrnaController(BaseController):
    """ Controlador base del cuadro de diálogo y formulario maestro de urna. """

    def __init__(self, view: UrnaDialog | UrnaView,
                 dao: UrnaDAO,
                 model: UrnaEntity):
        """
        Inicializa el controlador de la urna.
        :param view: UrnaDialog | UrnaView
        :param dao: UrnaDAO
        :param model: UrnaEntity
        """

        # Atributos
        self._urna_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llena los combos
        self._fill_combos()

    def _entity_configuration(self) -> UrnaEntity:
        """ Configura la entidad. """

        ent = UrnaEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.id_marca = ctrs.combo_marca.value()
        ent.modelo = ctrs.edit_modelo.value()
        ent.anchura = ctrs.edit_ancho.value()
        ent.profundidad = ctrs.edit_profundo.value()
        ent.altura = ctrs.edit_alto.value()
        ent.grosor_cristal = ctrs.edit_grosor.value()
        ent.volumen_tanque = ctrs.edit_volumen.value()
        ent.id_material = ctrs.combo_material.value()
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

        # Valida la marca
        res = UrnaValidator.validate_marca(
            self._view.frame.combo_marca
        )

        if not res.is_success:
            self._view.frame.combo_marca.setFocus()
            return res

        # Valida el modelo de la urna
        res = UrnaValidator.validate_modelo_urna(
            self._view.frame.edit_modelo
        )

        if not res.is_success:
            self._view.frame.edit_modelo.setFocus()
            return res

        # Valida el material de la urna
        res = UrnaValidator.validate_material(
            self._view.frame.combo_material
        )

        if not res.is_success:
            self._view.frame.combo_material.setFocus()
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

    def _get_urna(self):
        """ Devuelve la categoría de filtro resultante. """

        return self._urna_result

    def _load_record(self) -> Result:
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_marca()
        self._fill_combo_material()

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

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_marca.addItem(ent.nombre_marca, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_marca)

        # Deselecciona el valor
        self._view.frame.combo_marca.setCurrentIndex(-1)

    def _fill_combo_material(self):
        """ Llena el combo del material de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_material.clear()

        # Obtenemos los datos
        dao = MaterialUrnaDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'MATERIALES DE URNA'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_material.addItem(ent.material, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_material)

        # Deselecciona el valor
        self._view.frame.combo_material.setCurrentIndex(-1)

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

    def _open_material_urna_dialog(self):
        """ Abrimos el diálogo de categoria de acuario. """

        view = MaterialUrnaDialog(
            "INSERTAR MATERIAL DE URNA"
        )
        mod = MaterialUrnaEntity()
        dao = MaterialUrnaDAO()

        ctrl = MaterialUrnaDialogController(view, dao, mod)
        res = ctrl.show_modal()

        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_material

        self._fill_combo_material()
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
        self._view.frame.edit_ancho.setValue(ent.anchura)
        self._view.frame.edit_profundo.setValue(ent.profundidad)
        self._view.frame.edit_alto.setValue(ent.alto)
        self._view.frame.edit_grosor.setValue(ent.grosor)
        self._view.frame.edit_volumen.setValue(ent.volumen)
        self._view.frame.combo_material.setValue(ent.id_material)
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
