"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  01/10/2025
Comentarios:
    Controlador base del tipo de filtro.
"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Model.DAO.pais_dao import PaisDAO
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Services.Result.result import Result
from Services.Validators.marca_comercial_validator import \
    MarcaComercialValidator
from Views.Dialogs.marca_comercial_dialog import MarcaComercialDialog
from Views.Masters.marca_comercial_view import MarcaComercialView


class MarcaComercialController(BaseController):
    """ Controlador base del formulario maestro de tipo de filtro. """

    def __init__(self, view: MarcaComercialDialog | MarcaComercialView,
                 dao: MarcaComercialDAO,
                 model: MarcaComercialEntity):
        """
        Inicializa el controlador de tipo de filtro.
        :param view: MarcaComercialDialog | MarcaComercialView
        :param dao: MarcaComercialDAO
        :param model: MarcaComercialEntity
        """

        # Atributos
        self._marca_comercial_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

    def _entity_configuration(self) -> MarcaComercialEntity:
        """ Configura la entidad. """

        ent = MarcaComercialEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.nombre_marca = ctrs.edit_marca.value()
        ent.direccion = ctrs.edit_direccion.value()
        ent.cod_postal = ctrs.edit_cod_postal.value()
        ent.poblacion = ctrs.edit_poblacion.value()
        ent.provincia = ctrs.edit_provincia.value()
        ent.id_pais = ctrs.combo_pais.value()
        ent.observaciones = ctrs.text_observaciones.value()

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
        self._clean_view(self._view.frame.edit_marca)

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
        val = MarcaComercialValidator.validate_marca(
            self._view.frame.edit_marca
        )

        if not val.is_success:
            self._view.frame.edit_marca.setFocus()
            return val

        # Valida el país
        val = MarcaComercialValidator.validate_pais(
            self._view.frame.combo_pais
        )

        if not val.is_success:
            self._view.frame.combo_pais.setFocus()
            return val

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

    def _get_marca_comercial(self):
        """ Devuelve la categoría de filtro resultante. """

        return self._marca_comercial_result

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

        # Obtenemos la entidad
        id_ent = modelo.index(fila, 0).data()

        val = self._dao.get_entity_by_id(id_ent)
        if not val.is_success:
            return val

        ent = val.value

        # Cargamos los widgets
        self._view.frame.edit_id.setValue(ent.id)
        self._view.frame.edit_marca.setValue(ent.nombre_marca)
        self._view.frame.edit_direccion.setValue(ent.direccion)
        self._view.frame.edit_cod_postal.setValue(ent.cod_postal)
        self._view.frame.edit_poblacion.setValue(ent.poblacion)
        self._view.frame.edit_provincia.setValue(ent.provincia)
        self._view.frame.combo_pais.setValue(ent.id_pais)
        self._view.frame.text_observaciones.setValue(ent.observaciones)

        return Result.success(ent.id)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_pais()

    def _fill_combo_pais(self):
        """ Llena el combo de paises. """

        # Vaciamos el combo
        self._view.frame.combo_pais.clear()

        # Obtenemos los datos
        dao = PaisDAO()
        lista = dao.get_list_combo()
        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'PAISES'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_pais.addItem(ent.pais, ent.id)

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_pais)

        # Deselecciona el valor
        self._view.frame.combo_pais.setCurrentIndex(-1)
