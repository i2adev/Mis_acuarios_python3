"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad COMERCIO.
"""

import sys

from PyQt6.QtWidgets import QComboBox, QFrame, QVBoxLayout, QHBoxLayout, \
    QLabel, \
    QLineEdit, \
    QPlainTextEdit, QApplication, QSpacerItem, QSizePolicy


class ComercioForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad categoría
    de acuario.
    """

    def __init__(self):
        super().__init__()

        # self.setFixedHeight(150)

        self.create_widgets()
        self.build_layout()

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
        ### Comercio
        self.layout_comercio = QVBoxLayout()
        ### Dirección
        self.layout_dirección = QVBoxLayout()
        ### Código postal
        self.layout_cod_postal = QVBoxLayout()

        ## Segunda linea
        self.layout_second_line = QHBoxLayout()
        self.layout_second_line.setContentsMargins(0, 0, 0, 20)
        ### Población
        self.layout_poblacion = QVBoxLayout()
        ### Provincia
        self.layout_provincia = QVBoxLayout()
        ### País
        self.layout_pais = QVBoxLayout()

        ## Tercera línea
        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_comercio = QLabel("COMERCIO")
        self.label_direccion = QLabel("DIRECCIÓN")
        self.label_cod_postal = QLabel("COD. POSTAL")
        self.label_poblacion = QLabel("POBLACIÓN")
        self.label_provincia = QLabel("PROVINCIA")
        self.label_pais = QLabel("PAÍS")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)

        self.edit_comercio = QLineEdit()
        self.edit_comercio.setObjectName("edit_comercio")
        self.edit_comercio.setToolTip(
            """
            <h2>Nombre del comercio</h2>
            En este campo se inserta el nombre del comercio. Este campo es 
            <b>obligatorio</b>.
            """
        )

        self.edit_direccion = QLineEdit()
        self.edit_direccion.setObjectName("edit_direccion")
        self.edit_direccion.setMinimumWidth(300)
        self.edit_direccion.setToolTip(
            """
            <h2>Dirección postal del comercio</h2>
            En este campo se inserta la dirección postal del comercio.
            """
        )

        self.edit_cod_postal = QLineEdit()
        self.edit_cod_postal.setObjectName("edit_cod_postal")
        self.edit_cod_postal.setToolTip(
            """
            <h2>Código postal</h2>
            En este campo se inserta el código postal de la población del 
            comercio.
            """
        )

        self.edit_poblacion = QLineEdit()
        self.edit_poblacion.setObjectName("edit_poblacion")
        self.edit_poblacion.setToolTip(
            """
            <h2>Población</h2>
            En este campo se inserta la población donde se encuentra el 
            comercio. 
            """
        )

        self.edit_provincia = QLineEdit()
        self.edit_provincia.setObjectName("edit_provincia")
        self.edit_provincia.setToolTip(
            """
            <h2>Provincia</h2>
            En este campo se inserta la provincia donde se encuentra el 
            comercio.
            """
        )

        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_descripcion")
        self.text_observaciones.setFixedHeight(75)
        self.text_observaciones.setToolTip(
            """
            <h2>Observaciones sobre el comercio</h2>
            En este campo se insertan observaciones sobre el comercio.
            """
        )

        # Comboboxes
        self.combo_pais = QComboBox()
        self.combo_pais.setObjectName("combo_pais")
        self.combo_pais.setMinimumWidth(250)
        self.combo_pais.setEditable(True)
        self.combo_pais.setToolTip(
            """
            <h2>Pais</h2>
            En este campo se selecciona el país donde se encuentra el 
            comercio. Este campo es <b>obligatorio</b>.
            """
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Comercio
        self.layout_comercio.addWidget(self.label_comercio)
        self.layout_comercio.addWidget(self.edit_comercio)

        ## Dirección
        self.layout_dirección.addWidget(self.label_direccion)
        self.layout_dirección.addWidget(self.edit_direccion)

        ## Código postal
        self.layout_cod_postal.addWidget(self.label_cod_postal)
        self.layout_cod_postal.addWidget(self.edit_cod_postal)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_comercio)
        self.layout_first_line.addLayout(self.layout_dirección)
        self.layout_first_line.addLayout(self.layout_cod_postal)

        # Segunda linea
        ## Población
        self.layout_poblacion.addWidget(self.label_poblacion)
        self.layout_poblacion.addWidget(self.edit_poblacion)

        ## Provincia
        self.layout_provincia.addWidget(self.label_provincia)
        self.layout_provincia.addWidget(self.edit_provincia)

        ## País
        self.layout_pais.addWidget(self.label_pais)
        self.layout_pais.addWidget(self.combo_pais)

        ## Monta la segunda línea
        self.layout_second_line.addLayout(self.layout_poblacion)
        self.layout_second_line.addLayout(self.layout_provincia)
        self.layout_second_line.addLayout(self.layout_pais)

        # Tercera linea
        ## Observaciones
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_observaciones)

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ComercioForm()
    ventana.show()

    sys.exit(app.exec())
