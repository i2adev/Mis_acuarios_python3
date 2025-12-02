"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  07/10/2025
Comentarios:
    Controlador base de urna.
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Views.Dialogs.marca_comercial_dialog import MarcaComercialDialog
from Controllers.marca_comercial_dialog_controller import \
    MarcaComercialDialogController
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.DAO.material_urna_dao import MaterialUrnaDAO
from Views.Dialogs.material_urna_dialog import MaterialUrnaDialog
from Controllers.material_urna_dialog_controller import \
    MaterialUrnaDialogController
from Model.Entities.material_urna_entity import MaterialUrnaEntity
from Services.Result.result import Result
from Model.DAO.urna_dao import UrnaDAO
from Views.Dialogs.urna_dialog import UrnaDialog
from Model.Entities.urna_entity import UrnaEntity
from Services.Validators.urna_validator import UrnaValidator
from Views.Masters.urna_view import UrnaView


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

        # Llenamo los combos
        self._fill_combos()

    def _entity_configuration(self) -> UrnaEntity:
        """ Configura la entidad. """

        ent = UrnaEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.id_marca = self._view.frame.combo_marca.currentData()
        ent.modelo = self._view.frame.edit_modelo.text()
        ent.anchura = self._view.frame.edit_ancho.text()
        ent.profundidad = self._view.frame.edit_profundo.text()
        ent.altura = self._view.frame.edit_alto.text()
        ent.grosor_cristal = self._view.frame.edit_grosor.text()
        ent.volumen_tanque = self._view.frame.edit_volumen.text()
        ent.id_material = (self._view.frame.combo_material.currentData())
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

        # Valida la anchura de la urna
        res = UrnaValidator.validate_anchura(
            self._view.frame.edit_ancho
        )

        if not res.is_success:
            self._view.frame.edit_ancho.setFocus()
            return res

        # Valida la profundidad de la urna
        res = UrnaValidator.validate_profundidad(
            self._view.frame.edit_profundo
        )

        if not res.is_success:
            self._view.frame.edit_profundo.setFocus()
            return res

        # Valida la altura de la urna
        res = UrnaValidator.validate_altura(
            self._view.frame.edit_alto
        )

        if not res.is_success:
            self._view.frame.edit_alto.setFocus()
            return res

        # Válida el grosor del cristal
        res = UrnaValidator.validate_grosor(
            self._view.frame.edit_grosor
        )

        if not res.is_success:
            self._view.frame.edit_grosor.setFocus()
            return res

        # Válida el volumen del tanque
        res = UrnaValidator.validate_volumen(
            self._view.frame.edit_volumen
        )

        if not res.is_success:
            self._view.frame.edit_volumen.setFocus()
            return res

        # Válida el volumen del tanque
        res = UrnaValidator.validate_volumen(
            self._view.frame.edit_volumen
        )

        if not res.is_success:
            self._view.frame.edit_volumen.setFocus()
            return res

        # Valida el material de la urna
        res = UrnaValidator.validate_material(
            self._view.frame.combo_material
        )

        if not res.is_success:
            self._view.frame.combo_material.setFocus()
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

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_marca.addItem(ent.nombre_marca, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_marca)

        # Deseleccionamos el valor
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

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_material.addItem(ent.material, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_material)

        # Deseleccionamos el valor
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

        # Lee los datos del modelo
        id_ent = modelo.index(fila, 0).data()
        marca = modelo.index(fila,
                             2).data()  # La columna 1 es el nº correlativo.
        modelo_urna = modelo.index(fila, 3).data()
        ancho = modelo.index(fila, 4).data()
        profundo = modelo.index(fila, 5).data()
        alto = modelo.index(fila, 6).data()
        grosor = modelo.index(fila, 7).data()
        volumen = modelo.index(fila, 8).data()
        material = modelo.index(fila, 9).data()
        descripcion = modelo.index(fila, 10).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ent) if id_ent is not None else ""
        )
        self._view.frame.combo_marca.setCurrentIndex(
            self._view.frame.combo_marca.findText(marca)
        )
        self._view.frame.edit_modelo.setText(
            str(modelo_urna) if modelo_urna is not None else ""
        )
        self._view.frame.edit_ancho.setText(
            str(ancho) if ancho is not None else ""
        )
        self._view.frame.edit_profundo.setText(
            str(profundo) if profundo is not None else ""
        )
        self._view.frame.edit_alto.setText(
            str(alto) if alto is not None else ""
        )
        self._view.frame.edit_grosor.setText(
            str(grosor) if grosor is not None else ""
        )
        self._view.frame.edit_volumen.setText(
            str(volumen) if volumen is not None else ""
        )
        self._view.frame.combo_material.setCurrentIndex(
            self._view.frame.combo_material.findText(material)
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
