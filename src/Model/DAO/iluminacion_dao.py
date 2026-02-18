"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      22/12/2025
Comentarios:
    Módulo que contiene el DAO de la ILUMINACIÓN.
"""
import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.Entities.iluminacion_entity import IluminacionEntity
from Model.database import DBManager
from Services.Result.result import Result


class IluminacionDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    IluminacionEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """Obtiene el listado completo ordenado por marca-modelo."""

        sql = (
            """
            SELECT     I.ID_ILUMINACION AS ID,
                       ROW_NUMBER() OVER(ORDER BY M.MARCA, I.MODELO) AS NUM,
                       M.MARCA AS MARCA,
                       I.MODELO AS MODELO,
                       I.NUMERO_SERIE AS NUMERO_SERIE,
                       TI.TIPO_ILUMINACION AS TIPO_ILUMINACION,
                       I.POTENCIA_W AS POTENCIA,
                       I.FLUJO_LUMINOSO_LM AS FLUJO_LUMINOSO,
                       I.TEMPERATURA_K AS TEMPERATURA,
                       I.VIDA_UTIL AS VIDA_UTIL,
                       I.LONGITUD_CM AS LONGITUD,
                       I.ANCHO_CM AS ANCHO,
                       CI.TIPO_CONTROL AS CONTROL_ILUMINACION,
                       I.INTENSIDAD_REGULABLE AS INTERSIDAD_REGULABLE,
                       I.ESPECTRO_COMPLETO AS ESPECTRO_COMPLETO,
                       IFNULL(strftime('%d/%m/%Y', I.FECHA_ALTA, 
                            'unixepoch', 'localtime'), '') AS FECHA_ALTA, 
                       IFNULL(strftime('%d/%m/%Y', I.FECHA_BAJA, 
                            'unixepoch', 'localtime'), '') AS FECHA_BAJA, 
                       I.MOTIVO_BAJA AS MOTIVO_BAJA,
                       I.DESCRIPCION AS DESCRIPCION
            FROM       ILUMINACIONES I
            LEFT JOIN  TIPOS_ILUMINACION TI 
                ON     I.ID_TIPO_ILUMINACION = TI.ID_TIPO_ILUMINACION
            LEFT JOIN  MARCAS_COMERCIALES M 
                ON     I.ID_MARCA = M.ID_MARCA
            LEFT JOIN  CONTROLES_ILUMINACION CI 
                ON     I.ID_CONTROL_ILUMINACION = CI.ID_CONTROL_ILUMINACION
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    IluminacionEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_marca=f["MARCA"],
                        modelo=f["MODELO"],
                        num_serie=f["NUMERO_SERIE"],
                        id_tipo_iluminacion=f["TIPO_ILUMINACION"],
                        potencia=f["POTENCIA"],
                        flujo_luminico=f["FLUJO_LUMINOSO"],
                        temperatura=f["TEMPERATURA"],
                        vida_util=f["VIDA_UTIL"],
                        longitud=f["LONGITUD"],
                        anchura=f["CONSUMO"],
                        id_control_iluminacion=f["CONTROL_ILUMINACION"],
                        intensidad_regulable=f["INTERSIDAD_REGULABLE"],
                        espectro_completo=f["ESPECTRO_COMPLETO"],
                        fecha_alta=f["FECHA_ALTA"],
                        fecha_baja=f["FECHA_BAJA"],
                        motivo_baja=f["MOTIVO_BAJA"],
                        descripcion=f["DESCRIPCION"],
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
        Devuelve entidades con `num=None` y `observaciones=None`.
        """

        sql = (
            """
            SELECT     I.ID_ILUMINACION AS ID,
                       M.MARCA || ' ' || I.MODELO AS VALUE
            FROM       ILUMINACIONES I
            LEFT JOIN  MARCAS_COMERCIALES M ON I.ID_MARCA = M.ID_MARCA
            ORDER BY   VALUE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    IluminacionEntity(
                        id=f["ID"],
                        modelo=f["VALUE"]
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
    def insert(self, ent: IluminacionEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO ILUMINACIONES 
                        (ID_TIPO_ILUMINACION, ID_MARCA, MODELO, NUMERO_SERIE,
                        POTENCIA_W, FLUJO_LUMINOSO_LM, TEMPERATURA_K, 
                        VIDA_UTIL, LONGITUD_CM, ANCHO_CM, ID_CONTROL_ILUMINACION,
                        INTENSIDAD_REGULABLE, ESPECTRO_COMPLETO, FECHA_ALTA, 
                        FECHA_BAJA, MOTIVO_BAJA, DESCRIPCION)
            VALUES (:id_tipo, :id_marca, :modelo, :num_serie, :potencia,
                   :flujo_luminoso, :temperatura, :vida_util, :longitud, 
                   :anchura, :id_control, :intensidad_regulable, 
                   :espectro_completo, :fecha_alta, :fecha_baja, 
                   :motivo_baja, :descripcion);
            """
        )

        params = {
            "id_tipo": ent.id_tipo_iluminacion,
            "id_marca": ent.id_marca,
            "modelo": ent.modelo,
            "num_serie": ent.num_serie,
            "potencia": ent.potencia,
            "flujo_luminoso": ent.flujo_luminico,
            "temperatura": ent.temperatura,
            "vida_util": ent.vida_util,
            "longitud": ent.longitud,
            "anchura": ent.anchura,
            "id_control": ent.id_control_iluminacion,
            "intensidad_regulable": ent.intensidad_regulable,
            "espectro_completo": ent.espectro_completo,
            "fecha_alta": ent.fecha_alta,
            "fecha_baja": ent.fecha_baja,
            "motivo_baja": ent.motivo_baja,
            "descripcion": ent.descripcion
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
    def update(self, ent: IluminacionEntity) -> Result:

        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  ILUMINACIONES
            SET     ID_TIPO_ILUMINACION = :id_tipo,
                    ID_MARCA = :id_marca,
                    MODELO = :modelo,
                    NUMERO_SERIE = :numero_serie,
                    POTENCIA_W = :potencia,
                    FLUJO_LUMINOSO_LM = :flujo_luminoso,
                    TEMPERATURA_K = :temperatura,
                    VIDA_UTIL = :vida_util,
                    LONGITUD_CM = :longitud,
                    ANCHO_CM = :anchura,
                    ID_CONTROL_ILUMINACION = :id_control,
                    INTENSIDAD_REGULABLE = :intensidad_regulable,
                    ESPECTRO_COMPLETO = :espectro_completo,
                    FECHA_ALTA = :fecha_alta, 
                    FECHA_BAJA = :fecha_baja, 
                    MOTIVO_BAJA = :motivo_baja,
                    DESCRIPCION = :descripcion
            WHERE   ID_ILUMINACION = :id;
            """
        )

        params = {
            "id": ent.id,
            "id_tipo": ent.id_tipo_iluminacion,
            "id_marca": ent.id_marca,
            "modelo": ent.modelo,
            "numero_serie": ent.num_serie,
            "potencia": ent.potencia,
            "flujo_luminoso": ent.flujo_luminico,
            "temperatura": ent.temperatura,
            "vida_util": ent.vida_util,
            "longitud": ent.longitud,
            "anchura": ent.anchura,
            "id_control": ent.id_control_iluminacion,
            "intensidad_regulable": ent.intensidad_regulable,
            "espectro_completo": ent.espectro_completo,
            "fecha_alta": ent.fecha_alta,
            "fecha_baja": ent.fecha_baja,
            "motivo_baja": ent.motivo_baja,
            "descripcion": ent.descripcion
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
            DELETE FROM ILUMINACIONES
            WHERE       ID_ILUMINACION = :id;
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

    # def is_mounted(self, id_urna: int) -> Result:
    #     """ Determina si la luminaria está montada."""
    #
    #     sql = (
    #         """
    #         SELECT  CASE
    #                     WHEN FECHA_DESMONTAJE IS NULL THEN 1 ELSE 0
    #                 END AS MONTADO
    #         FROM    ACUARIOS
    #         WHERE   ID_URNA = :id;
    #         """
    #     )
    #
    #     params = {"id": id_urna}
    #
    #     try:
    #         with self.db.conn as con:
    #             cur = con.execute(sql, params)
    #             rows = cur.fetchall()
    #
    #             if rows is None:
    #                 return Result.failure(f"NO EXISTE NINGUNA URNA CON EL ID "
    #                                       f" {id_urna}")
    #
    #             is_mounted = any(row[0] == 1 for row in rows)
    #             return Result.success(is_mounted)
    #
    #     except sqlite3.IntegrityError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[INTEGRITY ERROR]\n {e}")
    #     except sqlite3.OperationalError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[OPERATIONAL ERROR]\n {e}")
    #     except sqlite3.ProgrammingError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[PROGRAMMING ERROR]\n {e}")
    #     except sqlite3.DatabaseError as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[DATABASE ERROR]\n {e}")
    #     except sqlite3.Error as e:
    #         # traceback.print_exc()
    #         return Result.failure(f"[SQLITE ERROR]\n {e}")
