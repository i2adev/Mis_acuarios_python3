"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Commentarios:
    Módulo que contiene la vista de la entidad CATEGORÍA DE INCIDENCIA.
"""
import sqlite3
import traceback


from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.categoria_incidencia_entity import CategoriaIncidenciaEntity
from Services.Result.result import Result


class CategoriaIncidenciaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    CategoriaIncidenciaEntity.
    """

    def __init__(self):
        """Constructor de clase."""

        self.db = DBManager()

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[CategoriaIncidenciaEntity]):
        """Obtiene el listado completo ordenado por categoría."""

        sql = (
            """
            SELECT  ID_CATEGORIA AS ID, 
                    ROW_NUMBER()  OVER (ORDER BY CATEGORIA_INCIDENCIA) AS NUM, 
                    CATEGORIA_INCIDENCIA AS CATEGORIA, 
                    OBSERVACIONES FROM CATEGORIAS_INCIDENCIA
            FROM    CATEGORIAS_INCIDENCIA;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    CategoriaIncidenciaEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        categoria_incidencia=f["SUBTIPO"],
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

    # ------------------------------------------------------------------
    def get_num_by_id(self, id_: int) -> Result(int):
        """
        Obtiene el valor NÚM. de la entidad dado un ID.
        :param id_: ID de la entidad
        """

        sql = (
            """
            SELECT NUM
            FROM   VISTA_CATEGORIAS_INCIDENCIA
            WHERE  ID = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                row = cur.fetchone()

                if row is not None:
                    return Result.success(row["NUM"])
                return Result.failure(
                    f"NO SE ENCONTRÓ NINGÚN RESULTADO CON EL ID '{id_}'.")

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

    # ------------------------------------------------------------------
    def get_list_combo(self) -> Result(list[CategoriaIncidenciaEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT    ID_CATEGORIA AS ID,
                      CATEGORIA_INCIDENCIA AS VALUE
            FROM      CATEGORIAS_INCIDENCIA
            ORDER BY  CATEGORIA_INCIDENCIA;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    CategoriaIncidenciaEntity(
                        id=f["ID"],
                        num=None,
                        categoria_incidencia=f["VALUE"],
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

    # ------------------------------------------------------------------
    def insert(self, ent: CategoriaIncidenciaEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO CATEGORIAS_INCIDENCIA 
                        (CATEGORIA_INCIDENCIA, OBSERVACIONES)
            VALUES      (:cat, :descripcion);
            """
        )
        params = {
                    "cat": ent.categoria_incidencia,
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

    # ------------------------------------------------------------------
    def update(self, ent: CategoriaIncidenciaEntity) -> Result(int):
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  CATEGORIAS_INCIDENCIA
            SET     CATEGORIA_INCIDENCIA = :cat,
                    OBSERVACIONES = :descripcion
            WHERE   ID_CATEGORIA = :id;
            """
        )
        params = {
                    "id": ent.id,
                    "cat": ent.categoria_incidencia,
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

    # ------------------------------------------------------------------
    def delete(self, id_: int) -> Result(int):
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM CATEGORIAS_INCIDENCIA
            WHERE       ID_CATEGORIA = :id;
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
