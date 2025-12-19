"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/12/2025
Comentarios:
    Módulo que contiene la vista de la entidad COMERCIO.
"""
import sqlite3
import traceback

from Model.DAO.base_dao import BaseDAO
from Model.database import DBManager
from Model.Entities.comercio_entity import ComercioEntity
from Services.Result.result import Result


class ComercioDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    ComercioEntity.
    """

    def __init__(self):
        """Constructor de clase."""

        self.db = DBManager()

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """Obtiene el listado completo ordenado por comercio."""

        sql = (
            """
            SELECT      C.ID_COMERCIO AS ID,
                        ROW_NUMBER() OVER(ORDER BY C.COMERCIO) AS NUM,
                        C.COMERCIO AS COMERCIO,
                        C.DIRECCION AS DIRECCION,
                        C.COD_POSTAL AS COD_POSTAL,
                        C.POBLACION AS POBLACION,
                        C.PROVINCIA AS PROVINCIA,
                        P.PAIS AS PAIS,
                        C.OBSERVACIONES AS OBSERVACIONES
            FROM        COMERCIOS C
            LEFT JOIN   PAISES P ON C.ID_PAIS = P.ID_PAIS;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    ComercioEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        nombre_comercio=f["COMERCIO"],
                        direccion=f["DIRECCION"],
                        cod_postal=f["COD_POSTAL"],
                        poblacion=f["POBLACION"],
                        provincia=f["PROVINCIA"],
                        id_pais=f["PAIS"],
                        observaciones=f["OBSERVACIONES"],
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

    # # ------------------------------------------------------------------
    # def get_num_by_id(self, id_: int) -> Result(int):
    #     """
    #     Obtiene el valor NÚM. de la entidad dado un ID.
    #     :param id_: ID de la entidad
    #     """
    #
    #     sql = (
    #         """
    #         SELECT NUM
    #         FROM   VISTA_CATEGORIAS_INCIDENCIA
    #         WHERE  ID = :id;
    #         """
    #     )
    #     params = {"id": id_}
    #
    #     try:
    #         with self.db.conn as con:
    #             cur = con.cursor()
    #             cur.execute(sql, params)
    #             row = cur.fetchone()
    #
    #             if row is not None:
    #                 return Result.success(row["NUM"])
    #             return Result.failure(
    #                 f"NO SE ENCONTRÓ NINGÚN RESULTADO CON EL ID '{id_}'.")
    #
    #     except sqlite3.IntegrityError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[INTEGRITY ERROR]\n {e}")
    #     except sqlite3.OperationalError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
    #     except sqlite3.ProgrammingError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
    #     except sqlite3.DatabaseError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[DATABASE ERROR]\n {e}")
    #     except sqlite3.Error as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[SQLITE ERROR]\n {e}")

    # ------------------------------------------------------------------
    def get_list_combo(self) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        """

        sql = (
            """
            SELECT      C.ID_COMERCIO AS ID,
                        C.COMERCIO AS VALUE
            FROM        COMERCIOS C
            ORDER BY    C.COMERCIO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    ComercioEntity(
                        id=f["ID"],
                        nombre_comercio=f["VALUE"],
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
    def insert(self, ent: ComercioEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO COMERCIOS   (COMERCIO, DIRECCION, COD_POSTAL, 
                                    POBLACION, PROVINCIA, ID_PAIS, 
                                    OBSERVACIONES)
            VALUES  (:comercio, :direccion, :cod_postal, :poblacion, :provincia, 
                    :id_pais, :observaciones);
            """
        )
        params = {
            "comercio": ent.nombre_comercio,
            "direccion": ent.direccion,
            "cod_postal": ent.cod_postal,
            "poblacion": ent.poblacion,
            "provincia": ent.provincia,
            "id_pais": ent.id_pais,
            "observaciones": ent.observaciones,
        }

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
    def update(self, ent: ComercioEntity) -> Result:
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  COMERCIOS
            SET     COMERCIO = :comercio,
                    DIRECCION = :direccion,
                    COD_POSTAL = :cod_postal,
                    POBLACION = :poblacion,
                    PROVINCIA = :provincia,
                    ID_PAIS = :id_pais,
                    OBSERVACIONES = :observaciones
            WHERE   ID_COMERCIO = :id;
            """
        )
        params = {
            "id": ent.id,
            "comercio": ent.nombre_comercio,
            "direccion": ent.direccion,
            "cod_postal": ent.cod_postal,
            "poblacion": ent.poblacion,
            "provincia": ent.provincia,
            "id_pais": ent.id_pais,
            "observaciones": ent.observaciones,
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
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM COMERCIOS
            WHERE ID_COMERCIO = :id;
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
