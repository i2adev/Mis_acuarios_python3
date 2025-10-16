"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      08/08/2025
Commentarios:
    Módulo que contiene los controles para la inserción de imagenes.
"""

import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QPixmap
from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QApplication, QHBoxLayout,
    QLabel, QSizePolicy, QPushButton, QSpacerItem, QMessageBox, QFileDialog)

from Model.DAO.fotografia_dao import FotografiaDAO
from Model.Entities.fotografia_entity import FotografiaEntity
from Services.Result.result import Result
from Views.Dialogs.base_dialog import BaseDialog
from Views.Masters.base_view import BaseView


class ImageForm(QFrame):
    """
    Clase que contiene los controles para gestionar imagenes.
    """

    def __init__(self, p_window: BaseView | BaseDialog, procedure: str):
        """ Constructor de clase. """
        
        # Constructor de la superclase
        super().__init__()

        # Atributos
        self.lista_fotos: list[FotografiaEntity] = []
        self.fdao = FotografiaDAO(procedure)
        self.parent_window = p_window

        # Configuramos el frame
        self.setMinimumWidth(150)
        self.create_widgets()
        self.build_layout()
        
        # Inicializamos los eventos
        self.init_handlers()

    def init_handlers(self):
        """ Inicializa los eventos de los controles. """
        
        # Botones de imagen
        self.button_add.clicked.connect(
            self.load_images_for_insert
        )

        self.button_remove.clicked.connect(
            self.delete_image
        )

        self.button_next.clicked.connect(
            self.next_image
        )

        self.button_prev.clicked.connect(
            self.prev_image
        )
    
    def create_widgets(self):
        """ Crea los widgets. """

        # Layouts
        ## Layout principal
        self.layout_form = QVBoxLayout()

        ## Layout controles
        self.layout_controls = QHBoxLayout()

        # Primera línea
        ## Label de la imagen
        self.label_image = QLabel()
        self.label_image.setObjectName("label_image")
        self.label_image.setSizePolicy(
            QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored
        )

        # Segunda línea
        ## Botón add
        self.button_add = QPushButton("+")
        self.button_add.setObjectName("button_add")
        self.button_add.setFixedWidth(20)
        self.button_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ## Botón Remove
        self.button_remove = QPushButton("-")
        self.button_remove.setObjectName("button_remove")
        self.button_remove.setFixedWidth(20)
        self.button_remove.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ## Botón previo
        self.button_prev = QPushButton("<")
        self.button_prev.setObjectName("button_prev")
        self.button_prev.setFixedWidth(20)
        self.button_prev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ## Label numero de imagen
        self.label_num_imagen = QLabel()
        self.label_num_imagen.setFixedWidth(30)
        self.label_num_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_num_imagen.setObjectName("label_num_imagen")
        ## Label DE
        self.label_de = QLabel(" DE ")
        self.label_de.setObjectName("DE")
        self.label_de.setFixedWidth(50)
        self.label_de.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ## Label número total de imagenes
        self.label_num_total_imegenes = QLabel()
        self.label_num_total_imegenes.setFixedWidth(30)
        self.label_num_total_imegenes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_num_total_imegenes.setObjectName("label_num_total_imegenes")
        ## Botón siguiente
        self.button_next = QPushButton(">")
        self.button_next.setObjectName("button_next")
        self.button_next.setFixedWidth(20)
        self.button_next.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def build_layout(self):
        """ Construye el layout. """

        # Controles
        self.layout_controls.addWidget(self.button_add)
        self.layout_controls.addWidget(self.button_remove)
        self.layout_controls.addSpacerItem(
            QSpacerItem(50,10, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Fixed)
        )
        self.layout_controls.addWidget(self.button_prev)
        self.layout_controls.addWidget(self.label_num_imagen)
        self.layout_controls.addWidget(self.label_de)
        self.layout_controls.addWidget(self.label_num_total_imegenes)
        self.layout_controls.addWidget(self.button_next)

        # Montar el layout
        self.layout_form.addWidget(self.label_image)
        self.layout_form.addLayout(self.layout_controls)

        self.setLayout(self.layout_form)

    def load_images_for_insert(self):
        """ Carga las imágenes a insertar. """

        # Configuramos el diálogo de apertura de imágenes
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Imágenes JPG (*.jpg *.jpeg)")

        if file_dialog.exec():
            i = self.get_max_num_in_list()

            files = file_dialog.selectedFiles()
            for f in files:
                self.lista_fotos.append(FotografiaEntity(
                    id = None,
                    num = i,
                    id_foranea = None,
                    ruta = f,
                    fotografia = Path(f).read_bytes()
                ))
                i += 1

            # Configurar linea de datos
            if self.label_num_imagen.text():
                image_num = int(self.label_num_imagen.text())
                self.show_image(image_num)
            else:
                self.label_num_imagen.setText("1")
                self.show_image()

            self.label_num_total_imegenes.setText(
                str(len(self.lista_fotos))
            )

    def get_max_num_in_list(self):
        """ Obtiene el número máximo de la lista de fotografías. """

        if self.lista_fotos:
            return max(f.num for f in self.lista_fotos)
        else:
            return 0

    def load_images(self, id_: int):
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

    def insert_foto(self, idf: int) -> Result:
        """ Inserta una fotografía en la base de datos. """

        # Insertamos las fotografías
        if self.lista_fotos:
            for f in self.lista_fotos:
                # En caso de que la imagen este en la base de datos
                if f.id:
                    continue

                # Asigna la clave foranea e inserta la imagen
                f.id_foranea = idf
                res_foto = self.fdao.insert(f)

                if not res_foto.is_success:
                    return Result.failure(res_foto.error_msg)

            return Result.success(len(self.lista_fotos))
        else:
            return Result.success(0)

    def delete_image(self):
        """
        Elimina una imagen de la lista. En caso de que la imagen este en
        la base de datos, se borra de la misma.
        """

        # Condiciones de salida
        if not self.label_num_imagen.text():
            return

        image_num = int(self.label_num_imagen.text())
        idx = image_num - 1

        if self.lista_fotos[idx].id:
            self.fdao.delete(self.lista_fotos[idx].id)

        del self.lista_fotos[idx]

        # Configurar linea de datos
        total_number = len(self.lista_fotos)

        if image_num > total_number:
            image_num -= 1

        self.label_num_imagen.setText(
            str(image_num)
        )

        self.label_num_total_imegenes.setText(
            str(total_number)
        )

        self.show_image(image_num)

    def show_image(self, number: int = 1):
        """
        Muestra la imagen.
        :param number: Número de imágen a mostrar
        """

        # Obtenemos el íncide de la foto en la lista
        idx = number - 1

        # En caso de que no haya fotos en la lista
        if idx == -1:
            self.label_image.clear()
            self.label_num_imagen.clear()
            self.label_num_total_imegenes.clear()
            return

        # Mostrar el el QLabel
        px = QPixmap()
        px.loadFromData(self.lista_fotos[idx].fotografia)

        if px.isNull():
            self.label_image.clear()
            return

        self.label_image.setPixmap(px.scaled(
            self.label_image.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        self.label_image.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

    def next_image(self):
        """ Muestra la siguiente imagen. """

        # Condiciones de salida
        if not self.lista_fotos:
            return

        # Consiguramos las páginas
        current_num = int(self.label_num_imagen.text())
        total_number = int(
            self.label_num_total_imegenes.text()
        )

        # Establecemos el número de imágen a mostrar
        show_number = current_num + 1
        if show_number <= total_number:
            self.show_image(show_number)
            self.label_num_imagen.setText(str(show_number))
        else:
            QMessageBox.information(
                self.parent_window,
                self.parent_window.window_title,
                "HA LLEGADO A LA ÚLTIMA IMAGEN"
            )

    def prev_image(self):
        """ Muestra la anterior imagen. """

        # Condiciones de salida
        if not self.lista_fotos:
            return

        # Consiguramos las páginas
        current_num = int(self.label_num_imagen.text())

        # Establecemos el número de imágen a mostrar
        show_number = current_num - 1
        if show_number >= 1:
            self.show_image(show_number)
            self.label_num_imagen.setText(str(show_number))
        else:
            QMessageBox.information(
                self.parent_window,
                self.parent_window.window_title,
                "HA LLEGADO A LA PRIMERA IMAGEN"
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ImageForm()
    ventana.show()

    sys.exit(app.exec())