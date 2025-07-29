"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene los métodos de acceso a la base de datos de la
    entidad TIPO DE FILTRO.
"""

# Importaciones
import sqlite3
from PyQt6.QtWidgets import QMessageBox
from Model.DAO.base_dao import BaseDAO
from Model.Entities.pais_entity import PaisEntity
from Services.Result.result import Result
from Model.DAO.database import DBManager

class PaisDAO (BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad país.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    def get_list(self) -> Result:
        """ Obtiene el listado completo. """

        with self.db:
            if not self.db.conn:
                QMessageBox.information(None, "CONEXIÓN", "CONEXIÓN NO "
                                                          "INICIALIZADA")

            # Obtenemos los datos
            sql = """
                SELECT    ID_PAIS AS ID,
                          ROW_NUMBER() OVER(ORDER BY PAIS) AS NUM,
                          PAIS AS PAIS,
                          CONTINENTE AS CONTINENTE
                FROM      PAISES;
            """

            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                value = [PaisEntity(f["ID"], f["NUM"], f["PAIS"],
                                         f["CONTINENTE"])
                        for f in cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(value)

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()

    def get_list_combo(self):
        """ Obtiene el listado para el combo. """

        with self.db:
            # Obtenemos los datos
            sql = """
                SELECT    ID_PAIS AS ID,
                          PAIS AS VALUE
                FROM      PAISES
                ORDER BY  PAIS;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [PaisEntity(f["ID"], None, f["VALUE"], None)
                          for f in cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(values)

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()

    def insert(self, ent: PaisEntity) -> Result:
        pass

    def update(self, ent: PaisEntity) -> Result:
        pass

    def delete(self, id: int) -> Result:
        pass