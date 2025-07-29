"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/07/2025
Commentarios:
    Módulo que contiene la vista de la entidad MARCA COMERCIAL.
"""

import traceback

from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
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

    def get_list(self) -> Result:
        """ Obtiene el listado completo. """

        with self.db:
            if not self.db.conn:
                QMessageBox.information(
                    None,
                    "CONEXIÓN",
                    "CONEXIÓN NO INICIALIZADA"
                )

            # Obtenemos los datos
            sql = """
                SELECT    M.ID_MARCA AS ID,
                          ROW_NUMBER() OVER(ORDER BY M.MARCA) AS NUM,
                          M.MARCA AS MARCA,
                          M.DIRECCION AS DIRECCXION,
                          M.COD_POSTAL AS CODIGO_POSTAL,
                          M.POBLACION AS POBLACION,
                          M.PROVINCIA AS PROVINCIA,
                          P.PAIS AS PAIS,
                          M.OBSERVACIONES
                FROM      MARCAS_PRODUCTO M
                LEFT JOIN PAISES P
                ON        M.ID_PAIS = P.ID_PAIS;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                value = [MarcaComercialEntity(
                    f["ID"], f["NUM"], f["MARCA"],f["DIRECCCION"],
                    f["CODIGO_POSTAL"], f["POBLACION"], f["PROVINCIA"],
                    f["PAIS"], f["OBSERVACIONES"]
                ) for f in cursor.fetchall()]

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

    def get_list_combo(self):
        """ Obtiene el listado para el combo. """

        with self.db:
            # Obtenemos los datos
            sql = """
                SELECT    ID_MARCA AS ID,
                          MARCA AS VALUE
                FROM      MARCAS_PRODUCTO
                ORDER BY  MARCA;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [MarcaComercialEntity(
                    f["ID"], None, f["VALUE"], None, None,
                    None, None, None, None
                ) for f in cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(values)

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

    def insert(self, ent: MarcaComercialEntity) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        :param ent: MarcaComercialEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                INSERT INTO MARCAS_COMERCIALES 
                            (MARCA, DIRECCION, COD_POSTAL, POBLACION, PROVINCIA, 
                            ID_PAIS, OBSERVACIONES)
                VALUES      (:marca, :direccion, :codp, :poblacion, :provincia, 
                            :idp, :observaciones);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "marca": ent.nombre_marca,
                    "direccion": ent.direccion,
                    "codp": ent.cod_postal,
                    "poblacion": ent.poblacion,
                    "provincia": ent.provincia,
                    "idp": ent.id_pais,
                    "observaciones": ent.observaciones
                })

                # Devolvemos los datos
                last_id = cursor.lastrowid
                self.db.conn.commit()
                return Result.success(last_id)

            except self.db.conn.OperationalError as e:
                traceback.print_exc()
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                self.db.close_connection()

    def update(self, ent: MarcaComercialEntity) -> Result:
        """
        Actualiza el registro de la base de datos.

        :param ent: MarcaComercialEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                UPDATE  MARCAS_COMERCIALES
                SET     MARCA = :marca,
                        DIRECCION = :direccion,
                        COD_POSTAL = :codp,
                        POBLACION = :poblacion,
                        PROVINCIA = :provincia,
                        ID_PAIS = :idp,
                        OBSERVACIONES = :observaciones
                WHERE   ID_MARCA = :id;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id": ent.id,
                    "marca": ent.nombre_marca,
                    "direccion": ent.direccion,
                    "codp": ent.cod_postal,
                    "poblacion": ent.poblacion,
                    "provincia": ent.provincia,
                    "idp": ent.id_pais,
                    "observaciones": ent.observaciones
                })

                # Devolvemos los datos
                self.db.conn.commit()
                return Result.success(ent.id)

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

    def delete(self, id: int) -> Result:
        """
        Elimina el registro de la base de datos.

        Parametros:
        - id: Id del registro a aliminar.
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                DELETE FROM MARCAS_COMERCIALES
                WHERE ID_MARCA = :id;
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

