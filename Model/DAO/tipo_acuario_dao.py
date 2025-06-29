"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad TIPO DE ACUARIO.
"""
from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Services.Result.result import Result


class TipoAcuarioDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    TipoAcuarioEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    def get_list(self) -> Result:
        """ Obtiene el listado completo. """

        with self.db:
            if not self.db.conn:
                QMessageBox.information(
                    None,
                    "CONEXIÓN",
                    "CONEXIÓN NO INICIALIZADA"
                )

            # Obtenemos los datos
            sql = """
                SELECT   ID_TIPO AS ID,
                         ROW_NUMBER() OVER(
                             ORDER BY TIPO_ACUARIO, SUBTIPO_ACUARIO
                         ) AS NUM,
                         TIPO_ACUARIO AS TIPO,
                         SUBTIPO_ACUARIO AS SUBTIPO,
                         OBSERVACIONES
                FROM     TIPOS_ACUARIO;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                value = [TipoAcuarioEntity(
                    f["ID"], f["NUM"], f["TIPO"], f["SUBTIPO"],
                    f["OBSERVACIONES"]
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

    def get_list_combo(self):
        """ Obtiene el listado para el combo. """

        with self.db:
            # # Chequeamos que la base de datos está abierta
            # if not self.db.is_opened():
            #     self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                SELECT  ID_TIPO AS ID,
                        TIPO_ACUARIO AS TIPO,
                        SUBTIPO_ACUARIO AS SUBTIPO
                FROM    TIPOS_ACUARIO;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [TipoAcuarioEntity(
                    None, None, f["TIPO"], f["SUBTIPO"], None)
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

    def insert(self, ent: TipoAcuarioEntity) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        Parametros:
        - ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                INSERT INTO TIPOS_ACUARIO 
                (TIPO_ACUARIO, SUBTIPO_ACUARIO, OBSERVACIONES)
                VALUES (:tipo, :subtipo, :observaciones);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "tipo": ent.tipo_acuario,
                    "subtipo": ent.subtipo_acuario,
                    "observaciones": ent.observaciones
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

    def update(self, ent: TipoAcuarioEntity) -> Result:
        """
        Actualiza el registro de la base de datos.

        Parametros:
        - ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                UPDATE  TIPOS_ACUARIO
                SET     TIPO_ACUARIO = :tipo,
                        SUBTIPO_ACUARIO = :subtipo,
                        OBSERVACIONES = :observaciones
                WHERE   ID_TIPO = :id_parent
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id_parent": ent.id,
                    "tipo": ent.tipo_acuario,
                    "subtipo": ent.subtipo_acuario,
                    "observaciones": ent.observaciones
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
            sql = """
                DELETE FROM TIPOS_ACUARIO
                WHERE ID_TIPO = :id;
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