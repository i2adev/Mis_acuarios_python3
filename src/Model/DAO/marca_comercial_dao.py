"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/07/2025
Comentarios:
    Módulo que contiene la vista de la entidad MARCA COMERCIAL.
"""
import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.database import DBManager
from Model.Entities.marca_comercial_entity import MarcaComercialEntity
from Services.Result.result import Result


class MarcaComercialDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    MarcaComercialEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[MarcaComercialEntity]):
        """Obtiene el listado completo ordenado por marca."""

        sql = (
            """
            SELECT    M.ID_MARCA AS ID,
                      ROW_NUMBER() OVER(ORDER BY M.MARCA) AS NUM,
                      M.MARCA AS MARCA,
                      M.DIRECCION AS DIRECCXION,
                      M.COD_POSTAL AS CODIGO_POSTAL,
                      M.POBLACION AS POBLACION,
                      M.PROVINCIA AS PROVINCIA,
                      P.PAIS AS PAIS,
                      M.OBSERVACIONES
            FROM      MARCAS_COMERCIALES M
            LEFT JOIN PAISES P
            ON        M.ID_PAIS = P.ID_PAIS;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    MarcaComercialEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        nombre_marca=f["MARCA"],
                        direccion=f["DIRECCCION"],
                        cod_postal=f["CODIGO_POSTAL"],
                        poblacion=f["POBLACION"],
                        provincia=f["PROVINCIA"],
                        id_pais=f["PAIS"],
                        observaciones=f["OBSERVACIONES"]
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
    def get_list_combo(self) -> Result(list[MarcaComercialEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        """

        sql = (
            """
            SELECT    ID_MARCA AS ID,
                      MARCA AS VALUE
            FROM      MARCAS_COMERCIALES
            ORDER BY  MARCA;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    MarcaComercialEntity(
                        id=f["ID"],
                        nombre_marca=f["VALUE"]
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

    def insert(self, ent: MarcaComercialEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO MARCAS_COMERCIALES 
                        (MARCA, DIRECCION, COD_POSTAL, POBLACION, PROVINCIA, 
                        ID_PAIS, OBSERVACIONES)
            VALUES      (:marca, :direccion, :codp, :poblacion, :provincia, 
                        :idp, :descripcion);
            """
        )
        params = {
            "marca": ent.nombre_marca,
            "direccion": ent.direccion,
            "codp": ent.cod_postal,
            "poblacion": ent.poblacion,
            "provincia": ent.provincia,
            "idp": ent.id_pais,
            "descripcion": ent.observaciones
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

    def update(self, ent: MarcaComercialEntity) -> Result(int):
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  MARCAS_COMERCIALES
            SET     MARCA = :marca,
                    DIRECCION = :direccion,
                    COD_POSTAL = :codp,
                    POBLACION = :poblacion,
                    PROVINCIA = :provincia,
                    ID_PAIS = :idp,
                    OBSERVACIONES = :descripcion
            WHERE   ID_MARCA = :id;
            """
        )
        params = {
            "id": ent.id,
            "marca": ent.nombre_marca,
            "direccion": ent.direccion,
            "codp": ent.cod_postal,
            "poblacion": ent.poblacion,
            "provincia": ent.provincia,
            "idp": ent.id_pais,
            "descripcion": ent.observaciones
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

    def delete(self, id_: int) -> Result(int):
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM MARCAS_COMERCIALES
            WHERE ID_MARCA = :id;
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
