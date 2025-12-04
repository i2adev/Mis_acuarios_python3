"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Comentarios:
    Módulo que contiene el DAO de la URNA.
"""
import sqlite3

from Model.DAO.base_dao import BaseDAO
from Model.DAO.database import DBManager
from Model.Entities.filtro_entity import FiltroEntity
from Services.Result.result import Result


class FiltroDAO(BaseDAO):
    """
    Clase que gestiona las operaciones en la base de datos de la entidad
    FiltroEntity.
    """

    def __init__(self):
        """ Constructor de clase. """

        self.db = DBManager()
        self.ent = None

    # ------------------------------------------------------------------
    def get_list(self) -> Result:
        """Obtiene el listado completo ordenado por categoría."""

        sql = (
            """
            SELECT    F.ID_FILTRO AS ID,
                      ROW_NUMBER() OVER(ORDER BY MC.MARCA, F.MODELO) AS NUM,
                      MC.MARCA AS MARCA,
                      F.MODELO AS MODELO,
                      TF.TIPO_FILTRO AS TIPO_FILTRO,
                      F.ES_THERMOFILTRO AS TERMOFILTRO,
                      F.NUMERO_SERIE AS NUMERO_SERIE,
                      F.VOLUMEN_MIN_ACUARIO || '/' || F.VOLUMEN_MAX_ACUARIO AS 
                      VOLUMEN_ACUARIO,
                      F.CAUDAL AS CAUDAL,
                      F.ALTURA_BOMBEO AS ALTURA_BOMBEO,
                      F.CONSUMO AS CONSUMO,
                      F.CONSUMO_CALENTADOR AS CONSUMO_CALENTADOR,
                      F.VOLUMEN_FILTRANTE AS VOLUMEN_FILTRANTE,
                      F.ANCHO || 'x' || F.FONDO || 'x' || F.ALTO AS DIMENSIONES,
                      F.fecha_compra AS FECHA_INSTALACIÓN,
                      F.FECHA_BAJA AS FECHA_BAJA,
                      F.MOTIVO_BAJA AS MOTIVO_BAJA,
                      F.DESCRIPCION AS DESCRIPCIÓN
            FROM      FILTROS F
            LEFT JOIN MARCAS_COMERCIALES MC ON F.ID_MARCA = MC.ID_MARCA
            LEFT JOIN TIPOS_FILTRO TF ON F.ID_TIPO = TF.ID_TIPO;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()

                valores = [
                    FiltroEntity(
                        id=f["ID"],
                        num=f["NUM"],
                        id_marca=f["MARCA"],
                        modelo=f["MODELO"],
                        id_tipo=f["TIPO_FILTRO"],
                        es_thermo=f["TERMOFILTRO"],
                        num_serie=f["NUMERO_SERIE"],
                        vol_min_acuario=f["VOLUMEN_ACUARIO"],
                        caudal=f["CAUDAL"],
                        altura_bombeo=f["ALTURA_BOMBEO"],
                        consumo=f["CONSUMO"],
                        consumo_calentador=f["CONSUMO_CALENTADOR"],
                        vol_filtrante=f["VOLUMEN_FILTRANTE"],
                        ancho=f["DIMENSIONES"],
                        fecha_compra=f["fecha_compra"],
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
            SELECT      F.ID_FILTRO AS ID,
                        MC.MARCA || F.MODELO AS VALUE
            FROM        FILTROS F
            LEFT JOIN   MARCAS_COMERCIALES MC ON F.ID_MARCA = MC.ID_MARCA
            ORDER BY    VALUE;
            """
        )

        try:
            with self.db.conn as con:
                cur = con.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
                valores = [
                    FiltroEntity(
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
    def insert(self, ent: FiltroEntity) -> Result:
        """
        Inserta un nuevo registro y devuelve el ID generado.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            INSERT INTO FILTROS (ID_TIPO, ID_MARCA, MODELO, NUMERO_SERIE,
                                 ES_THERMOFILTRO, VOLUMEN_MIN_ACUARIO,
                                 VOLUMEN_MAX_ACUARIO, CAUDAL, ALTURA_BOMBEO,
                                 CONSUMO, CONSUMO_CALENTADOR, VOLUMEN_FILTRANTE,
                                 ANCHO, FONDO, ALTO, fecha_compra, 
                                 FECHA_BAJA, MOTIVO_BAJA, DESCRIPCION)
            VALUES (:id_tipo, :id_marca, :modelo, :numero_serie, :es_thermo,
                    :vol_min_acuario, :vol_max_acuario, 
                    :caudal, :altura_bombeo, :consumo, :consumo_calentador, 
                    :vol_filtrante, :ancho, :fondo, :alto, 
                    :fecha_compra, :fecha_baja, :motivo_baja, 
                    :descripcion);
            """
        )

        params = {
            "id_tipo": ent.id_tipo,
            "id_marca": ent.id_marca,
            "modelo": ent.modelo,
            "numero_serie": ent.num_serie,
            "es_thermo": ent.es_thermo,
            "vol_min_acuario": ent.vol_min_acuario,
            "vol_max_acuario": ent.vol_max_acuario,
            "caudal": ent.caudal,
            "altura_bombeo": ent.altura_bombeo,
            "consumo": ent.consumo,
            "consumo_calentador": ent.consumo_calentador,
            "vol_filtrante": ent.vol_filtrante,
            "ancho": ent.ancho,
            "fondo": ent.fondo,
            "alto": ent.alto,
            "fecha_compra": ent.fecha_compra,
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
    def update(self, ent: FiltroEntity) -> Result:

        """
        Actualiza el registro en la base de datos. Devuelve el ID de la entidad
        modificada.
        :param ent: Entidad derivada de BaseEntity
        """

        sql = (
            """
            UPDATE  FILTROS
            SET     ID_FILTRO = :id,
                    ID_TIPO = :id_tipo,
                    ID_MARCA = :id_marca,
                    MODELO = :modelo,
                    NUMERO_SERIE = :numero_serie,
                    ES_THERMOFILTRO = :es_thermo,
                    VOLUMEN_MIN_ACUARIO = :vol_min_acuario,
                    VOLUMEN_MAX_ACUARIO = :vol_max_acuario,
                    CAUDAL = :caudal,
                    ALTURA_BOMBEO = :altura_bombeo,
                    CONSUMO = :consumo,
                    CONSUMO_CALENTADOR = :consumo_calentador,
                    VOLUMEN_FILTRANTE = :vol_filtrante,
                    ANCHO = :ancho,
                    FONDO = :fondo,
                    ALTO = :alto,
                    fecha_compra = :fecha_compra,
                    FECHA_BAJA = :fecha_baja,
                    MOTIVO_BAJA = :motivo_baja,
                    DESCRIPCION = :descripcion
            WHERE ID_FILTRO = :id;
            """
        )

        params = {
            "id": ent.id,
            "id_tipo": ent.id_tipo,
            "id_marca": ent.id_marca,
            "modelo": ent.modelo,
            "numero_serie": ent.num_serie,
            "es_thermo": ent.es_thermo,
            "vol_min_acuario": ent.vol_min_acuario,
            "vol_max_acuario": ent.vol_max_acuario,
            "caudal": ent.caudal,
            "altura_bombeo": ent.altura_bombeo,
            "consumo": ent.consumo,
            "consumo_calentador": ent.consumo_calentador,
            "vol_filtrante": ent.vol_filtrante,
            "ancho": ent.ancho,
            "fondo": ent.fondo,
            "alto": ent.alto,
            "fecha_compra": ent.fecha_compra,
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
            DELETE FROM FILTROS
            WHERE       ID_FILTRO = :id;
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

    def is_mounted(self, id_urna: int) -> Result:
        """ Determina si un filtro está montada."""

        sql = (
            """
            SELECT  CASE
                        WHEN FECHA_DESMONTAJE IS NULL THEN 1 ELSE 0
                    END AS MONTADO
            FROM    ACUARIOS
            WHERE   ID_URNA = :id;
            """
        )

        params = {"id": id_urna}

        try:
            with self.db.conn as con:
                cur = con.execute(sql, params)
                rows = cur.fetchall()

                if rows is None:
                    return Result.failure(f"NO EXISTE NINGUNA URNA CON EL ID "
                                          f" {id_urna}")

                is_mounted = any(row[0] == 1 for row in rows)
                return Result.success(is_mounted)

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
