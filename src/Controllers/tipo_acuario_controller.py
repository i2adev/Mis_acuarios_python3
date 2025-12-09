from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QPushButton, QMessageBox

from Controllers.base_controller import BaseController
from Controllers.categoria_acuario_dialog_controller import \
    CategoriaAcuarioDialogController
from Controllers.subcategoria_acuario_dialog_controller import \
    SubcategoriaAcuarioDialogController
from Model.DAO.categoria_acuario_dao import CategoriaAcuarioDAO
from Model.DAO.subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Model.Entities.subcategoria_acuario_entity import SubcategoriaAcuarioEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Services.Result.result import Result
from Services.Validators.tipo_acuario_validator import TipoAcuarioValidator
from Views.Dialogs.categoria_acuario_dialog import CategoriaAcuarioDialog
from Views.Dialogs.subcategoria_Acuario_dialog import SubcategoriaAcuarioDialog
from Views.Dialogs.tipo_acuario_dialog import TipoAcuarioDialog
from Views.Masters.tipo_acuario_view import TipoAcuarioView


class TipoAcuarioController(BaseController):
    """ Controlador base del formulario maestro de tipo de filtro. """

    def __init__(self, view: TipoAcuarioDialog | TipoAcuarioView,
                 dao: TipoAcuarioDAO,
                 model: TipoAcuarioEntity):
        """
        Inicializa el controlador de la subcategoría de acuario.
        :param view: TipoAcuarioDialog | TipoAcuarioView
        :param dao: TipoAcuarioDAO
        :param model: TipoAcuarioEntity
        """

        # Atributos
        self._tipo_acuario_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> TipoAcuarioEntity:
        """ Configura la entidad. """

        ent = TipoAcuarioEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.id_categoria_acuario = self._view.frame.combo_categoria_acuario.currentData()
        ent.id_subcategoria_acuario = (self._view.frame
                                       .combo_subcategoria_acuario.currentData())
        ent.observaciones = self._view.frame.text_observaciones.toPlainText()

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
        self._clean_view(self._view.frame.combo_subcategoria_acuario)

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

        # Valida el tipo de acuario
        res = TipoAcuarioValidator.validate_categoria_acuario(
            self._view.frame.combo_subcategoria_acuario
        )

        if not res.is_success:
            self._view.frame.combo_subcategoria_acuario.setFocus()
            return res

        # Valida el subtipo de acuario
        res = TipoAcuarioValidator.ValidateSubcategoriaAcuario(
            self._view.frame.combo_subcategoria_acuario
        )

        if not res.is_success:
            self._view.frame.combo_subcategoria_acuario.setFocus()
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

    def _get_tipo_acuario(self):
        """ Devuelve la categoría de filtro resultante. """

        return self._tipo_acuario_result

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
        id_ta = modelo.index(fila, 0).data()
        categoria = modelo.index(fila, 2).data()  # La columna 1 es el
        # númer correlativo.
        subcategoria = modelo.index(fila, 3).data()
        observaciones = modelo.index(fila, 4).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ta) if id_ta is not None else ""
        )

        self._view.frame.combo_categoria_acuario.setCurrentIndex(
            self._view.frame.combo_categoria_acuario.findText(categoria)
        )

        self._view.frame.combo_subcategoria_acuario.setCurrentIndex(
            self._view.frame.combo_subcategoria_acuario.findText(subcategoria)
        )

        self._view.frame.text_observaciones.setPlainText(
            str(observaciones) if observaciones is not None else ""
        )

        return Result.success(id_ta)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_categoria_acuario()

    def _fill_combo_categoria_acuario(self):
        """ Llena el combo de tipos de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_categoria_acuario.clear()

        # Obtenemos los datos
        dao = CategoriaAcuarioDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE FILTRO'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_categoria_acuario.addItem(ent.categoria,
                                                             ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_categoria_acuario)

        # Deseleccionamos el valor
        self._view.frame.combo_categoria_acuario.setCurrentIndex(-1)

    def _fill_combo_subcategoria_acuario(self, id_ta: int):
        """ Llena el combo de subcategoría de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_subcategoria_acuario.clear()

        # Condiciones de salida
        if id_ta == -1:
            return

        # Obtenemos los datos
        dao = SubcategoriaAcuarioDAO()
        lista = dao.get_list_combo_by_categoria(id_ta)
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'SUBCATEGORÍAS DE ACUARIO'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_subcategoria_acuario.addItem(
                ent.subcategoria, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_categoria_acuario)

        # Deseleccionamos el valor
        self._view.frame.combo_subcategoria_acuario.setCurrentIndex(-1)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_subcategoria_acuario)

    def _combo_categoria_indexchanged(self):
        """ Se ejecuta cuando el índice del combo cambia. """

        # Cuando en el combo categoría se limpia, se limpia a su vez el combo de
        # subcategoría
        if self._view.frame.combo_categoria_acuario.currentIndex() == -1:
            self._view.frame.combo_subcategoria_acuario.clear()
            return

        # Obtenemos el dato a cargar
        data = self._view.frame.combo_categoria_acuario.currentData()

        # Cargamos el combo subcategoría
        self._fill_combo_subcategoria_acuario(data)

    def _open_categoria_acuario_dialog(self):
        """ Abre el diálogo de categoría de acuario. """

        view = CategoriaAcuarioDialog(
            "INSERTAR CATEGORÍA DE ACUARIO"
        )
        mod = CategoriaAcuarioEntity()
        dao = CategoriaAcuarioDAO()

        ctrl = CategoriaAcuarioDialogController(view, dao, mod)
        res = ctrl.show_modal()

        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_categoria_acuario

        self._fill_combos()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_subcategoria_acuario_dialog(self):
        """ Abrimos el diálogo de subcategoria de acuario. """

        # Condiciones de salida
        data = self._view.frame.combo_categoria_acuario.currentData()
        if not data:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                """
                NO HAY NINGUNA CATEGORÍA SELECCIONADA.
                SELECCIONE PRIMERO UNA CATEGFORÍA.
                """
            )
            return

        # Configuramos el CONTROLADOR
        ix_cat = self._view.frame.combo_categoria_acuario.currentIndex()
        view = SubcategoriaAcuarioDialog("INSERTAR SUBCATEGORÍA")
        dao = SubcategoriaAcuarioDAO()
        mod = SubcategoriaAcuarioEntity()

        ctrl = SubcategoriaAcuarioDialogController(view, dao, mod, ix_cat)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_subcategoria_acuario

        self._fill_combo_subcategoria_acuario(data)
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)
