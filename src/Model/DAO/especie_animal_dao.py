"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      19/03/2026
Comentarios:
    Módulo que contiene el DAO del ESPECIE ANIMAL.
"""
import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.Entities.especie_animal_entity import EspecieAnimalEntity
from Model.database import DBManager
from Services.Result.result import Result


class EspecieAnimalDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    EspecieAnimalEntity.
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
                FROM   ESPECIES_ANIMALES
                WHERE  ID_ESPECIE = :id;
                """
            )

            params = {"id": ide, }

            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql, params)
                row = cur.fetchone()

                # Configuramos la entidad
                EspecieAnimalEntity(
                    id=row[0],
                    num=row[1],
                    reino=row[2],
                    filo=row[3],
                    clase=row[4],
                    orden=row[5],
                    familia=row[6],
                    genero=row[7],
                    especie=row[8],
                    nombre_cientifico=row[9],
                    nombre_comun=row[10],
                    es_hibrida=row[11],
                    nombre_especie_hibrida=row[12],
                    id_grupo_taxonomico=row[13],
                    ph_min=row[14],
                    ph_max=row[15],
                    kh_min=row[16],
                    kh_max=row[17],
                    gh_min=row[18],
                    gh_max=row[19],
                    temp_min=row[20],
                    temp_max=row[21],
                    origen=row[22],
                    tamano_cm=row[23],
                    id_comportamiento=row[24],
                    id_dieta=row[25],
                    id_nivel_nado=row[26],
                    descripcion=row[27],
                )

                return Result.success(ide)

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
                       E.REINO AS REINO,
                       E.FILO AS FILO,
                       E.CLASE AS CLASE,
                       E.ORDEN AS ORDEN,
                       E.FAMILIA AS FAMILIA,
                       E.GENERO AS GENERO,
                       E.ESPECIE AS ESPECIE,
                       E.NOMBRE_CIENTIFICO AS NOMBRE_CIENTIFICO,
                       E.NOMBRE_COMUN AS NOMBRE_COMUN,
                       E.ES_HIBRIDADA AS HIBRIDADA,
                       E.NOMBRE_ESPECIE_HIBRIDADA,
                       T.GRUPO_TAXONOMICO AS GRUPO_TAXONOMICO,
                       E.ORIGEN AS ORIGEN,
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
                       E.TAMANO_ADULTO_CM AS TAMANO,
                       C.COMPORTAMIENTO AS COMPORTAMIENTO,
                       D.DIETA AS DIETA,
                       N.NIVEL_NADO AS NIVEL_NADO,
                       E.DESCRIPCION AS DESCRIPCION
                FROM   ESPECIES_ANIMALES E
                LEFT JOIN GRUPOS_TAXONOMICOS T
                       ON E.ID_GRUPO_TAXONOMICO = T.ID_GRUPO_TAXONOMICO
                LEFT JOIN COMPORTAMIENTOS_FAUNA C
                       ON E.ID_COMPORTAMIENTO = C.ID_COMPORTAMIENTO
                LEFT JOIN DIETAS_FAUNA D
                       ON E.ID_DIETA = D.ID_DIETA
                LEFT JOIN NIVELES_NADO N
                       ON E.ID_NIVEL_NADO = N.ID_NIVEL_NADO;
                """
            )

            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    EspecieAnimalEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        reino=f["REINO"],
                        filo=f["FILO"],
                        clase=f["CLASE"],
                        orden=f["ORDEN"],
                        familia=f["FAMILIA"],
                        genero=f["GENERO"],
                        especie=f["ESPECIE"],
                        nombre_cientifico=f["NOMBRE_CIENTIFICO"],
                        nombre_comun=f["NOMBRE_COMUN"],
                        es_hibrida=f["HIBRIDADA"],
                        nombre_especie_hibrida=f["NOMBRE_ESPECIE_HIBRIDADA"],
                        id_grupo_taxonomico=f["GRUPO_TAXONOMICO"],
                        ph_min=f["PH"],
                        kh_min=f["KH"],
                        gh_min=f["GH"],
                        temp_min=f["TEMPERATURA"],
                        origen=f["ORIGEN"],
                        tamano_cm=f["TAMANO"],
                        id_comportamiento=f["COMPORTAMIENTO"],
                        id_dieta=f["DIETA"],
                        id_nivel_nado=f["NIVEL_NADO"],
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
            SELECT    ID_ESPECIE AS ID,
                      CASE
                          WHEN NOMBRE_COMUN IS NOT NULL 
                              THEN NOMBRE_CIENTIFICO || ' (' || NOMBRE_COMUN || ')'
                          ELSE NOMBRE_CIENTIFICO
                      END AS VALUE
            FROM      ESPECIES_ANIMALES
            ORDER BY  VALUE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    EspecieAnimalEntity(
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
    def insert(self, ent: EspecieAnimalEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO ESPECIES_ANIMALES 
                (REINO, FILO, CLASE, ORDEN, FAMILIA, GENERO, ESPECIE,
                 /*NOMBRE_CIENTIFICO,*/ NOMBRE_COMUN, ES_HIBRIDADA, 
                 NOMBRE_ESPECIE_HIBRIDADA, ID_GRUPO_TAXONOMICO, ORIGEN, 
                 PH_MINIMO, PH_MAXIMO, KH_MINIMO, KH_MAXIMO, GH_MINIMO, 
                 GH_MAXIMO, TEMPERATURA_MIN, TEMPERATURA_MAX, 
                 TAMANO_ADULTO_CM, ID_COMPORTAMIENTO, ID_DIETA,
                 ID_NIVEL_NADO, DESCRIPCION)
            VALUES 
                (:reino, :filo, :clase, :orden, :familia, :genero, :especie, 
                 /*:n_cientifico,*/ :n_comun, :hibridada, :n_e_hibridada, 
                 :gr_taxo, :origen, :ph_min, :ph_max, :kh_min, :kh_max, 
                 :gh_min, :gh_max, :temp_min, :temp_max, :tamano, 
                 :comportamiento, :dieta, :nivel_nado, :descripcion);
            """
        )

        params = {
            "reino": ent.reino,
            "filo": ent.filo,
            "clase": ent.clase,
            "orden": ent.orden,
            "familia": ent.familia,
            "genero": ent.genero,
            "especie": ent.especie,
            # "n_cientifico": ent.nombre_cientifico,
            "n_comun": ent.nombre_comun,
            "hibridada": ent.es_hibrida,
            "gr_taxo": ent.id_grupo_taxonomicvo,
            "origen": ent.origen,
            "ph_min": ent.ph_min,
            "ph_max": ent.ph_max,
            "kh_min": ent.kh_min,
            "kh_max": ent.kh_max,
            "gh_min": ent.gh_min,
            "gh_max": ent.gh_max,
            "temp_min": ent.temp_min,
            "temp_max": ent.temp_max,
            "tamano": ent.tamano_cm,
            "comportamiento": ent.id_comportamiento,
            "dieta": ent.id_dieta,
            "nivel_nado": ent.id_nivel_nado,
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
    def update(self, ent: EspecieAnimalEntity) -> Result:

        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE ESPECIES_ANIMALES
            SET    REINO = :reino,
                   FILO = :filo,
                   CLASE = :clase,
                   ORDEN = :orden,
                   FAMILIA = :familia,
                   GENERO = :genero,
                   ESPECIE = :especie,
                   --NOMBRE_CIENTIFICO = :n_cientifico,
                   NOMBRE_COMUN = :n_comun,
                   ES_HIBRIDADA = :hibridada,
                   NOMBRE_ESPECIE_HIBRIDADA = :n_e_hibridada,
                   ID_GRUPO_TAXONOMICO = :gr_taxo,
                   ORIGEN = :origen,
                   PH_MINIMO = :ph_min,
                   PH_MAXIMO = :ph_max,
                   KH_MINIMO = :kh_min,
                   KH_MAXIMO = :kh_max,
                   GH_MINIMO = :gh_min,
                   GH_MAXIMO = :gh_max,
                   TEMPERATURA_MIN = :temp_min,
                   TEMPERATURA_MAX = :temp_max,
                   TAMANO_ADULTO_CM = :tamano,
                   ID_COMPORTAMIENTO = :comportamiento,
                   ID_DIETA = :dieta,
                   ID_NIVEL_NADO = :nivel_nado,
                   DESCRIPCION = :descripcion
            WHERE  ID_ESPECIE = :id;
            """
        )

        params = {
            "id": ent.id,
            "reino": ent.reino,
            "filo": ent.filo,
            "clase": ent.clase,
            "orden": ent.orden,
            "familia": ent.familia,
            "genero": ent.genero,
            "especie": ent.especie,
            # "n_cientifico": ent.nombre_cientifico,
            "n_comun": ent.nombre_comun,
            "hibridada": ent.es_hibrida,
            "gr_taxo": ent.id_grupo_taxonomicvo,
            "origen": ent.origen,
            "ph_min": ent.ph_min,
            "ph_max": ent.ph_max,
            "kh_min": ent.kh_min,
            "kh_max": ent.kh_max,
            "gh_min": ent.gh_min,
            "gh_max": ent.gh_max,
            "temp_min": ent.temp_min,
            "temp_max": ent.temp_max,
            "tamano": ent.tamano_cm,
            "comportamiento": ent.id_comportamiento,
            "dieta": ent.id_dieta,
            "nivel_nado": ent.id_nivel_nado,
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
            DELETE FROM ESPECIES_ANIMALES
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
