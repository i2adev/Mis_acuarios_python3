"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/06/2025
Commentarios:
    Controlador que se encarga de la revisión de ortografía de los
    controles de inserción de texto.
"""

# Importaciones1
import os
from pathlib import Path
import enchant

from PyQt6.QtGui import QTextCharFormat, QColor
from PyQt6.QtCore import Qt

class SpellCheckController:
    def __init__(self):
        """ Constructor de la clase. """
        self.dic_path = (Path(__file__).resolve().parent.parent /
                         "Services" / "Dictionaries")

        os.environ["ENCHANT_HUNSPELL_DICT_DIR"] = str(self.dic_path)

        self.aff_path = self.dic_path / "es_ES.aff"
        self.dic_file = self.dic_path / "es_ES.dic"

        print(f"📁 Diccionario: {self.dic_file}")
        print(f"📁 Afirmaciones: {self.aff_path}")

        if not self.aff_path.exists() or not self.dic_file.exists():
            raise FileNotFoundError("❌ Faltan archivos del diccionario Hunspell")

        try:
            self.dic = enchant.Dict("es_ES")
            print("✅ Diccionario cargado correctamente")
        except enchant.errors.DictNotFoundError:
            print("❌ No se pudo cargar el diccionario 'es_ES'")

    def habilitar_en_widget(self, widget):
        if hasattr(widget, "textChanged"):
            widget.textChanged.connect(lambda: self._verificar(widget))
        elif hasattr(widget, "editingFinished"):
            widget.editingFinished.connect(lambda: self._verificar_line_edit(widget))

    def _verificar(self, widget):
        if not hasattr(widget, "toPlainText"):
            return

        texto = widget.toPlainText()
        cursor = widget.textCursor()
        cursor.select(cursor.SelectionType.Document)
        cursor.setCharFormat(QTextCharFormat())

        palabras = texto.split()
        for palabra in palabras:
            limpia = palabra.strip(".,;:!?()\"“”¡¿")
            if not self.dict.check(limpia):
                fmt = QTextCharFormat()
                fmt.setUnderlineColor(QColor("red"))
                fmt.setUnderlineStyle(QTextCharFormat.UnderlineStyle.SpellCheckUnderline)
                buscador = widget.document().find(limpia)
                while not buscador.isNull():
                    buscador.mergeCharFormat(fmt)
                    buscador = widget.document().find(limpia, buscador)

    def _verificar_line_edit(self, widget):
        texto = widget.text()
        palabras = texto.split()
        errores = [p for p in palabras if not self.dict.check(p.strip(".,;:!?()\"“”¡¿"))]

        if errores:
            print(f"❌ Ortografía incorrecta en QLineEdit: {errores}")
        else:
            print("✅ Ortografía correcta en QLineEdit.")

if __name__ == "__main__":
    sc = SpellCheckController()

""" USO DEL CORRECTOR
from pathlib import Path

ruta_diccionario = Path("C:/Hunspell/es_ES")  # Cambia por la ruta correcta
corrector = CorrectorOrtograficoController(ruta_diccionario)

corrector.habilitar_en_widget(self.miTextEdit)
corrector.habilitar_en_widget(self.miPlainTextEdit)
corrector.habilitar_en_widget(self.miLineEdit)
 
"""