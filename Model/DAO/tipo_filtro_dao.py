﻿"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene los métodos de acceso a la base de datos de la
    entidad TqIPO DE FILTRO.
"""
import sqlite3

# Importaciones
from Services.Result.result import Result
from Model.DAO.database import DBManager
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity

class TipoFiltroDAO:
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    TipoFiltroEntity.
    """

    def __init__(self):
        """ Constructor de clase. """
        self.db = DBManager()
        self.ent = None

    def get_data(self):
        """ Obtiene el listado completo. """

        with self.db:
            # Chequeamos que la base de datos está abierta
            if not self.db.is_opened():
                self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                SELECT  ID_TIPO AS ID,
                        ROW_NUMBER() OVER(ORDER BY TIPO_FILTRO) AS NUM,
                        TIPO_FILTRO AS TIPO,
                        OBSERVACIONES AS OBSERVACIONES
                FROM    TIPOS_FILTRO;
            """
            try:
                self.db.conn.cursor = self.db.conn.cursor()
                self.db.conn.cursor.execute(sql)
                value = [TipoFiltroEntity(f["ID"], f["NUM"], f["TIPO"],
                                         f["OBSERVACIONES"])
                        for f in self.db.conn.cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(value)

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()

    def get_combo(self):
        """ Obtiene el listado para el combo. """

        with self.db:
            # Chequeamos que la base de datos está abierta
            if not self.db.is_opened():
                self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                  SELECT  ID_TIPO AS ID,
                          TIPO_FILTRO AS TIPO
                  FROM    TIPOS_FILTRO;
              """
            try:
                self.db.conn.cursor = self.db.conn.cursor()
                self.db.conn.cursor.execute(sql)
                value = [TipoFiltroEntity(None, None, f["TIPO"],
                                          f["OBSERVACIONES"])
                         for f in self.db.conn.cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(value)

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()

    def insert(self, ent: TipoFiltroEntity):
        """
        Inserta un nuevo registro en la base de datos.
        Parametros:
        -   ENT: Entidad derivada de BaseEntity
        """

        with self.db:
            # Chequeamos que la base de datos está abierta
            if not self.db.is_opened():
                self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                INSERT INTO TIPOS_FILTRO
                    (TIPO_FILTRO, OBSERVACIONES)
                VALUES (:tipo, :observaciones);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "tipo": ent.tipo_filtro,
                    "observaciones": ent.observaciones
                })

                # Devolvemos los datos
                last_id = cursor.lastrowid
                self.db.conn.commit()
                return Result.success(last_id)

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()

    def update(self, ent: TipoFiltroEntity):
        """
        Actualiza el registro de la base de datos.
        Parametros:
        -   ENT: Entidad derivada de BaseEntity
        """

        with self.db:
            # Chequeamos que la base de datos está abierta
            if not self.db.is_opened():
                self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                UPDATE  TIPOS_FILTRO
                SET     TIPO_FILTRO = :tipo,
                        OBSERVACIONES = :observaciones
                WHERE   ID_TIPO = :id
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id": ent.id_tf,
                    "tipo": ent.tipo_filtro,
                    "observaciones": ent.observaciones
                })

                # Devolvemos los datos
                self.db.conn.commit()
                return Result.success(ent.id_tf)

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()

    def delete(self, id: int):
        """
        Elimina el registro de la base de datos.
        Parametros:
        -   ID: Id del registro a aliminar.
        """

        with self.db:
            # Chequeamos que la base de datos está abierta
            if not self.db.is_opened():
                self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                DELETE FROM TIPOS_FILTRO
                WHERE ID_TIPO = :id;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {"id": id})

                # Devolvemos los datos
                self.db.conn.commit()
                return Result.success(id)

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()