"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      03/07/2025
Commentarios:
    Módulo que contiene la vista de la entidad SUBCATEGORÍA DE ACUARIO.
"""
import sqlite3
import traceback


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

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[SubcategoriaAcuarioEntity]):
        """Obtiene el listado completo ordenado por subcategoría."""

        sql = (
            """
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
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    SubcategoriaAcuarioEntity(
                        f["ID"], None, None, f["VALUE"]
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")
    # ------------------------------------------------------------------
    def get_list_combo(self) -> Result(list[SubcategoriaAcuarioEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT    ID_SUBCATEGORIA_ACUARIO AS ID,
                      SUBCATEGORIA_aCUARIO AS VALUE
            FROM      SUBCATEGORIAS_ACUARIO
            ORDER BY  SUBCATEGORIA_ACUARIO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    SubcategoriaAcuarioEntity(
                        f["ID"], None, None, f["VALUE"]
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def get_list_combo_by_categoria(self, id_cat: int) \
            -> Result(list[SubcategoriaAcuarioEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Lista dependiente de la categoría de acuario.
        :param id_cat: ID de la categoría de acuario
        """

        sql = (
            """
            SELECT    ID_SUBCATEGORIA_ACUARIO AS ID,
                      SUBCATEGORIA_ACUARIO AS VALUE
            FROM      SUBCATEGORIAS_ACUARIO
            WHERE     ID_CATEGORIA_ACUARIO = :id
            ORDER BY  SUBCATEGORIA_ACUARIO;
            """
        )

        params = {"id": id_cat}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                rows = cur.fetchall()
                valores = [
                    SubcategoriaAcuarioEntity(
                        f["ID"], None, None, f["VALUE"]
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def insert(self, ent: SubcategoriaAcuarioEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO SUBCATEGORIAS_ACUARIO 
            (ID_CATEGORIA_ACUARIO, SUBCATEGORIA_ACUARIO, OBSERVACIONES)
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
            traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def update(self, ent: SubcategoriaAcuarioEntity) -> Result:
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE SUBCATEGORIAS_ACUARIO
            SET    ID_CATEGORIA_ACUARIO = :id_cat,
                   SUBCATEGORIA_ACUARIO = :subcat,
                   OBSERVACIONES = :descripcion
            WHERE ID_SUBCATEGORIA_ACUARIO = :id;
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
            traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def delete(self, id_: int) -> Result(int):
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM SUBCATEGORIAS_ACUARIO
            WHERE       ID_SUBCATEGORIA_ACUARIO = :id;
            """
        )

        params = {"id": id_}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(id_)

        except sqlite3.IntegrityError as e:
            traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

