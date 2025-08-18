"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad TIPO DE ACUARIO.
"""
import traceback

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
            SELECT       TA.ID_TIPO AS ID,
                         ROW_NUMBER() OVER(
                             ORDER BY CA.CATEGORIA_ACUARIO, 
                             SA.SUBCATEGORIA_ACUARIO
                         ) AS NUM,
                         CA.CATEGORIA_ACUARIO AS TIPO,
                         SA.SUBCATEGORIA_ACUARIO AS SUBTIPO,
                         TA.OBSERVACIONES
            FROM         TIPOS_ACUARIO AS TA
            LEFT JOIN    CATEGORIA_ACUARIO AS CA
            ON           TA.ID_CATEGORIA_aCUARIO = CA.ID_CATEGORIA_ACUARIO
            LEFT JOIN    SUBCATEGORIA_ACUARIO AS SA
            ON           TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO;
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
            SELECT       TA.ID_TIPO AS ID,
                         CA.CATEGORIA_ACUARIO || ' / ' 
                         || SA.SUBCATEGORIA_ACUARIO AS VALUE
            FROM         TIPOS_ACUARIO AS TA
            LEFT JOIN    CATEGORIA_ACUARIO AS CA
            ON           TA.ID_CATEGORIA_aCUARIO = CA.ID_CATEGORIA_ACUARIO
            LEFT JOIN    SUBCATEGORIA_ACUARIO AS SA
            ON           TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO;
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

    def get_list_tipos_acuario(self) -> Result:
        """ Obtiene el listado de los tipos de acuario """

        with self.db:
            # # Chequeamos que la base de datos está abierta
            # if not self.db.is_opened():
            #     self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                SELECT    ID_CATEGORIA_ACUARIO AS ID,
                          CATEGORIA_ACUARIO AS VALUE
                FROM      CATEGORIA_ACUARIO;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [TipoAcuarioEntity(
                    f["ID"], None, f["VALUE"], None, None)
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
                INSERT INTO     TIPOS_ACUARIO
                                (ID_CATEGORIA_ACUARIO, ID_SUBCATEGORIA_ACUARIO, 
                                OBSERVACIONES)
                VALUES          (:cat, :subcat, :descripcion)
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "cat": ent.id_categoria_acuario,
                    "subcat": ent.id_subcategoria_acuario,
                    "descripcion": ent.observaciones
                })

                # Devolvemos los datos
                last_id = cursor.lastrowid
                self.db.conn.commit()
                return Result.success(last_id)

            except self.db.conn.OperationalError as e:
                traceback.print_exc()
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
                SET     ID_CATEGORIA_ACUARIO = :cat,
                        ID_SUBCATEGORIA_ACUARIO = :subcat,
                        OBSERVACIONES = :descripcion
                WHERE   ID_TIPO = :id_parent
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id_parent": ent.id,
                    "cat": ent.id_categoria_acuario,
                    "subcat": ent.id_subcategoria_acuario,
                    "descripcion": ent.observaciones
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

