"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      13/03/2026
Comentarios:
    DAO para la entidad DificultadPlantaEntity.
"""
from __future__ import annotations

import sqlite3
import traceback

from Model.DAO.base_dao import BaseDAO
from Model.Entities.dificultad_planta_entity import DificultadPlantaEntity
from Model.database import DBManager
from Services.Result.result import Result


class DificultadPlantaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    DificultadPlantaEntity.
    """

    def __init__(self) -> None:
        """Constructor de clase."""
        self.db = DBManager()

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """ Obtiene el listado completo. """

        sql = (
            """
            SELECT  ID_DIFICULTAD AS ID,
                    ROW_NUMBER() OVER(ORDER BY NIVEL) AS NUM,
                    NIVEL AS NIVEL,
                    DIFICULTAD_PLANTA AS DIFICULTAD,
                    DESCRIPCION AS DESCRIPCION
            FROM    DIFICULTADES_PLANTAS;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    DificultadPlantaEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        nivel=f["NIVEL"],
                        dificultad=f["DIFICULTAD"],
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
        Obtiene el valor NUM de la vista

        :param id_: ID de la entidad.
        """
        sql = (
            """
            SELECT NUM
            FROM   VISTA_DIFICULTAD_PLANTAS
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
            SELECT      ID_DIFICULTAD AS ID,
                        NIVEL || ' (' || DIFICULTAD_PLANTA || ')' AS VALUE
            FROM        DIFICULTADES_PLANTAS
            ORDER BY    NIVEL;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    DificultadPlantaEntity(
                        id=f["ID"],
                        dificultad=f["VALUE"],
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
    def insert(self, ent: DificultadPlantaEntity) -> Result:
        """Inserta un nuevo registro y devuelve el ID generado."""

        sql = (
            """
            INSERT INTO DIFICULTADES_PLANTAS (NIVEL, DIFICULTAD_PLANTA, 
                                              DESCRIPCION)
            VALUES (:nivel, :dificultad, :descripcion);
            """
        )
        params = {"nivel": ent.nivel,
                  "dificultad": ent.dificultad,
                  "descripcion": ent.descripcion}

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
    def update(self, ent: DificultadPlantaEntity) -> Result(int):
        """Actualiza un registro. Devuelve el ID de la entidad modificada."""

        sql = (
            """
            UPDATE  DIFICULTADES_PLANTAS
            SET     NIVEL = :nivel,
                    DIFICULTAD_PLANTA = :dificultad,
                    DESCRIPCION = :descripcion
            WHERE   ID_DIFICULTAD = :id;
            """
        )
        params = {"id": ent.id,
                  "nivel": ent.nivel,
                  "dificultad": ent.dificultad,
                  "descripcion": ent.descripcion}
        try:
            with self.db.conn as con:
                _ = con.execute(sql, params)
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
            DELETE FROM DIFICULTADES_PLANTAS
            WHERE ID_DIFICULTAD = :id;
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
