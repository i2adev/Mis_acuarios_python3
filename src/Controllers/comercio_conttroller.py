"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  19/12/2025
Comentarios:
    Controlador base del comercio.
"""

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Controllers.base_controller import BaseController
from Model.DAO.comercio_dao import ComercioDAO
from Model.DAO.pais_dao import PaisDAO
from Model.Entities.comercio_entity import ComercioEntity
from Services.Result.result import Result
from Services.Validators.comercio_validator import ComercioValidator
from Views.Dialogs.comercio_dialog import ComercioDialog
from Views.Masters.comercio_view import ComercioView


class ComercioController(BaseController):
    """ Controlador base del formulario de comercio. """

    def __init__(self, view: ComercioDialog | ComercioView,
                 dao: ComercioDAO,
                 model: ComercioEntity):
        """
        Inicializa el controlador de tipo de filtro.
        :param view: ComercioDialog | ComercioView
        :param dao: ComercioDAO
        :param model: ComercioEntity
        """

        # Atributos
        self._comercio_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos()

    def _entity_configuration(self) -> ComercioEntity:
        """ Configura la entidad. """

        ent = ComercioEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.nombre_comercio = self._view.frame.edit_comercio.text()
        ent.direccion = self._view.frame.edit_direccion.text()
        ent.cod_postal = self._view.frame.edit_cod_postal.text()
        ent.poblacion = self._view.frame.edit_poblacion.text()
        ent.provincia = self._view.frame.edit_provincia.text()
        ent.id_pais = int(self._view.frame.combo_pais.currentData())
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
        self._clean_view(self._view.frame.edit_comercio)

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
        self._clean_view(self._view.frame.edit_comercio)
        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self) -> Result:
        """ Valida el formulario. """

        # Valída el nombre del comercio
        res = ComercioValidator.validate_comercio(
            self._view.frame.edit_comercio
        )

        if not res.is_success:
            self._view.frame.edit_comercio.setFocus()
            return res

        # Valida la dirección
        res = ComercioValidator.validate_direccion(
            self._view.frame.edit_direccion
        )

        if not res.is_success:
            self._view.frame.edit_direccion.setFocus()
            return res

        # Valida la código postal
        res = ComercioValidator.validate_cod_postal(
            self._view.frame.edit_cod_postal
        )

        if not res.is_success:
            self._view.frame.edit_cod_postal.setFocus()
            return res

        # Valida la población
        res = ComercioValidator.validate_poblacion(
            self._view.frame.edit_poblacion
        )

        if not res.is_success:
            self._view.frame.edit_poblacion.setFocus()
            return res

        # Valida la provincia
        res = ComercioValidator.validate_provincia(
            self._view.frame.edit_provincia
        )

        if not res.is_success:
            self._view.frame.edit_provincia.setFocus()
            return res

        # Valida el país
        res = ComercioValidator.validate_pais(
            self._view.frame.combo_pais
        )

        if not res.is_success:
            self._view.frame.combo_pais.setFocus()
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

    def _get_comercio(self):
        """ Devuelve el comercio resultante. """

        return self._comercio_result

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
        comercio = modelo.index(fila, 2).data()
        direccion = modelo.index(fila, 3).data()
        cod_postal = modelo.index(fila, 4).data()
        poblacion = modelo.index(fila, 5).data()
        provincia = modelo.index(fila, 6).data()
        pais = modelo.index(fila, 7).data()
        observaciones = modelo.index(fila, 8).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ta) if id_ta is not None else ""
        )

        self._view.frame.edit_comercio.setText(
            str(comercio) if comercio else ""
        )

        self._view.frame.edit_direccion.setText(
            str(direccion) if direccion else ""
        )

        self._view.frame.edit_cod_postal.setText(
            str(cod_postal) if cod_postal else ""
        )

        self._view.frame.edit_poblacion.setText(
            str(poblacion) if poblacion else ""
        )

        self._view.frame.edit_provincia.setText(
            str(provincia) if provincia else ""
        )

        self._view.frame.combo_pais.setCurrentIndex(
            self._view.frame.combo_pais.findText(pais)
        )

        self._view.frame.text_observaciones.setPlainText(
            str(observaciones) if observaciones is not None else ""
        )

        return Result.success(id_ta)

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
            self._view.frame.combo_pais.addItem(
                ent.pais, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_pais)

        # montaje el valor
        self._view.frame.combo_pais.setCurrentIndex(-1)
