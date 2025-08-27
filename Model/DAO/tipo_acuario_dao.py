"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad TIPO DE ACUARIO.
"""
import sqlite3
import traceback


from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Services.Result.result import Result


class TipoAcuarioDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    TipoAcuarioEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[TipoAcuarioEntity]):
        """Obtiene el listado completo ordenado por categoría."""

        sql = (
            """
            SELECT       TA.ID_TIPO AS ID,
                         ROW_NUMBER() OVER(
                             ORDER BY CA.CATEGORIA_ACUARIO, 
                             SA.SUBCATEGORIA_ACUARIO
                         ) AS NUM,
                         CA.CATEGORIA_ACUARIO AS TIPO,
                         SA.SUBCATEGORIA_ACUARIO AS SUBTIPO,
                         TA.OBSERVACIONES
            FROM         TIPOS_ACUARIO AS TA
            LEFT JOIN    CATEGORIA_ACUARIO AS CA
            ON           TA.ID_CATEGORIA_aCUARIO = CA.ID_CATEGORIA_ACUARIO
            LEFT JOIN    SUBCATEGORIA_ACUARIO AS SA
            ON           TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    TipoAcuarioEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_categoria_acuario=f["TIPO"],
                        id_subcategoria_acuario=f["SUBTIPO"],
                        observaciones=f["OBSERVACIONES"]
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
    def get_list_combo(self) -> Result(list[TipoAcuarioEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT       TA.ID_TIPO AS ID,
                         CA.CATEGORIA_ACUARIO || ' / ' 
                         || SA.SUBCATEGORIA_ACUARIO AS VALUE
            FROM         TIPOS_ACUARIO AS TA
            LEFT JOIN    CATEGORIA_ACUARIO AS CA
            ON           TA.ID_CATEGORIA_aCUARIO = CA.ID_CATEGORIA_ACUARIO
            LEFT JOIN    SUBCATEGORIA_ACUARIO AS SA
            ON          TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    TipoAcuarioEntity(
                        id=f["ID"],
                        num=None,
                        id_categoria_acuario=f["VALUE"],
                        id_subcategoria_acuario=None,
                        observaciones=None
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
    def get_list_combo_tipos_acuario(self) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT    ID_CATEGORIA_ACUARIO AS ID,
                      CATEGORIA_ACUARIO AS VALUE
            FROM      CATEGORIA_ACUARIO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    TipoAcuarioEntity(
                        id=f["ID"],
                        num=None,
                        id_categoria_acuario=f["VALUE"],
                        id_subcategoria_acuario=None,
                        observaciones=None
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
    def insert(self, ent: TipoAcuarioEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO     TIPOS_ACUARIO
                            (ID_CATEGORIA_ACUARIO, ID_SUBCATEGORIA_ACUARIO, 
                            OBSERVACIONES)
            VALUES          (:cat, :subcat, :descripcion)
            """
        )
        params = {
            "cat": ent.id_categoria_acuario,
            "subcat": ent.id_subcategoria_acuario,
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
    def update(self, ent: TipoAcuarioEntity) -> Result:
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  TIPOS_ACUARIO
            SET     ID_CATEGORIA_ACUARIO = :cat,
                    ID_SUBCATEGORIA_ACUARIO = :subcat,
                    OBSERVACIONES = :descripcion
            WHERE   ID_TIPO = :id_parent
            """
        )
        params = {
                    "id_parent": ent.id,
                    "cat": ent.id_categoria_acuario,
                    "subcat": ent.id_subcategoria_acuario,
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
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM TIPOS_ACUARIO
            WHERE ID_TIPO = :id;
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


