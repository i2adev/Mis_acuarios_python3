"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      03/07/2025
Commentarios:
    Módulo que contiene la vista de la entidad SUBCATEGORÍA DE ACUARIO.
"""
from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.subcategoria_acuario_entity import SubcategoriaAcuarioEntity
from Services.Result.result import Result


class SubcategoriaAcuarioDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    SubcategoriaAcuarioEntity.
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
                SELECT    S.ID_SUBCATEGORIA_ACUARIO AS ID,
                          ROW_NUMBER() OVER(ORDER BY S.SUBCATEGORIA_ACUARIO) AS NUM,
                          C.CATEGORIA_ACUARIO AS CATEGORIA,
                          S.SUBCATEGORIA_ACUARIO AS SUBCATEGORIA,
                          S.OBSERVACIONES
                FROM      SUBCATEGORIAS_ACUARIO AS S
                LEFT JOIN CATEGORIA_ACUARIO AS C
                ON        S.ID_CATEGORIA_ACUARIO = C.ID_CATEGORIA_aCUARIO
                ORDER BY  S.SUBCATEGORIA_aCUARIO;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                value = [SubcategoriaAcuarioEntity(
                    f["ID"], f["NUM"], f["CATEGORIA"], f["SUBCATEGORIA"],
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

    # def get_list_by_categoria(self, id_cat: int) -> Result:
    #     """
    #     Obtiene el listado completo.
    #
    #     Parámetros:
    #     :param id_cat: Id de la categoría de acuario.
    #     """
    #
    #     with self.db:
    #         if not self.db.conn:
    #             QMessageBox.information(
    #                 None,
    #                 "CONEXIÓN",
    #                 "CONEXIÓN NO INICIALIZADA"
    #             )
    #
    #         # Obtenemos los datos
    #         sql = """
    #             SELECT    S.ID_SUBCATEGORIA_ACUARIO AS ID,
    #                       ROW_NUMBER() OVER(ORDER BY S.SUBCATEGORIA_ACUARIO) AS NUM,
    #                       C.CATEGORIA_ACUARIO AS CATEGORIA,
    #                       S.SUBCATEGORIA_ACUARIO AS SUBCATEGORIA,
    #                       S.OBSERVACIONES
    #             FROM      SUBCATEGORIA_ACUARIO AS S
    #             LEFT JOIN CATEGORIA_ACUARIO AS C
    #             ON        S.ID_CATEGORIA_ACUARIO = C.ID_CATEGORIA_aCUARIO
    #             WHERE     C.ID_SUBCATEGORIA_ACUARIO = :id
    #             ORDER BY  S.SUBCATEGORIA_aCUARIO;
    #         """
    #         try:
    #             cursor = self.db.conn.cursor()
    #             cursor.execute(sql, {
    #                 "id": id_cat
    #             })
    #             value = [SubcategoriaAcuarioEntity(
    #                 f["ID"], f["NUM"], f["CATEGORIA"], f["SUBCATEGORIA"],
    #                 f["OBSERVACIONES"]
    #             ) for f in cursor.fetchall()]
    #
    #             # Devolvemos los datos
    #             return Result.success(value)
    #
    #         except self.db.conn.OperationalError as e:
    #             return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
    #         except self.db.conn.ProgrammingError as e:
    #             return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
    #         except self.db.conn.DatabaseError as e:
    #             return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
    #         except self.db.conn.Error as e:
    #             return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
    #         finally:
    #             self.db.close_connection()

    def get_list_combo(self) -> Result:
        """ Obtiene el listado para el combo. """

        with self.db:
            # # Chequeamos que la base de datos está abierta
            # if not self.db.is_opened():
            #     self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                SELECT    ID_SUBCATEGORIA_ACUARIO AS ID,
                          SUBCATEGORIA_aCUARIO AS VALUE
                FROM      SUBCATEGORIAS_ACUARIO
                ORDER BY  SUBCATEGORIA_ACUARIO;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [SubcategoriaAcuarioEntity(
                    f["ID"], None, None, f["VALUE"]) for f in cursor.fetchall()]

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

    def get_list_combo_by_categoria(self, id_cat: int) -> Result:
        """ Obtiene el listado por categoría para el combo. """

        with self.db:
            # # Chequeamos que la base de datos está abierta
            # if not self.db.is_opened():
            #     self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                SELECT    ID_SUBCATEGORIA_ACUARIO AS ID,
                          SUBCATEGORIA_aCUARIO AS VALUE
                FROM      SUBCATEGORIAS_ACUARIO
                WHERE     ID_CATEGORIA_ACUARIO = :id
                ORDER BY  SUBCATEGORIA_ACUARIO;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id": id_cat
                })
                values = [SubcategoriaAcuarioEntity(
                    f["ID"], None, None, f["VALUE"]) for f in cursor.fetchall()]

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

    def insert(self, ent: SubcategoriaAcuarioEntity) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        Parametros:
        :param ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                INSERT INTO SUBCATEGORIAS_ACUARIO 
                (ID_CATEGORIA_ACUARIO, SUBCATEGORIA_ACUARIO, OBSERVACIONES)
                VALUES (:id_cat, :subcat, :descripcion);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id_cat": ent.id_categoria,
                    "subcat": ent.subcategoria,
                    "descripcion": ent.observaciones
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

    def update(self, ent: SubcategoriaAcuarioEntity) -> Result:
        """
        Actualiza el registro de la base de datos.

        Parametros:
        - ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                UPDATE SUBCATEGORIAS_ACUARIO
                SET    ID_CATEGORIA_ACUARIO = :id_cat,
                       SUBCATEGORIA_ACUARIO = :subcat,
                       OBSERVACIONES = :descripcion
                WHERE ID_SUBCATEGORIA_ACUARIO = :id;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id": ent.id,
                    "id_cat": ent.id_categoria,
                    "subcat": ent.subcategoria,
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
                DELETE FROM SUBCATEGORIAS_ACUARIO
                WHERE       ID_SUBCATEGORIA_ACUARIO = :id;
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