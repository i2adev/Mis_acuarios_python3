"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/10/2025
Commentarios:
    Módulo que contiene los métodos de acceso a la base de datos de la
    entidad PROYECTO.
"""

import sqlite3
import traceback

import globals
from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.proyecto_entity import ProyectoEntity
from Services.Result.result import Result


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
                        id=f["ID"],
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
                        id=f["ID"],
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
                        id=f["ID"],
                        nombre=f["VALUE"]
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
            INSERT INTO PROYECTOS (ID_USUARIO, NOMBRE, ID_ESTADO, FECHA_INICIO,
                        FECHA_FIN, MOTIVO_CIERRE, DESCRIPCION)
            VALUES (:id_usuario, :nombre, :id_estado, :fecha_inicio,
                    :fecha_fin, :motivo_cierre, :descripcion);
            """
        )

        params = {
            "id_usuario": globals.CURRENT_USER.id,
            "nombre": ent.nombre,
            "id_estado": ent.id_estado,
            "fecha_inicio": ent.fecha_inicio,
            "fecha_fin": ent.fecha_fin,
            "motivo_cierre": ent.motivo_cierre,
            "descripcion": ent.descripcion,
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
            UPDATE  PROYECTOS
            SET     ID_USUARIO = :id_usuario,
                    NOMBRE = :nombre,
                    ID_ESTADO = :id_estado,
                    FECHA_INICIO = :fecha_inicio,
                    FECHA_FIN = :fecha_fin,
                    MOTIVO_CIERRE = :motivo_cierre,
                    DESCRIPCION = :descripcion
            WHERE   ID_PROYECTO = :id;
            """
        )

        params = {
            "id": ent.id,
            "id_usuario": globals.CURRENT_USER.id,
            "nombre": ent.nombre,
            "id_estado": ent.id_estado,
            "fecha_inicio": ent.fecha_inicio,
            "fecha_fin": ent.fecha_fin,
            "motivo_cierre": ent.motivo_cierre,
            "descripcion": ent.descripcion,
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
