"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/09/2025
Commentarios:
    Módulo que contiene el DAO de la URNA.
"""
import sqlite3
import traceback

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.usuario_entity import UsuarioEntity
from Services.Result.result import Result


class UsuarioDAO (BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    UsuarioEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result(list[UsuarioEntity]):
        pass

    # ------------------------------------------------------------------
    def get_list_combo(self) -> Result(list[UsuarioEntity]):
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT    ID_USUARIO AS ID,
                      IFNULL(PRIMER_APELLIDO, '') || ' ' 
                          || IFNULL(SEGUNDO_APELLIDO, '') || ', ' 
                          || IFNULL(NOMBRE, '') AS VALUE
            FROM      USUARIOS;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    UsuarioEntity(
                        id=f["ID"],
                        num=None,
                        nombre=f["VALUE"],
                        apellido1=None,
                        apellido2=None,
                        e_mail=None,
                        usuario=None,
                        password=None
                    )
                    for f in rows
                ]
                return Result.success(valores)

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
    def insert(self, ent: UsuarioEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO USUARIOS    (NOMBRE, PRIMER_APELLIDO, SEGUNDO_APELLIDO, 
                                    E_MAIL, USUARIO, PASSWORD)
            VALUES                  (:nombre, :apellido1, :apellido2, :e_mail, 
                                    :usuario, :password);
            """
        )
        params = {
            "nombre": ent.nombre,
            "apellido1": ent.apellido1,
            "apellido2": ent.apellido2,
            "e_mail": ent.e_mail,
            "usuario": ent.usuario,
            "password": ent.password
        }

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(cur.lastrowid)

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
    def update(self, ent: UsuarioEntity) -> Result(int):
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE USUARIOS
            SET    NOMBRE = :nombre,
                   PRIMER_APELLIDO = :apellido1,
                   SEGUNDO_APELLIDO = :apellido2,
                   E_MAIL = :e_mail,
                   USUARIO = :usuario,
                   PASSWORD = :password
             WHERE ID_USUARIO = :id;
            """
        )
        params = {
            "id": ent.id,
            "nombre": ent.nombre,
            "apellido1": ent.apellido1,
            "apellido2": ent.apellido2,
            "e_mail": ent.e_mail,
            "usuario": ent.usuario,
            "password": ent.password
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
    def delete(self, id_: int) -> Result(int):
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM USUARIOS
            WHERE       ID_USUARIO = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                return Result.success(id_)

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
