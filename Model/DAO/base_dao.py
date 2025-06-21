"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      17/06/2025
Commentarios:
    Clase base de las que ejecutan los comandos sobre la base de datos
    (DAOs).
"""

from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QMessageBox
from Model.DAO.database import DBManager
from Model.Entities.base_entity import BaseEntity
from Model.Entities.tipo_filtro_entity import TipoFiltroEntity
from Services.Result.result import Result


class BaseDAO(ABC):
    """ Clase base de las DAOs. """

    @abstractmethod
    def get_list(self) -> Result:
        pass

    @abstractmethod
    def get_list_combo(self) -> Result:
        pass

    @abstractmethod
    def insert(self, ent: BaseEntity) -> Result:
        pass

    @abstractmethod
    def update(self, ent: BaseEntity) -> Result:
        pass

    @abstractmethod
    def delete(self, id: int) -> Result:
        pass

    @staticmethod
    def get_db_tables(cls) -> Result:
        """ Obtiene la lista con las tablas de la base de datos. """

        db = DBManager()

        with db:
            if not db.conn:
                QMessageBox.information(
                    None,
                    "CONEXIÓN",
                    "CONEXIÓN NO INICIALIZADA."
                )

            # Obtenemos los datos
            sql = """
                SELECT  name 
                FROM    sqlite_master 
                WHERE   type='table' AND name NOT LIKE 'sqlite_%';
            """
            try:
                cursor = db.conn.cursor()
                cursor.execute(sql)
                value = [fila[0] for fila in cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(value)

            except db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                db.close_connection()
                del db

    @staticmethod
    def get_db_views():
        """ Obtiene la lista con las vistas de la base de datos. """

        db = DBManager()

        with db:
            if not db.conn:
                QMessageBox.information(
                    None,
                    "CONEXIÓN",
                    "CONEXIÓN NO INICIALIZADA."
                )

            # Obtenemos los datos
            sql = """
                SELECT  name 
                FROM    sqlite_master 
                WHERE   type='view';
            """
            try:
                cursor = db.conn.cursor()
                cursor.execute(sql)
                value = [fila[0] for fila in cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(value)

            except db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                db.close_connection()
                del db

    @staticmethod
    def get_total_data(procedure: str, col_parent: str = None,
                        id_parent: int = None) -> Result:
        """
        Obtiene todos los datos de la vista especificada.

        Parámetros:
        - PROCEDURE: La vista de la que se tienen que obtener los datos.
        - COL_PARENT: Nombre de la columna a la que hay que aplicar el
          filtro del ID.
        - ID_PARENT: Entero que representa el ID del cual dependes los
                     datos.
        """

        db = DBManager()

        with db:
            if not db.conn:
                QMessageBox.information(
                    None,
                    "CONEXIÓN",
                    "CONEXIÓN NO INICIALIZADA."
                )

            # Obtenemos los datos
            if not col_parent:
                sql = f"""
                    SELECT  * 
                    FROM    {procedure};
                """
            else:
                sql = f"""
                    SELECT  * 
                    FROM    {procedure}
                    WHERE   {col_parent} = :id_parent;
                """

            try:
                cursor = db.conn.cursor()

                if col_parent:
                    params = {
                        "id_parent": id_parent,
                    }
                    cursor.execute(sql, params)
                else:
                    cursor.execute(sql)

                value = [TipoFiltroEntity(f["ID"], f["NUM"], f["TIPO"],
                                         f["OBSERVACIONES"])
                        for f in cursor.fetchall()]

                # Devolvemos los datos
                return Result.success(value)

            except db.conn.OperationalError as e:
                return Result.failure(f"[ERROR OPERACIONAL]\n {e}")
            except db.conn.ProgrammingError as e:
                return Result.failure(f"[ERROR DE PROGRAMACIÓN]\n {e}")
            except db.conn.DatabaseError as e:
                return Result.failure(f"[ERROR DE BASE DE DATOS]\n {e}")
            except db.conn.Error as e:
                return Result.failure(f"[ERROR GENERAL SQLITE]\n {e}")
            finally:
                db.close_connection()
                del db

    @staticmethod
    def clean_database():
        """
        Limpia la base de datos:
        - Elimina todos los registros.
        - Inicializa los autonúmericos.
        """

        db = DBManager()
        with db:
            if not db.conn:
                return Result.failure("❌ CONEXIÓN NO INICIALIZADA.")

            cursor = db.conn.cursor()

            # Obtener las tablas del usuario
            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name NOT LIKE 'sqlite_%';
            """)
            tablas = [row[0] for row in cursor.fetchall()]

            # Eliminar datos y reiniciar los AUTOINCREMENT
            for tabla in tablas:
                cursor.execute(f"DELETE FROM {tabla};")
                cursor.execute(
                    f"UPDATE sqlite_sequence SET seq = 10000 WHERE name = '{tabla}';"
                )

            db.conn.commit()
            return Result.success(
                f"✅ {len(tablas)} tablas limpiadas correctamente."
            )

    @staticmethod
    def export_db_sql(db_path: str, export_path: str) -> bool:
        """
        Exporta la base de datos SQLite completa a un archivo SQL.

        Parámetros:
        - db_path: Ruta al archivo de base de datos SQLite.
        - export_path: Ruta donde se guardará el archivo SQL exportado.

        Retorna:
        - True si la exportación fue exitosa, False en caso de error.
        """

        try:
            conn = DBManager().get_connection()
            with open(export_path, 'w', encoding='utf-8') as f:
                for line in conn.iterdump():
                    f.write(f"{line}\n")
            conn.close()
            return True
        except Exception as e:
            print(f"Error al exportar la base de datos: {e}")
            return False