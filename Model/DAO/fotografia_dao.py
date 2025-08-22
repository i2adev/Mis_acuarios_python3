"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad CATEGORÍA DE ACUARIO.
"""
import sqlite3

from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.fotografia_entity import FotografiaEntity
from Services.Result.result import Result


class FotografiaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    FotografiaEntity.
    """

    def __init__(self, tabla: str):
        """
        Constructor de clase.
        :param tabla: Nombre de la tabla en la que se insertarán las fotos.
        """

        self.db = DBManager()
        self.ent = None
        self.tabla = tabla

    def get_list_combo(self) -> Result:
        pass

    def get_list(self) -> Result:
        pass

    def get_list_by_id(self, idf: int) -> Result:
        """ Obtiene el listado completo. """

        with self.db:
            if not self.db.conn:
                QMessageBox.information(
                    None,
                    "CONEXIÓN",
                    "CONEXIÓN NO INICIALIZADA"
                )

            # Obtenemos los datos
            sql = f"""
                SELECT  ID_FOTOGRAFIA AS ID,
                        ROW_NUMBER() OVER(ORDER BY ID_FOTOGRAFIA DESC) AS NUM,
                        ID_FORANEA AS ID_FORANEA,
                        FOTOGRAFIA AS FOTOGRAFIA
                FROM    {self.tabla}                
                WHERE   ID_FORANEA = :idf
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "idf": idf
                })
                rows = [FotografiaEntity(
                    f["ID"], f["NUM"], f["ID_FORANEA"], None, f["FOTOGRAFIA"]
                ) for f in cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(rows)

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

    def insert(self, ent: FotografiaEntity) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        Parametros:
        :param ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = f"""
                INSERT INTO {self.tabla} (ID_FORANEA, FOTOGRAFIA)
                VALUES (:idf, :foto);
            """

            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "idf": ent.id_foranea,
                    "foto": sqlite3.Binary(ent.fotografia)
                })

                # Devolvemos los datos
                last_id = cursor.lastrowid
                self.db.conn.commit()
                return Result.success(last_id)

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

    def update(self, ent: FotografiaEntity) -> Result:
        """
        Actualiza el registro de la base de datos.

        Parametros:
        - ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = f"""
                UPDATE  {self.tabla}
                SET     ID_FORANEA = :idf,
                        FOTOGRAFIA = :foto
                WHERE   ID_FOTOGRAFIA = :id;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "idf": ent.id_foranea,
                    "foto": ent.fotografia,
                    "id": ent.id
                })

                # Devolvemos los datos
                self.db.conn.commit()
                return Result.success(ent.id)

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

    def delete(self, id: int) -> Result:
        """
        Elimina el registro de la base de datos.

        Parametros:
        - id: Id del registro a aliminar.
        """

        with self.db:
            # Obtenemos los datos
            sql = f"""
                DELETE FROM {self.tabla}
                WHERE       ID_FOTOGRAFIA = :id;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {"id": id})

                # Devolvemos los datos
                self.db.conn.commit()
                return Result.success(id)

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

