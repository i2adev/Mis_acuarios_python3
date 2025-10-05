"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  05/10/2025
Commentarios:
    Controlador base de la subcategoría de acuario.
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from base_controller import BaseController
from categoria_acuario_dao import CategoriaAcuarioDAO
from result import Result
from subcategoria_Acuario_dialog import SubcategoriaAcuarioDialog
from subcategoria_acuario_dao import SubcategoriaAcuarioDAO
from subcategoria_acuario_entity import SubcategoriaAcuarioEntity
from subcategoria_acuario_validator import SubcategoriaAcuarioValidator
from subcategoria_acuario_view import SubcategoriaAcuarioView


class SubcategoriaAcuarioController(BaseController):
    """ Controlador base del formulario maestro de tipo de filtro. """

    def __init__(self, view: SubcategoriaAcuarioDialog | SubcategoriaAcuarioView,
                 dao: SubcategoriaAcuarioDAO,
                 model: SubcategoriaAcuarioEntity):
        """
        Inicializa el controlador de la subcategoría de acuario.
        :param view: SubcategoriaAcuarioDialog | SubcategoriaAcuarioView
        :param dao: SubcategoriaAcuarioDAO
        :param model: SubcategoriaAcuarioEntity
        """

        # Atributos
        self._subcategoria_acuario_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> SubcategoriaAcuarioEntity:
        """ Configura la entidad. """

        ent = SubcategoriaAcuarioEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.id_categoria = self._view.frame.combo_categoria_acuario.currentData()
        ent.subcategoria = self._view.frame.edit_subcategoria_acuario.text()
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
        self._clean_view(self._view.frame.combo_categoria_acuario)

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

        # Valida la categoría de acuario
        val = SubcategoriaAcuarioValidator.validate_categoria_acuario(
            self._view.frame.combo_categoria_acuario
        )

        if not val.is_success:
            self._view.frame.combo_categoria_acuario.setFocus()
            return val

        # Valida la subcategoría de acuario
        val = SubcategoriaAcuarioValidator.validate_subcategoria_acuario(
            self._view.frame.edit_subcategoria_acuario
        )

        if not val.is_success:
            self._view.frame.edit_subcategoria_acuario.setFocus()
            return val

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

    def _get_subcategoria_acuario(self):
        """ Devuelve la categoría de filtro resultante. """

        return self._subcategoria_acuario_result

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
        id_cat = modelo.index(fila, 0).data()
        categoria = modelo.index(fila, 2).data()  # La columna 1 es el
                                                    # númer correlativo.
        subcategoria = modelo.index(fila, 3).data()
        observaciones = modelo.index(fila, 4).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_cat) if id_cat is not None else ""
        )

        self._view.frame.edit_subcategoria_acuario.setText(
            str(subcategoria) if categoria is not None else ""
        )

        self._view.frame.combo_categoria_acuario.setCurrentIndex(
            self._view.frame.combo_categoria_acuario.findText(categoria)
        )

        self._view.frame.text_observaciones.setPlainText(
            str(observaciones) if observaciones is not None else ""
        )

        return Result.success(id_cat)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_categoria_acuario()

    def _fill_categoria_acuario(self):
        """ Llena el combo. """

        # Vaciamos el combo
        self._view.frame.combo_categoria_acuario.clear()

        # Obtenemos los datos
        dao = CategoriaAcuarioDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'CATEGORÍAS DE ACUARIO'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_categoria_acuario.addItem(ent.categoria, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_categoria_acuario)

        # Deseleccionamos el valor
        self._view.frame.combo_categoria_acuario.setCurrentIndex(-1)