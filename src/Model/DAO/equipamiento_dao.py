"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/12/2025
Comentarios:
    Módulo que contiene el DAO del EQUIPAMIENTO.
"""
import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.equipamiento_entity import EquipamientoEntity
from Services.Result.result import Result


class EquipamientoDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    EquipamientoEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """Obtiene el listado completo ordenado por marca y modelo."""

        try:
            sql = (
                """
                SELECT  E.ID_EQUIPAMIENTO AS ID,
                        ROW_NUMBER() OVER(ORDER BY E.ID_MARCA, E.MODELO) AS NUM,
                        C.CATEGORIA_EQUIPAMIENTO AS CATEGORIA,
                        E.ID_MARCA AS MARCA,
                        E.MODELO AS MODELO,
                        E.NUMERO_SERIE AS NUMERO_SERIE,
                        IFNULL(strftime('%d/%m/%Y', E.FECHA_ALTA, 'unixepoch', 'localtime'), '') AS FECHA_ALTA, 
                        IFNULL(strftime('%d/%m/%Y', E.FECHA_BAJA, 'unixepoch', 'localtime'), '') AS FECHA_BAJA,
                        E.MOTIVO_BAJA AS MOTIVO_BAJA,
                        E.DESCRIPCION AS DESCRIPCION
                FROM    EQUIPAMIENTOS E
                LEFT JOIN CATEGORIAS_EQUIPAMIENTO C ON E.ID_CATEGORIA_EQUIPAMIENTO = C.ID_CATEGORIA_EQUIPAMIENTO
                LEFT JOIN MARCAS_COMERCIALES M ON E.ID_MARCA = M.ID_MARCA;
                """
            )

            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    EquipamientoEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_categoria=f["CATEGORIA"],
                        id_marca=f["MARCA"],
                        modelo=f["MODELO"],
                        numero_serie=f["NUMERO_SERIE"],
                        fecha_alta=f["FECHA_ALTA"],
                        fecha_baja=f["FECHA_BAJA"],
                        motivo_baja=f["MOTIVO_BAJA"],
                        descripcion=f["DESCRIPCION"],
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
    def get_list_combo(self) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT  E.ID_EQUIPAMIENTO AS ID,
                    '(' || C.CATEGORIA_EQUIPAMIENTO || ') ' || M.MARCA || ' ' || E.MODELO AS VALUE
            FROM    EQUIPAMIENTOS E
            LEFT JOIN CATEGORIAS_EQUIPAMIENTO C ON E.ID_CATEGORIA_EQUIPAMIENTO = C.ID_CATEGORIA_EQUIPAMIENTO
            LEFT JOIN MARCAS_COMERCIALES M ON E.ID_MARCA = M.ID_MARCA
            ORDER BY  VALUE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    EquipamientoEntity(
                        id=f["ID"],
                        modelo=f["VALUE"]
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
    def insert(self, ent: EquipamientoEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO EQUIPAMIENTOS 
                (ID_CATEGORIA_EQUIPAMIENTO, ID_MARCA, MODELO, NUMERO_SERIE,
                 FECHA_ALTA, FECHA_BAJA, MOTIVO_BAJA, DESCRIPCION)
            VALUES (:id_categoria, :id_marca, :modelo, :num_serie, :f_alta,
                    :f_baja, :motivo_baja, :descripcion);
            """
        )

        params = {
            "id_categoria": ent.id_categoria,
            "id_marca": ent.id_marca,
            "modelo": ent.modelo,
            "num_serie": ent.numero_serie,
            "f_alta": ent.fecha_alta,
            "f_baja": ent.fecha_baja,
            "motivo_baja": ent.motivo_baja,
            "descripcion": ent.descripcion
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
    def update(self, ent: EquipamientoEntity) -> Result:

        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  EQUIPAMIENTOS
            SET     ID_EQUIPAMIENTO = :id,
                    ID_CATEGORIA_EQUIPAMIENTO = :id_categoria,
                    ID_MARCA = :id_marca,
                    MODELO = :modelo,
                    NUMERO_SERIE = :num_serie,
                    FECHA_ALTA = :f_alta,
                    FECHA_BAJA = :f_baja,
                    MOTIVO_BAJA = :motivo_baja,
                    DESCRIPCION = :descripcion
            WHERE   ID_EQUIPAMIENTO = :id;
            """
        )

        params = {
            "id": ent.id,
            "id_categoria": ent.id_categoria,
            "id_marca": ent.id_marca,
            "modelo": ent.modelo,
            "num_serie": ent.numero_serie,
            "f_alta": ent.fecha_alta,
            "f_baja": ent.fecha_baja,
            "motivo_baja": ent.motivo_baja,
            "descripcion": ent.descripcion
        }

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
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM EQUIPAMIENTOS
            WHERE       ID_EQUIPAMIENTO = :id;
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
