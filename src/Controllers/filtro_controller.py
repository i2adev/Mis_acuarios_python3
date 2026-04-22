"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  28/11/2025
Comentarios:
    Controlador base de filtro.
"""

from Controllers.base_controller import BaseController
from Controllers.marca_comercial_dialog_controller import \
    MarcaComercialDialogController
from Controllers.tipo_filtro_dialog_controller import \
    TipoFiltroDialogController
from Model.DAO.base_dao import BaseDAO
from Model.DAO.filtro_dao import FiltroDAO
from Model.DAO.marca_comercial_dao import MarcaComercialDAO
from Model.DAO.tipo_filtro_dao import TipoFiltroDAO
from Model.Entities.filtro_entity import FiltroEntity
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from PyQt6.QtCore import QDate, QDateTime, QTime, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton
from Services.Result.result import Result
from Services.Validators.filtro_validator import FiltroValidator
from Views.Dialogs.filtro_dialog import FiltroDialog
from Views.Dialogs.marca_comercial_dialog import MarcaComercialDialog
from Views.Dialogs.tipo_filtro_dialog import TipoFiltroDialog
from Views.Masters.filtro_view import FiltroView


class FiltroController(BaseController):
    """ 
    Controlador base del cuadro de diálogo y formulario maestro de proyecto. 
    """

    def __init__(self, view: FiltroDialog | FiltroView,
                 dao: FiltroDAO,
                 model: FiltroEntity):
        """
        Inicializa el controlador de la urna.
        :param view: FiltroDialog | FiltroView
        :param dao: FiltroDAO
        :param model: FiltroEntity
        """

        # Atributos
        self._filtro_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenas los combos
        self._fill_combos()

    def _entity_configuration(self) -> FiltroEntity:
        """ Configura la entidad. """

        ent = FiltroEntity()
        ctrs = self._view.frame

        # ID
        if ctrs.edit_id.text():
            ent.id = int(ctrs.edit_id.text())
        else:
            ent.id = None

        # Tipo de filtro
        ent.id_tipo = ctrs.combo_tipo_filtro.value()

        # Específica sí cuenta con calentador
        ent.es_thermo = True if ctrs.check_termofiltro.isChecked() else False

        # Marca
        ent.id_marca = ctrs.combo_marca.currentData()

        # Modelo
        ent.modelo = ctrs.edit_modelo.value()

        # Número de serie
        ent.num_serie = ctrs.edit_num_serie.value()

        # Volumen mínimo del acuario
        ent.vol_min_acuario = ctrs.edit_vol_min_acuario.value()

        # Volumen máximo del acuario
        ent.vol_max_acuario = ctrs.edit_vol_max_acuario.value()

        # Consumo eléctrico del filtro
        ent.consumo = ctrs.edit_consumo_filtro.value()

        # Consumo eléctrico del calentador del filtro
        ent.consumo_calentador = ctrs.edit_consumo_calentador.value()

        # Dimensiones: Ancho
        ent.ancho = ctrs.edit_ancho.value()

        # Dimensiones: Fondo
        ent.fondo = ctrs.edit_fondo.value()

        # Dimensiones: Alto
        ent.alto = ctrs.edit_alto.value()

        # Capacidad de carga filtrante
        ent.vol_filtrante = ctrs.edit_vol_material.value()

        # Altura máxima de bombeo
        ent.altura_bombeo = ctrs.edit_altura_max_bombeo.value()

        # Caudal del filtro
        ent.caudal = ctrs.edit_caudal.value()

        # Fecha de instalación
        instalacion = ctrs.fecha_instalacion.date()
        if instalacion.isValid():
            time_compra = QDateTime(instalacion, QTime(0, 0))
            ent.fecha_compra = int(time_compra.toSecsSinceEpoch())
        else:
            ent.fecha_compra = None

        # Fecha de baja
        baja = ctrs.fecha_baja.date()
        if baja.isValid():
            time_baja = QDateTime(baja, QTime(0, 0))
            ent.fecha_baja = int(time_baja.toSecsSinceEpoch())
        else:
            ent.fecha_baja = None

        # Motivo de la baja
        ent.motivo_baja = ctrs.edit_motivo_baja.value()

        # Descripción
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

        # Valida el tipo de filtro
        res = FiltroValidator.validate_tipo_filtro(
            self._view.frame.combo_tipo_filtro
        )

        if not res.is_success:
            self._view.frame.combo_tipo_filtro.setFocus()
            return res

        # Valida la marca del filtro
        res = FiltroValidator.validate_marca(
            self._view.frame.combo_marca
        )

        if not res.is_success:
            self._view.frame.combo_marca.setFocus()
            return res

        # Valida el modelo
        res = FiltroValidator.validate_modelo(
            self._view.frame.edit_modelo
        )

        if not res.is_success:
            self._view.frame.edit_modelo.setFocus()
            return res

        # Valida el número de serie
        res = FiltroValidator.validate_numero_serie(
            self._view.frame.edit_num_serie
        )

        if not res.is_success:
            self._view.frame.edit_num_serie.setFocus()
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

    def _get_filtro(self):
        """ Devuelve el filtro resultante. """

        return self._filtro_result

    def _load_record(self):
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_tipo_filtro()
        self._fill_combo_marca()

    def _fill_combo_tipo_filtro(self):
        """ Llena el combo de la urna. """

        # Vaciamos el combo
        self._view.frame.combo_tipo_filtro.clear()

        # Obtenemos los datos
        dao = TipoFiltroDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE FILTRO'."
            )

        # Llenas el combo
        for ent in lista.value:
            self._view.frame.combo_tipo_filtro.addItem(
                ent.tipo_filtro, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_tipo_filtro)

        # montaje el valor
        self._view.frame.combo_tipo_filtro.setCurrentIndex(-1)

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

    def _open_tipo_acuario_dialog(self):
        """ Abrimos el diálogo del tipo de filtro. """

        # Configuramos el CONTROLADOR
        view = TipoFiltroDialog("INSERTAR TIPO DE FILTRO")
        dao = TipoFiltroDAO()
        mod = TipoFiltroEntity()

        ctrl = TipoFiltroDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.conbo_tipo_filtro

        self._fill_combo_tipo_filtro()
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

        # Obtenemos la entidad
        id_ent = modelo.index(fila, 0).data()

        val = self._dao.get_entity_by_id(id_ent)
        if not val.is_success:
            return val

        ent = val.value

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(ent.id) if ent.id is not None else ""
        )
        self._view.frame.combo_tipo_filtro.setValue(ent.id_tipo)
        self._view.frame.check_termofiltro.setChecked(
            True if ent.es_thermo else False)
        self._view.frame.combo_marca.setValue(ent.id_marca)
        self._view.frame.edit_modelo.setValue(ent.modelo)
        self._view.frame.edit_num_serie.setValue(ent.num_serie)
        self._view.frame.edit_vol_min_acuario.setValue(ent.vol_min_acuario)
        self._view.frame.edit_vol_max_acuario.setValue(ent.vol_max_acuario)
        self._view.frame.edit_consumo_filtro.setValue(ent.consumo)
        self._view.frame.edit_consumo_calentador.setValue(
            ent.consumo_calentador)
        self._view.frame.edit_ancho.setValue(ent.ancho)
        self._view.frame.edit_fondo.setValue(ent.fondo)
        self._view.frame.edit_alto.setValue(ent.alto)
        self._view.frame.edit_vol_material.setValue(ent.vol_filtrante)
        self._view.frame.edit_altura_max_bombeo.setValue(ent.altura_bombeo)
        self._view.frame.edit_caudal.setValue(ent.caudal)
        self._view.frame.fecha_instalacion.setDate(
            BaseDAO._seconds_to_date(ent.fecha_instalacion))
        self._view.frame.fecha_baja.setDate(
            BaseDAO._seconds_to_date(ent.fecha_baja))
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

    def _open_tipo_filtro_dialog(self):
        """ Abrimos el diálogo de tipo de acuario. """

        # Configuramos el CONTROLADOR
        view = TipoFiltroDialog("INSERTAR TIPO DE ACUARIO")
        dao = TipoFiltroDAO()
        mod = TipoFiltroEntity()

        ctrl = TipoFiltroDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_marca

        self._fill_combo_tipo_filtro()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def brakdown_volumes(self, volumes: str) -> list[str] | None:
        """
        Desmonta una lista de 2 strings que representan el volumen mínimo y
        máximo del acuario recomendado por el fabricante.
        :param volumes: Cadena que contiene los volúmenes a separar
        """
        if not volumes:
            return None

        lista = volumes.split("/")

        return lista

    def brakdown_dimensions(self, dimensions: str) -> list[str] | None:
        """
        Desmonta una lista de 3 strings que representan las dimensiones del
        filtro (ancho x fondo x alto).
        :param dimensions: Cadena que contiene los dimensiones a separar
        """
        if not dimensions:
            return None

        lista = dimensions.split("x")

        return lista

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
