"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/10/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad PROYECTO.
"""

import sys

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPlainTextEdit, QApplication, QComboBox

from CustomControls.nullable_date_edit import NullableDateEdit


class ProyectoForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad proyecto.
    """

    def __init__(self):
        super().__init__()

        # self.setFixedHeight(300)

        self.create_widgets()
        self.build_layout()
        # self.init_form_handlers()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """
        # Layouts
        ## Layout principal
        self.layout_form = QVBoxLayout()

        ## Layout primera linea
        self.layout_first_line = QHBoxLayout()
        self.layout_first_line.setContentsMargins(0, 0, 0, 20)
        ### ID
        self.layout_id = QVBoxLayout()
        ### Nombre del proyecto
        self.layout_nombre_proyecto = QVBoxLayout()
        ### Estado del proyecto
        self.layout_estado_proyecto = QVBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        self.layout_second_line.setContentsMargins(0, 0, 0, 20)
        ### Fecha de inicio
        self.layout_fecha_inicio = QVBoxLayout()
        ### Fecha de finalización
        self.layout_fecha_fin = QVBoxLayout()

        ## Tercera linea
        # self.layout_third_line = QHBoxLayout()
        ### Motivo de cierre
        self.layout_motivo_cierre = QVBoxLayout()
        self.layout_motivo_cierre.setContentsMargins(0, 0, 0, 20)

        ## Cuarta linea
        ### Observaciones
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_nombre_proyecto = QLabel("NOMBRE DEL PROYECTO")
        self.label_estado_proyecto = QLabel("ESTADO DEL PROYECTO")
        self.label_fecha_inicio = QLabel("FECHA DE INICIO")
        self.label_fecha_fin = QLabel("FECHA DE CIERRE")
        self.label_motivo_cierre = QLabel("MOTIVO DE CIERRE/CANCELACIÓN")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_nombre_proyecto = QLineEdit()
        self.edit_nombre_proyecto.setObjectName("edit_nombre_proyecto")
        self.edit_motivo_cierre = QLineEdit()
        self.edit_motivo_cierre.setObjectName("edit_motivo_cierre")
        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setMinimumHeight(50)

        # Combos
        self.combo_estado_proyecto = QComboBox()
        self.combo_estado_proyecto.setMinimumWidth(250)
        self.combo_estado_proyecto.setObjectName("combo_estado_proyecto")
        self.combo_estado_proyecto.setEditable(True)

        # Datetimepickers
        self.date_inicio = NullableDateEdit()
        self.date_inicio.setDisplayFormat("dd/MM/yyyy")
        self.date_inicio.setObjectName("date_inicio")
        self.date_inicio.setDate(None)
        self.date_fin = NullableDateEdit()
        self.date_fin.setObjectName("date_fin")
        self.date_fin.edit_date.setObjectName("date_fin_proyecto")
        self.date_fin.setDisplayFormat("dd/MM/yyyy")
        self.date_fin.setObjectName("date_fin")
        self.date_fin.setDate(None)

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Nombre del proyecto
        self.layout_nombre_proyecto.addWidget(self.label_nombre_proyecto)
        self.layout_nombre_proyecto.addWidget(self.edit_nombre_proyecto)

        ## Estado del proyecto
        self.layout_estado_proyecto.addWidget(self.label_estado_proyecto)
        self.layout_estado_proyecto.addWidget(self.combo_estado_proyecto)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_nombre_proyecto)
        self.layout_first_line.addLayout(self.layout_estado_proyecto)

        # Segunda línea
        ## Fecha de inicio
        self.layout_fecha_inicio.addWidget(self.label_fecha_inicio)
        self.layout_fecha_inicio.addWidget(self.date_inicio)

        ## Fecha de inicio
        self.layout_fecha_fin.addWidget(self.label_fecha_fin)
        self.layout_fecha_fin.addWidget(self.date_fin)

        ## Montamos la segunda línea
        self.layout_second_line.addLayout(self.layout_fecha_inicio)
        self.layout_second_line.addLayout(self.layout_fecha_fin)

        # Tercera línea
        ## Motivo de cierre
        self.layout_motivo_cierre.addWidget(self.label_motivo_cierre)
        self.layout_motivo_cierre.addWidget(self.edit_motivo_cierre)

        # Cuarta línea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_motivo_cierre)
        self.layout_form.addLayout(self.layout_descripcion)

        self.setLayout(self.layout_form)

    # def init_form_handlers(self):
    #     self.date_fin.edit_date.editingFinished.connect(
    #         self._on_date_fin_lost_focus
    #     )
    #
    # def _on_date_fin_lost_focus(self):
    #     QMessageBox.information(None, "oooo", "FECHA DE CIERRE")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ProyectoForm()
    ventana.show()

    sys.exit(app.exec())
