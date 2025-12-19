"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Comentarios:
    Módulo que contien la clase que gestiona las connexiones a la base
    de datos.
"""
# Importaciones
import sqlite3
from pathlib import Path


class DBManager:
    """ Clase para gestionar la conexión a la base de datos. """

    def __init__(self):
        """ Inicializa la conexión a la base de datos. """
        self.conn = None
        self.initialize_db()

    def __enter__(self):
        if not self.is_opened():
            self.initialize_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    def initialize_db(self):
        """ Inicializa la conexión con la base de datos. """
        try:
            file = (Path(__file__).resolve().parent.parent /
                    "Services" / "Database" / "MISACUARIOS.sqlite3")

            if not file.exists():
                raise FileNotFoundError(
                    f"No se encontró la base de datos en: {file}")

            self.conn = sqlite3.connect(file)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = ON")

        except Exception as e:
            print(f"ERROR INESPERADO.\n{e}")

    def get_connection(self):
        """ Devuelve la conexión activa. """
        return self.conn

    def close_connection(self):
        """ Cierra la conexión. """
        if self.conn:
            self.conn.close()
            self.conn = None

    def is_opened(self) -> bool:
        """ Indica si la conexión está abierta. """
        return self.conn is not None
