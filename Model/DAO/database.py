"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contien la clase que gestiona las connexiones a la base
    de datos.
"""
# Importaciones
import sqlite3
from pathlib import Path

class DBManager:
    """Clase para gestionar la conexión a la base de datos."""

    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.conn = None
        self.initialize_db()

    def initialize_db(self):
        """Inicializa la conexión con la base de datos."""
        try:
            file = (Path(__file__).resolve().parent.parent / "MisAcuarios" / "MISACUARIOS.sqlite3")
            if not file.exists():
                print("EL ARCHIVO NO EXISTE")
                return

            self.conn = sqlite3.connect(file)
            self.conn.execute("PRAGMA foreign_keys = ON")

        except Exception as e:
            print(f"ERROR INESPERADO.\n{e}")

    def get_connection(self):
        """Devuelve la conexión activa."""
        return self.conn

    def close_connection(self):
        """Cierra la conexión."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def is_opened(self) -> bool:
        """
        Indica si la conexión está abierta:
        -   True: Si la conexión está abierta.
        -   False: Si la conexión está cerrada.
        """
        if self.conn is not None:
            return True
        else:
            return False