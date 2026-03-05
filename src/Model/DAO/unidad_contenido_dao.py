"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      05/03/2026
Comentarios:
    DAO para la entidad UnidadContenidoEntity.
"""

import sqlite3
import traceback

from Model.DAO.base_dao import BaseDAO
from Model.Entities.unidades_contenido_entity import UnidadContenidoEntity
from Model.database import DBManager
from Services.Result.result import Result


class UnidadContenidoDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    UnidadContenidoEntity.
    """

    def __init__(self) -> None:
        """ Constructor de clase. """

        self.db = DBManager()

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """ Obtiene el listado completo ordenado por categoría. """

        sql = (
            """
            SELECT ID_UNIDAD_CONTENIDO AS ID,
                   ROW_NUMBER() OVER(ORDER BY ID_UNIDAD_CONTENIDO) AS NUM,
                   UNIDAD AS UNIDAD,
                   DESCRIPCION AS DESCRIPCION
            FROM   UNIDADES_CONTENIDO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    UnidadContenidoEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        unidad=f["UNIDAD"],
                        descripcion=f["DESCRIPCION"],
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
    def get_num_by_id(self, id_: int) -> Result:
        """
        Obtiene el valor NÚM. de la vista VISTA_UNIDAD_CONTENIDO dado
        un ID.
        """
        sql = (
            """
            SELECT NUM
            FROM   VISTA_UNIDAD_CONTENIDO
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
    def get_list_combo(self) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        """

        sql = (
            """
            SELECT    ID_UNIDAD_CONTENIDO AS ID,
                      UNIDAD || ' (' || DESCRIPCION || ')' AS VALUE
            FROM      UNIDADES_CONTENIDO
            ORDER BY  ID_UNIDAD_CONTENIDO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    UnidadContenidoEntity(
                        id=f["ID"],
                        descripcion=f["VALUE"],
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
    def insert(self, ent: UnidadContenidoEntity) -> Result:
        """Inserta un nuevo registro y devuelve el ID generado."""

        sql = (
            """
            INSERT INTO UNIDADES_CONTENIDO (UNIDAD, DESCRIPCION)
            VALUES (:unidad, :descripcion);
            """
        )
        params = {"unidad": ent.unidad, "descripcion": ent.descripcion}

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
    def update(self, ent: UnidadContenidoEntity) -> Result:
        """Actualiza un registro. Devuelve el ID de la entidad modificada."""

        sql = (
            """
            UPDATE  UNIDADES_CONTENIDO
            SET     UNIDAD = :unidad,
                    DESCRIPCION = :descripcion
            WHERE   ID_UNIDAD_CONTENIDO = :id;
            """
        )
        params = {"id": ent.id, "unidad": ent.unidad,
                  "descripcion": ent.descripcion}

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
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM UNIDADES_CONTENIDO
            WHERE       ID_UNIDAD_CONTENIDO = :id;
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
