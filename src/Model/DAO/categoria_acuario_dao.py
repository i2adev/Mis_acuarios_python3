"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Comentarios:
    DAO para la entidad CategoriaAcuarioEntity.
"""
from __future__ import annotations

import sqlite3
import traceback
from typing import List

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Services.Result.result import Result


class CategoriaAcuarioDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    CategoriaAcuarioEntity.
    """

    def __init__(self) -> None:
        """Constructor de clase."""
        self.db = DBManager()

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """Obtiene el listado completo ordenado por categoría."""

        sql = (
            """
            SELECT  ID_CATEGORIA_ACUARIO AS ID,
                    ROW_NUMBER() OVER(ORDER BY CATEGORIA_ACUARIO) AS NUM,
                    CATEGORIA_ACUARIO AS CATEGORIA,
                    OBSERVACIONES
            FROM    CATEGORIAS_ACUARIO
            ORDER BY CATEGORIA_ACUARIO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    CategoriaAcuarioEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        categoria=f["CATEGORIA"],
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
        Obtiene el valor NÚM. de la vista VISTA_CATEGORIAS_ACUARIO dado
        un ID.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            SELECT NUM
            FROM   VISTA_CATEGORIAS_ACUARIO
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
                return Result.failure(f"NO SE ENCONTRÓ NINGÚN RESULTADO CON EL ID '{id_}'.")

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
    def get_list_combo(self) -> Result(List[CategoriaAcuarioEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """
        sql = (
            """
            SELECT  ID_CATEGORIA_ACUARIO AS ID,
                    CATEGORIA_ACUARIO     AS VALUE
            FROM    CATEGORIAS_ACUARIO
            ORDER BY CATEGORIA_ACUARIO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    CategoriaAcuarioEntity(
                        id=f["ID"],
                        num=None,
                        categoria=f["VALUE"],
                        observaciones=None
                    )
                    for f in rows
                ]
                return Result.success(valores)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def insert(self, ent: CategoriaAcuarioEntity) -> Result(int):
        """Inserta un nuevo registro y devuelve el ID generado."""

        sql = (
            """
            INSERT INTO CATEGORIAS_ACUARIO (CATEGORIA_ACUARIO, OBSERVACIONES)
            VALUES (:cat, :descripcion);
            """
        )
        params = {"cat": ent.categoria, "descripcion": ent.observaciones}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(cur.lastrowid)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def update(self, ent: CategoriaAcuarioEntity) -> Result(int):
        """Actualiza un registro. Devuelve el ID de la entidad modificada."""

        sql = (
            """
            UPDATE  CATEGORIAS_ACUARIO
            SET     CATEGORIA_ACUARIO = :cat,
                    OBSERVACIONES     = :descripcion
            WHERE   ID_CATEGORIA_ACUARIO = :id;
            """
        )
        params = {"id": ent.id, "cat": ent.categoria, "descripcion": ent.observaciones}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(ent.id)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def delete(self, id_: int) -> Result(int):
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM CATEGORIAS_ACUARIO
            WHERE ID_CATEGORIA_ACUARIO = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(id_)

        except sqlite3.IntegrityError as e:
            # traceback.print_exc()
            return Result.failure(f"[INTEGRITY ERROR]\n {e}")
        except sqlite3.OperationalError as e:
            # traceback.print_exc()
            return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
        except sqlite3.ProgrammingError as e:
            # traceback.print_exc()
            return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
        except sqlite3.DatabaseError as e:
            # traceback.print_exc()
            return Result.failure(f"[DATABASE ERROR]\n {e}")
        except sqlite3.Error as e:
            # traceback.print_exc()
            return Result.failure(f"[SQLITE ERROR]\n {e}")


