"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Commentarios:
    Módulo que contiene el DAO de la URNA.
"""
import sqlite3
import traceback

from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.urna_entity import UrnaEntity
from Services.Result.result import Result


class UrnaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    UrnaEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[UrnaEntity]):
        """Obtiene el listado completo ordenado por categoría."""

        sql = (
            """
            SELECT    A.ID_URNA AS ID,
                      ROW_NUMBER() OVER (ORDER BY M.MARCA, A.MODELO) AS NUM,
                      M.MARCA AS MARCA,
                      A.MODELO AS MODELO,
                      A.ANCHURA AS ANCHURA,
                      A.PROFUNDIDAD AS PROFUNDIDAD,
                      A.ALTURA AS ALTURA,
                      A.GROSOR_CRISTAL AS GROSOR,
                      A.VOLUMEN_TANQUE AS VOLUMEN_BRUTO,
                      T.MATERIAL AS MATERIAL,
                      A.DESCRIPCION AS DESCRIPCION
            FROM      URNAS AS A
            LEFT JOIN MARCAS_COMERCIALES AS M ON A.ID_MARCA = M.ID_MARCA
            LEFT JOIN MATERIALES_URNA T ON A.ID_MATERIAL = T.ID_MATERIAL;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    UrnaEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_marca=f["MARCA"],
                        modelo=f["MODELO"],
                        anchura=f["ANCHURA"],
                        profundidad=f["PROFUNDIDAD"],
                        altura=f["ALTURA"],
                        grosor_cristal=f["GROSOR"],
                        volumen_tanque=f["VOLUMEN_BRUTO"],
                        id_material=f["MATERIAL"],
                        descripcion=f["DESCRIPCION"]
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
    def get_list_combo(self) -> Result(list[UrnaEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT    A.ID_ACUARIO AS ID,
                      CONCAT(M.MARCA, ' ', A.MODELO) AS VALUE
            FROM      URNAS AS A
            LEFT JOIN MARCAS_COMERCIALES AS M
            ON        A.ID_MARCA = M.ID_MARCA
            ORDER BY  VALUE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    UrnaEntity(
                        id=f["ID"],
                        num=None,
                        id_marca=None,
                        modelo=f["VALUE"],
                        anchura=None,
                        profundidad=None,
                        altura=None,
                        grosor_cristal=None,
                        volumen_tanque=None,
                        id_material=None,
                        descripcion=None
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
    def insert(self, ent: UrnaEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO URNAS 
                   (ID_MARCA, MODELO, ANCHURA, PROFUNDIDAD,  ALTURA, 
                    GROSOR_CRISTAL, VOLUMEN_TANQUE, ID_MATERIAL, 
                    DESCRIPCION)
            VALUES  (:idm, :modelo, :anch, :prof, :alt, :grosor, :vol, 
                    :mat, :obs);
            """
        )

        params = {
            "idm": ent.id_marca,
            "modelo": ent.modelo,
            "anch": ent.anchura,
            "prof": ent.profundidad,
            "alt": ent.altura,
            "grosor": ent.grosor_cristal,
            "vol": ent.volumen_tanque,
            "mat": ent.id_material,
            "obs": ent.descripcion
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
    def update(self, ent: UrnaEntity) -> Result(int):

        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
                UPDATE  URNAS
                SET     ID_MARCA = :idm,
                        MODELO = :modelo,
                        ANCHURA = :anch,
                        PROFUNDIDAD = :prof,
                        ALTURA = :alt,
                        GROSOR_CRISTAL = :grosor,
                        VOLUMEN_TANQUE = :vol,
                        ID_MATERIAL = :mat,
                        DESCRIPCION = :obs
                WHERE   ID_URNA = :id;
            """
        )

        params = {
            "id": ent.id,
            "idm": ent.id_marca,
            "modelo": ent.modelo,
            "anch": ent.anchura,
            "prof": ent.profundidad,
            "alt": ent.altura,
            "grosor": ent.grosor_cristal,
            "vol": ent.volumen_tanque,
            "mat": ent.id_material,
            "obs": ent.descripcion
        }

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
            DELETE FROM URNAS
            WHERE       ID_URNA = :id;
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

