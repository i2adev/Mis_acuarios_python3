"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad CATEGORÍA DE ACUARIO.
"""
from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.fotografia import FotografiaEntity
from Services.Result.result import Result


class FotografiaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    FotografiaEntity.
    """

    def get_list_combo(self) -> Result:
        pass

    def get_list(self) -> Result:
        pass

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    def get_list_id(self, tabla: str, idf: int) -> Result:
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
                WHERE   ID_FORANEA = :idf
                FROM    {tabla}
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "idf": idf
                })
                value = [FotografiaEntity(
                    f["ID"], f["NUM"], f["ID_FORANEA"], f["FOTOGRAFIA"]
                ) for f in cursor.fetchall()]

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

    def insert(self, ent: FotografiaEntity, tabla: str) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        Parametros:
        :param ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = f"""
                INSERT INTO {tabla} (ID_FORANEA, FOTOGRAFIA)
                VALUES (:idf, :foto);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "idf": ent.id,
                    "foto": ent.fotografia
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

    def update(self, ent: FotografiaEntity, tabla: str) -> Result:
        """
        Actualiza el registro de la base de datos.

        Parametros:
        - ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = f"""
                UPDATE  {tabla}
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

    def delete(self, id: int, tabla: str) -> Result:
        """
        Elimina el registro de la base de datos.

        Parametros:
        - id: Id del registro a aliminar.
        """

        with self.db:
            # Obtenemos los datos
            sql = f"""
                DELETE FROM {tabla}
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

