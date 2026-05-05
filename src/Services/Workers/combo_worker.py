"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      25/04/2026
Comentarios:
    Clase basada en QObject que implementa el patrón worker de Qt para
    ejecutar una función en segundo plano (normalmente en un QThread)
    sin bloquear la interfaz gráfica. Recibe una función (fn) en su
    constructor, la ejecuta en el metodo run y comunica el resultado
    mediante la señal finished, o cualquier error mediante la señal
    error. Su diseño es genérico y reutilizable, lo que permite
    desacoplar la lógica de obtención de datos (por ejemplo, consultas a
    base de datos) de la capa de presentación, manteniendo la UI
    reactiva y gestionando la comunicación entre hilos de forma segura a
    través de señales.
"""

import traceback

from PyQt6.QtCore import QObject, pyqtSignal


class ComboWorker(QObject):
    finished = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
            self.finished.emit(result)
        except Exception:
            self.error.emit(traceback.format_exc())
