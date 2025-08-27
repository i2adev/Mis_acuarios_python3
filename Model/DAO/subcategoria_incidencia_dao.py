"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      03/07/2025
Commentarios:
    Módulo que contiene la vista de la entidad SUBCATEGORÍA DE ACUARIO.
"""
import sqlite3
import traceback

from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.subcategoria_incidencia import SubcategoriaIncidenciaEntity
from Services.Result.result import Result


class SubcategoriaIncidenciaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    SubcategoriaIncidenciaEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[SubcategoriaIncidenciaEntity]):
        """Obtiene el listado completo ordenado por subcategoría."""

        sql = (
            """
            SELECT      S.ID_SUBCATEGORIA AS ID,
                        ROW_NUMBER() OVER(ORDER BY S.NOMBRE_SUBCATEGORIA) AS NUM,
                        C.NOMBRE_CATEGORIA AS CATEGORIA,
                        S.NOMBRE_SUBCATEGORIA AS SUBCATEGORIA,
                        S.DESCRIPCION AS OBSERVACIONES
            FROM        SUBCATEGORIAS_INCIDENCIA S
            LEFT JOIN   CATEGORIAS_INCIDENCIA C
            ON          S.ID_CATEGORIA = C.ID_CATEGORIA;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    SubcategoriaIncidenciaEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_categoria=f["CATEGORIA"],
                        subcategoria=f["SUBCATEGORIA"],
                        observaciones=f["OBSERVACIONES"],
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

        # with self.db:
        #     if not self.db.conn:
        #         QMessageBox.information(
        #             None,
        #             "CONEXIÓN",
        #             "CONEXIÓN NO INICIALIZADA"
        #         )
        #
        #     # Obtenemos los datos
        #     sql = """
        #     SELECT      S.ID_SUBCATEGORIA AS ID,
        #                 ROW_NUMBER() OVER(ORDER BY S.NOMBRE_SUBCATEGORIA) AS NUM,
        #                 C.NOMBRE_CATEGORIA AS CATEGORIA,
        #                 S.NOMBRE_SUBCATEGORIA AS SUBCATEGORIA,
        #                 S.DESCRIPCION AS OBSERVACIONES
        #     FROM        SUBCATEGORIAS_INCIDENCIA S
        #     LEFT JOIN   CATEGORIAS_INCIDENCIA C
        #     ON          S.ID_CATEGORIA = C.ID_CATEGORIA;
        #     """
        #     try:
        #         cursor = self.db.conn.cursor()
        #         cursor.execute(sql)
        #         value = [SubcategoriaIncidenciaEntity(
        #             f["ID"], f["NUM"], f["CATEGORIA"], f["SUBCATEGORIA"],
        #             f["OBSERVACIONES"]
        #         ) for f in cursor.fetchall()]
        #
        #         # Devolvemos los datos
        #         return Result.success(value)
        #
        #     except self.db.conn.OperationalError as e:
        #         return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
        #     except self.db.conn.ProgrammingError as e:
        #         return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
        #     except self.db.conn.DatabaseError as e:
        #         return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
        #     except self.db.conn.Error as e:
        #         return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
        #     finally:
        #         self.db.close_connection()

    # ------------------------------------------------------------------
    def get_list_combo(self) -> Result(list[SubcategoriaIncidenciaEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT    ID_SUBCATEGORIA AS ID,
                      NOMBRE_SUBCATEGORIA AS VALUE
            FROM      SUBCATEGORIAS_INCIDENCIA  
            ORDER BY  NOMBRE_SUBCATEGORIA;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    SubcategoriaIncidenciaEntity(
                        id=f["ID"],
                        num=None,
                        id_categoria=None,
                        subcategoria=f["SUBCATEGORIA"],
                        observaciones=None,
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

        # with self.db:
        #     # Obtenemos los datos
        #     sql = """
        #         SELECT    ID_SUBCATEGORIA AS ID,
        #                   NOMBRE_SUBCATEGORIA AS VALUE
        #         FROM      SUBCATEGORIAS_INCIDENCIA
        #         ORDER BY  NOMBRE_SUBCATEGORIA;
        #       """
        #     try:
        #         cursor = self.db.conn.cursor()
        #         cursor.execute(sql)
        #         values = [SubcategoriaIncidenciaEntity(
        #             f["ID"], None, None, f["VALUE"]) for f in cursor.fetchall()]
        #
        #         # Devolvemos los datos
        #         return Result.success(values)
        #
        #     except self.db.conn.OperationalError as e:
        #         return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
        #     except self.db.conn.ProgrammingError as e:
        #         return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
        #     except self.db.conn.DatabaseError as e:
        #         return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
        #     except self.db.conn.Error as e:
        #         return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
        #     finally:
        #         self.db.close_connection()

    # ------------------------------------------------------------------
    def get_list_combo_by_categoria(self, id_cat: int) \
            -> Result(list[SubcategoriaIncidenciaEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT    ID_SUBCATEGORIA AS ID,
                      NOMBRE_SUBCATEGORIA AS VALUE
            FROM      SUBCATEGORIAS_INCIDENCIA  
            WHERE     ID_SUBCATEGORIA = :id
            ORDER BY  NOMBRE_SUBCATEGORIA;
            """
        )

        params = {"id": id_cat}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                rows = cur.fetchall()
                valores = [
                    SubcategoriaIncidenciaEntity(
                        id=f["ID"],
                        num=None,
                        id_categoria=None,
                        subcategoria=f["SUBCATEGORIA"],
                        observaciones=None,
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

        # with self.db:
        #     # Obtenemos los datos
        #     sql = """
        #         SELECT    ID_SUBCATEGORIA AS ID,
        #                   NOMBRE_SUBCATEGORIA AS VALUE
        #         FROM      SUBCATEGORIAS_INCIDENCIA
        #         WHERE     ID_SUBCATEGORIA = :id
        #         ORDER BY  NOMBRE_SUBCATEGORIA;
        #       """
        #     try:
        #         cursor = self.db.conn.cursor()
        #         cursor.execute(sql, {
        #             "id": id_cat
        #         })
        #         values = [SubcategoriaIncidenciaEntity(
        #             f["ID"], None, None, f["VALUE"]) for f in cursor.fetchall()]
        #
        #         # Devolvemos los datos
        #         return Result.success(values)
        #
        #     except self.db.conn.OperationalError as e:
        #         return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
        #     except self.db.conn.ProgrammingError as e:
        #         return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
        #     except self.db.conn.DatabaseError as e:
        #         return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
        #     except self.db.conn.Error as e:
        #         return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
        #     finally:
        #         self.db.close_connection()

    # ------------------------------------------------------------------
    def insert(self, ent: SubcategoriaIncidenciaEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO SUBCATEGORIAS_INCIDENCIA 
            (ID_CATEGORIA, NOMBRE_SUBCATEGORIA, DESCRIPCION)
            VALUES (:id_cat, :subcat, :descripcion);
            """
        )
        params = {
            "id_cat": ent.id_categoria,
            "subcat": ent.subcategoria,
            "descripcion": ent.observaciones
        }

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(cur.lastrowid)

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

        # with self.db:
        #     # Obtenemos los datos
        #     sql = """
        #         INSERT INTO SUBCATEGORIAS_INCIDENCIA
        #         (ID_CATEGORIA, NOMBRE_SUBCATEGORIA, DESCRIPCION)
        #         VALUES (:id_cat, :subcat, :descripcion);
        #     """
        #     try:
        #         cursor = self.db.conn.cursor()
        #         cursor.execute(sql, {
        #             "id_cat": ent.id_categoria,
        #             "subcat": ent.subcategoria,
        #             "descripcion": ent.observaciones
        #         })
        #
        #         # Devolvemos los datos
        #         last_id = cursor.lastrowid
        #         self.db.conn.commit()
        #         return Result.success(last_id)
        #
        #     except self.db.conn.OperationalError as e:
        #         return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
        #     except self.db.conn.ProgrammingError as e:
        #         return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
        #     except self.db.conn.DatabaseError as e:
        #         return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
        #     except self.db.conn.Error as e:
        #         return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
        #     finally:
        #         self.db.close_connection()

    # ------------------------------------------------------------------
    def update(self, ent: SubcategoriaIncidenciaEntity) -> Result(int):
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  SUBCATEGORIAS_INCIDENCIA
            SET     ID_CATEGORIA = :id_cat,
                    NOMBRE_SUBCATEGORIA = :subcat,
                    DESCRIPCION = :descripcion
            WHERE   ID_SUBCATEGORIA = :id
            """
        )
        params = {
            "id": ent.id,
            "id_cat": ent.id_categoria,
            "subcat": ent.subcategoria,
            "descripcion": ent.observaciones
        }

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(ent.id)

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

        # with self.db:
        #     # Obtenemos los datos
        #     sql = """
        #         UPDATE  SUBCATEGORIAS_INCIDENCIA
        #         SET     ID_CATEGORIA = :id_cat,
        #                 NOMBRE_SUBCATEGORIA = :subcat,
        #                 DESCRIPCION = :descripcion
        #         WHERE   ID_SUBCATEGORIA = :id
        #     """
        #     try:
        #         cursor = self.db.conn.cursor()
        #         cursor.execute(sql, {
        #             "id": ent.id,
        #             "id_cat": ent.id_categoria,
        #             "subcat": ent.subcategoria,
        #             "descripcion": ent.observaciones
        #         })
        #
        #         # Devolvemos los datos
        #         self.db.conn.commit()
        #         return Result.success(ent.id)
        #
        #     except self.db.conn.OperationalError as e:
        #         return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
        #     except self.db.conn.ProgrammingError as e:
        #         return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
        #     except self.db.conn.DatabaseError as e:
        #         return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
        #     except self.db.conn.Error as e:
        #         return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
        #     finally:
        #         self.db.close_connection()

    # ------------------------------------------------------------------
    def delete(self, id_: int) -> Result(int):
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM SUBCATEGORIAS_INCIDENCIA
            WHERE       ID_SUBCATEGORIA = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(id_)

        except sqlite3.IntegrityError as e:
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            return Result.failure(f"[SQLITE ERROR]\n {e}")

        # with self.db:
        #     # Obtenemos los datos
        #     sql = """
        #         DELETE FROM SUBCATEGORIAS_INCIDENCIA
        #         WHERE       ID_SUBCATEGORIA = :id;
        #     """
        #     try:
        #         cursor = self.db.conn.cursor()
        #         cursor.execute(sql, {"id": id})
        #
        #         # Devolvemos los datos
        #         self.db.conn.commit()
        #         return Result.success(id)
        #
        #     except self.db.conn.OperationalError as e:
        #         return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
        #     except self.db.conn.ProgrammingError as e:
        #         return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
        #     except self.db.conn.DatabaseError as e:
        #         return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
        #     except self.db.conn.Error as e:
        #         return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
        #     finally:
        #         self.db.close_connection()