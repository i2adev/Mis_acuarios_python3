"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  11/03/2026
Comentarios:
    Controlador base de consumible.
"""
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Controllers.categoria_consumible_dialog_controller import \
    CategoriaConsumibleDialogController
from Controllers.formato_consumible_dialog_controller import \
    FormatoConsumibleDialogController
from Controllers.marca_comercial_dialog_controller import \
    MarcaComercialDialogController
from Controllers.unidad_contenido_dialog_controller import \
    UnidadContenidoDialogController
from Model.DAO.categoria_consumible_dao import CategoriaConsumibleDAO
from Model.DAO.consumible_dao import ConsumibleDAO
from Model.DAO.formato_consumible_dao import FormatoConsumibleDAO
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Model.DAO.unidad_contenido_dao import UnidadContenidoDAO
from Model.Entities.categoria_consumible_entity import \
    CategoriaConsumibleEntity
from Model.Entities.consumible_entity import ConsumibleEntity
from Model.Entities.formato_consumible_entity import FormatoConsumibleEntity
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.Entities.unidad_contenido_entity import UnidadContenidoEntity
from Services.Result.result import Result
from Services.Validators.consumible_validator import ConsumibleValidator
from Views.Dialogs.categoria_consumible_dialog import CategoriaConsumibleDialog
from Views.Dialogs.consumible_dialogo import ConsumibleDialog
from Views.Dialogs.formato_consumible_dialog import FormatoConsumibleDialog
from Views.Dialogs.marca_comercial_dialog import MarcaComercialDialog
from Views.Dialogs.unidad_contenido_dialog import UnidadContenidoDialog
from Views.Masters.consumible_view import ConsumibleView


class ConsumibleController(BaseController):
    """ 
    Controlador base del cuadro de diálogo y formulario maestro de consumible. 
    """

    def __init__(self, view: ConsumibleDialog | ConsumibleView,
                 dao: ConsumibleDAO,
                 model: ConsumibleEntity):
        """
        Inicializa el controlador de la urna.
        :param view: ConsumibleDialog | ConsumibleView
        :param dao: ConsumibleDAO
        :param model: ConsumibleEntity
        """

        # Atributos
        self._consumible_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos()

    def _entity_configuration(self) -> ConsumibleEntity:
        """ Configura la entidad. """

        ent = ConsumibleEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.id_marca = ctrs.combo_marca.value()
        ent.producto = ctrs.edit_producto.value()
        ent.id_categoria = ctrs.combo_categoria.value()
        ent.id_formato = ctrs.combo_formato.value()
        ent.contenido = ctrs.edit_contenido.value()
        ent.id_unidad = ctrs.combo_unidad.value()
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
        """

        # Valida la marca
        res = ConsumibleValidator.validate_marca(self._view.frame.combo_marca)

        if not res.is_success:
            self._view.frame.combo_marca.setFocus()
            return res

        # Valida el producto
        res = ConsumibleValidator.validate_producto(
            self._view.frame.edit_producto
        )

        if not res.is_success:
            self._view.frame.edit_producto.setFocus()
            return res

        # Valida el contenido
        res = ConsumibleValidator.validate_contenido(
            self._view.frame.edit_contenido
        )

        if not res.is_success:
            self._view.frame.edit_contenido.setFocus()
            return res

        # Valida la unidad
        res = ConsumibleValidator.validate_unidad(
            self._view.frame.combo_unidad
        )

        if not res.is_success:
            self._view.frame.combo_unidad.setFocus()
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

    def _get_consumible(self):
        """ Devuelve el consumible resultante. """

        return self._consumible_result

    def _load_record(self):
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_marca()
        self._fill_combo_categoria()
        self._fill_combo_formato()
        self._fill_combo_unidad()

    def _fill_combo_formato(self):
        """ Llena el combo de los formatos. """

        # Vaciamos el combo
        self._view.frame.combo_formato.clear()

        # Obtenemos los datos
        dao = FormatoConsumibleDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'FORMATOS DE CONSUMIBLE'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_formato.addItem(
                ent.formato, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_formato)

        # Deselecciona el valor
        self._view.frame.combo_formato.setCurrentIndex(-1)

    def _fill_combo_unidad(self):
        """ Llena el combo de las unidades de contenido. """

        # Vaciamos el combo
        self._view.frame.combo_unidad.clear()

        # Obtenemos los datos
        dao = UnidadContenidoDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'UNIDADES DE CONTENIDO'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_unidad.addItem(
                ent.unidad, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_unidad)

        # Deselecciona el valor
        self._view.frame.combo_unidad.setCurrentIndex(-1)

    def _fill_combo_marca(self):
        """ Llena el combo de la marca. """

        # Vaciamos el combo
        self._view.frame.combo_marca.clear()

        # Obtenemos los datos
        dao = MarcaComercialDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'MARCAS'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_marca.addItem(
                ent.nombre_marca, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_marca)

        # Deselecciona el valor
        self._view.frame.combo_marca.setCurrentIndex(-1)

    def _fill_combo_categoria(self):
        """ Llena el combo la categoría del consumible. """

        # Vaciamos el combo
        self._view.frame.combo_categoria.clear()

        # Obtenemos los datos
        dao = CategoriaConsumibleDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'CATEGORÍAS DE CONSUMIBLE'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_categoria.addItem(
                ent.categoria, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_categoria)

        # Deselecciona el valor
        self._view.frame.combo_categoria.setCurrentIndex(-1)

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
        self._view.frame.combo_marca.setValue(ent.id_marca)
        self._view.frame.edit_producto.setValue(ent.producto)
        self._view.frame.combo_categoria.setValue(ent.id_categoria)
        self._view.frame.combo_formato.setValue(ent.id_formato)
        self._view.frame.edit_contenido.setValue(ent.contenido)
        self._view.frame.combo_unidad.setValue(ent.id_unidad)
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

    def _open_marca_dialog(self):
        """ Abrimos el diálogo de marca. """

        # Configuramos el CONTROLADOR
        view = MarcaComercialDialog("INSERTAR MARCA")
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

    def _open_categoria_dialog(self):
        """ Abrimos el diálogo de categoría. """

        # Configuramos el CONTROLADOR
        view = CategoriaConsumibleDialog("INSERTAR CATEGORÍA DE CONSUMIBLE")
        dao = CategoriaConsumibleDAO()
        mod = CategoriaConsumibleEntity()

        ctrl = CategoriaConsumibleDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_categoria

        self._fill_combo_categoria()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_formato_dialog(self):
        """ Abrimos el diálogo de formato de consumible. """

        # Configuramos el CONTROLADOR
        view = FormatoConsumibleDialog("INSERTAR FORMATO DE CONSUMIBLE")
        dao = FormatoConsumibleDAO()
        mod = FormatoConsumibleEntity()

        ctrl = FormatoConsumibleDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_formato

        self._fill_combo_formato()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_unidad_dialog(self):
        """ Abrimos el diálogo de unidad de contenido. """

        # Configuramos el CONTROLADOR
        view = UnidadContenidoDialog("INSERTAR UNIDAD DE CONTENIDO")
        dao = UnidadContenidoDAO()
        mod = UnidadContenidoEntity()

        ctrl = UnidadContenidoDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_unidad

        self._fill_combo_unidad()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)
