"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      29/09/2026
Comentarios:
    Módulo de acceso a datos de la tarjeta de acuario
"""
import sqlite3
from abc import abstractclassmethod

from Main.Model.DAO.base_dao import BaseDAO
from ModuloMaestro.Model.Entities.base_entity import BaseEntity
from ModuloProyecto.Models.Entities.tarjeta_acuaerio_entity import \
    TarjetaAcuarioEntity
from Services.Database.database import DBManager
from Services.Result.result import Result


class TarjetaAcuarioDAO:
    """
    Clase de accesoa a datos de la tarjeta de acuario.
    """

    def __init__(self):
        """ Constructor de la clase. """

        self.db = DBManager()
        self.ent = None

    def get_acuarios_by_project(self, idp: int) -> Result:
        """
        Obtiene las tarjetas de acuario.
        :param idp: Id del proyecto des cuál se obtienen los acuarios.
        :return: Lista de tarjetas de acuario.
        """

        sql = (
            """
            SELECT      A.ID_ACUARIO AS ID,
                        ROW_NUMBER() OVER(ORDER BY A.ID_ACUARIO) AS NUM,
                        A.ID_PROYECTO AS PROYECTO,
                        A.COD_COLOR AS COLOR,
                        A.NOMBRE AS NOMBRE,
                        U.MODELO AS MODELO,
                        (
                            SELECT F.FOTOGRAFIA
                            FROM FOTOGRAFIAS_ACUARIO F
                            WHERE F.ID_FORANEA = A.ID_ACUARIO
                            ORDER BY F.ID_FOTOGRAFIA DESC
                            LIMIT 1
                        ) AS FOTO
            FROM        ACUARIOS A
            LEFT JOIN   URNAS U
                ON      A.ID_URNA = U.ID_URNA
            WHERE       A.ID_PROYECTO = :idp;
            """
        )

        params = {
            "idp": idp,
        }

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                rows = cur.fetchall()

                valores = [
                    TarjetaAcuarioEntity(
                        id=f[0],
                        num=f[1],
                        id_proyecto=f[2],
                        cod_color=f[3],
                        nombre=f[4],
                        modelo=f[5],
                        fotografia=f[6],
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
