"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      12/08/2025
Commentarios:
    Módulo que contiene la vista de la entidad MATERIAL DE URNA.
"""

import traceback

from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.material_urna import MaterialUrnaEntity
from Model.TableModel.urna_table_model import UrnaTableModel
from Services.Result.result import Result


class MaterialUrnaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    MaterialUrnaEntity.
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
                SELECT    ID_MATERIAL AS ID,
                          ROW_NUMBER() OVER(ORDER BY MATERIAL) AS NUM,
                          MATERIAL AS MATERIAL,
                          DESCRIPCION AS DESCRIPCION
                FROM      MATERIALES_URNA;
            """
            try:
                # dims = UrnaTableModel.brakdown_dimensions()
                cursor = self.db.conn.cursor()
                cursor.execute(sql)

                # POSIBLE ERROR AL DESGLOSAR LAS DIMENSIONES
                value = [MaterialUrnaEntity(
                    f["ID"], f["NUM"], f["MATERIAL"],f["DESCRIPCION"]
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
                SELECT    ID_MATERIAL AS ID,
                          MATERIAL AS VALUE
                FROM      MATERIALES_URNA
                ORDER BY  MATERIAL;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [MaterialUrnaEntity(
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

    def insert(self, ent: MaterialUrnaEntity) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        :param ent: MaterialUrnaEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                INSERT INTO MATERIALES_URNA (MATERIAL, DESCRIPCION)
                VALUES                      (:mat, :desc);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "mat": ent.material,
                    "desc": ent.descripcion
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

    def update(self, ent: MaterialUrnaEntity) -> Result:
        """
        Actualiza el registro de la base de datos.

        :param ent: MaterialUrnaEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                UPDATE    MATERIALES_URNA
                SET       MATERIAL = :mat,
                          DESCRIPCION = :desc
                WHERE     ID_MATERIAL = :id;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id": ent.id,
                    "mat": ent.material,
                    "desc": ent.descripcion
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
                DELETE FROM MATERIALES_URNA
                WHERE       ID_MATERIAL = :id;
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

