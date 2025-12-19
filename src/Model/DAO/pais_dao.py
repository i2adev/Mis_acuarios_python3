"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Comentarios:
    Módulo que contiene los métodos de acceso a la base de datos de la
    entidad TIPO DE FILTRO.
"""

import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.Entities.pais_entity import PaisEntity
from Services.Result.result import Result
from Model.database import DBManager


class PaisDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad país.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[PaisEntity]):
        """Obtiene el listado completo ordenado por categoría."""

        sql = (
            """
            SELECT    ID_PAIS AS ID,
                      ROW_NUMBER() OVER(ORDER BY PAIS) AS NUM,
                      PAIS AS PAIS,
                      CONTINENTE AS CONTINENTE
            FROM      PAISES;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    PaisEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        pais=f["PAIS"],
                        continente=f["CONTINENTE"],
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
    def get_list_combo(self) -> Result(list[PaisEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y 'continente=None'.
        """

        sql = (
            """
            SELECT    ID_PAIS AS ID,
                      PAIS AS VALUE
            FROM      PAISES
            ORDER BY  PAIS;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    PaisEntity(
                        id=f["ID"],
                        num=None,
                        pais=f["VALUE"],
                        continente=None
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

    def insert(self, ent: PaisEntity) -> Result:
        pass

    def update(self, ent: PaisEntity) -> Result:
        pass

    def delete(self, id: int) -> Result:
        pass
