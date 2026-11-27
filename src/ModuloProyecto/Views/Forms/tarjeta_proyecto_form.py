"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/10/2026
Comentarios:
    Frame de la tarjeta de proyecto.
"""

import sys
from pathlib import Path

import globales

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from ModuloProyecto.Models.Entities.tarjeta_proyecto_entity import (
    TarjetaProyectoEntity
)


class TarjetaProyectoFrame(QFrame):
    """ Frame de la tarjeta de proyecto. """

    def __init__(self, proyecto: TarjetaProyectoEntity):
        # Llama al constructor padre
        super().__init__()

        # Inicializa las variables
        self.id = proyecto.id
        self.id_usuario = proyecto.id_usuario
        self.nombre = proyecto.nombre
        self.estado = proyecto.estado
        self.fecha_inicio = proyecto.fecha_inicio
        self.fecha_fin = proyecto.fecha_fin
        self.fotografia = proyecto.fotografia

        # Establece el nombre del control
        self.setObjectName("TarjetaProyecto")

        # Establece el estilo
        self.setStyleSheet("""
            QFrame#TarjetaProyecto {
                background-color: #232323;
                border: none;
                border-radius: 10px;
            }
        """)

        # Carga la imagen de selección
        self.pixmap_selected = QPixmap(
            str(Path(globales.PATH_IMAGES) / "checked.png")
        )

        # Crea los controles
        self.create_widgets()

        # Construye el layout
        self.build_layout()

    def create_widgets(self):
        """ Crea los widgets de la tarjeta de proyecto. """

        # --------------------------------------------------------------
        # LABEL DE SELECCIÓN
        # --------------------------------------------------------------

        self.label_selected = QLabel(parent=self)
        self.label_selected.setFixedSize(25, 25)

        if not self.pixmap_selected.isNull():
            self.label_selected.setPixmap(
                self.pixmap_selected.scaled(
                    self.label_selected.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )

        self.label_selected.setVisible(False)
        self.label_selected.setStyleSheet(
            "background-color: transparent; border: none;"
        )

        # --------------------------------------------------------------
        # LABEL COLOR DE ESTADO
        # --------------------------------------------------------------

        self.label_color_estado = QLabel(parent=self)
        self.label_color_estado.setFixedSize(24, 24)

        self.label_color_estado.setStyleSheet(f"""
            background-color: {self.get_color_estado()};
            border-radius: 12px;
            border: none;
        """)

        # --------------------------------------------------------------
        # LABEL IMAGEN DEL PROYECTO
        # --------------------------------------------------------------

        self.pixmap = QPixmap()

        if self.fotografia:
            if isinstance(self.fotografia, (bytes, bytearray)):
                self.pixmap.loadFromData(self.fotografia)

            elif isinstance(self.fotografia, str):
                self.pixmap.load(self.fotografia)

        self.label_imagen = QLabel(parent=self)
        self.label_imagen.setFixedSize(75, 75)
        self.label_imagen.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.label_imagen.setStyleSheet(
            "background-color: transparent; border: none;"
        )

        if not self.pixmap.isNull():
            self.label_imagen.setPixmap(
                self.pixmap.scaled(
                    self.label_imagen.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )

        # --------------------------------------------------------------
        # LABEL NOMBRE DEL PROYECTO
        # --------------------------------------------------------------

        self.label_nombre_proyecto = QLabel(
            parent=self,
            text=self.nombre
        )

        self.label_nombre_proyecto.setStyleSheet("""
            font-family: Roboto Bold;
            font-size: 14pt;
            background-color: transparent;
            border: none;
        """)

        # --------------------------------------------------------------
        # LABEL ESTADO
        # --------------------------------------------------------------

        self.label_estado = QLabel(
            parent=self,
            text=self.estado
        )

        self.label_estado.setStyleSheet("""
            font-family: Roboto Thin;
            font-size: 12pt;
            background-color: transparent;
            border: none;
        """)

        # --------------------------------------------------------------
        # LABEL FECHA INICIO
        # --------------------------------------------------------------

        self.label_fecha_inicio = QLabel(
            parent=self,
            text=f"F. inicio: {self.fecha_inicio or '-'}"
        )

        self.label_fecha_inicio.setStyleSheet("""
            font-family: Roboto Thin;
            font-size: 12pt;
            background-color: transparent;
            border: none;
        """)

        # --------------------------------------------------------------
        # LABEL FECHA FIN
        # --------------------------------------------------------------

        self.label_fecha_fin = QLabel(
            parent=self,
            text=f"F. fin: {self.fecha_fin or '-'}"
        )

        self.label_fecha_fin.setStyleSheet("""
            font-family: Roboto Thin;
            font-size: 12pt;
            background-color: transparent;
            border: none;
        """)

        # --------------------------------------------------------------
        # BOTÓN DE OPCIONES
        # --------------------------------------------------------------

        self.button_opciones = QPushButton("...")
        self.button_opciones.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_opciones.setFixedSize(50, 50)

        self.button_opciones.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 18pt;
            }

            QPushButton:hover {
                background-color: #383838;
                border-radius: 5px;
            }
        """)

    def build_layout(self):
        """ Construye el layout de la tarjeta de proyecto. """

        # --------------------------------------------------------------
        # LAYOUT PRINCIPAL
        # --------------------------------------------------------------

        self.layout_principal = QHBoxLayout(self)
        self.layout_principal.setContentsMargins(10, 10, 10, 10)
        self.layout_principal.setSpacing(5)

        # --------------------------------------------------------------
        # LAYOUT ESTADO
        # --------------------------------------------------------------

        self.layout_estado = QHBoxLayout()
        self.layout_estado.setSpacing(8)

        self.layout_estado.addWidget(self.label_color_estado)
        self.layout_estado.addWidget(self.label_estado)

        # --------------------------------------------------------------
        # LAYOUT ETIQUETAS
        # --------------------------------------------------------------

        self.layout_etiquetas = QVBoxLayout()
        self.layout_etiquetas.setSpacing(5)

        self.layout_etiquetas.addWidget(
            self.label_nombre_proyecto
        )

        self.layout_etiquetas.addWidget(
            self.label_fecha_inicio
        )

        self.layout_etiquetas.addWidget(
            self.label_fecha_fin
        )

        self.layout_etiquetas.addLayout(
            self.layout_estado
        )

        # --------------------------------------------------------------
        # CONSTRUCCIÓN DEL LAYOUT PRINCIPAL
        # --------------------------------------------------------------

        self.layout_principal.addWidget(
            self.label_imagen
        )

        self.layout_principal.addLayout(
            self.layout_etiquetas,
            stretch=1
        )

        self.layout_principal.addWidget(
            self.button_opciones
        )

        self.layout_principal.addWidget(
            self.label_selected
        )

    def get_color_estado(self) -> str:
        """
        Obtiene el color del estado del proyecto.

        :return: Color correspondiente al estado del proyecto.
        """

        colores = {
            "Planificación": globales.COLOR_PLANIFICACION,
            "En curso": globales.COLOR_EN_CURSO,
            "Finalizado": globales.COLOR_FINALIZADO,
            "Cancelado": globales.COLOR_CANCELADO
        }

        return colores.get(self.estado, "transparent")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = TarjetaProyectoFrame(
        TarjetaProyectoEntity(
            id_usuario=1,
            id=1,
            nombre="Etxebarri 40",
            estado="En curso",
            fecha_inicio="10/09/2026",
            fecha_fin="02/10/2026"
        )
    )

    # Cargar el archivo .qss
    ruta_estilos = Path(globales.PATH_STYLES) / "main_style.qss"

    with open(ruta_estilos, "r", encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()

    sys.exit(app.exec())

# """
# Autor:      Inigo Iturriagaetxebarria
# Fecha:      02/10/2026
# Comentarios:
#     Frame de la tarjeta de proyecto.
# """
# import sys
# from pathlib import Path
#
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QCursor, QPixmap
# from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, \
#     QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout
#
# import globales
# from ModuloProyecto.Models.Entities.tarjeta_proyecto_entity import \
#     TarjetaProyectoEntity
#
#
# class TarjetaProyectoFrame(QFrame):
#     """
#     Frame de la tarjeta de proyecto.
#     """
#
#     def __init__(self, proyecto: TarjetaProyectoEntity):
#         # Llama al constructor padre
#         super().__init__()
#
#         # Establece el estilo
#         self.setStyleSheet("""
#             background-color: #232323;
#             border: 0px solid gray;
#             border-radius: 10px;
#         """)
#
#         # Inicializa las variables
#         self.id = proyecto.id
#         self.id_usuario = proyecto.id_usuario
#         self.nombre = proyecto.nombre
#         self.estado = proyecto.estado
#         self.fecha_inicio = proyecto.fecha_inicio
#         self.fecha_fin = proyecto.fecha_fin
#         self.fotografia = proyecto.fotografia
#
#         # Establece las variables
#         self.pixmap_selected = QPixmap(
#             str(Path(globales.PATH_IMAGES) / "checked.png")
#         )
#
#         self.setObjectName("TarjetaProyecto")
#
#         self.create_widgets()
#         self.build_layout()
#
#     def create_widgets(self):
#         """ Crea los widgets de la tarjeta de proyecto. """
#
#         # Label de selección
#         self.label_selected = QLabel(parent=self, text=None)
#         self.label_selected.setFixedSize(25, 25)
#         self.label_selected.setPixmap(self.pixmap_selected.scaled(
#             self.label_selected.size(),
#             Qt.AspectRatioMode.KeepAspectRatio,
#             Qt.TransformationMode.SmoothTransformation
#         ))
#         self.label_selected.setVisible(False)
#
#         # Label color de estado
#         self.label_color_estado = QLabel(parent=self, text=None)
#         self.label_color_estado.setFixedSize(24, 24)
#         self.label_color_estado.setStyleSheet(
#             # f"background-color:{};"
#             f"""
#             background-color: {self.get_color_estado()};
#             border-radius: 12px;
#             """)
#
#         # Label imagen del proyecto
#         self.pixmap = QPixmap()
#         if self.fotografia:
#             self.pixmap.loadFromData(self.fotografia)
#
#         self.label_imagen = QLabel(parent=self, text=None)
#         self.label_imagen.setFixedSize(75, 75)
#         self.label_imagen.setPixmap(self.pixmap.scaled(
#             self.label_imagen.size(),
#             Qt.AspectRatioMode.KeepAspectRatio,
#             Qt.TransformationMode.SmoothTransformation
#         ))
#
#         # Label nombre de proyecto
#         self.label_nombre_proyecto = QLabel(parent=self, text=self.nombre)
#         self.label_nombre_proyecto.setStyleSheet("""
#             font-family: Roboto Bold;
#             font-size: 14pt;
#             background-color: transparent;
#         """)
#
#         # Label estado
#         self.label_estado = QLabel(parent=self,
#                                    text=self.estado)
#         self.label_estado.setStyleSheet("""
#             font-family: Roboto Thin;
#             font-size: 12pt;
#             background-color: transparent;
#         """)
#
#         # Label fechas
#         self.label_fecha_inicio = QLabel(parent=self,
#                                          text=f"F. inicio: {
#                                          self.fecha_inicio}")
#         self.label_fecha_inicio.setStyleSheet("""
#             font-family: Roboto Thin;
#             font-size: 12pt;
#             background-color: transparent;
#         """)
#
#         self.label_fecha_fin = QLabel(parent=self,
#                                       text=f"F. fin: {self.fecha_fin}")
#         self.label_fecha_fin.setStyleSheet("""
#             font-family: Roboto Thin;
#             font-size: 12pt;
#             background-color: transparent;
#         """)
#
#         # Botón de opciones
#         self.button_opciones = QPushButton("...")
#         self.button_opciones.setCursor(
#             QCursor(Qt.CursorShape.PointingHandCursor)
#         )
#         self.button_opciones.setFixedSize(50, 50)
#         self.button_opciones.setStyleSheet("""
#             background-color: transparent;
#         """)
#
#     def build_layout(self):
#         """ Construye el layout de la tarjeta de proyecto. """
#
#         # Layout principal
#         self.layout = QHBoxLayout(self)
#         self.layout.setContentsMargins(10, 10, 10, 10)
#         self.layout.setSpacing(5)
#
#         # Layout labels
#         self.layout_estado = QHBoxLayout(self)
#         self.layout_estado.addWidget(self.label_color_estado)
#         self.layout_estado.addWidget(self.label_estado)
#
#         self.layout_etiquetas = QVBoxLayout(self)
#         self.layout_etiquetas.addWidget(self.label_nombre_proyecto)
#         self.layout_etiquetas.addWidget(self.label_fecha_inicio)
#         self.layout_etiquetas.addWidget(self.label_fecha_fin)
#         self.layout_etiquetas.addLayout(self.layout_estado)
#
#         # Construimos el layout
#         self.layout.addWidget(self.label_imagen)
#         self.layout.addLayout(self.layout_etiquetas)
#         # self.layout.addSpacerItem(
#         #     QSpacerItem(10, 0, QSizePolicy.Policy.Expanding,
#         #                 QSizePolicy.Policy.Minimum)
#         # )
#         self.layout.addWidget(self.button_opciones)
#         self.layout.addWidget(self.label_selected)
#
#     def get_color_estado(self) -> str | None:
#         """
#         Obtiene el color del estado de proyecto.
#         :return: Devuelve el color del estado de proyecto.
#         """
#
#         if self.estado == "Planificación":
#             return globales.COLOR_PLANIFICACION
#         elif self.estado == "En curso":
#             return globales.COLOR_EN_CURSO
#         elif self.estado == "Finalizado":
#             return globales.COLOR_FINALIZADO
#         elif self.estado == "Cancelado":
#             return globales.COLOR_CANCELADO
#         else:
#             return None
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     ventana = TarjetaProyectoFrame(
#         TarjetaProyectoEntity(id_usuario=1,
#                               id=1,
#                               nombre="Etxebarri 40",
#                               estado="En curso",
#                               fecha_inicio="10/09/2026",
#                               fecha_fin="02/10/2026",
#                               ))
#
#     # Cargar el archivo .qss
#     with open(str(Path(globales.PATH_STYLES) / "main_style.qss"), "r",
#               encoding="utf-8-sig") as f:
#         estilo = f.read()
#         app.setStyleSheet(estilo)
#
#     ventana.show()
#     sys.exit(app.exec())
