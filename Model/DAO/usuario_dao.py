"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/09/2025
Commentarios:
    Módulo que contiene el DAO de la URNA.
"""
import sqlite3
import traceback

import bcrypt

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
                        nick=None,
                        password=None
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
    def insert(self, ent: UsuarioEntity) -> Result(int):
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO USUARIOS    (NOMBRE, PRIMER_APELLIDO, SEGUNDO_APELLIDO, 
                                    NICK_USUARIO, PASSWORD)
            VALUES                  (:nombre, :apellido1, :apellido2, :nick, 
                                    :password);
            """
        )
        params = {
            "nombre": ent.nombre,
            "apellido1": ent.apellido1,
            "apellido2": ent.apellido2,
            "nick": ent.nick,
            "password": self.hash_password(ent.password)
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
                   NICK_USUARIO = :nick,
                   PASSWORD = :password
             WHERE ID_USUARIO = :id;
            """
        )
        params = {
            "id": ent.id,
            "nombre": ent.nombre,
            "apellido1": ent.apellido1,
            "apellido2": ent.apellido2,
            "nick": ent.nick,
            "password": self.hash_password(ent.password)
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

    def get_validated_user(self, nick: str, pwd: str) -> Result(UsuarioEntity):
        """
        Obtiene el usuario con el nick especificado.
        :param nick: Nick del usuario
        """

        sql = (
            """
            SELECT  ID_USUARIO AS ID,
                    NOMBRE AS NOMBRE,
                    PRIMER_APELLIDO AS APELLIDO1,
                    SEGUNDO_APELLIDO AS APELLIDO2,
                    NICK_USUARIO AS NICK,
                    PASSWORD AS PASSWORD
            FROM    USUARIOS
            WHERE   NICK_USUARIO = :nick;
            """
        )
        params = {"nick": nick}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                row = cur.fetchone()

                if not row:
                    return Result.failure("ERROR DE AUTENTICACIÓN")

                usuario = UsuarioEntity(
                        id=row["ID"],
                        num=None,
                        nombre=row["NOMBRE"],
                        apellido1=row["APELLIDO1"],
                        apellido2=row["APELLIDO2"],
                        nick=row["NICK"],
                        password=row["PASSWORD"])

                # Validamos las credencfiales
                if self.verify_password(pwd, usuario.password):
                    return Result.success(usuario)
                else:
                    return Result.failure("ERROR DE AUTENTICACIÓN")

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

    def hash_password(self, password: str) -> str | None:
        """
        Encripta la contraseña.
        :param password: Contraseña del usuario
        """

        # En caso de que no se haya insertado la contraseña
        if not password:
            return None

        # Se crea la encriptación
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    def verify_password(self, password: str, hashed: str) -> bool:
        """
        Verifica la contraseña del usuario.
        :param password: Contraseña a verificar
        :param hashed: Contraseña almacenada
        """

        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))