"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      16/09/2026
Comentarios:
    Módulo que contiene los métodos de acceso a la base de datos de la
    entidad CONTROL DE TEMPERATURA.
"""
import sqlite3

from Main.Model.DAO.base_dao import BaseDAO
from Main.Model.Entities.combo_data_entity import ComboDataEntity
from ModuloMaestro.Model.Entities.control_temperatura_entity import \
    ControladorTemperaturaEntity
from Services.Database.database import DBManager
from Services.Result.result import Result


class ControladorTemperaturaDAO(BaseDAO):
    """
    Clase que gestiona las operaciones de la base de datos de la
    entidad control de temperatura.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_entity_by_id(self, ide: int) -> Result:
        """
        Obtiene el registro con el ID pasado como argumento.
        :param ide: ID de la entidad a recuperar
        """

        try:
            sql = (
                """
                SELECT ID_CONTROL_TEMPERATURA,
                       ID_MARCA,
                       ID_TIPO_CONTROL_TEMPERATURA,
                       MODELO,
                       NUMERO_SERIE,
                       TEMPERATURA_MINIMA,
                       TEMPERATURA_MAXIMA,
                       CONSUMO,
                       FECHA_ALTA,
                       FECHA_BAJA,
                       MOTIVO_BAJA,
                       DESCRIPCION
                FROM   CONTROLADORES_TEMPERATURA
                WHERE  ID_CONTROL_TEMPERATURA = :id;
                """
            )

            params = {"id": ide, }

            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                row = cur.fetchone()

                # Configuramos la entidad
                ent = ControladorTemperaturaEntity(
                    id=row[0],
                    id_marca=row[1],
                    id_tipo_control_temperatura=row[2],
                    modelo=row[3],
                    numero_serie=row[4],
                    temperatura_minima=row[5],
                    temperatura_maxima=row[6],
                    consumo=row[7],
                    fecha_alta=row[8],
                    fecha_baja=row[9],
                    motivo_baja=row[10],
                    descripcion=row[11],
                )

                return Result.success(ent)

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

    def get_list(self) -> Result:
        """ Obtiene el listado completo. """

        sql = (
            """
            SELECT  C.ID_CONTROL_TEMPERATURA AS ID, 
                    ROW_NUMBER()  OVER (ORDER BY C.ID_CONTROL_TEMPERATURA) AS NUM, 
                    M.MARCA AS MARCA, 
                    T.TIPO_CONTROL_TEMPERATURA AS TIPO_CONTROL, 
                    C.MODELO AS MODELO, 
                    C.NUMERO_SERIE AS NUMERO_SERIE, 
                    C.TEMPERATURA_MINIMA AS T_MIN, 
                    C.TEMPERATURA_MAXIMA AS T_MAX, 
                    C.CONSUMO AS CONSUMO,
                    IFNULL(strftime('%d/%m/%Y', C.FECHA_ALTA, 'unixepoch', 
                        'localtime'), '') AS FECHA_ALTA, 
                    IFNULL(strftime('%d/%m/%Y', C.FECHA_BAJA, 'unixepoch', 
                        'localtime'), '') AS FECHA_BAJA,
                    C.MOTIVO_BAJA AS MOTIVO_BAJA, 
                    C.DESCRIPCION AS DESCRIPCION 
            FROM CONTROLADORES_TEMPERATURA C 
            LEFT JOIN MARCAS_COMERCIALES M 
                ON C.ID_MARCA = M.ID_MARCA 
            LEFT JOIN TIPOS_CONTROL_TEMPERATURA T 
                ON C.ID_TIPO_CONTROL_TEMPERATURA = T.ID_TIPO_CONTROL_TEMPERATURA
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    ControladorTemperaturaEntity(
                        id=f[0],
                        num=f[1],
                        id_marca=f[2],
                        id_tipo_control_temperatura=f[3],
                        modelo=f[4],
                        numero_serie=f[5],
                        temperatura_minima=f[6],
                        temperatura_maxima=f[7],
                        consumo=f[8],
                        fecha_alta=f[9],
                        fecha_baja=f[10],
                        motivo_baja=f[11],
                        descripcion=f[12],
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
    def get_list_combo(self) -> Result:
        """
        Obtiene una lista ligera para combos (ID y texto visible).
        """

        sql = (
            """
            SELECT    C.ID_CONTROL_TEMPERATURA AS ID,
                      UPPER(T.TIPO_CONTROL_TEMPERATURA) || ' - '
                      || M.MARCA || ' ' || C.MODELO AS VALUE
            FROM      CONTROLADORES_TEMPERATURA C
            LEFT JOIN MARCAS_COMERCIALES M
                ON    C.ID_MARCA = M.ID_MARCA
            LEFT JOIN TIPOS_CONTROL_TEMPERATURA T
                ON    C.ID_TIPO_CONTROL_TEMPERATURA = T.ID_TIPO_CONTROL_TEMPERATURA
            ORDER BY  VALUE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    ComboDataEntity(
                        id=f["ID"],
                        value=f["VALUE"],
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
    def insert(self, ent: ControladorTemperaturaEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO CONTROLADORES_TEMPERATURA 
                (ID_MARCA, ID_TIPO_CONTROL_TEMPERATURA, MODELO, NUMERO_SERIE, 
                TEMPERATURA_MINIMA, TEMPERATURA_MAXIMA, CONSUMO, 
                FECHA_ALTA, FECHA_BAJA,  MOTIVO_BAJA,DESCRIPCION)
            VALUES 
                (:id_marca, :id_tipo, :modelo, :numero_serie, :temp_min, 
                :temp_max, :consumo, :fecha_alta, :fecha_baja, :motivo_baja, 
                :descripcion);
            """
        )
        params = {
            "id_marca": ent.id_marca,
            "id_tipo": ent.id_tipo_control_temperatura,
            "modelo": ent.modelo,
            "numero_serie": ent.numero_serie,
            "temp_min": ent.temperatura_minima,
            "temp_max": ent.temperatura_maxima,
            "consumo": ent.consumo,
            "fecha_alta": ent.fecha_alta,
            "fecha_baja": ent.fecha_baja,
            "motivo_baja": ent.motivo_baja,
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
    def update(self, ent: ControladorTemperaturaEntity) -> Result:
        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE CONTROLADORES_TEMPERATURA
            SET    ID_MARCA = :id_marca,
                   ID_TIPO_CONTROL_TEMPERATURA = :id_tipo,
                   MODELO = :modelo,
                   NUMERO_SERIE = :numero_serie,
                   TEMPERATURA_MINIMA = :temp_min,
                   TEMPERATURA_MAXIMA = :temp_max,
                   CONSUMO = :consumo,
                   FECHA_ALTA = :fecha_alta,
                   FECHA_BAJA = :fecha_baja,
                   MOTIVO_BAJA = :motivo_baja,
                   DESCRIPCION = :descripcion
             WHERE ID_CONTROL_TEMPERATURA = :id;
            """
        )
        params = {
            "id": ent.id,
            "id_marca": ent.id_marca,
            "id_tipo": ent.id_tipo_control_temperatura,
            "modelo": ent.modelo,
            "numero_serie": ent.numero_serie,
            "temp_min": ent.temperatura_minima,
            "temp_max": ent.temperatura_maxima,
            "consumo": ent.consumo,
            "fecha_alta": ent.fecha_alta,
            "fecha_baja": ent.fecha_baja,
            "motivo_baja": ent.motivo_baja,
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
    def delete(self, id_: int) -> Result:
        """
        Elimina el registro. Devuelve el ID de la entidad eliminada.
        :param id_: ID de la entidad a eliminar
        """
        sql = (
            """
            DELETE FROM CONTROLADORES_TEMPERATURA
            WHERE ID_CONTROL_TEMPERATURA = :id;
            """
        )
        params = {"id": id_}

        try:
            with self.db.conn as con:
                _ = con.execute(sql, params)
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
