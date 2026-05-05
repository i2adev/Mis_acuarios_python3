"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/03/2026
Comentarios:
    DAO para la entidad RequerimientoIluminacionEntity.
"""
from __future__ import annotations

import sqlite3
import traceback

from Main.Model.DAO.base_dao import BaseDAO
from Main.Model.Entities.combo_data_entity import ComboDataEntity
from ModuloMaestro.Model.Entities.requerimiento_iluminacion_entity import \
    RequerimientoIluminacionEntity
from Services.Database.database import DBManager
from Services.Result.result import Result


class RequerimientoIluminacionDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    RequerimientoIluminacionEntity.
    """

    def __init__(self) -> None:
        """Constructor de clase."""
        self.db = DBManager()

    # ------------------------------------------------------------------
    def get_entity_by_id(self, ide: int) -> Result:
        """
        Obtiene el registro con el ID pasado como argumento.
        :param ide: ID de la entidad a recuperar
        """

        try:
            sql = (
                """
                SELECT *
                FROM   REQUERIMIENTOS_ILUMINACION
                WHERE  ID_REQUERIMIENTO_ILUMINACION = :id;
                """
            )

            params = {"id": ide, }

            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                row = cur.fetchone()

                # Configuramos la entidad
                ent = RequerimientoIluminacionEntity(
                    id=row[0],
                    requerimiento=row[1],
                    descripcion=row[2],
                )

                return Result.success(ent)

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

    def get_list(self) -> Result:
        """ Obtiene el listado completo. """

        sql = (
            """
            SELECT ID_REQUERIMIENTO_ILUMINACION AS ID,
                   ROW_NUMBER() OVER(ORDER BY ID_REQUERIMIENTO_ILUMINACION) AS NUM,
                   REQUERIMIENTO_ILUMINACION AS REQUERIMIENTO_ILUMINACION,
                   DESCRIPCION AS DESCRIPCION
            FROM   REQUERIMIENTOS_ILUMINACION;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    RequerimientoIluminacionEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        requerimiento=f["REQUERIMIENTO_ILUMINACION"],
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

    def get_num_by_id(self, id_: int) -> Result:
        """
        Obtiene el valor NUM de la vista

        :param id_: ID de la entidad.
        """
        sql = (
            """
            SELECT NUM
            FROM   VISTA_REQUERIMIENTOS_ILUMINACION
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
            SELECT      ID_REQUERIMIENTO_ILUMINACION AS ID,
                        REQUERIMIENTO_ILUMINACION AS VALUE
            FROM        REQUERIMIENTOS_ILUMINACION
            ORDER BY    ID;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    ComboDataEntity(
                        id=f["ID"],
                        value=f["VALUE"],
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
    def insert(self, ent: RequerimientoIluminacionEntity) -> Result:
        """ Inserta un nuevo registro y devuelve el ID generado. """

        sql = (
            """
            INSERT INTO REQUERIMIENTOS_ILUMINACION (REQUERIMIENTO_ILUMINACION, DESCRIPCION)
            VALUES (:requerimiento, :descripcion);
            """
        )
        params = {"requerimiento": ent.requerimiento,
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
    def update(self, ent: RequerimientoIluminacionEntity) -> Result(int):
        """Actualiza un registro. Devuelve el ID de la entidad modificada."""

        sql = (
            """
            UPDATE  REQUERIMIENTOS_ILUMINACION
            SET     REQUERIMIENTO_ILUMINACION = :requerimiento,
                    DESCRIPCION = :descripcion
            WHERE   ID_REQUERIMIENTO_ILUMINACION = :id;
            """
        )
        params = {"id": ent.id,
                  "requerimiento": ent.requerimiento,
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
            DELETE FROM REQUERIMIENTOS_ILUMINACION
            WHERE ID_REQUERIMIENTO_ILUMINACION = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                _ = con.execute(sql, params)
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
