"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      08/04/2026
Comentarios:
    Módulo que contiene el DAO del ESPECIE VEGETAL.
"""
import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.Entities.especie_vegetal_entity import EspecieVegetalEntity
from Model.database import DBManager
from Services.Result.result import Result


class EspecieVegetalDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    EspecieVegetalEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_entity_by_id(self, ide: int) -> Result:
        """
        Obtiene la especie con el ID pasado como argumento.
        :param ide: ID de la entidad a recuperar
        """

        try:
            sql = (
                """
                SELECT *
                FROM   ESPECIES_VEGETALES
                WHERE  ID_ESPECIE = :id;
                """
            )

            params = {"id": ide, }

            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                row = cur.fetchone()

                # Configuramos la entidad
                ent = EspecieVegetalEntity(
                    id=row[0],
                    reino=row[1],
                    division=row[2],
                    clase=row[3],
                    orden=row[4],
                    familia=row[5],
                    genero=row[6],
                    especie=row[7],
                    nombre_cientifico=row[8],
                    nombre_comun=row[9],
                    ph_min=row[10],
                    ph_max=row[11],
                    kh_min=row[12],
                    kh_max=row[13],
                    gh_min=row[14],
                    gh_max=row[15],
                    temp_min=row[16],
                    temp_max=row[17],
                    origen=row[18],
                    id_posicion_acuario=row[19],
                    id_req_iluminacion=row[20],
                    id_req_co2=row[21],
                    id_tasa_crecimiento=row[22],
                    id_dificultad=row[23],
                    descripcion=row[24],
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
        """Obtiene el listado completo ordenado por marca y modelo."""

        try:
            sql = (
                """
                SELECT E.ID_ESPECIE AS ID,
                       ROW_NUMBER() OVER(ORDER BY E.GENERO, E.ESPECIE) AS NUM,
                       E.REINO AS REINO,
                       E.DIVISION AS DIVISION,
                       E.CLASE AS CLASE,
                       E.ORDEN AS ORDEN,
                       E.FAMILIA AS FAMILIA,
                       E.GENERO AS GENERO,
                       E.ESPECIE AS ESPECIE,
                       E.NOMBRE_CIENTIFICO AS NOMBRE_CIENTIFICO,
                       E.NOMBRE_COMUN AS NOMBRE_COMUN,
                       CASE
                           WHEN E.PH_MINIMO IS NULL AND E.PH_MAXIMO IS NULL THEN NULL
                           WHEN E.PH_MINIMO IS NOT NULL AND E.PH_MAXIMO IS NULL THEN 'Mín. ' || E.PH_MINIMO
                           WHEN E.PH_MINIMO IS NULL AND E.PH_MAXIMO IS NOT NULL THEN 'Máx. ' || E.PH_MAXIMO
                           ELSE E.PH_MINIMO || ' - ' || E.PH_MAXIMO
                       END AS PH,
                       CASE
                           WHEN E.KH_MINIMO IS NULL AND E.KH_MAXIMO IS NULL THEN NULL
                           WHEN E.KH_MINIMO IS NOT NULL AND E.KH_MAXIMO IS NULL THEN 'Mín. ' || E.KH_MINIMO
                           WHEN E.KH_MINIMO IS NULL AND E.KH_MAXIMO IS NOT NULL THEN 'Máx. ' || E.KH_MAXIMO
                           ELSE E.KH_MINIMO || ' - ' || E.KH_MAXIMO
                       END AS KH,
                       CASE
                           WHEN E.GH_MINIMO IS NULL AND E.GH_MAXIMO IS NULL THEN NULL
                           WHEN E.GH_MINIMO IS NOT NULL AND E.GH_MAXIMO IS NULL THEN 'Mín. ' || E.GH_MINIMO
                           WHEN E.GH_MINIMO IS NULL AND E.GH_MAXIMO IS NOT NULL THEN 'Máx. ' || E.GH_MAXIMO
                           ELSE E.GH_MINIMO || ' - ' || E.GH_MAXIMO
                       END AS GH,
                       CASE
                           WHEN E.TEMPERATURA_MIN IS NULL AND E.TEMPERATURA_MAX IS NULL THEN NULL
                           WHEN E.TEMPERATURA_MIN IS NOT NULL AND E.TEMPERATURA_MAX IS NULL THEN 'Mín. ' || E.TEMPERATURA_MIN
                           WHEN E.TEMPERATURA_MIN IS NULL AND E.TEMPERATURA_MAX IS NOT NULL THEN 'Máx. ' || E.TEMPERATURA_MAX
                           ELSE E.TEMPERATURA_MIN || ' - ' || E.TEMPERATURA_MAX
                       END AS TEMPERATURA,
                       E.ORIGEN AS ORIGEN,
                       P.POSICION AS POSICION_ACUARIO,
                       I.REQUERIMIENTO_ILUMINACION AS REQUERIMIENTO_ILUMINACION,
                       C.REQUERIMIENTO_CO2 AS REQUERIMIENTO_CO2,
                       T.CRECIMIENTO AS TASA_CRECIMIENTO,
                       D.DIFICULTAD_PLANTA AS DIFICULTAD,
                       E.OBSERVACIONES AS OBSERVACIONES
                FROM   ESPECIES_VEGETALES E
                LEFT JOIN POSICIONES_PLANTAS_ACUARIO P
                    ON    E.ID_POSICION_ACUARIO = P.ID_POSICION_ACUARIO
                LEFT JOIN REQUERIMIENTOS_ILUMINACION I
                    ON    E.ID_REQUERIMIENTO_ILUMINACION = I.ID_REQUERIMIENTO_ILUMINACION
                LEFT JOIN REQUERIMIENTOS_CO2 C
                    ON    E.ID_REQUERIMIENTO_CO2 = C.ID_REQUERIMIENTO_CO2
                LEFT JOIN TASAS_CRECIMIENTO T
                    ON    E.ID_TASA_CRECIMIENTO = T.ID_TASA_CRECIMIENTO
                LEFT JOIN DIFICULTADES_PLANTAS D
                    ON    E.ID_DIFICULTAD = D.ID_DIFICULTAD
                """
            )

            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    EspecieVegetalEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        reino=f["REINO"],
                        division=f["DIVISION"],
                        clase=f["CLASE"],
                        orden=f["ORDEN"],
                        familia=f["FAMILIA"],
                        genero=f["GENERO"],
                        especie=f["ESPECIE"],
                        nombre_cientifico=f["NOMBRE_CIENTIFICO"],
                        nombre_comun=f["NOMBRE_COMUN"],
                        ph_min=f["PH"],
                        kh_min=f["KH"],
                        gh_min=f["GH"],
                        temp_min=f["TEMPERATURA"],
                        origen=f["ORIGEN"],
                        id_posicion_acuario=f["POSICION_ACUARIO"],
                        id_req_iluminacion=f["REQUERIMIENTO_ILUMINACION"],
                        id_req_co2=f["REQUERIMIENTO_CO2"],
                        id_tasa_crecimiento=f["TASA_CRECIMIENTO"],
                        id_dificultad=f["DIFICULTAD"],
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
            SELECT ID_ESPECIE AS ID,
                   CASE
                       WHEN NOMBRE_COMUN IS NOT NULL THEN
                           NOMBRE_CIENTIFICO || ' (' || NOMBRE_COMUN || ')'
                       ELSE NOMBRE_CIENTIFICO
                   END AS VALUE
            FROM   ESPECIES_VEGETALES
            ORDER BY GENERO, ESPECIE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    EspecieVegetalEntity(
                        id=f["ID"],
                        nombre_cientifico=f["VALUE"]
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
    def insert(self, ent: EspecieVegetalEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO ESPECIES_VEGETALES 
                (REINO, DIVISION, CLASE, ORDEN, FAMILIA,
                 GENERO, ESPECIE, NOMBRE_COMUN, PH_MINIMO, PH_MAXIMO,
                 KH_MINIMO, KH_MAXIMO, GH_MINIMO, GH_MAXIMO,
                 TEMPERATURA_MIN, TEMPERATURA_MAX, ORIGEN, ID_POSICION_ACUARIO,
                 ID_REQUERIMIENTO_ILUMINACION, ID_REQUERIMIENTO_CO2, 
                 ID_TASA_CRECIMIENTO, ID_DIFICULTAD, OBSERVACIONES)
            VALUES 
                (:reino, :division, :clase, :orden, :familia,
                 :genero, :especie, :n_comun, :ph_min, :ph_max, :kh_min, 
                 :kh_max, :gh_min, :gh_max, :temp_min, :temp_max, :origen, 
                 :id_posicion, :id_req_ilum, :id_req_co2, :id_crecimiento, 
                 :id_dificultad, :observaciones);
            """
        )

        params = {
            "reino": ent.reino,
            "division": ent.division,
            "clase": ent.clase,
            "orden": ent.orden,
            "familia": ent.familia,
            "genero": ent.genero,
            "especie": ent.especie,
            "n_comun": ent.nombre_comun,
            "ph_min": ent.ph_min,
            "ph_max": ent.ph_max,
            "kh_min": ent.kh_min,
            "kh_max": ent.kh_max,
            "gh_min": ent.gh_min,
            "gh_max": ent.gh_max,
            "temp_min": ent.temp_min,
            "temp_max": ent.temp_max,
            "origen": ent.origen,
            "id_posicion": ent.id_posicion_acuario,
            "id_req_ilum": ent.id_req_iluminacion,
            "id_req_co2": ent.id_req_co2,
            "id_crecimiento": ent.id_tasa_crecimiento,
            "id_dificultad": ent.id_dificultad,
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
    def update(self, ent: EspecieVegetalEntity) -> Result:

        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """     
            UPDATE  ESPECIES_VEGETALES
            SET     REINO = :reino,
                    DIVISION = :division,
                    CLASE = :clase,
                    ORDEN = :orden,
                    FAMILIA = :familia,
                    GENERO = :genero,
                    ESPECIE = :especie,
                    NOMBRE_COMUN = n_comun,
                    PH_MINIMO = :ph_min,
                    PH_MAXIMO = :ph_max,
                    KH_MINIMO = :kh_min,
                    KH_MAXIMO = :kh_max,
                    GH_MINIMO = :gh_min,
                    GH_MAXIMO = :gh_max,
                    TEMPERATURA_MIN = :temp_min,
                    TEMPERATURA_MAX = :temp_max,
                    ORIGEN = :origen,
                    ID_POSICION_ACUARIO = :id_posicion,
                    ID_REQUERIMIENTO_ILUMINACION = :id_req_ilum,
                    ID_REQUERIMIENTO_CO2 = :id_req_co2,
                    ID_TASA_CRECIMIENTO = :id_crecimiento,
                    ID_DIFICULTAD = :id_dificultad,
                    OBSERVACIONES = :observaciones
            WHERE   ID_ESPECIE = :id;
            """
        )

        params = {
            "id": ent.id,
            "reino": ent.reino,
            "division": ent.division,
            "clase": ent.clase,
            "orden": ent.orden,
            "familia": ent.familia,
            "genero": ent.genero,
            "especie": ent.especie,
            "n_comun": ent.nombre_comun,
            "ph_min": ent.ph_min,
            "ph_max": ent.ph_max,
            "kh_min": ent.kh_min,
            "kh_max": ent.kh_max,
            "gh_min": ent.gh_min,
            "gh_max": ent.gh_max,
            "temp_min": ent.temp_min,
            "temp_max": ent.temp_max,
            "origen": ent.origen,
            "id_posicion": ent.id_posicion_acuario,
            "id_req_ilum": ent.id_req_iluminacion,
            "id_req_co2": ent.id_req_co2,
            "id_crecimiento": ent.id_tasa_crecimiento,
            "id_dificultad": ent.id_dificultad,
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
            DELETE FROM ESPECIES_VEGETALES
            WHERE       ID_ESPECIE = :id;
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
