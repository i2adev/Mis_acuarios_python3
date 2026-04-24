"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  17/12/2025
Comentarios:
    Controlador base de equipamiento.
"""
from PyQt6.QtCore import QDateTime, QTime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Main.Controllers.base_controller import BaseController
from ModuloMaestro.Controllers.categoria_equipamiento_dialog_controller import \
    CategoriaEquipamientoDialogController
from ModuloMaestro.Controllers.marca_comercial_dialog_controller import \
    MarcaComercialDialogController
from Main.Model.DAO.base_dao import BaseDAO
from ModuloMaestro.Model.DAO.categoria_equipamiento_dao import \
    CategoriaEquipamientoDAO
from ModuloMaestro.Model.DAO.equipamiento_dao import EquipamientoDAO
from ModuloMaestro.Model.DAO.marca_comercial_dao import MarcaComercialDAO
from ModuloMaestro.Model.Entities.categoria_equipamiento_entity import \
    CategoriaEquipamientoEntity
from ModuloMaestro.Model.Entities.equipamiento_entity import EquipamientoEntity
from ModuloMaestro.Model.Entities.marca_comercial_entity import \
    MarcaComercialEntity
from Services.Result.result import Result
from Services.Validators.equipamiento_validator import EquipamientoValidator
from ModuloMaestro.Views.Dialogs.cattegoria_equipamiento_dialog import \
    CategoriaEquipamientoDialog
from ModuloMaestro.Views.Dialogs.equipamiento_dialog import EquipamientoDialog
from ModuloMaestro.Views.Dialogs.marca_comercial_dialog import MarcaComercialDialog
from ModuloMaestro.Views.Masters.equipamiento_view import EquipamientoView


class EquipamientoController(BaseController):
    """ 
    Controlador base del cuadro de diálogo y formulario de equipamiento. 
    """

    def __init__(self, view: EquipamientoDialog | EquipamientoView,
                 dao: EquipamientoDAO,
                 model: EquipamientoEntity):
        """
        Inicializa el controlador de equipamiento.
        :param view: EquipamientoDialog | EquipamientoView
        :param dao: EquipamientoDAO
        :param model: EquipamientoEntity
        """

        # Atributos
        self._equipamiento_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos()

    def _entity_configuration(self) -> EquipamientoEntity:
        """ Configura la entidad. """

        ent = EquipamientoEntity()
        ctrs = self._view.frame

        ent.id = self._view.frame.edit_id.value()
        ent.id_categoria = ctrs.combo_categoria_equipamiento.value()
        ent.id_marca = int(ctrs.combo_marca.value())
        ent.modelo = ctrs.edit_modelo.value()
        ent.numero_serie = ctrs.edit_num_serie.value()

        alta = ctrs.fecha_alta.date()
        if alta.isValid():
            time_alta = QDateTime(alta, QTime(0, 0))
            ent.fecha_alta = int(time_alta.toSecsSinceEpoch())
        else:
            ent.fecha_alta = None

        baja = ctrs.fecha_baja.date()
        if baja.isValid():
            time_baja = QDateTime(baja, QTime(0, 0))
            ent.fecha_baja = int(time_baja.toSecsSinceEpoch())
        else:
            ent.fecha_baja = None

        ent.motivo_baja = ctrs.edit_motivo_baja.value()
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

        # Válida la categoría del equipo
        res = EquipamientoValidator.validate_categoria_equipamiento(
            self._view.frame.combo_categoria_equipamiento
        )

        if not res.is_success:
            self._view.frame.combo_categoria_equipamiento.setFocus()
            return res

        # Válida la marca del equipo
        res = EquipamientoValidator.validate_marca(
            self._view.frame.combo_marca
        )

        if not res.is_success:
            self._view.frame.combo_marca.setFocus()
            return res

        # Valida el modelo
        res = EquipamientoValidator.validate_modelo(
            self._view.frame.edit_modelo
        )

        if not res.is_success:
            self._view.frame.edit_modelo.setFocus()
            return res

        # Valida el número de serie
        res = EquipamientoValidator.validate_numero_serie(
            self._view.frame.edit_num_serie
        )

        if not res.is_success:
            self._view.frame.edit_num_serie.setFocus()
            return res

        # Valida la fecha de alta
        res = EquipamientoValidator.validate_fecha_alta(
            self._view.frame.fecha_alta.edit_date
        )

        if not res.is_success:
            self._view.frame.fecha_alta.edit_date.setFocus()
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

    def _get_equipamiento(self):
        """ Devuelve el equipamiento resultante. """

        return self._equipamiento_result

    def _load_record(self):
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_categoria()
        self._fill_combo_marca()

    def _fill_combo_categoria(self):
        """ Llena el combo de la categoria. """

        # Vaciamos el combo
        self._view.frame.combo_categoria_equipamiento.clear()

        # Obtenemos los datos
        dao = CategoriaEquipamientoDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'CATEGORÍAS'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_categoria_equipamiento.addItem(
                ent.categoria_equipamiento, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_categoria_equipamiento)

        # montaje el valor
        self._view.frame.combo_categoria_equipamiento.setCurrentIndex(-1)

    def _fill_combo_marca(self):
        """ Llena el combo del tipo de acuario. """

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
            self._view.frame.combo_marca.addItem(
                ent.nombre_marca, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_marca)

        # montaje el valor
        self._view.frame.combo_marca.setCurrentIndex(-1)

    def _open_categoria_dialog(self):
        """ Abrimos el diálogo del tipo de filtro. """

        # Configuramos el CONTROLADOR
        view = CategoriaEquipamientoDialog("INSERTAR CATEGORIA DE "
                                           "EQUIPAMIENTO")
        dao = CategoriaEquipamientoDAO()
        mod = CategoriaEquipamientoEntity()

        ctrl = CategoriaEquipamientoDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_categoria_equipamiento

        self._fill_combo_categoria()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)
                break

    def _open_marca_dialog(self):
        """ Abrimos el diálogo de urna. """

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
                break

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
        self._view.frame.combo_categoria_equipamiento.setValue(
            ent.id_categoria)
        self._view.frame.combo_marca.setValue(ent.id_marca)
        self._view.frame.edit_modelo.setValue(ent.modelo)
        self._view.frame.edit_num_serie.setValue(ent.num_series)
        self._view.frame.fecha_alta.setDate(BaseDAO._seconds_to_date(
            ent.fecha_alta))
        self._view.frame.fecha_baja.setDate(BaseDAO._seconds_to_date(
            ent.fecha_baja))
        self._view.frame.edit_motivo_baja.setValue(ent.motivo_baja)
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

    def _on_text_changed(self):
        """
        Se ejecuta cuando se modifica el texto.
        """

        if self._view.frame.fecha_baja.edit_date.text():
            self._setDisabledControl(
                self._view.frame.layout_motivo_baja, False)
        else:
            self._setDisabledControl(
                self._view.frame.layout_motivo_baja, True)
