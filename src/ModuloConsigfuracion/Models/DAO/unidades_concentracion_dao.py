"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  24/11/2026
Comentarios:
    DAO de las unidades de concentración.
"""
import sqlite3

from Main.Model.DAO.base_dao import BaseDAO
from Main.Model.Entities.combo_data_entity import ComboDataEntity
from ModuloMaestro.Model.Entities.base_entity import BaseEntity
from Services.Database.database import DBManager
from Services.Result.result import Result


class UnidadesConcentracionDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    unidades de concentración.
    """

    def __init__(self) -> None:
        """Constructor de clase."""

        self.db = DBManager()

    def get_list(self) -> Result:
        pass

    # ------------------------------------------------------------------
    def get_list_combo(self) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        """
        sql = (
            """
            SELECT  SIMBOLO AS ID,
                    UNIDAD_CONCENTRACION || ' (' || SIMBOLO || ')' AS VALUE
            FROM    UNIDADES_CONCENTRACION;
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

    def insert(self, ent: BaseEntity) -> Result:
        pass

    def update(self, ent: BaseEntity) -> Result:
        pass

    def delete(self, id: int) -> Result:
        pass
