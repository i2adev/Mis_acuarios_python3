"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad CATEGORÍA DE ACUARIO.
"""
from PyQt6.QtWidgets import QMessageBox

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.categoria_acuario_entity import CategoriaAcuarioEntity
from Services.Result.result import Result


class CategoriaAcuarioDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    CategoriaAcuarioEntity.
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
                SELECT    ID_CATEGORIA_ACUARIO AS ID,
                          ROW_NUMBER() OVER(ORDER BY CATEGORIA_ACUARIO) AS NUM,
                          CATEGORIA_ACUARIO AS CATEGORIA,
                          OBSERVACIONES
                FROM      CATEGORIAS_ACUARIO;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                value = [CategoriaAcuarioEntity(
                    f["ID"], f["NUM"], f["TIPO"], f["SUBTIPO"],
                    f["OBSERVACIONES"]
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

    def get_num_by_id(self, id_: int) -> Result:
        """
        Obtiene el valor NUM de la vista VISTA_CATEGORIAS_ACUARIO dado un ID.
        """

        with self.db:
            if not self.db.conn:
                QMessageBox.information(
                    None,
                    "CONEXIÓN",
                    "CONEXIÓN NO INICIALIZADA"
                )
                # return Result.failure(
                #     "NO SE HA PODIDO CONECTAR CON LA BASE DE DATOS."
                # )

            # Obtenemos el dato
            sql = """
                SELECT NUM
                FROM   VISTA_CATEGORIAS_ACUARIO
                WHERE  ID = :id;
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {"id": id_})
                row = cursor.fetchone()

                if row is not None:
                    return Result.success(row["NUM"])
                else:
                    return Result.failure(
                        f"NO SE ENCONTRÓ NINGÚN RESULTADO CON EL ID '{id_}'."
                    )

            except self.db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n{e}")
            except self.db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n{e}")
            except self.db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n{e}")
            except self.db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n{e}")
            finally:
                self.db.close_connection()

    def get_list_combo(self):
        """ Obtiene el listado para el combo. """

        with self.db:
            # # Chequeamos que la base de datos está abierta
            # if not self.db.is_opened():
            #     self.db.conn = self.db.initialize_db()

            # Obtenemos los datos
            sql = """
                SELECT    ID_CATEGORIA_ACUARIO AS ID,
                          CATEGORIA_ACUARIO AS VALUE
                FROM      CATEGORIAS_ACUARIO
                ORDER BY  CATEGORIA_ACUARIO;
              """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql)
                values = [CategoriaAcuarioEntity(
                    f["ID"], None, f["VALUE"]) for f in cursor.fetchall()]

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

    def insert(self, ent: CategoriaAcuarioEntity) -> Result:
        """
        Inserta un nuevo registro en la base de datos.

        Parametros:
        :param ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                INSERT INTO     CATEGORIAS_ACUARIO
                                (CATEGORIA_ACUARIO, OBSERVACIONES)
                VALUES          (:cat, :observaciones);
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "cat": ent.categoria,
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

    def update(self, ent: CategoriaAcuarioEntity) -> Result:
        """
        Actualiza el registro de la base de datos.

        Parametros:
        - ent: Entidad derivada de BaseEntity
        """

        with self.db:
            # Obtenemos los datos
            sql = """
                UPDATE  CATEGORIAS_ACUARIO
                SET     CATEGORIA_ACUARIO = :cat,
                        OBSERVACIONES = :observaciones
                WHERE   ID_CATEGORIA_ACUARIO = :id
            """
            try:
                cursor = self.db.conn.cursor()
                cursor.execute(sql, {
                    "id": ent.id,
                    "cat": ent.categoria,
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
                DELETE FROM CATEGORIAS_ACUARIO
                WHERE ID_CATEGORIA_ACUARIO = :id;
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

