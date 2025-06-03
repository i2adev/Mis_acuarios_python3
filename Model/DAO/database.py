"""
Modulo que contiene la clase 'DatabaseManager'.
"""
# Importaciones
import sqlite3
from pathlib import Path

class DatabaseManager():
    """ Singleton para manejar la conexión a la base de datos """
    _instance = None

    def __new__(cls):
        """Crea una instancia de la base de datos"""

        # Si la instancia de la base de datos no esta inicializada...
        if cls._instance is None:
            # ...inicializa una nueva instancia
            cls._instance = super().__new__(cls)
            cls._instance._initialize_db()

        # Devuelve la instancia
        return cls._instance
    
    def _initialize_db(self):
        """Inicializa la instancia de la base de datos"""
        
        try:
            file = (Path(__file__).parent.parent / "MisAcuarios" /
                    "MISACUARIOS.sqlite3")
            if not Path.exists(file):
                print("EL ARCHIVO NO EXISTE")
                return None
            self.conn = sqlite3.connect(file)
            self.conn.execute("PRAGMA foreign_keys = ON")
        except FileNotFoundError as e:
            print("NO SE HA ENCONTRADO LA BASE DE DATOS.")
        except Exception as e:
            print(f"ERROR INESPERADO.\n {e}")
