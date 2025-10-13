"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/10/2025
Commentarios:
    Módulo que contiene los métodos de acceso a la base de datos de la
    entidad PROYECTO.
"""

import sqlite3

from base_dao import BaseDAO
from database import DBManager
from proyecto_entity import ProyectoEntity
from result import Result


class ProyectoDAO (BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    proyecto.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """ Obtiene el listado completo ordenado por fecha de inicio. """

        sql = (
            """
            SELECT P.ID_PROYECTO AS ID,
                   ROW_NUMBER() OVER(ORDER BY P.ID_PROYECTO) AS NUM,
                   P.ID_USUARIO AS ID_USUARIO,
                   P.NOMBRE AS NOMBRE,
                   E.NOMBRE_ESTADO AS ESTADO,
                   IFNULL(
                           strftime(
                                   '%Y-%m-%d', P.FECHA_INICIO, 
                                   'unixepoch', 
                                   'localtime'
                           ), 
                           ''
                   ) AS FECHA_INICIO,
                   IFNULL(
                           strftime(
                                   '%Y-%m-%d', P.FECHA_FIN, 
                                   'unixepoch', 
                                   'localtime'
                           ), 
                           ''
                   ) AS FECHA_FIN,
                   P.MOTIVO_CIERRE AS MOTIVO_CIERRE,
                   P.DESCRIPCION AS DESCRIPCION
            FROM   PROYECTOS P
            LEFT JOIN ESTADOS_PROYECTO E
            ON     P.ID_ESTADO = E.ID_ESTADO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    ProyectoEntity(
                        ide=f["ID"],
                        num=f["NUM"],
                        id_usuario=f["ID_USUARIO"],
                        nombre=f["NOMBRE"],
                        id_estado=f["ESTADO"],
                        fecha_inicio=f["FECHA_INICIO"],
                        fecha_fin=f["FECHA_FIN"],
                        motivo_cierre=f["MOTIVO_CIERRE"],
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
    def get_list_by_user(self, id_user: int) -> Result:
        """ Obtiene el listado por usuario. """

        sql = (
            """
            SELECT  P.ID_PROYECTO AS ID,
                    ROW_NUMBER() OVER(ORDER BY P.ID_PROYECTO) AS NUM,
                    P.ID_USUARIO AS ID_USUARIO,
                    P.NOMBRE AS NOMBRE,
                    E.NOMBRE_ESTADO AS ESTADO,
                    IFNULL(
                           strftime(
                                   '%Y-%m-%d', P.FECHA_INICIO, 
                                   'unixepoch', 
                                   'localtime'
                           ), 
                           ''
                    ) AS FECHA_INICIO,
                    IFNULL(
                           strftime(
                                   '%Y-%m-%d', P.FECHA_CIERRE, 
                                   'unixepoch', 
                                   'localtime'
                           ), 
                           ''
                    ) AS FECHA_FIN,
                    P.MOTIVO_CIERRE AS MOTIVO_CIERRE,
                    P.DESCRIPCION AS DESCRIPCION
            FROM    PROYECTOS P
            LEFT JOIN ESTADOS_PROYECTO E
            ON      P.ID_ESTADO = E.ID_ESTADO
            WHERE   P.ID_USUARIO = :id_user;
            """
        )
        params = {"id_usuario": id_user}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                rows = cur.fetchall()

                valores = [
                    ProyectoEntity(
                        ide=f["ID"],
                        num=f["NUM"],
                        id_usuario=f["ID_USUARIO"],
                        nombre=f["NOMBRE"],
                        id_estado=f["ESTADO"],
                        fecha_inicio=f["FECHA_INICIO"],
                        fecha_fin=f["FECHA_FIN"],
                        motivo_cierre=f["MOTIVO_CIERRE"],
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
    def get_list_combo(self,) -> Result:
        pass

    # ------------------------------------------------------------------
    def get_list_combo_by_user(self, id_usuario: int) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible) por usuario.
        """

        sql = (
            """
            SELECT      ID_PROYECTO AS ID,
                        NOMBRE AS VALUE,
                        ID_USUARIO AS ID_USUARIO
            FROM        PROYECTOS
            WHERE       ID_USUARIO = :id_usuario
            ORDER BY    NOMBRE;
            """
        )
        params = {"id_usuario": id_usuario}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                rows = cur.fetchall()
                valores = [
                    ProyectoEntity(
                        ide=f["ID"],
                        id_usuario=f["ID_USUARIO"],
                        nombre=f["NOMBRE"]
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
    def insert(self, ent: ProyectoEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO TIPOS_FILTRO
                        (TIPO_FILTRO, OBSERVACIONES)
            VALUES      (:tipo, :descripcion);
            """
        )
        params = {
                    "tipo": ent.tipo_filtro,
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

    # ------------------------------------------------------------------
    def update(self, ent: ProyectoEntity) -> Result:
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  TIPOS_FILTRO
            SET     TIPO_FILTRO = :tipo,
                    OBSERVACIONES = :descripcion
            WHERE   ID_TIPO = :id;
            """
        )
        params = {
                    "id": ent.id,
                    "tipo": ent.tipo_filtro,
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

    # ------------------------------------------------------------------
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM PROYECTOS
            WHERE ID_PROYECTO = :id
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
