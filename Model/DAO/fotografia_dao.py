"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad CATEGORÍA DE ACUARIO.
"""
import sqlite3
import traceback


from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.fotografia_entity import FotografiaEntity
from Services.Result.result import Result


class FotografiaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    FotografiaEntity.
    """

    def __init__(self, tabla: str):
        """
        Constructor de clase.
        :param tabla: Nombre de la tabla en la que se insertarán las fotos.
        """

        self.db = DBManager()
        self.ent = None
        self.tabla = tabla

    def get_list_combo(self) -> Result:
        pass

    def get_list(self) -> Result:
        pass

    # ------------------------------------------------------------------
    def get_list_by_id(self, id_f: int) -> Result:
        """
        Obtiene el valor NÚM. de la entidad dado un ID.
        :param id_f: ID de la entidad
        """

        sql = (
            f"""
            SELECT  ID_FOTOGRAFIA AS ID,
                    ROW_NUMBER() OVER(ORDER BY ID_FOTOGRAFIA DESC) AS NUM,
                    ID_FORANEA AS ID_FORANEA,
                    FOTOGRAFIA AS FOTOGRAFIA
            FROM    {self.tabla}
            WHERE   ID_FORANEA = :idf
            """
        )

        params = {"idf": id_f}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)

                rows = cur.fetchall()
                valores = [
                    FotografiaEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_foranea=f["ID_FORANEA"],
                        ruta=None,
                        fotografia=f["FOTOGRAFIA"],
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
    def insert(self, ent: FotografiaEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            f"""
            INSERT INTO {self.tabla} (ID_FORANEA, FOTOGRAFIA)
            VALUES (:idf, :foto);
            """
        )
        params = {
                    "idf": ent.id_foranea,
                    "foto": sqlite3.Binary(ent.fotografia)
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
    def update(self, ent: FotografiaEntity) -> Result:
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            f"""
            UPDATE  {self.tabla}
            SET     ID_FORANEA = :idf,
                    FOTOGRAFIA = :foto
            WHERE   ID_FOTOGRAFIA = :id;
            """
        )
        params = {
                    "idf": ent.id_foranea,
                    "foto": ent.fotografia,
                    "id": ent.id
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
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            f"""
            DELETE FROM {self.tabla}
            WHERE       ID_FOTOGRAFIA = :id;
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

