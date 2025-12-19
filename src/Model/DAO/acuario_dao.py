"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/10/2025
Comentarios:
    Módulo que contiene los métodos de acceso a la base de datos de la
    entidad ACUARIO.
"""
import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.database import DBManager
from Model.Entities.acuario_entity import AcuarioEntity
from Services.Result.result import Result


class AcuarioDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    acuario.
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
            SELECT      A.ID_ACUARIO AS ID,
                        A.ID_PROYECTO AS ID_PROYECTO,
                        ROW_NUMBER() OVER(ORDER BY A.NOMBRE) AS NUM,
                        A.COD_COLOR AS COLOR,
                        A.NOMBRE AS NOMBRE,
                        MC.MARCA || ' ' || U.MODELO AS URNA,
                        CA.CATEGORIA_ACUARIO || ' > ' || SA.SUBCATEGORIA_ACUARIO AS TIPO,
                        U.VOLUMEN_TANQUE || '/' || A.VOLUMEN_NETO AS VOLUMEN_B_N,
                        A.FECHA_MONTAJE AS FECHA_MONTAJE,
                        A.FECHA_INICIO_CICLADO AS FECHA_INICIO_CICLADO,
                        A.FECHA_FIN_CICLADO AS FECHA_FIN_CICLADO,
                        A.UBICACION_ACUARIO AS UBICACION,
                        A.FECHA_DESMONTAJE AS FECHA_DESMONTAJE,
                        A.MOTIVO_DESMONTAJE AS MOTIVO_DESMONTAJE,
                        A.DESCRIPCION AS DESCRIPCION
            FROM        ACUARIOS A
            LEFT JOIN   URNAS U ON A.ID_URNA = U.ID_URNA
            LEFT JOIN   MARCAS_COMERCIALES MC ON U.ID_MARCA = MC.ID_MARCA
            LEFT JOIN   TIPOS_ACUARIO TA ON A.ID_TIPO = TA.ID_TIPO
            LEFT JOIN   CATEGORIAS_ACUARIO CA 
                ON      TA.ID_CATEGORIA_ACUARIO = CA.ID_CATEGORIA_ACUARIO
            LEFT JOIN   SUBCATEGORIAS_ACUARIO SA 
                ON      TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    AcuarioEntity(
                        id=f["ID"],
                        id_proyecto=f["ID_PROYECTO"],
                        num=f["NUM"],
                        cod_color=f["COLOR"],
                        nombre=f["NOMBRE"],
                        id_urna=f["URNA"],
                        id_tipo=f["TIPO"],
                        volumen_neto=f["VOLUMEN_B_N"],
                        fecha_montaje=f["FECHA_MONTAJE"],
                        fecha_inicio_ciclado=f["FECHA_INICIO_CICLADO"],
                        fecha_fin_ciclado=f["FECHA_FIN_CICLADO"],
                        ubicacion_acuario=f["UBICACION"],
                        fecha_desmontaje=f["FECHA_DESMONTAJE"],
                        motivo_desmontaje=f["MOTIVO_DESMONTAJE"],
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
    def get_list_by_project(self, id_proyecto: int) -> Result:
        """ Obtiene el listado por proyecto. """

        sql = (
            """
            SELECT      A.ID_ACUARIO AS ID,
                        A.ID_PROYECTO AS ID_PROYECTO,
                        ROW_NUMBER() OVER(ORDER BY A.NOMBRE) AS NUM,
                        A.COD_COLOR AS COLOR,
                        A.NOMBRE AS NOMBRE,
                        MC.MARCA || ' ' || U.MODELO AS URNA,
                        CA.CATEGORIA_ACUARIO || ' > ' || SA.SUBCATEGORIA_ACUARIO AS TIPO,
                        U.VOLUMEN_TANQUE || '/' || A.VOLUMEN_NETO AS VOLUMEN_B_N,
                        A.FECHA_MONTAJE AS FECHA_MONTAJE,
                        A.FECHA_INICIO_CICLADO AS FECHA_INICIO_CICLADO,
                        A.FECHA_FIN_CICLADO AS FECHA_FIN_CICLADO,
                        A.UBICACION_ACUARIO AS UBICACION,
                        A.FECHA_DESMONTAJE AS FECHA_DESMONTAJE,
                        A.MOTIVO_DESMONTAJE AS MOTIVO_DESMONTAJE,
                        A.DESCRIPCION AS DESCRIPCION
            FROM        ACUARIOS A
            LEFT JOIN   URNAS U ON A.ID_URNA = U.ID_URNA
            LEFT JOIN   MARCAS_COMERCIALES MC ON U.ID_MARCA = MC.ID_MARCA
            LEFT JOIN   TIPOS_ACUARIO TA ON A.ID_TIPO = TA.ID_TIPO
            LEFT JOIN   CATEGORIAS_ACUARIO CA 
                ON      TA.ID_CATEGORIA_ACUARIO = CA.ID_CATEGORIA_ACUARIO
            LEFT JOIN   SUBCATEGORIAS_ACUARIO SA 
                ON      TA.ID_SUBCATEGORIA_ACUARIO = SA.ID_SUBCATEGORIA_ACUARIO
            WHERE       A.ID_PROYECTO = :id_proyecto;
            """
        )

        params = {"id_proyecto": id_proyecto}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                rows = cur.fetchall()

                valores = [
                    AcuarioEntity(
                        id=f["ID"],
                        id_proyecto=f["ID_PROYECTO"],
                        num=f["NUM"],
                        cod_color=f["COLOR"],
                        nombre=f["NOMBRE"],
                        id_urna=f["URNA"],
                        id_tipo=f["TIPO"],
                        volumen_neto=f["VOLUMEN_B_N"],
                        fecha_montaje=f["FECHA_MONTAJE"],
                        fecha_inicio_ciclado=f["FECHA_INICIO_CICLADO"],
                        fecha_fin_ciclado=f["FECHA_FIN_CICLADO"],
                        ubicacion_acuario=f["UBICACION"],
                        fecha_desmontaje=f["FECHA_DESMONTAJE"],
                        motivo_desmontaje=f["MOTIVO_DESMONTAJE"],
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
    def get_list_combo(self, ) -> Result:
        pass

    # ------------------------------------------------------------------
    def get_list_combo_by_proyect(self, id_usuario: int) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible) por usuario.
        """

        sql = (
            """
            SELECT      A.ID_ACUARIO AS ID,
                        A.NOMBRE || ' (' || MC.MARCA 
                            || ' ' || U.MODELO || ')' AS VALUE
            FROM        ACUARIOS A
            LEFT JOIN   URNAS U ON A.ID_URNA = U.ID_URNA
            LEFT JOIN   MARCAS_COMERCIALES MC ON U.ID_MARCA = MC.ID_MARCA
            WHERE       A.ID_PROYECTO = :id_proyecto;
            """
        )
        params = {"id_usuario": id_usuario}

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                rows = cur.fetchall()
                valores = [
                    AcuarioEntity(
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
    def insert(self, ent: AcuarioEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO ACUARIOS 
                (ID_PROYECTO, COD_COLOR, NOMBRE, ID_URNA, ID_TIPO, VOLUMEN_NETO, 
                FECHA_MONTAJE, FECHA_INICIO_CICLADO, FECHA_FIN_CICLADO, 
                UBICACION_ACUARIO, FECHA_DESMONTAJE, MOTIVO_DESMONTAJE, 
                DESCRIPCION)
            VALUES 
                (:id_proyecto, :cod_color, :nombre, :id_urna, :id_tipo, 
                :volumen, :f_montaje, :f_i_ciclado, :f_f_ciclado, :ubicacion, 
                :f_desmontaje, :motivo_desmontaje, :descripcion);
            """
        )

        params = {
            "id_proyecto": ent.id_proyecto,
            "cod_color": ent.cod_color,
            "nombre": ent.nombre,
            "id_urna": ent.id_urna,
            "id_tipo": ent.id_tipo,
            "volumen": ent.volumen_neto,
            "f_montaje": ent.fecha_montaje,
            "f_i_ciclado": ent.fecha_inicio_ciclado,
            "f_f_ciclado": ent.fecha_fin_ciclado,
            "ubicacion": ent.ubicacion_acuario,
            "f_desmontaje": ent.fecha_desmontaje,
            "motivo_desmontaje": ent.motivo_desmontaje,
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
    def update(self, ent: AcuarioEntity) -> Result:
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  ACUARIOS
            SET     ID_PROYECTO = :id_proyecto,
                    COD_COLOR = :cod_color,
                    NOMBRE = :nombre,
                    ID_URNA = :id_urna,
                    ID_TIPO = :id_tipo,
                    VOLUMEN_NETO = :volumen,
                    FECHA_MONTAJE = :f_montaje,
                    FECHA_INICIO_CICLADO = :f_i_ciclado,
                    FECHA_FIN_CICLADO = :f_f_ciclado,
                    UBICACION_ACUARIO = :ubicacion,
                    FECHA_DESMONTAJE = :f_desmontaje,
                    MOTIVO_DESMONTAJE = :motivo_desmontaje,
                    DESCRIPCION = :descripcion
            WHERE   ID_ACUARIO = :id;
            """
        )

        params = {
            "id": ent.id,
            "id_proyecto": ent.id_proyecto,
            "cod_color": ent.cod_color,
            "nombre": ent.nombre,
            "id_urna": ent.id_urna,
            "id_tipo": ent.id_tipo,
            "volumen": ent.volumen_neto,
            "f_montaje": ent.fecha_montaje,
            "f_i_ciclado": ent.fecha_inicio_ciclado,
            "f_f_ciclado": ent.fecha_fin_ciclado,
            "ubicacion": ent.ubicacion_acuario,
            "f_desmontaje": ent.fecha_desmontaje,
            "motivo_desmontaje": ent.motivo_desmontaje,
            "descripcion": ent.descripcion,
        }

        try:
            with self.db.conn as con:
                _ = con.execute(sql, params)
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
    def delete(self, id: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM ACUARIOS
            WHERE       ID_ACUARIO = :id
            """
        )
        params = {"id": id}

        try:
            with self.db.conn as con:
                _ = con.execute(sql, params)
                return Result.success(id)

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

    def color_exists(self, cod_color: str, id_proyectto: int) -> Result:
        """
        Devuelve si ya existe un acuario con el mismo color en el proyecto.
        :param cod_color: Codigo del color de acuario a consultyar
        :param id_proyectto: ID del proyecto
        """

        sql = (
            """
            SELECT EXISTS(
                SELECT 1
                FROM ACUARIOS
                WHERE COD_COLOR = :cod_color AND ID_PROYECTO = :id_proyecto
            ) AS Existe;
            """
        )
        params = {
            "cod_color": cod_color,
            "id_proyecto": id_proyectto
        }

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                row = cur.fetchone()
                exists = bool(row[0])
                return Result.success(exists)

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
