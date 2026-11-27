"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/10/2026
Comentarios:
    Módulo de acceso a datos de la tarjeta de proyecto
"""
import sqlite3

from ModuloProyecto.Models.Entities.tarjeta_proyecto_entity import \
    TarjetaProyectoEntity
from Services.Database.database import DBManager
from Services.Result.result import Result


class TarjetaProyectoDAO:
    """
    Clase de accesoa a datos de la tarjeta de proyecto.
    """

    def __init__(self):
        """ Constructor de la clase. """

        self.db = DBManager()
        self.ent = None

    def get_proyectos(self) -> Result:
        """
        Obtiene las tarjetas de proyecto.
        :return: Lista de tarjetas de proyecto.
        """

        sql = (
            """
            SELECT     P.ID_PROYECTO AS ID,
                       ROW_NUMBER() OVER(ORDER BY P.ID_PROYECTO) AS NUM,
                       P.NOMBRE AS NOMBRE,
                       E.NOMBRE_ESTADO AS ESTADO,
                       IFNULL(strftime('%d/%m/%Y', P.FECHA_INICIO, 'unixepoch', 'localtime'), '') AS FECHA_INICIO,
                       IFNULL(strftime('%d/%m/%Y', P.FECHA_FIN, 'unixepoch', 'localtime'), '') AS FECHA_FIN,
                       P.MOTIVO_CIERRE AS MOTIVO_CIERRE,
                       P.DESCRIPCION AS DESCRIPCION,
                       (
                            SELECT F.FOTOGRAFIA
                            FROM FOTOGRAFIAS_PROYECTO F
                            WHERE F.ID_FORANEA = P.ID_PROYECTO
                            ORDER BY F.ID_FOTOGRAFIA DESC
                            LIMIT 1
                        ) AS FOTO
            FROM       PROYECTOS P
            LEFT JOIN  ESTADOS_PROYECTO E
                ON     P.ID_ESTADO = E.ID_ESTADO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    TarjetaProyectoEntity(
                        id=f[0],
                        num=f[1],
                        nombre=f[2],
                        estado=f[3],
                        fecha_inicio=f[4],
                        fecha_fin=f[5],
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
