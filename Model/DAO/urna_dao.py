"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Commentarios:
    Módulo que contiene la vista de la entidad ACUARIO.
"""

import traceback

from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.fotografia import FotografiaEntity
from Model.Entities.urna_entity import UrnaEntity
from Model.TableModel.urna_table_model import UrnaTableModel
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
            try:
                # dims = UrnaTableModel.brakdown_dimensions()
                cursor = self.db.conn.cursor()
                cursor.execute(sql)

                # POSIBLE ERROR AL DESGLOSAR LAS DIMENSIONES
                value = [UrnaEntity(
                    f["ID"], f["NUM"], f["MARCA"],f["MODELO"],
                    f["ANCHURA"], f["PROFUNDIDAD"], f["ALTURA"],
                    f["GROSOR"], f["VOLUMEN_BRUTO"], f["MATERIAL"],
                    f["DESCRIPCION"]
                ) for f in cursor.fetchall()]

                for ent in value:
                    QMessageBox.information(None, "oooo", str(ent))

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
                SELECT    A.ID_ACUARIO AS ID,
                          CONCAT(M.MARCA, ' ', A.MODELO) AS VALUE
                FROM      URNAS AS A
                LEFT JOIN MARCAS_COMERCIALES AS M
                ON        A.ID_MARCA = M.ID_MARCA
                ORDER BY  VALUE;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [UrnaEntity(
                    f["ID"], None, f["VALUE"]
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

    def insert(self, ent: UrnaEntity) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        :param ent: UrnaEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                INSERT INTO URNAS 
                            (ID_MARCA, MODELO, ANCHURA, PROFUNDIDAD,  ALTURA, 
                            GROSOR_CRISTAL, VOLUMEN_TANQUE, ID_MATERIAL, 
                            DESCRIPCION)
                VALUES      (:idm, :modelo, :anch, :prof, :alt, :grosor, :vol, 
                            :mat, :obs);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "idm": ent.id_marca,
                    "modelo": ent.modelo,
                    "anch": ent.anchura,
                    "prof": ent.profundidad,
                    "alt": ent.altura,
                    "grosor": ent.grosor_cristal,
                    "vol": ent.volumen_tanque,
                    "mat": ent.id_material,
                    "obs": ent.descripcion
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

    def update(self, ent: UrnaEntity) -> Result:
        """
        Actualiza el registro de la base de datos.

        :param ent: UrnaEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
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
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
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

        :param id: Id del registro a aliminar.
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                DELETE FROM URNAS
                WHERE       ID_URNA = :id;
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

